# Especificação de APIs Microsoft Graph — Secretário de Reunião Teams

> **Autor:** Igor — Especialista em Integração, Squad MEQ
> **Versão:** 1.0.0
> **Data:** 2026-06-08
> **Status:** Draft

---

## 1. Visão Geral das APIs Necessárias

O agente "Secretário de Reunião Teams" consome as seguintes APIs do Microsoft Graph para capturar dados de reuniões, processar conteúdo e devolver atas/resumos.

| # | API | Endpoint Principal | Método | Permissão Delegated | Permissão Application | Admin Consent | Observação |
|---|-----|--------------------|--------|---------------------|-----------------------|---------------|------------|
| 1 | Online Meetings | `/users/{userId}/onlineMeetings/{meetingId}` | GET | `OnlineMeetings.Read` | `OnlineMeetings.Read.All` | Sim | Metadados da reunião |
| 2 | Meeting Transcripts (lista) | `/users/{userId}/onlineMeetings/{meetingId}/transcripts` | GET | `OnlineMeetingTranscript.Read.All` | `OnlineMeetingTranscript.Read.All` | Sim | Lista transcrições disponíveis |
| 3 | Meeting Transcripts (conteúdo) | `/users/{userId}/onlineMeetings/{meetingId}/transcripts/{transcriptId}/content` | GET | `OnlineMeetingTranscript.Read.All` | `OnlineMeetingTranscript.Read.All` | Sim | Formatos: `text/vtt`, `application/vnd.openxmlformats-officedocument.wordprocessingml.document` |
| 4 | Meeting Recordings (lista) | `/users/{userId}/onlineMeetings/{meetingId}/recordings` | GET | `OnlineMeetingRecording.Read.All` | `OnlineMeetingRecording.Read.All` | Sim | Lista gravações |
| 5 | Meeting Recordings (conteúdo) | `/users/{userId}/onlineMeetings/{meetingId}/recordings/{recordingId}/content` | GET | `OnlineMeetingRecording.Read.All` | `OnlineMeetingRecording.Read.All` | Sim | Stream binário do vídeo |
| 6 | Attendance Reports | `/users/{userId}/onlineMeetings/{meetingId}/attendanceReports` | GET | `OnlineMeetingArtifact.Read.All` | `OnlineMeetingArtifact.Read.All` | Sim | Relatórios de presença |
| 7 | Attendance Records | `/users/{userId}/onlineMeetings/{meetingId}/attendanceReports/{reportId}/attendanceRecords` | GET | `OnlineMeetingArtifact.Read.All` | `OnlineMeetingArtifact.Read.All` | Sim | Detalhes por participante |
| 8 | Call Records | `/communications/callRecords/{id}` | GET | — | `CallRecords.Read.All` | Sim | Somente Application; métricas de chamada |
| 9 | Change Notifications | `/subscriptions` | POST | Varia por recurso | Varia por recurso | Sim | Webhooks para eventos em tempo real |
| 10 | Chat Messages (leitura) | `/chats/{chatId}/messages` | GET | `Chat.Read` | `Chat.Read.All` | Sim (App) | Mensagens do chat da reunião |
| 11 | Chat Messages (envio) | `/chats/{chatId}/messages` | POST | `Chat.ReadWrite` | `Chat.ReadWrite.All` | Sim (App) | Envio de ata/Adaptive Card |

---

## 2. Online Meetings API

### Finalidade

Obter metadados completos de uma reunião Teams: assunto, horários, participantes, link de acesso.

### Endpoints

```
GET /users/{userId}/onlineMeetings/{meetingId}
GET /users/{userId}/onlineMeetings?$filter=JoinWebUrl eq '{joinWebUrl}'
```

### Permissões

| Tipo | Permissão | Admin Consent |
|------|-----------|---------------|
| Delegated | `OnlineMeetings.Read` | Não |
| Delegated | `OnlineMeetings.ReadWrite` | Não |
| Application | `OnlineMeetings.Read.All` | Sim |

### Dados Retornados (Propriedades Principais)

```json
{
  "id": "AAMkAG...",
  "subject": "Sprint Planning Q3",
  "startDateTime": "2026-06-08T14:00:00Z",
  "endDateTime": "2026-06-08T15:00:00Z",
  "joinWebUrl": "https://teams.microsoft.com/l/meetup-join/...",
  "chatInfo": {
    "threadId": "19:meeting_abc123@thread.v2",
    "messageId": "0"
  },
  "participants": {
    "organizer": {
      "identity": {
        "user": {
          "id": "user-guid",
          "displayName": "Alessandro Lisboa"
        }
      }
    },
    "attendees": [
      {
        "identity": {
          "user": {
            "id": "attendee-guid",
            "displayName": "Participante A"
          }
        },
        "role": "attendee"
      }
    ]
  },
  "videoTeleconferenceId": "...",
  "externalId": "..."
}
```

