# Arquitetura Técnica — Teams Meeting Secretary Agent

> **Projeto:** Secretário de Reunião Teams  
> **Versão:** 1.0  
> **Data:** 08/06/2026  
> **Autor:** Wagner — Arquiteto de Software, Squad MEQ  
> **Status:** Draft  

---

## Índice

1. [Resumo Executivo](#1-resumo-executivo)
2. [Arquitetura Lógica](#2-arquitetura-lógica)
3. [Arquitetura Física (Azure)](#3-arquitetura-física-azure)
4. [Fluxo da Solução](#4-fluxo-da-solução)
5. [Microsoft Graph APIs Utilizadas](#5-microsoft-graph-apis-utilizadas)
6. [Modelo de Dados](#6-modelo-de-dados)
7. [Segurança e Identidade](#7-segurança-e-identidade)
8. [Licenciamento Necessário](#8-licenciamento-necessário)
9. [Observabilidade](#9-observabilidade)
10. [Estratégia de Deploy](#10-estratégia-de-deploy)
11. [Riscos e Mitigações](#11-riscos-e-mitigações)
12. [Estimativa de Custo (Azure)](#12-estimativa-de-custo-azure)

---

## 1. Resumo Executivo

O **Teams Meeting Secretary Agent** é um agente inteligente que opera como um "secretário invisível" em reuniões do Microsoft Teams. Ele captura automaticamente transcrições, listas de presença e metadados das reuniões e, ao término de cada sessão, utiliza Azure OpenAI (GPT-4o) para gerar:

- **Ata de Reunião Estruturada** — com tópicos discutidos, decisões tomadas, ações atribuídas e prazos
- **Resumo Executivo** — síntese objetiva para quem não pôde participar

A solução é 100% event-driven: nenhuma intervenção humana é necessária após a configuração inicial. Quando uma reunião encerra e a transcrição fica disponível, o fluxo é disparado automaticamente via Graph Change Notifications. O resultado é entregue como Adaptive Card no chat da reunião, salvo como página no SharePoint e, opcionalmente, enviado por e-mail.

**Princípios de design:**

| Princípio | Decisão |
|---|---|
| Serverless-first | Azure Functions (sem infra para gerenciar) |
| Event-driven | Graph Change Notifications como trigger principal |
| Least-privilege | Apenas permissões Graph estritamente necessárias |
| Custo proporcional ao uso | Cosmos DB Serverless + Functions Consumption |
| Tecnologia "chata" que funciona | Stack Microsoft nativa — sem dependências exóticas |

---

## 2. Arquitetura Lógica

### 2.1 Diagrama de Componentes (Textual)

```
┌──────────────────────────────────────────────────────────────────────┐
│                        EVENT SOURCES                                 │
│                                                                      │
│  Microsoft Graph Change Notifications                                │
│  ├── /communications/onlineMeetings (meeting ended)                  │
│  ├── /communications/callRecords   (call record available)           │
│  └── Polling fallback: transcript & recording availability           │
└──────────────────┬───────────────────────────────────────────────────┘
                   │ HTTPS webhook
                   ▼
┌──────────────────────────────────────────────────────────────────────┐
│                      DATA INGESTION LAYER                            │
│                                                                      │
│  Azure Function: WebhookReceiver                                     │
│  ├── Valida notificação (clientState token)                          │
│  ├── Enfileira processamento (Queue Storage)                         │
│  └── Retorna 202 Accepted imediatamente                              │
│                                                                      │
│  Azure Function: MeetingDataCollector (Queue Trigger)                │
│  ├── Graph API → GET transcript (vtt/docx)                           │
│  ├── Graph API → GET attendance report                               │
│  ├── Graph API → GET meeting metadata (subject, organizer, times)    │
│  ├── Graph API → GET chat messages (meeting chat)                    │
│  └── Salva raw data no Blob Storage                                  │
└──────────────────┬───────────────────────────────────────────────────┘
                   │ Queue message
                   ▼
┌──────────────────────────────────────────────────────────────────────┐
│                      PROCESSING LAYER                                │
│                                                                      │
│  Azure Function: TranscriptProcessor (Queue Trigger)                 │
│  ├── Azure OpenAI GPT-4o                                             │
│  │   ├── Extração de tópicos discutidos                              │
│  │   ├── Identificação de decisões                                   │
│  │   ├── Extração de ações e responsáveis                            │
│  │   ├── Análise de sentimento geral                                 │
│  │   └── Geração de resumo executivo                                 │
│  └── Structured Output (JSON) → validação com schema                 │
│                                                                      │
│  Azure Function: MinutesGenerator (Queue Trigger)                    │
│  ├── Compõe Ata de Reunião (Markdown/HTML)                           │
│  └── Gera Adaptive Card JSON                                         │
└──────────────────┬───────────────────────────────────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────────────────────────────────┐
│                        STORAGE LAYER                                 │
│                                                                      │
│  Cosmos DB (Serverless)                                              │
│  ├── Container: meetings         (metadata + status)                 │
│  ├── Container: decisions        (decisões extraídas)                │
│  ├── Container: action-items     (ações com responsáveis)            │
│  └── Container: meeting-minutes  (ata final gerada)                  │
│                                                                      │
│  Azure Blob Storage                                                  │
│  ├── Container: raw-transcripts  (VTT/DOCX originais)               │
│  ├── Container: raw-recordings   (MP4 referências)                   │
│  └── Container: processed-data   (JSON intermediários)               │
│                                                                      │
│  SharePoint                                                          │
│  └── Document Library: Atas de Reunião (páginas HTML/ASPX)           │
└──────────────────┬───────────────────────────────────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────────────────────────────────┐
│                        OUTPUT LAYER                                  │
│                                                                      │
│  Azure Function: NotificationDispatcher (Queue Trigger)              │
│  ├── Adaptive Card → enviada ao chat da reunião (Graph API)          │
│  ├── SharePoint Page → criada/atualizada na library                  │
│  └── Email (opcional) → enviado via Graph API (sendMail)             │
└──────────────────────────────────────────────────────────────────────┘
```

### 2.2 Comunicação entre Componentes

| De | Para | Mecanismo | Formato |
|---|---|---|---|
| Graph | WebhookReceiver | HTTPS POST | JSON (change notification) |
| WebhookReceiver | MeetingDataCollector | Azure Queue Storage | JSON message |
| MeetingDataCollector | Blob Storage | Azure SDK | VTT/DOCX/JSON |
| MeetingDataCollector | TranscriptProcessor | Azure Queue Storage | JSON message |
| TranscriptProcessor | Azure OpenAI | HTTPS REST | JSON (chat completions) |
| TranscriptProcessor | MinutesGenerator | Azure Queue Storage | JSON message |
| MinutesGenerator | Cosmos DB | Azure SDK | JSON documents |
| MinutesGenerator | NotificationDispatcher | Azure Queue Storage | JSON message |
| NotificationDispatcher | Graph API | HTTPS REST | JSON (Adaptive Card / email) |
| NotificationDispatcher | SharePoint | Graph API / CSOM | HTML page |

### 2.3 Decisão: Por que Filas entre Functions?

A decomposição em múltiplas Functions com filas intermediárias não é over-engineering — é parede de sustentação:

1. **Resiliência** — Se o OpenAI estiver lento ou indisponível, a fila retém a mensagem e o retry é automático
2. **Observabilidade** — Cada etapa tem métricas independentes (duration, failures, queue depth)
3. **Escala independente** — O webhook responde em <200ms; o processamento pesado escala separadamente
4. **Custo** — Functions idle = zero cost no Consumption Plan

---

## 3. Arquitetura Física (Azure)

### 3.1 Resource Group

```
rg-teams-secretary-{env}
├── func-teams-secretary-{env}          # Azure Functions App
├── cosmos-teams-secretary-{env}        # Cosmos DB Account
├── st-teamssec{env}                    # Storage Account (Blobs + Queues)
├── kv-teams-secretary-{env}            # Key Vault
├── appi-teams-secretary-{env}          # Application Insights
├── log-teams-secretary-{env}           # Log Analytics Workspace
├── oai-teams-secretary-{env}           # Azure OpenAI Service
└── plan-teams-secretary-{env}          # App Service Plan (se Premium)
```

> `{env}` = `dev`, `stg` ou `prd`

### 3.2 Recursos e Configuração

| Recurso | SKU / Tier | Justificativa |
|---|---|---|
| **Azure Functions** | Consumption Plan (dev/stg), Premium EP1 (prd) | Consumption para custo zero em idle; Premium em produção para VNET integration e warm instances |
| **Cosmos DB** | Serverless | Volume de reuniões não justifica throughput provisionado; serverless cobra por RU consumida |
| **Storage Account** | Standard LRS (dev), Standard GRS (prd) | GRS em produção para redundância geográfica |
| **Key Vault** | Standard | Armazena secrets, connection strings, certificados |
| **Application Insights** | Pay-as-you-go | Telemetria, distributed tracing, métricas customizadas |
| **Log Analytics** | Pay-per-GB | Centralização de logs de todos os recursos |
| **Azure OpenAI** | S0 (Standard) | GPT-4o deployment com rate limit configurável |
| **App Registration** | N/A (Entra ID) | Identidade da aplicação para Graph API |

### 3.3 Diagrama de Rede (Produção)

```
┌─────────────────────────────────────────────────────┐
│                    VNET (prd)                        │
│                                                     │
│  ┌─────────────────┐    ┌──────────────────┐        │
│  │ Azure Functions  │───▶│ Private Endpoints │       │
│  │ (Premium EP1)    │    │ ├── Cosmos DB     │       │
│  │ VNET integrated  │    │ ├── Storage       │       │
│  └────────┬─────────┘    │ ├── Key Vault     │       │
│           │              │ └── OpenAI        │       │
│           │              └──────────────────┘        │
└───────────┼──────────────────────────────────────────┘
            │ Outbound (internet)
            ▼
  ┌──────────────────┐
  │ Microsoft Graph   │
  │ (graph.microsoft  │
  │  .com)            │
  └──────────────────┘
```

---

## 4. Fluxo da Solução

### 4.1 Fluxo Principal (Passo a Passo)

```
 ① Reunião agendada no Teams (transcrição habilitada)
 │
 ② Reunião encerra
 │  └── Graph emite Change Notification (callRecord created)
 │
 ③ Azure Function [WebhookReceiver] recebe POST
 │  ├── Valida clientState token
 │  ├── Extrai meetingId / callRecordId
 │  └── Enfileira mensagem na queue "meeting-ended"
 │
 ④ Azure Function [MeetingDataCollector] é acionada (queue trigger)
 │  ├── Aguarda transcript ficar disponível (polling com backoff)
 │  ├── GET /me/onlineMeetings/{id}/transcripts/{id}/content
 │  ├── GET /communications/callRecords/{id}
 │  ├── GET /me/onlineMeetings/{id}/attendanceReports
 │  ├── GET meeting metadata (subject, startDateTime, endDateTime)
 │  ├── GET /chats/{id}/messages (mensagens do chat da reunião)
 │  ├── Salva raw transcript no Blob Storage
 │  └── Enfileira mensagem na queue "transcript-ready"
 │
 ⑤ Azure Function [TranscriptProcessor] é acionada (queue trigger)
 │  ├── Lê transcript do Blob Storage
 │  ├── Monta prompt com instruções estruturadas
 │  └── Chama Azure OpenAI GPT-4o:
 │      ├── System prompt com template de extração
 │      └── User prompt com transcript completo
 │
 ⑥ Azure OpenAI retorna JSON estruturado:
 │  {
 │    "topicos": [...],
 │    "decisoes": [...],
 │    "acoes": [{ "descricao", "responsavel", "prazo" }],
 │    "resumo_executivo": "...",
 │    "sentimento_geral": "positivo|neutro|negativo",
 │    "palavras_chave": [...]
 │  }
 │
 ⑦ Dados estruturados salvos no Cosmos DB
 │  ├── Meeting document (metadata + status)
 │  ├── Decisions (vinculadas ao meetingId)
 │  └── ActionItems (vinculados ao meetingId)
 │
 ⑧ Azure Function [MinutesGenerator] gera Ata de Reunião
 │  ├── Template Markdown/HTML preenchido
 │  ├── Ata salva no SharePoint (Document Library)
 │  └── Enfileira mensagem na queue "minutes-ready"
 │
 ⑨ Azure Function [NotificationDispatcher] envia notificações
 │  ├── Adaptive Card com resumo → POST /chats/{id}/messages
 │  └── Email opcional → POST /users/{id}/sendMail
 │
 ⑩ Participantes recebem:
    ├── Adaptive Card no chat da reunião (clicável, com link para ata)
    ├── Página de ata completa no SharePoint
    └── Email com resumo (se configurado)
```

### 4.2 Fluxo de Retry e Tratamento de Falha

| Etapa | Possível Falha | Estratégia |
|---|---|---|
| Webhook | Graph não entrega notificação | Polling periódico como fallback (Timer Trigger a cada 15 min) |
| Coleta de dados | Transcript ainda não disponível | Retry com exponential backoff (30s, 1min, 2min, 5min) até 30 min |
| OpenAI | Rate limit (429) ou timeout | Retry com backoff; queue visibility timeout; dead-letter após 5 tentativas |
| Cosmos DB | Throttling (429 RU) | SDK retry policy built-in; autoscale se necessário |
| SharePoint | Site indisponível | Retry 3x; salva ata no Blob como fallback |
| Notificação | Graph API erro | Dead-letter queue; alerta no Application Insights |

### 4.3 Fluxo de Subscription Lifecycle

As subscriptions do Graph expiram (máximo 4230 minutos para callRecords). É necessário:

```
Timer Trigger [SubscriptionRenewal] — executa a cada 12 horas
├── Lista subscriptions ativas no Cosmos DB
├── Renova subscriptions próximas de expirar (< 24h)
└── Recria subscriptions expiradas
```

---

## 5. Microsoft Graph APIs Utilizadas

### 5.1 APIs Principais

| API | Endpoint | Método | Tipo de Permissão | Permissão | Admin Consent |
|---|---|---|---|---|---|
| **Criar Subscription** | `POST /subscriptions` | POST | Application | `CallRecords.Read.All` | ✅ Sim |
| **Renovar Subscription** | `PATCH /subscriptions/{id}` | PATCH | Application | `CallRecords.Read.All` | ✅ Sim |
| **Call Records** | `GET /communications/callRecords/{id}` | GET | Application | `CallRecords.Read.All` | ✅ Sim |
| **Online Meeting (by join URL)** | `GET /users/{userId}/onlineMeetings?$filter=joinWebUrl eq '{url}'` | GET | Application | `OnlineMeetings.Read.All` | ✅ Sim |
| **Online Meeting (by ID)** | `GET /users/{userId}/onlineMeetings/{meetingId}` | GET | Application | `OnlineMeetings.Read.All` | ✅ Sim |
| **Listar Transcripts** | `GET /users/{userId}/onlineMeetings/{meetingId}/transcripts` | GET | Application | `OnlineMeetingTranscript.Read.All` | ✅ Sim |
| **Obter Conteúdo Transcript** | `GET /users/{userId}/onlineMeetings/{meetingId}/transcripts/{transcriptId}/content` | GET | Application | `OnlineMeetingTranscript.Read.All` | ✅ Sim |
| **Listar Recordings** | `GET /users/{userId}/onlineMeetings/{meetingId}/recordings` | GET | Application | `OnlineMeetingRecording.Read.All` | ✅ Sim |
| **Attendance Reports** | `GET /users/{userId}/onlineMeetings/{meetingId}/attendanceReports` | GET | Application | `OnlineMeetingArtifact.Read.All` | ✅ Sim |
| **Attendance Records** | `GET /users/{userId}/onlineMeetings/{meetingId}/attendanceReports/{reportId}/attendanceRecords` | GET | Application | `OnlineMeetingArtifact.Read.All` | ✅ Sim |
| **Chat Messages** | `GET /chats/{chatId}/messages` | GET | Application | `Chat.Read.All` | ✅ Sim |
| **Enviar Mensagem (Adaptive Card)** | `POST /chats/{chatId}/messages` | POST | Application | `Chat.ReadWrite.All` | ✅ Sim |
| **Enviar Email** | `POST /users/{userId}/sendMail` | POST | Application | `Mail.Send` | ✅ Sim |
| **SharePoint — Criar Página** | `POST /sites/{siteId}/pages` | POST | Application | `Sites.ReadWrite.All` | ✅ Sim |
| **SharePoint — Upload Arquivo** | `PUT /sites/{siteId}/drive/items/{parentId}:/{filename}:/content` | PUT | Application | `Files.ReadWrite.All` | ✅ Sim |

### 5.2 Formato do Transcript

O conteúdo do transcript está disponível em dois formatos:

| Accept Header | Formato | Uso |
|---|---|---|
| `text/vtt` | WebVTT (legendas com timestamps) | Processamento por IA (preferido) |
| `application/vnd.openxmlformats-officedocument.wordprocessingml.document` | DOCX | Arquivamento |

**Recomendação:** Usar `text/vtt` para envio ao OpenAI — o formato com timestamps permite à IA correlacionar falas com tempo, melhorando a extração de tópicos.

### 5.3 Change Notification Payload (Exemplo)

```json
{
  "value": [
    {
      "subscriptionId": "guid",
      "changeType": "created",
      "resource": "communications/callRecords/guid",
      "resourceData": {
        "@odata.type": "#microsoft.graph.callRecord",
        "id": "guid"
      },
      "clientState": "secreto-validacao-token"
    }
  ]
}
```

### 5.4 Permissões Consolidadas (App Registration)

```
Application Permissions (todas requerem Admin Consent):
├── CallRecords.Read.All
├── OnlineMeetings.Read.All
├── OnlineMeetingTranscript.Read.All
├── OnlineMeetingRecording.Read.All
├── OnlineMeetingArtifact.Read.All
├── Chat.Read.All
├── Chat.ReadWrite.All
├── Mail.Send
├── Sites.ReadWrite.All
└── Files.ReadWrite.All
```

---

## 6. Modelo de Dados

### 6.1 Cosmos DB — Estrutura de Containers

**Database:** `teams-secretary-db`  
**Partition Strategy:** Partition key = `/meetingId` em todos os containers (colocalização de dados por reunião)

### 6.2 Entidades

#### Meeting

```json
{
  "id": "guid",
  "meetingId": "teams-meeting-id",
  "callRecordId": "guid",
  "subject": "Sprint Planning - Squad MEQ",
  "organizerId": "user-guid",
  "organizerName": "Alessandro Lisboa",
  "organizerEmail": "alessandro@foursys.com.br",
  "startDateTime": "2026-06-08T14:00:00Z",
  "endDateTime": "2026-06-08T15:30:00Z",
  "durationMinutes": 90,
  "joinWebUrl": "https://teams.microsoft.com/l/meetup-join/...",
  "chatId": "19:meeting_...",
  "transcriptAvailable": true,
  "recordingAvailable": false,
  "processingStatus": "completed",
  "processingStartedAt": "2026-06-08T15:31:00Z",
  "processingCompletedAt": "2026-06-08T15:32:15Z",
  "errorMessage": null,
  "type": "meeting",
  "_ts": 1749398400
}
```

#### Participant

```json
{
  "id": "guid",
  "meetingId": "teams-meeting-id",
  "userId": "user-guid",
  "displayName": "Wagner Souza",
  "email": "wagner@foursys.com.br",
  "role": "presenter",
  "joinDateTime": "2026-06-08T14:00:30Z",
  "leaveDateTime": "2026-06-08T15:30:00Z",
  "attendanceDurationSeconds": 5370,
  "type": "participant"
}
```

#### Transcript

```json
{
  "id": "guid",
  "meetingId": "teams-meeting-id",
  "graphTranscriptId": "transcript-guid",
  "format": "text/vtt",
  "blobUrl": "https://st-teamssecprd.blob.core.windows.net/raw-transcripts/2026/06/08/{meetingId}.vtt",
  "sizeBytes": 45230,
  "languageCode": "pt-BR",
  "createdDateTime": "2026-06-08T15:30:45Z",
  "type": "transcript"
}
```

#### Decision

```json
{
  "id": "guid",
  "meetingId": "teams-meeting-id",
  "sequenceNumber": 1,
  "description": "Adotar Cosmos DB Serverless em vez de throughput provisionado",
  "context": "Discussão sobre custos de infraestrutura",
  "decidedBy": "Wagner Souza",
  "timestamp": "2026-06-08T14:35:00Z",
  "tags": ["infraestrutura", "custo", "cosmos-db"],
  "type": "decision"
}
```

#### ActionItem

```json
{
  "id": "guid",
  "meetingId": "teams-meeting-id",
  "sequenceNumber": 1,
  "description": "Criar POC de integração com Graph API para transcripts",
  "assignee": "Felipe Santos",
  "assigneeEmail": "felipe@foursys.com.br",
  "dueDate": "2026-06-15",
  "priority": "alta",
  "status": "pendente",
  "tags": ["poc", "graph-api"],
  "type": "action-item"
}
```

#### MeetingMinutes

```json
{
  "id": "guid",
  "meetingId": "teams-meeting-id",
  "version": 1,
  "format": "html",
  "sharepointUrl": "https://foursys.sharepoint.com/sites/meq/atas/2026-06-08-sprint-planning.aspx",
  "blobUrl": "https://st-teamssecprd.blob.core.windows.net/meeting-minutes/2026/06/08/{meetingId}.html",
  "summary": "Reunião de Sprint Planning focada em...",
  "topicsCount": 5,
  "decisionsCount": 3,
  "actionItemsCount": 7,
  "sentimentOverall": "positivo",
  "keywords": ["sprint", "planejamento", "cosmos-db", "graph-api"],
  "generatedAt": "2026-06-08T15:32:10Z",
  "aiModel": "gpt-4o",
  "aiTokensUsed": 4520,
  "type": "meeting-minutes"
}
```

### 6.3 Indexing Policy (Cosmos DB)

```json
{
  "indexingMode": "consistent",
  "includedPaths": [
    { "path": "/meetingId/?" },
    { "path": "/type/?" },
    { "path": "/processingStatus/?" },
    { "path": "/startDateTime/?" },
    { "path": "/organizerEmail/?" },
    { "path": "/assigneeEmail/?" },
    { "path": "/status/?" }
  ],
  "excludedPaths": [
    { "path": "/*" }
  ],
  "compositeIndexes": [
    [
      { "path": "/type", "order": "ascending" },
      { "path": "/startDateTime", "order": "descending" }
    ]
  ]
}
```

### 6.4 Blob Storage — Organização

```
raw-transcripts/
  └── {yyyy}/{MM}/{dd}/{meetingId}.vtt

raw-recordings/
  └── {yyyy}/{MM}/{dd}/{meetingId}_ref.json    # Referência/metadados (não armazena MP4)

processed-data/
  └── {yyyy}/{MM}/{dd}/{meetingId}_openai_response.json

meeting-minutes/
  └── {yyyy}/{MM}/{dd}/{meetingId}.html
```

---

## 7. Segurança e Identidade

### 7.1 App Registration (Entra ID)

| Configuração | Valor |
|---|---|
| **Nome** | teams-secretary-agent-{env} |
| **Tipo** | Multi-tenant: Não (single tenant) |
| **Authentication** | Client credentials (certificate preferred) |
| **Redirect URIs** | Nenhum (daemon app) |
| **Implicit grant** | Desabilitado |

### 7.2 Autenticação e Credenciais

| Componente | Estratégia |
|---|---|
| **Azure Functions → Graph API** | App Registration com certificado (X.509) armazenado no Key Vault |
| **Azure Functions → Cosmos DB** | Managed Identity (System-assigned) com RBAC role `Cosmos DB Built-in Data Contributor` |
| **Azure Functions → Blob Storage** | Managed Identity com RBAC role `Storage Blob Data Contributor` |
| **Azure Functions → Azure OpenAI** | Managed Identity com RBAC role `Cognitive Services OpenAI User` |
| **Azure Functions → Key Vault** | Managed Identity com Access Policy `Get, List` para Secrets e Certificates |

### 7.3 Princípio de Least Privilege

```
Graph Permissions Justification:
├── CallRecords.Read.All        → Detectar término de reuniões
├── OnlineMeetings.Read.All     → Obter metadata da reunião
├── OnlineMeetingTranscript.Read.All → Ler transcrição
├── OnlineMeetingRecording.Read.All  → Verificar se há gravação
├── OnlineMeetingArtifact.Read.All   → Relatório de presença
├── Chat.Read.All               → Ler mensagens do chat
├── Chat.ReadWrite.All          → Enviar Adaptive Card (**única permissão de escrita em Teams**)
├── Mail.Send                   → Email de notificação (restringir via Application Access Policy)
├── Sites.ReadWrite.All         → Criar páginas de ata no SharePoint
└── Files.ReadWrite.All         → Upload de documentos no SharePoint
```

**Restrições adicionais:**

- **Application Access Policy** para `Mail.Send`: restringir a um mailbox específico (ex: `secretary@foursys.com.br`) para evitar que a app envie email como qualquer usuário
- **Application Access Policy** para `Chat.ReadWrite.All`: restringir via policy se disponível, ou monitorar via audit logs
- **Sites.ReadWrite.All**: considerar migrar para `Sites.Selected` quando o cenário suportar, limitando acesso a um único site SharePoint

### 7.4 Key Vault — Secrets Armazenados

| Secret | Descrição |
|---|---|
| `graph-app-certificate` | Certificado X.509 para autenticação Graph |
| `graph-client-id` | Client ID da App Registration |
| `graph-tenant-id` | Tenant ID do Entra ID |
| `cosmos-connection-string` | Fallback se Managed Identity não for viável |
| `webhook-client-state` | Token de validação das change notifications |
| `openai-endpoint` | Endpoint do Azure OpenAI (não é secret, mas centralizado) |

### 7.5 Proteção de Dados

| Controle | Implementação |
|---|---|
| **Criptografia em trânsito** | TLS 1.2+ obrigatório em todas as comunicações |
| **Criptografia em repouso** | Azure-managed keys (Cosmos DB, Blob, Key Vault) |
| **Data residency** | Todos os recursos na região Brazil South |
| **Retenção de dados** | Transcripts raw: 90 dias; Atas: indefinido; Cosmos TTL configurável |
| **PII handling** | Nomes e emails de participantes são dados pessoais — documentar no ROPA |
| **Conditional Access** | App Registration incluída nas políticas de Conditional Access do tenant |

---

## 8. Licenciamento Necessário

### 8.1 Microsoft 365 / Teams

| Requisito | Licença Mínima | Observação |
|---|---|---|
| **Transcrição de reunião** | Microsoft Teams Premium **ou** Microsoft 365 E5 | Transcrição automática requer Teams Premium ou E5. E3 permite transcrição manual apenas |
| **Gravação de reunião** | Microsoft 365 E3+ (com OneDrive/SharePoint) | Não obrigatório para a solução — transcript é suficiente |
| **Graph API (Application)** | Qualquer licença Microsoft 365 | Desde que o admin consinta as permissões |
| **Intelligent Recap** | Teams Premium | Opcional — concorrente/complementar à nossa solução |

> **Decisão:** A solução foi projetada para funcionar com **transcript** como fonte primária. Recording é consultado como fallback mas não é processado diretamente (evita custo de transcrição de áudio).

### 8.2 Azure

| Serviço | Modelo de Cobrança |
|---|---|
| **Azure Functions** | Consumption: por execução + tempo de execução; Premium: por instância |
| **Cosmos DB Serverless** | Por RU consumida + storage (GB/mês) |
| **Blob Storage** | Por GB armazenado + operações |
| **Azure OpenAI (GPT-4o)** | Por 1K tokens (input + output) |
| **Key Vault** | Por operação (transações) |
| **Application Insights** | Por GB ingerido |

### 8.3 Pré-requisitos Organizacionais

- [x] Admin consent para as Graph permissions listadas
- [x] Política de transcrição habilitada no Teams Admin Center
- [x] Azure subscription com cota para Azure OpenAI aprovada
- [x] Site SharePoint criado para armazenar atas
- [x] Mailbox de serviço para envio de emails (se habilitado)

---

## 9. Observabilidade

### 9.1 Stack de Observabilidade

```
Application Insights
├── Distributed Tracing (operation_Id para correlacionar todas as Functions)
├── Custom Metrics (meetingsProcessed, transcriptSize, aiLatency)
├── Custom Events (MeetingProcessed, DecisionExtracted, ActionItemCreated)
├── Dependency Tracking (Graph API, OpenAI, Cosmos DB)
└── Exceptions (com stack trace completo)

Log Analytics Workspace
├── Logs de Azure Functions (FunctionAppLogs)
├── Logs de Cosmos DB (DataPlaneRequests)
├── Logs de Key Vault (AuditEvent)
├── Logs de Storage (StorageRead, StorageWrite)
└── Queries KQL customizadas
```

### 9.2 Métricas Customizadas

| Métrica | Tipo | Descrição |
|---|---|---|
| `meetings.processed.count` | Counter | Total de reuniões processadas |
| `meetings.processing.duration_ms` | Histogram | Tempo total de processamento (webhook → notificação) |
| `transcript.size_bytes` | Histogram | Tamanho dos transcripts processados |
| `openai.tokens.used` | Counter | Tokens consumidos no OpenAI |
| `openai.latency_ms` | Histogram | Latência das chamadas ao OpenAI |
| `decisions.extracted.count` | Counter | Total de decisões extraídas |
| `action_items.extracted.count` | Counter | Total de ações extraídas |
| `notifications.sent.count` | Counter | Cards/emails enviados |
| `errors.count` | Counter | Erros por tipo e etapa |

### 9.3 Alertas

| Alerta | Condição | Severidade | Ação |
|---|---|---|---|
| **Processing Failure** | `errors.count` > 3 em 15 min | Sev 2 | Notificar equipe no Teams |
| **High Latency** | `meetings.processing.duration_ms` P95 > 5 min | Sev 3 | Investigar gargalo |
| **OpenAI Rate Limit** | HTTP 429 do OpenAI > 5 em 5 min | Sev 2 | Verificar quota |
| **Queue Depth** | Mensagens na dead-letter > 0 | Sev 1 | Investigar imediatamente |
| **Subscription Expiring** | Subscription Graph expira em < 6h | Sev 2 | Verificar renewal function |
| **Cosmos DB Throttling** | HTTP 429 do Cosmos > 10 em 5 min | Sev 3 | Avaliar autoscale |

### 9.4 Dashboard (Azure Workbook)

Workbook consolidado com:

1. **Visão geral** — Reuniões processadas hoje/semana/mês, taxa de sucesso
2. **Pipeline** — Latência por etapa (coleta → AI → geração → notificação)
3. **Custos AI** — Tokens consumidos, custo estimado por reunião
4. **Erros** — Top erros, dead-letter queue status
5. **Graph API** — Latência e throttling das chamadas Graph

---

## 10. Estratégia de Deploy

### 10.1 Infraestrutura como Código (IaC)

**Ferramenta escolhida:** Bicep (nativo Azure, sem dependência externa)

```
infra/
├── main.bicep                  # Orquestrador principal
├── modules/
│   ├── function-app.bicep      # Azure Functions + App Service Plan
│   ├── cosmos-db.bicep         # Cosmos DB Account + Database + Containers
│   ├── storage.bicep           # Storage Account (Blobs + Queues)
│   ├── key-vault.bicep         # Key Vault + Access Policies
│   ├── monitoring.bicep        # App Insights + Log Analytics + Alerts
│   ├── openai.bicep            # Azure OpenAI + Deployment
│   └── networking.bicep        # VNET + Private Endpoints (prd only)
├── parameters/
│   ├── dev.bicepparam
│   ├── stg.bicepparam
│   └── prd.bicepparam
└── scripts/
    ├── deploy.ps1              # Script de deploy local
    └── graph-permissions.ps1   # Configura App Registration + consent
```

### 10.2 Ambientes

| Ambiente | Propósito | Infra | Deploy |
|---|---|---|---|
| **dev** | Desenvolvimento e testes locais | Consumption, Cosmos Serverless, sem VNET | Push to branch `develop` |
| **stg** | Validação pré-produção | Consumption, Cosmos Serverless, sem VNET | PR merge to `main` |
| **prd** | Produção | Premium EP1, Cosmos Serverless, VNET + Private Endpoints | Release tag `v*` |

### 10.3 CI/CD Pipeline (Azure DevOps)

```yaml
# Pipeline simplificado (azure-pipelines.yml)

trigger:
  branches:
    include: [main, develop]
  tags:
    include: ['v*']

stages:
  - stage: Build
    jobs:
      - job: BuildFunctions
        steps:
          - task: DotNetCoreCLI@2     # ou Node, Python — TBD
            inputs:
              command: 'publish'
          - publish: $(Build.ArtifactStagingDirectory)

  - stage: DeployDev
    condition: eq(variables['Build.SourceBranch'], 'refs/heads/develop')
    jobs:
      - deployment: DeployToDev
        environment: 'dev'
        strategy:
          runOnce:
            deploy:
              steps:
                - task: AzureCLI@2
                  inputs:
                    scriptType: 'bash'
                    scriptLocation: 'inlineScript'
                    inlineScript: |
                      az deployment group create \
                        --resource-group rg-teams-secretary-dev \
                        --template-file infra/main.bicep \
                        --parameters infra/parameters/dev.bicepparam
                - task: AzureFunctionApp@2
                  inputs:
                    azureSubscription: 'azure-service-connection'
                    appName: 'func-teams-secretary-dev'

  - stage: DeployStg
    condition: eq(variables['Build.SourceBranch'], 'refs/heads/main')
    jobs:
      - deployment: DeployToStg
        environment: 'staging'
        strategy:
          runOnce:
            deploy:
              steps:
                # Bicep deploy + Function deploy (similar a dev)

  - stage: DeployPrd
    condition: startsWith(variables['Build.SourceBranch'], 'refs/tags/v')
    jobs:
      - deployment: DeployToPrd
        environment: 'production'    # Requer approval gate
        strategy:
          runOnce:
            deploy:
              steps:
                # Bicep deploy + Function deploy (com VNET)
```

### 10.4 Checklist de Primeiro Deploy

1. [ ] Criar App Registration no Entra ID
2. [ ] Solicitar Admin Consent para Graph permissions
3. [ ] Gerar certificado X.509 e armazenar no Key Vault
4. [ ] Executar `infra/main.bicep` para provisionar recursos
5. [ ] Configurar Application Access Policy para Mail.Send
6. [ ] Habilitar transcrição no Teams Admin Center
7. [ ] Deploy das Azure Functions
8. [ ] Criar subscription no Graph (`/communications/callRecords`)
9. [ ] Testar com reunião de validação
10. [ ] Configurar alertas e dashboard

---

## 11. Riscos e Mitigações

### 11.1 Riscos Técnicos

| # | Risco | Probabilidade | Impacto | Mitigação |
|---|---|---|---|---|
| R1 | **Transcript não disponível após fim da reunião** — delay de minutos a horas no Graph | Alta | Alto | Polling com exponential backoff; Timer Function como fallback; armazenar callRecordId e re-processar |
| R2 | **Graph API rate limiting** (429) em tenants com alto volume | Média | Médio | Implementar retry com backoff; batch requests onde possível; monitorar headers `Retry-After` |
| R3 | **Azure OpenAI quota insuficiente** para volume de reuniões | Média | Alto | Solicitar aumento de quota proativamente; implementar fila de prioridade; fallback para modelo menor (GPT-4o-mini) |
| R4 | **Qualidade da extração por IA** — alucinações, itens inventados | Alta | Alto | Structured output com JSON schema; validação programática; confidence score; human-in-the-loop para atas críticas |
| R5 | **Transcrição em múltiplos idiomas** na mesma reunião | Média | Médio | Detectar idioma no transcript; instruir OpenAI a manter idioma original; normalizar output para PT-BR |
| R6 | **Reuniões muito longas** (>2h) excedem context window do GPT-4o | Baixa | Alto | Chunking do transcript com summarização intermediária; usar context window de 128K tokens |
| R7 | **Alteração de APIs do Graph** (breaking changes) | Baixa | Alto | Usar versão específica da API (v1.0, não beta); monitorar Microsoft 365 Roadmap; testes de integração |

### 11.2 Riscos Organizacionais

| # | Risco | Probabilidade | Impacto | Mitigação |
|---|---|---|---|---|
| R8 | **Admin consent negado** pelo time de segurança | Média | Crítico | Apresentar análise de permissões com justificativa; propor Application Access Policies; agendar reunião com TI |
| R9 | **Licenciamento Teams Premium** não disponível para todos os usuários | Média | Alto | Identificar quais usuários precisam de transcrição; propor licenças E5 como alternativa; MVP com grupo piloto |
| R10 | **Resistência dos usuários** — preocupação com "vigilância" | Alta | Médio | Comunicação clara sobre opt-in; transparência no processamento; Adaptive Card explica o que foi capturado |
| R11 | **LGPD / Proteção de dados** — transcrições contêm dados pessoais | Alta | Alto | ROPA atualizado; política de retenção clara; direito de exclusão implementado; consentimento via meeting policy |

### 11.3 Riscos de Custo

| # | Risco | Probabilidade | Impacto | Mitigação |
|---|---|---|---|---|
| R12 | **Custo de OpenAI escala com volume** de reuniões | Média | Médio | Monitorar tokens/reunião; otimizar prompts; usar GPT-4o-mini para reuniões curtas; budget alerts no Azure |
| R13 | **Cosmos DB RU spikes** em horários de pico | Baixa | Baixo | Serverless absorve spikes; monitorar consumo; autoscale se necessário |

---

## 12. Estimativa de Custo (Azure)

### 12.1 Premissas

| Parâmetro | Valor Estimado |
|---|---|
| Reuniões processadas/mês | 500 |
| Duração média da reunião | 45 minutos |
| Tamanho médio do transcript | 30 KB (VTT) |
| Tokens médios por processamento (input + output) | 8.000 tokens |
| Região Azure | Brazil South |

### 12.2 Estimativa Mensal (Produção)

| Recurso | Cálculo | Custo Estimado (USD/mês) |
|---|---|---|
| **Azure Functions (Premium EP1)** | 1 instância × ~$150/mês | $150.00 |
| **Cosmos DB Serverless** | ~500 reuniões × ~10 RUs/operação × ~5 ops/reunião + 1 GB storage | $5.00 - $15.00 |
| **Blob Storage (LRS)** | ~15 MB/mês de transcripts + atas + dados processados | $0.50 |
| **Azure OpenAI (GPT-4o)** | 500 reuniões × 8K tokens × ($0.005/1K input + $0.015/1K output) | $40.00 - $60.00 |
| **Key Vault** | ~5.000 operações/mês | $0.15 |
| **Application Insights** | ~500 MB/mês de telemetria | $1.15 |
| **Log Analytics** | ~1 GB/mês | $2.76 |
| **Queue Storage** | ~10.000 operações/mês | $0.01 |
| **Total Estimado** | | **$200 - $230/mês** |

### 12.3 Cenário Consumption (Alternativa para menor custo)

Se o volume de reuniões não justificar Premium EP1:

| Recurso | Custo Estimado (USD/mês) |
|---|---|
| **Azure Functions (Consumption)** | $0 - $5 (free tier: 1M execuções/mês) |
| **Demais recursos** | ~$50 - $80 |
| **Total (Consumption)** | **$50 - $85/mês** |

> **Trade-off:** Consumption Plan tem cold start (até 10s na primeira execução após idle). Para webhooks do Graph, isso é aceitável pois o processamento não é real-time.

### 12.4 Custo por Reunião

| Cenário | Custo/Reunião |
|---|---|
| **Premium (produção)** | ~$0.40 - $0.46 |
| **Consumption (menor custo)** | ~$0.10 - $0.17 |

> Valores estimados. O custo real depende do tamanho dos transcripts, complexidade das reuniões e região Azure. Recomenda-se monitorar o Cost Management do Azure após o primeiro mês de operação.

---

## Apêndices

### A. Prompt Template (Azure OpenAI)

```
System:
Você é um assistente especializado em gerar atas de reunião estruturadas.
Analise o transcript fornecido e extraia as seguintes informações em formato JSON:

{
  "topicos": [
    {
      "titulo": "string",
      "resumo": "string",
      "participantes_envolvidos": ["string"],
      "timestamp_inicio": "string (HH:MM:SS)",
      "timestamp_fim": "string (HH:MM:SS)"
    }
  ],
  "decisoes": [
    {
      "descricao": "string",
      "contexto": "string",
      "decidido_por": "string",
      "timestamp": "string"
    }
  ],
  "acoes": [
    {
      "descricao": "string",
      "responsavel": "string",
      "prazo": "string (YYYY-MM-DD ou 'não definido')",
      "prioridade": "alta|média|baixa"
    }
  ],
  "resumo_executivo": "string (3-5 frases)",
  "sentimento_geral": "positivo|neutro|negativo|misto",
  "palavras_chave": ["string"],
  "duracao_efetiva_minutos": "number",
  "idioma_predominante": "string"
}

Regras:
- Extraia APENAS informações explícitas no transcript
- NÃO invente decisões ou ações que não foram mencionadas
- Se não houver decisões, retorne array vazio
- Atribua ações apenas quando o nome do responsável for explicitamente mencionado
- O resumo deve ser objetivo e em terceira pessoa
```

### B. Adaptive Card Template (Simplificado)

```json
{
  "type": "AdaptiveCard",
  "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
  "version": "1.5",
  "body": [
    {
      "type": "TextBlock",
      "text": "📋 Ata de Reunião",
      "weight": "Bolder",
      "size": "Large"
    },
    {
      "type": "TextBlock",
      "text": "${meetingSubject}",
      "weight": "Bolder",
      "size": "Medium"
    },
    {
      "type": "FactSet",
      "facts": [
        { "title": "Data", "value": "${meetingDate}" },
        { "title": "Duração", "value": "${duration} min" },
        { "title": "Participantes", "value": "${participantCount}" }
      ]
    },
    {
      "type": "TextBlock",
      "text": "Resumo Executivo",
      "weight": "Bolder"
    },
    {
      "type": "TextBlock",
      "text": "${summaryText}",
      "wrap": true
    },
    {
      "type": "TextBlock",
      "text": "✅ Decisões: ${decisionsCount} | 📌 Ações: ${actionsCount}",
      "weight": "Bolder"
    }
  ],
  "actions": [
    {
      "type": "Action.OpenUrl",
      "title": "Ver Ata Completa",
      "url": "${sharepointUrl}"
    }
  ]
}
```

### C. Referências

| Documento | URL |
|---|---|
| Graph API — Online Meetings | https://learn.microsoft.com/graph/api/resources/onlinemeeting |
| Graph API — Transcripts | https://learn.microsoft.com/graph/api/resources/calltranscript |
| Graph API — Call Records | https://learn.microsoft.com/graph/api/resources/callrecords-api-overview |
| Graph API — Change Notifications | https://learn.microsoft.com/graph/webhooks |
| Azure OpenAI — Structured Outputs | https://learn.microsoft.com/azure/ai-services/openai/how-to/structured-outputs |
| Adaptive Cards | https://adaptivecards.io |
| Cosmos DB Serverless | https://learn.microsoft.com/azure/cosmos-db/serverless |
| Azure Functions Premium Plan | https://learn.microsoft.com/azure/azure-functions/functions-premium-plan |

---

> **Wagner — Arquiteto de Software, Squad MEQ**  
> *"Tecnologia chata que funciona. Cada decisão aqui serve ao produto e à produtividade do time."*