### Observações

- O `chatInfo.threadId` é essencial para acessar mensagens de chat da reunião.
- O `meetingId` pode ser obtido via Change Notification ou filtro por `JoinWebUrl`.
- Para fluxo application-only, o `userId` deve ser o organizador da reunião.

---

## 3. Meeting Transcripts API

### Finalidade

Capturar a transcrição completa de uma reunião Teams para processamento por IA.

### Endpoints

```
GET /users/{userId}/onlineMeetings/{meetingId}/transcripts
GET /users/{userId}/onlineMeetings/{meetingId}/transcripts/{transcriptId}/content
```

### Permissões

| Tipo | Permissão | Admin Consent |
|------|-----------|---------------|
| Delegated | `OnlineMeetingTranscript.Read.All` | Sim |
| Application | `OnlineMeetingTranscript.Read.All` | Sim |

### Formatos de Conteúdo

| Accept Header | Formato | Uso Recomendado |
|---------------|---------|-----------------|
| `text/vtt` | WebVTT (legendas com timestamps) | Processamento por IA — preferido |
| `application/vnd.openxmlformats-officedocument.wordprocessingml.document` | DOCX | Armazenamento/arquivo |

### Exemplo de Request

```http
GET /users/{userId}/onlineMeetings/{meetingId}/transcripts/{transcriptId}/content
Accept: text/vtt
Authorization: Bearer {token}
```

### Exemplo de Resposta (VTT)

```vtt
WEBVTT

00:00:05.000 --> 00:00:10.000
<v Alessandro Lisboa>Vamos começar a Sprint Planning.</v>

00:00:10.500 --> 00:00:18.000
<v Participante A>Tenho um ponto sobre a estimativa da story 42.</v>
```

### Considerações Críticas

| Item | Detalhe |
|------|---------|
| **Disponibilidade** | A transcrição pode levar de 1 a 5 minutos para ficar disponível após o fim da reunião. Implementar polling com backoff. |
| **Pré-requisito** | A transcrição precisa estar habilitada na reunião (pelo organizador ou por política do tenant). |
| **Tamanho** | Reuniões longas geram transcrições grandes. Considerar chunking para processamento com Azure OpenAI. |
| **Idioma** | O VTT preserva o idioma falado. O Azure OpenAI lida bem com pt-BR. |
| **Retry** | Se retornar `404`, a transcrição ainda não está pronta. Retry com exponential backoff (2s, 4s, 8s, 16s, max 5min). |

### Estratégia de Polling

```
Intervalo inicial: 30 segundos após fim da reunião
Backoff: exponencial com jitter (30s → 60s → 120s → 240s)
Timeout máximo: 10 minutos
Fallback: registrar log e notificar via chat que a transcrição não ficou disponível
```

---

## 4. Meeting Recordings API

### Finalidade

Acessar metadados e conteúdo de gravações para referência ou processamento adicional.

### Endpoints

```
GET /users/{userId}/onlineMeetings/{meetingId}/recordings
GET /users/{userId}/onlineMeetings/{meetingId}/recordings/{recordingId}/content
```

### Permissões

| Tipo | Permissão | Admin Consent |
|------|-----------|---------------|
| Delegated | `OnlineMeetingRecording.Read.All` | Sim |
| Application | `OnlineMeetingRecording.Read.All` | Sim |

### Dados Retornados (Lista)

```json
{
  "value": [
    {
      "id": "recording-guid",
      "createdDateTime": "2026-06-08T15:05:00Z",
      "recordingContentUrl": "...",
      "meetingOrganizerId": "user-guid"
    }
  ]
}
```

### Observações

| Item | Detalhe |
|------|---------|
| **Conteúdo** | O endpoint `/content` retorna stream binário (video/mp4). |
| **Uso no projeto** | Para o Secretário de Reunião, a transcrição é a fonte primária. A recording serve como backup e referência. |
| **Armazenamento** | Não armazenar localmente — usar URL temporária ou referência ao OneDrive/SharePoint onde o Teams salva. |
| **Disponibilidade** | Semelhante à transcrição: pode levar minutos para ficar disponível. |

---

## 5. Attendance Reports API

### Finalidade

Obter relatórios de presença: quem entrou, quando, quanto tempo ficou.

### Endpoints

```
GET /users/{userId}/onlineMeetings/{meetingId}/attendanceReports
GET /users/{userId}/onlineMeetings/{meetingId}/attendanceReports/{reportId}/attendanceRecords
```

### Permissões

| Tipo | Permissão | Admin Consent |
|------|-----------|---------------|
| Delegated | `OnlineMeetingArtifact.Read.All` | Sim |
| Application | `OnlineMeetingArtifact.Read.All` | Sim |

### Dados Retornados — Attendance Report

```json
{
  "id": "report-guid",
  "totalParticipantCount": 8,
  "meetingStartDateTime": "2026-06-08T14:00:00Z",
  "meetingEndDateTime": "2026-06-08T15:02:00Z"
}
```

### Dados Retornados — Attendance Records

```json
{
  "value": [
    {
      "id": "record-guid",
      "emailAddress": "alessandro@foursys.com.br",
      "identity": {
        "displayName": "Alessandro Lisboa"
      },
      "role": "Organizer",
      "totalAttendanceInSeconds": 3720,
      "attendanceIntervals": [
        {
          "joinDateTime": "2026-06-08T13:58:00Z",
          "leaveDateTime": "2026-06-08T15:00:00Z",
          "durationInSeconds": 3720
        }
      ]
    }
  ]
}
```

### Uso no Projeto

- Incluir lista de presença na ata gerada.
- Calcular duração efetiva de participação.
- Identificar participantes que entraram/saíram múltiplas vezes.

---

## 6. Call Records API

### Finalidade

Acessar registros detalhados de chamadas para métricas e diagnóstico.

### Endpoint

```
GET /communications/callRecords/{id}
GET /communications/callRecords/{id}?$expand=sessions($expand=segments)
```

### Permissões

| Tipo | Permissão | Admin Consent |
|------|-----------|---------------|
| Application | `CallRecords.Read.All` | Sim |

> **Nota:** Esta API está disponível somente para permissões Application. Não existe permissão Delegated.

### Dados Retornados

```json
{
  "id": "call-record-guid",
  "type": "groupCall",
  "modalities": ["audio", "video", "screenSharing"],
  "startDateTime": "2026-06-08T14:00:00Z",
  "endDateTime": "2026-06-08T15:02:00Z",
  "organizer": {
    "user": {
      "id": "user-guid",
      "displayName": "Alessandro Lisboa"
    }
  },
  "participants": [...],
  "sessions": [
    {
      "id": "session-guid",
      "caller": {...},
      "callee": {...},
      "segments": [...]
    }
  ]
}
```

### Uso no Projeto

- Correlacionar com dados de attendance para enriquecer a ata.
- Obter métricas de qualidade (jitter, packet loss) se necessário.
- O `id` do callRecord é recebido via Change Notification.

---

## 7. Change Notifications (Webhooks)

### Finalidade

Receber notificações em tempo real quando reuniões começam, terminam, ou artefatos ficam disponíveis.

### Endpoint

```
POST /subscriptions
```

### Recursos Disponíveis para Subscription

| Resource | Descrição | Permissão Application |
|----------|-----------|-----------------------|
| `/communications/callRecords` | Notifica quando um call record é criado | `CallRecords.Read.All` |
| `/communications/onlineMeetings/getAllTranscripts` | Notifica quando transcrições ficam disponíveis | `OnlineMeetingTranscript.Read.All` |
| `/communications/onlineMeetings/getAllRecordings` | Notifica quando gravações ficam disponíveis | `OnlineMeetingRecording.Read.All` |
| `/users/{userId}/onlineMeetings/getAllTranscripts` | Transcrições de um usuário específico | `OnlineMeetingTranscript.Read.All` |
| `/users/{userId}/onlineMeetings/getAllRecordings` | Gravações de um usuário específico | `OnlineMeetingRecording.Read.All` |

### Exemplo de Criação de Subscription

```json
POST /subscriptions
Content-Type: application/json

{
  "changeType": "created",
  "notificationUrl": "https://func-meq-teams-agent.azurewebsites.net/api/webhook/graph",
  "resource": "/communications/onlineMeetings/getAllTranscripts",
  "expirationDateTime": "2026-06-11T14:00:00Z",
  "clientState": "meq-secretario-reuniao-v1",
  "includeResourceData": true,
  "encryptionCertificate": "{base64-encoded-cert}",
  "encryptionCertificateId": "cert-id-meq"
}
```

### Lifecycle da Subscription

```
┌──────────────────────────────────────────────────────────┐
│                  LIFECYCLE DE SUBSCRIPTION                │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  1. CRIAÇÃO                                              │
│     POST /subscriptions                                  │
│     → Graph valida notificationUrl (validation token)    │
│     → Retorna subscription com id e expirationDateTime   │
│                                                          │
│  2. VALIDAÇÃO DO ENDPOINT                                │
│     Graph envia GET para notificationUrl com:            │
│     ?validationToken={token}                             │
│     → Endpoint DEVE retornar 200 com o token no body    │
│     → Content-Type: text/plain                           │
│     → Timeout: 10 segundos                               │
│                                                          │
│  3. RENOVAÇÃO (antes da expiração)                       │
│     PATCH /subscriptions/{id}                            │
│     Body: { "expirationDateTime": "nova-data" }          │
│     → Max lifetime varia por recurso (ver tabela)        │
│                                                          │
│  4. EXPIRAÇÃO                                            │
│     Se não renovada, a subscription expira silentemente  │
│     → Implementar job de renovação com margem de 12h     │
│                                                          │
│  5. DELEÇÃO                                              │
│     DELETE /subscriptions/{id}                           │
│     → Cleanup ao desativar o agente                      │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

### Tempo Máximo de Vida por Recurso

| Recurso | Max Lifetime |
|---------|--------------|
| `/communications/callRecords` | 4230 minutos (~2,9 dias) |
| `/communications/onlineMeetings/getAllTranscripts` | 4230 minutos (~2,9 dias) |
| `/communications/onlineMeetings/getAllRecordings` | 4230 minutos (~2,9 dias) |

### Validation Token Flow

```
1. App cria subscription via POST /subscriptions
2. Graph envia GET para notificationUrl:
   GET https://func-meq.../api/webhook/graph?validationToken=abc123
3. Azure Function responde:
   HTTP 200
   Content-Type: text/plain
   Body: abc123
4. Graph confirma subscription como ativa
```

### Requisitos de Criptografia (includeResourceData=true)

Quando `includeResourceData` é `true`, o Graph criptografa dados sensíveis no payload da notificação:

1. Gerar um par de chaves RSA (2048 bits mínimo).
2. Fornecer o certificado público (base64) na criação da subscription.
3. O Graph usa a chave pública para criptografar uma chave simétrica AES.
4. O payload de notificação contém `encryptedContent` com:
   - `data`: conteúdo criptografado com AES
   - `dataKey`: chave AES criptografada com RSA
   - `dataSignature`: HMAC-SHA256 para validação
5. Azure Function descriptografa: RSA → AES key → AES decrypt → dados.

### Formato da Notificação Recebida

```json
{
  "value": [
    {
      "subscriptionId": "sub-guid",
      "changeType": "created",
      "clientState": "meq-secretario-reuniao-v1",
      "resource": "communications/onlineMeetings('meeting-id')/transcripts('transcript-id')",
      "resourceData": {
        "@odata.type": "#Microsoft.Graph.callTranscript",
        "id": "transcript-id",
        "meetingId": "meeting-id",
        "meetingOrganizerId": "user-id"
      },
      "tenantId": "tenant-guid"
    }
  ]
}
```

---

## 8. Chat Messages API (Leitura)

### Finalidade

Capturar mensagens trocadas no chat da reunião para enriquecer a ata (links compartilhados, decisões textuais, referências).

### Endpoints

```
GET /chats/{chatId}/messages
GET /chats/{chatId}/messages?$top=50&$orderby=createdDateTime desc
```

> O `chatId` corresponde ao `chatInfo.threadId` retornado pela Online Meetings API.

### Permissões

| Tipo | Permissão | Admin Consent |
|------|-----------|---------------|
| Delegated | `Chat.Read` | Não |
| Application | `Chat.Read.All` | Sim |

### Dados Retornados

```json
{
  "value": [
    {
      "id": "msg-id",
      "messageType": "message",
      "createdDateTime": "2026-06-08T14:15:00Z",
      "from": {
        "user": {
          "id": "user-guid",
          "displayName": "Alessandro Lisboa"
        }
      },
      "body": {
        "contentType": "html",
        "content": "<p>Segue o link do documento: <a href=\"...\">Proposta Q3</a></p>"
      },
      "attachments": [
        {
          "id": "att-id",
          "contentType": "reference",
          "contentUrl": "https://foursys.sharepoint.com/...",
          "name": "proposta-q3.docx"
        }
      ]
    }
  ]
}
```

### Observações

- Mensagens do tipo `systemEventMessage` indicam eventos (entrada/saída de participantes).
- Filtrar por `messageType eq 'message'` para obter somente mensagens de texto.
- Paginação via `@odata.nextLink` para reuniões com muito chat.

---

## 9. Send Chat Message / Adaptive Card

### Finalidade

Enviar a ata/resumo gerado como mensagem no chat da reunião, utilizando Adaptive Cards para formatação rica.

### Endpoint

```
POST /chats/{chatId}/messages
```

### Permissões

| Tipo | Permissão | Admin Consent |
|------|-----------|---------------|
| Delegated | `Chat.ReadWrite` | Não |
| Application | `Chat.ReadWrite.All` | Sim |

### Exemplo de Request — Adaptive Card

```json
POST /chats/{chatId}/messages
Content-Type: application/json

{
  "body": {
    "contentType": "html",
    "content": "<attachment id=\"ata-reuniao\"></attachment>"
  },
  "attachments": [
    {
      "id": "ata-reuniao",
      "contentType": "application/vnd.microsoft.card.adaptive",
      "contentUrl": null,
      "content": "{\"$schema\":\"http://adaptivecards.io/schemas/adaptive-card.json\",\"type\":\"AdaptiveCard\",\"version\":\"1.5\",\"body\":[{\"type\":\"TextBlock\",\"text\":\"📋 Ata de Reunião\",\"weight\":\"bolder\",\"size\":\"large\"},{\"type\":\"TextBlock\",\"text\":\"Sprint Planning Q3\",\"weight\":\"bolder\",\"size\":\"medium\"},{\"type\":\"FactSet\",\"facts\":[{\"title\":\"Data\",\"value\":\"08/06/2026 14:00-15:00\"},{\"title\":\"Participantes\",\"value\":\"8 presentes\"},{\"title\":\"Organizador\",\"value\":\"Alessandro Lisboa\"}]},{\"type\":\"TextBlock\",\"text\":\"**Resumo Executivo**\",\"weight\":\"bolder\",\"wrap\":true},{\"type\":\"TextBlock\",\"text\":\"Foram definidas as prioridades do Q3 com foco em...\",\"wrap\":true},{\"type\":\"TextBlock\",\"text\":\"**Ações Definidas**\",\"weight\":\"bolder\",\"wrap\":true},{\"type\":\"TextBlock\",\"text\":\"1. [Alessandro] Revisar backlog até 10/06\\n2. [Participante A] Preparar estimativas story 42\",\"wrap\":true}],\"actions\":[{\"type\":\"Action.OpenUrl\",\"title\":\"Ver ata completa\",\"url\":\"https://foursys.sharepoint.com/.../ata-20260608.pdf\"}]}"
    }
  ]
}
```

### Estrutura Recomendada da Adaptive Card (Ata)

```
┌─────────────────────────────────────────┐
│ 📋 Ata de Reunião                       │
│ Sprint Planning Q3                      │
├─────────────────────────────────────────┤
│ Data:          08/06/2026 14:00-15:00   │
│ Participantes: 8 presentes              │
│ Organizador:   Alessandro Lisboa        │
├─────────────────────────────────────────┤
│ Resumo Executivo                        │
│ Foram definidas as prioridades do Q3... │
├─────────────────────────────────────────┤
│ Tópicos Discutidos                      │
│ 1. Priorização do backlog               │
│ 2. Estimativa de stories                │
│ 3. Alocação de recursos                 │
├─────────────────────────────────────────┤
│ Ações Definidas                         │
│ ☐ [Alessandro] Revisar backlog          │
│ ☐ [Participante A] Estimativas story 42 │
├─────────────────────────────────────────┤
│ [ Ver ata completa ]                    │
└─────────────────────────────────────────┘
```

### Observações

- O campo `content` do attachment deve ser uma string JSON escapada (não objeto).
- Limite de tamanho do card: ~28 KB. Para atas longas, incluir resumo e link para documento completo.
- Testar o card no [Adaptive Cards Designer](https://adaptivecards.io/designer/) antes de deploy.

---

## 10. App Registration Setup

### Passo a Passo

#### 10.1 Criar App Registration no Azure AD

1. Acesse [Azure Portal](https://portal.azure.com) → **Microsoft Entra ID** → **App registrations**.
2. Clique em **New registration**.
3. Configure:
   - **Name:** `MEQ-Secretario-Reuniao-Teams`
   - **Supported account types:** "Accounts in this organizational directory only" (Single tenant)
   - **Redirect URI:** Deixar vazio (fluxo client_credentials não usa)
4. Clique em **Register**.
5. Anote: **Application (client) ID** e **Directory (tenant) ID**.

#### 10.2 Configurar Permissões

1. Na App Registration, vá em **API permissions** → **Add a permission** → **Microsoft Graph**.
2. Selecione **Application permissions**.
3. Adicione todas as permissões listadas na Seção 11 (Matriz Consolidada).
4. Clique em **Grant admin consent for [Tenant]** (requer Global Admin ou Privileged Role Admin).

#### 10.3 Criar Certificado (Recomendado)

Certificate-based authentication é mais seguro que client secret para cenários de produção.

```powershell
# Gerar certificado autoassinado (dev/staging)
$cert = New-SelfSignedCertificate `
  -Subject "CN=MEQ-Secretario-Reuniao" `
  -CertStoreLocation "Cert:\CurrentUser\My" `
  -KeyExportPolicy Exportable `
  -KeySpec Signature `
  -KeyLength 2048 `
  -KeyAlgorithm RSA `
  -HashAlgorithm SHA256 `
  -NotAfter (Get-Date).AddYears(2)

# Exportar .cer (público) para upload no Azure AD
Export-Certificate -Cert $cert -FilePath ".\MEQ-Secretario-Reuniao.cer"

# Exportar .pfx (privado) para a Azure Function
$password = ConvertTo-SecureString -String "SenhaForte123!" -Force -AsPlainText
Export-PfxCertificate -Cert $cert -FilePath ".\MEQ-Secretario-Reuniao.pfx" -Password $password
```

4. Na App Registration, vá em **Certificates & secrets** → **Certificates** → **Upload certificate**.
5. Faça upload do arquivo `.cer`.

#### 10.4 Configurar na Azure Function

```
App Settings:
  AZURE_TENANT_ID=<tenant-id>
  AZURE_CLIENT_ID=<client-id>
  AZURE_CLIENT_CERTIFICATE_PATH=/home/site/certs/MEQ-Secretario-Reuniao.pfx
  AZURE_CLIENT_CERTIFICATE_PASSWORD=<referência ao Key Vault>
```

#### 10.5 Managed Identity (Alternativa Recomendada para Azure Functions)

```
1. Na Azure Function → Identity → System assigned → Status: On
2. No Microsoft Entra ID → Enterprise Applications → localizar a Managed Identity
3. Atribuir permissões via PowerShell (Graph não tem UI para MI):
```

```powershell
# Atribuir permissões de Graph à Managed Identity
$graphAppId = "00000003-0000-0000-c000-000000000000"
$sp = Get-MgServicePrincipal -Filter "appId eq '$graphAppId'"
$miObjectId = "<object-id-da-managed-identity>"

# Permissões necessárias
$permissions = @(
    "OnlineMeetings.Read.All",
    "OnlineMeetingTranscript.Read.All",
    "OnlineMeetingRecording.Read.All",
    "OnlineMeetingArtifact.Read.All",
    "CallRecords.Read.All",
    "Chat.Read.All",
    "Chat.ReadWrite.All"
)

foreach ($permName in $permissions) {
    $role = $sp.AppRoles | Where-Object { $_.Value -eq $permName }
    New-MgServicePrincipalAppRoleAssignment `
        -ServicePrincipalId $miObjectId `
        -PrincipalId $miObjectId `
        -ResourceId $sp.Id `
        -AppRoleId $role.Id
}
```

---

## 11. Matriz de Permissões Consolidada

| # | Operação | Permissão | Tipo | Admin Consent | Observação |
|---|----------|-----------|------|---------------|------------|
| 1 | Ler metadados de reuniões | `OnlineMeetings.Read.All` | Application | Sim | Obrigatória |
| 2 | Listar e ler transcrições | `OnlineMeetingTranscript.Read.All` | Application | Sim | Obrigatória — core do projeto |
| 3 | Listar e ler gravações | `OnlineMeetingRecording.Read.All` | Application | Sim | Opcional — somente se for usar recordings |
| 4 | Ler relatórios de presença | `OnlineMeetingArtifact.Read.All` | Application | Sim | Obrigatória — lista de presença na ata |
| 5 | Ler registros de chamada | `CallRecords.Read.All` | Application | Sim | Obrigatória — webhook trigger |
| 6 | Ler mensagens do chat | `Chat.Read.All` | Application | Sim | Recomendada — enriquece a ata |
| 7 | Enviar mensagem/ata no chat | `Chat.ReadWrite.All` | Application | Sim | Obrigatória — envio da ata |

### Permissões Mínimas (MVP)

Para um MVP funcional, o conjunto mínimo é:

```
OnlineMeetings.Read.All
OnlineMeetingTranscript.Read.All
OnlineMeetingArtifact.Read.All
CallRecords.Read.All
Chat.ReadWrite.All
```

### Permissões Completas (Produção)

Adicionar ao MVP:

```
OnlineMeetingRecording.Read.All
Chat.Read.All
```

---

## 12. Rate Limiting e Throttling

### Limites por API

| API / Recurso | Limite | Escopo |
|----------------|--------|--------|
| Microsoft Graph (geral) | 10.000 requests / 10 min | Por app + tenant |
| Subscriptions | 10.000 subscriptions ativas | Por app + tenant |
| Chat Messages | 2 requests/segundo por chat | Por chat thread |
| Call Records | Sem limite documentado específico | Throttle padrão Graph |
| Online Meetings | 2.000 requests / 20 segundos | Por app |

### Headers de Throttle

Quando throttled (HTTP 429), o Graph retorna:

```http
HTTP/1.1 429 Too Many Requests
Retry-After: 30
```

### Estratégia de Retry (Exponential Backoff com Jitter)

```
Tentativa 1: aguardar Retry-After header (ou 2s se ausente)
Tentativa 2: 4s + jitter (0-1s)
Tentativa 3: 8s + jitter (0-2s)
Tentativa 4: 16s + jitter (0-4s)
Tentativa 5: 32s + jitter (0-8s)
Max tentativas: 5
```

### Implementação Recomendada

```typescript
async function graphRequestWithRetry<T>(
  client: Client,
  path: string,
  maxRetries = 5
): Promise<T> {
  for (let attempt = 0; attempt <= maxRetries; attempt++) {
    try {
      return await client.api(path).get();
    } catch (error: any) {
      if (error.statusCode === 429 && attempt < maxRetries) {
        const retryAfter = parseInt(error.headers?.['retry-after'] || '2');
        const backoff = Math.pow(2, attempt) * 1000;
        const jitter = Math.random() * attempt * 1000;
        const delay = Math.max(retryAfter * 1000, backoff) + jitter;
        await new Promise(resolve => setTimeout(resolve, delay));
        continue;
      }
      throw error;
    }
  }
  throw new Error(`Graph request failed after ${maxRetries} retries: ${path}`);
}
```

### Batch Requests

Para múltiplas operações independentes, usar JSON batching:

```json
POST /$batch
Content-Type: application/json

{
  "requests": [
    {
      "id": "1",
      "method": "GET",
      "url": "/users/{userId}/onlineMeetings/{meetingId}"
    },
    {
      "id": "2",
      "method": "GET",
      "url": "/users/{userId}/onlineMeetings/{meetingId}/attendanceReports"
    },
    {
      "id": "3",
      "method": "GET",
      "url": "/chats/{chatId}/messages?$top=50"
    }
  ]
}
```

> Limite de batch: 20 requests por batch. Usar quando possível para reduzir latência e consumo de quota.

---

## 13. Considerações de Segurança

### 13.1 Princípio do Menor Privilégio (Least Privilege)

- Solicitar **somente** as permissões listadas na Seção 11.
- **Não** solicitar permissões genéricas como `User.Read.All` ou `Directory.Read.All`.
- Revisar permissões trimestralmente — remover as que não são mais necessárias.
- Usar Conditional Access Policies para restringir de quais IPs/redes o app pode autenticar.

### 13.2 Rotação de Certificados

| Item | Política |
|------|----------|
| Validade do certificado | Máximo 2 anos |
| Rotação | A cada 12 meses (ou conforme política corporativa) |
| Processo | Upload do novo cert antes de expirar o antigo → testar → remover o antigo |
| Armazenamento | Azure Key Vault — nunca em código ou variáveis de ambiente em texto |
| Alerta | Configurar Azure Monitor alert para 30 dias antes da expiração |

### 13.3 Token Caching

- Usar MSAL built-in token cache (in-memory para Functions, distributed para App Services).
- Tokens de app (client_credentials) duram ~1 hora por padrão.
- MSAL gerencia refresh automaticamente — não implementar lógica manual.
- Para Azure Functions com múltiplas instâncias, considerar distributed cache (Redis) para evitar token requests redundantes.

### 13.4 Audit Logging

| Evento | O que Logar | Destino |
|--------|-------------|---------|
| Autenticação | Token acquisition success/failure, scopes | Application Insights |
| Acesso a dados | Meeting ID acessado, tipo de artefato, user ID | Application Insights + Log Analytics |
| Webhook recebido | Subscription ID, resource type, timestamp | Application Insights |
| Envio de ata | Chat ID, meeting ID, status | Application Insights |
| Erros de permissão | 401/403, endpoint, permissão faltante | Application Insights + Alerta |

### 13.5 Proteção de Dados

- Transcrições e atas contêm dados sensíveis — classificar como **Confidencial**.
- Não persistir transcrições em texto plano — criptografar at rest.
- Definir política de retenção: manter atas processadas por N dias, purgar transcrições brutas após processamento.
- Compliance: verificar requisitos de LGPD para dados de áudio/transcrição.

### 13.6 Network Security

- Azure Functions deve usar Private Endpoints quando possível.
- Webhook endpoint deve validar `clientState` em toda notificação recebida.
- Implementar IP allowlist se o Graph suportar (atualmente não restringe por IP de origem).

---

## 14. Fluxo de Autenticação

### 14.1 MSAL com Certificate-Based Auth

Fluxo principal para Azure Functions com App Registration.

```
┌─────────────────┐     ┌──────────────────┐     ┌────────────────┐
│ Azure Function   │────▶│ Microsoft Entra   │────▶│ Microsoft      │
│ (MSAL Client)   │◀────│ ID (OAuth 2.0)   │     │ Graph API      │
│                  │     │                  │     │                │
│ Certificate .pfx │     │ Validates cert   │     │ Validates token│
│ Client ID        │     │ Issues token     │     │ Returns data   │
│ Tenant ID        │     │ (JWT, ~1h TTL)   │     │                │
└─────────────────┘     └──────────────────┘     └────────────────┘
```

### Fluxo Detalhado (Client Credentials com Certificado)

```
1. Azure Function inicializa MSAL ConfidentialClientApplication
   - client_id: Application (client) ID
   - authority: https://login.microsoftonline.com/{tenant-id}
   - certificate: thumbprint + private key do .pfx

2. Function chama acquireTokenByClientCredential()
   - scopes: ["https://graph.microsoft.com/.default"]
   
3. MSAL monta JWT assertion assinado com o certificado
   - Header: { "alg": "RS256", "x5t": "{thumbprint}" }
   - Payload: { "iss": "{client_id}", "sub": "{client_id}", 
                "aud": "https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token" }
   
4. MSAL envia para token endpoint:
   POST https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token
   grant_type=client_credentials
   &client_id={client_id}
   &client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer
   &client_assertion={signed-jwt}
   &scope=https://graph.microsoft.com/.default

5. Entra ID valida:
   - Certificado corresponde ao registrado na App Registration
   - App tem as permissões solicitadas
   - Admin consent foi concedido

6. Entra ID retorna access token (JWT, ~3600s TTL)

7. Function usa token para chamar Graph API:
   GET https://graph.microsoft.com/v1.0/users/{userId}/onlineMeetings/{meetingId}/transcripts
   Authorization: Bearer {access_token}
```

### 14.2 Managed Identity para Azure Functions

Alternativa sem gerenciamento de certificados — o Azure gerencia as credenciais.

```typescript
import { DefaultAzureCredential } from "@azure/identity";
import { Client } from "@microsoft/microsoft-graph-client";
import { TokenCredentialAuthenticationProvider } from
  "@microsoft/microsoft-graph-client/authProviders/azureTokenCredentials";

const credential = new DefaultAzureCredential();

const authProvider = new TokenCredentialAuthenticationProvider(credential, {
  scopes: ["https://graph.microsoft.com/.default"]
});

const graphClient = Client.initWithMiddleware({ authProvider });

const transcripts = await graphClient
  .api(`/users/${userId}/onlineMeetings/${meetingId}/transcripts`)
  .get();
```

> **Pré-requisito:** As permissões de Graph precisam ser atribuídas à Managed Identity via PowerShell (ver Seção 10.5).

### 14.3 Token Refresh Strategy

```
┌──────────────────────────────────────────────────────────────┐
│                    TOKEN REFRESH STRATEGY                     │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  MSAL gerencia automaticamente:                              │
│                                                              │
│  • Cache interno: token reutilizado enquanto válido          │
│  • Refresh proativo: MSAL renova ~5min antes de expirar      │
│  • Retry: se token endpoint falhar, retry com backoff        │
│                                                              │
│  NÃO implementar manualmente:                                │
│  ✗ Verificação de expiração                                  │
│  ✗ Refresh token logic (client_credentials não usa refresh)  │
│  ✗ Token parsing para verificar exp claim                    │
│                                                              │
│  Configuração recomendada:                                   │
│  • Singleton ConfidentialClientApplication por Function App   │
│  • Distributed cache (Redis) se múltiplas instâncias         │
│  • Log token acquisition metrics no App Insights             │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

---

## Apêndice A — Referências

| Recurso | URL |
|---------|-----|
| Online Meetings API | https://learn.microsoft.com/en-us/graph/api/resources/onlinemeeting |
| Meeting Transcripts | https://learn.microsoft.com/en-us/graph/api/resources/calltranscript |
| Meeting Recordings | https://learn.microsoft.com/en-us/graph/api/resources/callrecording |
| Attendance Reports | https://learn.microsoft.com/en-us/graph/api/resources/meetingattendancereport |
| Call Records | https://learn.microsoft.com/en-us/graph/api/resources/callrecords-callrecord |
| Change Notifications | https://learn.microsoft.com/en-us/graph/api/resources/webhooks |
| Chat Messages | https://learn.microsoft.com/en-us/graph/api/resources/chatmessage |
| Adaptive Cards | https://adaptivecards.io/designer/ |
| MSAL Node.js | https://github.com/AzureAD/microsoft-authentication-library-for-js |
| Graph SDK TypeScript | https://github.com/microsoftgraph/msgraph-sdk-typescript |
| Graph Throttling | https://learn.microsoft.com/en-us/graph/throttling |
| Graph Permissions Reference | https://learn.microsoft.com/en-us/graph/permissions-reference |

---

## Apêndice B — Checklist de Setup

- [ ] App Registration criada no Azure AD
- [ ] Permissões de Application adicionadas (Seção 11)
- [ ] Admin consent concedido por Global Admin
- [ ] Certificado gerado e upload no App Registration
- [ ] Certificado privado (.pfx) armazenado no Azure Key Vault
- [ ] Azure Function configurada com variáveis de ambiente
- [ ] Managed Identity habilitada (se usando MI)
- [ ] Permissões de Graph atribuídas à MI via PowerShell
- [ ] Endpoint de webhook implementado (validation token)
- [ ] Subscription de Change Notification criada
- [ ] Job de renovação de subscription agendado
- [ ] Application Insights configurado para logging
- [ ] Alerta de expiração de certificado configurado
- [ ] Teste de integração end-to-end validado
- [ ] Revisão de segurança aprovada
