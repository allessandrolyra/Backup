# Segurança e Compliance — Secretário de Reunião Teams

> **Versão:** 1.0  
> **Data:** 08/06/2026  
> **Classificação:** Confidencial  
> **Status:** Em elaboração

---

## 1. Resumo de Segurança

O **Secretário de Reunião Teams** é um agente automatizado que captura transcrições de reuniões do Microsoft Teams via Microsoft Graph API, processa o conteúdo com Azure OpenAI para geração de atas estruturadas e armazena os resultados em Cosmos DB e SharePoint.

### Postura de Segurança

| Camada | Controle |
|---|---|
| **Identidade** | Azure AD App Registration com certificate-based auth + Managed Identity |
| **Autorização** | RBAC em todos os recursos Azure; permissões Graph com least privilege |
| **Dados em trânsito** | TLS 1.2+ obrigatório em todas as comunicações |
| **Dados em repouso** | Criptografia nativa Azure (AES-256) em Cosmos DB, Blob Storage e SharePoint |
| **Secrets** | Azure Key Vault para certificados, connection strings e chaves de API |
| **Auditoria** | Application Insights + Azure Activity Log com retenção de 1 ano |
| **Compliance** | LGPD, políticas corporativas de retenção e classificação de dados |
| **Rede** | VNet integration, Private Endpoints e NSG rules em produção |

### Princípios Orientadores

- **Defense in Depth**: múltiplas camadas de segurança independentes
- **Least Privilege**: cada componente possui apenas as permissões estritamente necessárias
- **Zero Trust**: nunca confiar, sempre verificar — toda requisição é autenticada e autorizada
- **Data Minimization**: processar e armazenar apenas o mínimo necessário
- **Transparency**: participantes de reuniões são notificados sobre o processamento

---

## 2. Modelo de Identidade e Acesso

### 2.1 App Registration

O agente utiliza um **App Registration** no Azure AD (Entra ID) com autenticação baseada em certificado (certificate-based authentication), eliminando o uso de client secrets.

| Propriedade | Valor |
|---|---|
| **Tipo de autenticação** | Certificate-based (X.509) |
| **Armazenamento do certificado** | Azure Key Vault |
| **Rotação do certificado** | A cada 6 meses (automatizada) |
| **Multi-tenant** | Não — single-tenant |
| **Redirect URIs** | Nenhuma (daemon application) |

### 2.2 Managed Identity

As Azure Functions utilizam **System-Assigned Managed Identity** para acessar recursos Azure sem credenciais explícitas:

- Acesso ao Azure Key Vault (Get Secrets, Get Certificates)
- Acesso ao Cosmos DB (data plane via RBAC)
- Acesso ao Blob Storage (read/write)
- Acesso ao Application Insights (telemetria)

### 2.3 Least Privilege Principle

Cada componente possui apenas as permissões mínimas necessárias:

```
Azure Functions (Managed Identity)
├── Key Vault: Key Vault Secrets User, Key Vault Certificates User
├── Cosmos DB: Cosmos DB Built-in Data Contributor (somente databases necessários)
├── Blob Storage: Storage Blob Data Contributor (somente containers necessários)
└── Application Insights: Monitoring Metrics Publisher

App Registration (Graph API)
├── OnlineMeetings.Read.All
├── OnlineMeetingTranscript.Read.All
├── Calendars.Read
├── User.Read.All
├── Sites.ReadWrite.All (SharePoint — escrita de atas)
└── Chat.Read.All (se necessário para reuniões de canal)
```

### 2.4 RBAC para Recursos Azure

| Recurso | Role | Principal |
|---|---|---|
| Key Vault | Key Vault Secrets User | Managed Identity das Functions |
| Key Vault | Key Vault Administrator | Equipe de operações (break-glass) |
| Cosmos DB | Cosmos DB Built-in Data Contributor | Managed Identity das Functions |
| Blob Storage | Storage Blob Data Contributor | Managed Identity das Functions |
| Resource Group | Reader | Equipe de desenvolvimento |
| Resource Group | Contributor | Pipeline de CI/CD |

### 2.5 Conditional Access Policies

Políticas de Acesso Condicional aplicáveis ao cenário:

- **Acesso administrativo ao portal Azure**: MFA obrigatório + dispositivo gerenciado
- **Service Principal sign-ins**: monitoramento via Entra ID sign-in logs (workload identities)
- **Break-glass accounts**: contas de emergência com auditoria reforçada

---

## 3. Graph API Security

### 3.1 Modelo de Permissões

O agente opera exclusivamente com **permissões application-only** (sem contexto de usuário), executando como daemon application.

| Permissão | Tipo | Justificativa |
|---|---|---|
| `OnlineMeetings.Read.All` | Application | Listar reuniões e obter metadados (organizador, participantes, horário) |
| `OnlineMeetingTranscript.Read.All` | Application | Acessar transcrições das reuniões para processamento |
| `Calendars.Read` | Application | Identificar reuniões agendadas e seus metadados |
| `User.Read.All` | Application | Resolver nomes e e-mails dos participantes para a ata |
| `Sites.ReadWrite.All` | Application | Salvar atas geradas em bibliotecas SharePoint |
| `Chat.Read.All` | Application | Acessar mensagens de chat de reuniões de canal (se aplicável) |

> **Nota:** Todas as permissões application-only requerem **admin consent** de um Global Administrator ou Application Administrator.

### 3.2 Admin Consent

- Admin consent é concedido de forma explícita e documentada
- Revisão periódica das permissões concedidas (trimestral)
- Registro de quem concedeu o consent e quando
- Processo formal de solicitação e aprovação de novas permissões

### 3.3 Escopo Restrito via Application Access Policy

Para limitar o escopo do `OnlineMeetings.Read.All` (que por padrão permite acesso a todas as reuniões do tenant), utiliza-se **Application Access Policy**:

```powershell
# Criar um grupo de segurança com os usuários cujas reuniões serão processadas
# Aplicar a policy para restringir o acesso do app apenas a esse grupo
New-ApplicationAccessPolicy `
  -AppId "<app-client-id>" `
  -PolicyScopeGroupId "<security-group-id>" `
  -AccessType RestrictAccess `
  -Description "Restringe acesso do Secretário de Reunião ao grupo autorizado"
```

### 3.4 Certificate Rotation Policy

| Item | Política |
|---|---|
| **Período de validade** | 12 meses |
| **Rotação** | A cada 6 meses (overlap de 6 meses para transição) |
| **Armazenamento** | Azure Key Vault (auto-rotation habilitada) |
| **Alertas** | 30 dias antes da expiração via Key Vault alerting |
| **Automação** | Azure Automation Runbook para rotação + atualização no App Registration |

### 3.5 Token Caching Seguro

- Access tokens cacheados em memória (in-process) com MSAL — nunca persistidos em disco
- Token lifetime respeitado conforme emitido pelo Azure AD (tipicamente 1 hora)
- Refresh automático via MSAL ConfidentialClientApplication
- Nenhum token armazenado em logs, Cosmos DB ou qualquer storage persistente

---

## 4. Proteção de Dados

### 4.1 Dados em Trânsito

| Comunicação | Protocolo |
|---|---|
| Azure Functions → Graph API | HTTPS / TLS 1.2+ |
| Azure Functions → Azure OpenAI | HTTPS / TLS 1.2+ |
| Azure Functions → Cosmos DB | HTTPS / TLS 1.2+ |
| Azure Functions → Blob Storage | HTTPS / TLS 1.2+ |
| Azure Functions → Key Vault | HTTPS / TLS 1.2+ |
| Azure Functions → SharePoint | HTTPS / TLS 1.2+ |

- TLS 1.0 e 1.1 desabilitados em todos os recursos
- Minimum TLS version configurado como 1.2 em todos os serviços Azure

### 4.2 Dados em Repouso

| Armazenamento | Criptografia | Gerenciamento de Chaves |
|---|---|---|
| Cosmos DB | AES-256 (SSE) | Microsoft-managed keys (padrão) |
| Blob Storage | AES-256 (SSE) | Microsoft-managed keys (padrão) |
| SharePoint Online | AES-256 | Microsoft-managed (per-file keys) |
| Key Vault | HSM-backed | Azure-managed HSM |

> **Nota:** Para ambientes com requisitos de compliance mais rigorosos, considerar Customer-Managed Keys (CMK) via Key Vault.

### 4.3 Azure Key Vault

Recursos gerenciados pelo Key Vault:

| Secret/Certificate | Propósito |
|---|---|
| App Registration Certificate | Autenticação na Graph API |
| Cosmos DB Connection String | Acesso ao banco de dados operacional |
| Azure OpenAI API Key | Acesso ao serviço de processamento de linguagem |
| Storage Account Connection String | Acesso ao Blob Storage (transcrições temporárias) |

Políticas do Key Vault:
- **Soft-delete** habilitado (90 dias de retenção)
- **Purge protection** habilitado
- **Access via RBAC** (não via Access Policies legadas)
- **Diagnostic logging** habilitado para auditoria de acessos

### 4.4 Classificação de Dados

| Tipo de Dado | Classificação | Localização | Retenção |
|---|---|---|---|
| Transcrições brutas | **Confidencial** | Blob Storage (temporário) | 30 dias |
| Atas geradas | **Confidencial** | SharePoint | Conforme política organizacional |
| Metadados de reunião | **Interno** | Cosmos DB | 90 dias |
| Audit logs | **Interno** | Application Insights | 1 ano |
| Tokens/Certificados | **Restrito** | Key Vault | Conforme rotação |

### 4.5 Minimização de Dados (No PII Storage)

- **Transcrições brutas** são armazenadas temporariamente apenas para processamento e excluídas após geração da ata
- **Atas geradas** contêm apenas nomes de participantes e conteúdo da reunião — sem dados pessoais sensíveis adicionais
- **Nenhum dado biométrico** é armazenado (voz, vídeo)
- **E-mails e nomes** são utilizados apenas para identificação na ata, não para profiling
- O processamento via Azure OpenAI **não retém dados** de entrada/saída (data, no retention policy do Azure OpenAI)

---

## 5. LGPD Compliance

### 5.1 Base Legal para Processamento

O processamento de transcrições de reuniões enquadra-se nas seguintes bases legais da LGPD (Lei nº 13.709/2018):

| Base Legal | Artigo LGPD | Aplicação |
|---|---|---|
| **Legítimo Interesse** | Art. 7º, IX | Processamento de transcrições para geração de atas de reuniões corporativas, beneficiando a eficiência organizacional |
| **Execução de Contrato** | Art. 7º, V | Quando a geração de atas é parte de obrigação contratual ou regulatória |
| **Consentimento** | Art. 7º, I | Opt-in explícito quando exigido pela política organizacional |

> **Recomendação:** Conduzir um **Relatório de Impacto à Proteção de Dados Pessoais (RIPD)** — equivalente ao DPIA do GDPR — para documentar a análise de legítimo interesse (LIA).

### 5.2 Direitos dos Titulares

O sistema deve suportar os seguintes direitos dos titulares de dados:

| Direito | Art. LGPD | Implementação |
|---|---|---|
| **Confirmação e acesso** | Art. 18, I e II | Consulta de quais dados do titular foram processados |
| **Correção** | Art. 18, III | Mecanismo para solicitar correção de atas que contenham informações incorretas |
| **Anonimização/bloqueio/eliminação** | Art. 18, IV | Exclusão de transcrições e atas sob solicitação |
| **Portabilidade** | Art. 18, V | Exportação de atas em formato estruturado |
| **Eliminação de dados consentidos** | Art. 18, VI | Remoção completa quando base legal é consentimento |
| **Informação sobre compartilhamento** | Art. 18, VII | Transparência sobre quais serviços processam os dados |
| **Revogação de consentimento** | Art. 18, IX | Opt-out disponível e facilmente acessível |

**Processo para atendimento:**
1. Solicitação recebida via canal de privacidade (e-mail/portal DPO)
2. Verificação de identidade do solicitante
3. Busca nos sistemas (Cosmos DB, SharePoint, Blob Storage)
4. Atendimento dentro do prazo legal (15 dias úteis — Art. 19)
5. Registro da solicitação e resposta no log de auditoria

### 5.3 Registro de Atividades de Tratamento (ROPA)

| Campo | Descrição |
|---|---|
| **Controlador** | [Nome da organização] |
| **Operador** | Microsoft Azure (infraestrutura), Azure OpenAI (processamento) |
| **Finalidade** | Geração automatizada de atas de reuniões corporativas |
| **Categorias de dados** | Nomes, e-mails, falas transcritas em reuniões |
| **Categorias de titulares** | Colaboradores e convidados que participam de reuniões Teams |
| **Base legal** | Legítimo interesse (Art. 7º, IX) |
| **Prazo de retenção** | Transcrições: 30 dias; Atas: conforme política organizacional |
| **Medidas de segurança** | Criptografia, RBAC, Key Vault, auditoria, VNet |
| **Transferência internacional** | Dados processados em região Azure Brasil South (quando disponível) ou East US 2 — verificar DPA Microsoft |

### 5.4 Encarregado de Dados (DPO)

- O Encarregado de Dados da organização deve ser informado sobre esta solução
- Canal de contato do DPO deve ser incluído nas notificações aos participantes
- DPO deve aprovar o RIPD antes do go-live
- Revisão anual pela área de Privacidade/DPO

### 5.5 Notificação aos Participantes

Todos os participantes de reuniões processadas devem ser informados:

- **Antes da reunião**: e-mail de convite ou política organizacional comunicada
- **No início da reunião**: mensagem automática no chat do Teams:

> "Esta reunião será processada pelo Secretário de Reunião para geração automática de ata. Os dados serão tratados conforme a Política de Privacidade da [Organização]. Para opt-out, envie 'não gravar' no chat ou entre em contato com [dpo@organizacao.com.br]."

- **Após a reunião**: ata compartilhada com os participantes para revisão

### 5.6 Data Minimization

- Processar **apenas transcrições de reuniões habilitadas** (não capturar reuniões sem transcrição)
- Extrair da transcrição apenas o necessário para a ata (decisões, ações, próximos passos)
- **Não armazenar** transcrições completas permanentemente
- **Não processar** dados de áudio ou vídeo
- **Não realizar** profiling ou análise comportamental dos participantes
- Prompts do Azure OpenAI instruídos a **não reter** dados pessoais além do escopo da ata

### 5.7 Prazo de Retenção

| Dado | Retenção | Justificativa |
|---|---|---|
| Transcrição bruta (Blob Storage) | 30 dias | Tempo para reprocessamento se necessário |
| Ata gerada (SharePoint) | Conforme política da organização | Documento oficial de registro |
| Metadados operacionais (Cosmos DB) | 90 dias | Operação e troubleshooting |
| Audit logs | 1 ano mínimo | Compliance e investigação |

---

## 6. Política de Retenção

### 6.1 Ciclo de Vida dos Dados

```
Reunião concluída
    │
    ▼
Transcrição capturada (Graph API)
    │
    ▼
Armazenada temporariamente (Blob Storage) ──── TTL: 30 dias ──── Exclusão automática
    │
    ▼
Processada (Azure OpenAI)
    │
    ├──▶ Ata gerada (SharePoint) ──── Retenção: política organizacional
    │
    └──▶ Metadados (Cosmos DB) ──── TTL: 90 dias ──── Exclusão automática
```

### 6.2 Regras de Retenção por Armazenamento

| Armazenamento | Tipo de Dado | TTL | Mecanismo de Exclusão |
|---|---|---|---|
| **Blob Storage** | Transcrições brutas | 30 dias | Lifecycle Management Policy (auto-delete) |
| **Cosmos DB** | Metadados operacionais | 90 dias | TTL nativo do Cosmos DB (campo `_ttl`) |
| **Cosmos DB** | Status de processamento | 90 dias | TTL nativo do Cosmos DB |
| **SharePoint** | Atas geradas | Política organizacional | Retention Label via Purview |
| **Application Insights** | Logs de auditoria | 1 ano (365 dias) | Workspace retention policy |
| **Key Vault** | Secrets/Certificates | Conforme rotação | Soft-delete + purge protection |

### 6.3 Configuração por Tenant/Organização

A política de retenção deve ser configurável via parâmetros de configuração:

```json
{
  "retention": {
    "rawTranscription": {
      "days": 30,
      "autoDelete": true
    },
    "cosmosDbOperational": {
      "days": 90,
      "autoDelete": true
    },
    "generatedMinutes": {
      "policy": "organizational",
      "purviewLabel": "Business-Record"
    },
    "auditLogs": {
      "days": 365,
      "minimumRetention": true
    }
  }
}
```

### 6.4 Exclusão e Purge

- Exclusão de transcrições é **irreversível** após o período de soft-delete
- Processo de exclusão sob demanda (LGPD) deve ser documentado e auditado
- Exclusão em cascata: ao excluir dados de uma reunião, excluir transcrição, metadados e ata associada
- Verificação periódica (mensal) de que as políticas de TTL estão funcionando corretamente

---

## 7. Auditoria e Logging

### 7.1 Application Insights

Todas as operações do agente são logadas no Application Insights:

| Evento | Dados Registrados | Severidade |
|---|---|---|
| Transcrição capturada | Meeting ID, organizador, timestamp, tamanho | Information |
| Processamento iniciado | Meeting ID, modelo OpenAI utilizado | Information |
| Ata gerada com sucesso | Meeting ID, SharePoint URL, duração do processamento | Information |
| Erro no processamento | Meeting ID, tipo de erro, stack trace (sem PII) | Error |
| Transcrição excluída (TTL) | Meeting ID, timestamp de exclusão | Information |
| Acesso negado (Graph API) | Meeting ID, código de erro, permissão faltante | Warning |
| Solicitação LGPD recebida | Tipo de solicitação, ID do titular (hash) | Information |

### 7.2 Audit Trail

Cada operação gera um registro de auditoria com os seguintes campos:

```json
{
  "timestamp": "2026-06-08T14:30:00Z",
  "operation": "TranscriptionProcessed",
  "meetingId": "meeting-uuid",
  "organizerUpn": "usuario@organizacao.com.br",
  "participantCount": 5,
  "processingDurationMs": 12500,
  "outputLocation": "sharepoint://site/library/ata-2026-06-08.docx",
  "status": "Success",
  "correlationId": "correlation-uuid"
}
```

> **Importante:** Logs **não devem conter** conteúdo de transcrições ou atas — apenas metadados operacionais.

### 7.3 Graph API Audit Logs

- Sign-in logs do Service Principal monitorados via Entra ID
- Acessos a recursos da Graph API registrados nos Unified Audit Logs do Microsoft 365
- Alertas configurados para padrões anômalos (volume incomum de requisições, acessos fora do horário esperado)

### 7.4 Azure Activity Log

- Todas as operações de infraestrutura registradas no Azure Activity Log
- Alterações em RBAC, configurações de rede, deployment de Functions
- Integração com Azure Monitor para alertas em tempo real

### 7.5 Retenção de Logs

| Log | Retenção | Destino |
|---|---|---|
| Application Insights (telemetria) | 90 dias (padrão) | Log Analytics Workspace |
| Application Insights (auditoria) | 365 dias | Log Analytics Workspace (tabela customizada) |
| Azure Activity Log | 90 dias (padrão) + export | Log Analytics Workspace (365 dias) |
| Entra ID Sign-in Logs | 30 dias (padrão) + export | Log Analytics Workspace (365 dias) |
| Microsoft 365 Unified Audit Log | Conforme licenciamento | Microsoft 365 |

---

## 8. Consentimento e Transparência

### 8.1 Notificação no Início da Reunião

Quando o agente é acionado para processar uma reunião, uma mensagem é enviada automaticamente no chat da reunião:

> **Secretário de Reunião ativo** 📋  
> Esta reunião será processada automaticamente para geração de ata. Os seguintes dados serão utilizados: transcrição da reunião, nomes dos participantes e horário.  
> A ata será compartilhada com os participantes após a reunião.  
> Para opt-out desta reunião, digite **!optout** no chat.  
> Dúvidas: [dpo@organizacao.com.br]

### 8.2 Mecanismo de Opt-Out

| Método | Descrição |
|---|---|
| **Comando no chat** | Participante digita `!optout` — reunião é excluída do processamento |
| **Tag no convite** | Organizador adiciona `[no-minutes]` no assunto — reunião ignorada |
| **Configuração de usuário** | Usuário se exclui globalmente via portal de self-service |
| **Lista de exclusão** | Administrador configura reuniões/salas que nunca são processadas |

### 8.3 Transparência sobre Dados Processados

Documentação pública (intranet) descrevendo:

- Quais dados são capturados (transcrição de texto, nomes, horários)
- Quais dados **não** são capturados (áudio, vídeo, arquivos compartilhados)
- Como os dados são processados (Azure OpenAI)
- Onde os dados são armazenados (Azure Brasil South / East US 2)
- Por quanto tempo os dados são retidos
- Como exercer direitos LGPD

### 8.4 Política de Uso Aceitável

Regras claras sobre o uso do Secretário de Reunião:

- Reuniões **confidenciais ou restritas** devem usar opt-out
- O agente **não substitui** a gravação oficial de reuniões deliberativas
- Atas geradas devem ser **revisadas** pelo organizador antes de distribuição ampla
- **Proibido** utilizar o agente para monitoramento de produtividade individual
- **Proibido** utilizar atas para avaliação de desempenho sem consentimento explícito

---

## 9. Purview Integration

### 9.1 Sensitivity Labels

Atas geradas são automaticamente classificadas com **sensitivity labels** do Microsoft Purview:

| Label | Aplicação | Proteção |
|---|---|---|
| **Confidential** | Padrão para todas as atas | Criptografia AIP, marca d'água "Confidencial" |
| **Highly Confidential** | Reuniões de diretoria/estratégicas | Criptografia AIP + restrição de forwarding |
| **Internal** | Reuniões operacionais rotineiras | Sem criptografia adicional, marca d'água "Uso Interno" |

A label é aplicada via Graph API ao fazer upload para o SharePoint:

```http
PATCH /sites/{site-id}/drives/{drive-id}/items/{item-id}
{
  "sensitivityLabel": {
    "labelId": "<label-guid>",
    "assignmentMethod": "auto"
  }
}
```

### 9.2 DLP Policies

Políticas de Prevenção contra Perda de Dados aplicáveis às atas:

- **Detecção de PII**: CPF, RG, dados bancários mencionados em reunião → alerta ao DPO
- **Conteúdo sensível**: termos financeiros confidenciais, informações de M&A → label Highly Confidential automática
- **Compartilhamento externo**: bloquear compartilhamento de atas com sensitivity label Confidential/Highly Confidential para fora da organização

### 9.3 eDiscovery

- Atas armazenadas no SharePoint são automaticamente indexadas e localizáveis via eDiscovery
- Metadata incluído: data da reunião, participantes, organizador, assunto
- Retenção legal (legal hold) pode ser aplicada a atas específicas quando necessário
- Formato de exportação compatível com ferramentas de eDiscovery (docx + metadata JSON)

### 9.4 Information Protection — Classificação Automática

Regras de auto-labeling baseadas no conteúdo da ata:

| Condição | Label Aplicada |
|---|---|
| Contém termos financeiros (receita, EBITDA, forecast) | Highly Confidential |
| Contém nomes de clientes e valores de contrato | Highly Confidential |
| Reunião com participantes externos | Confidential + External |
| Reunião padrão interna | Confidential |

---

## 10. Network Security

### 10.1 Arquitetura de Rede

```
Internet
    │
    ▼
Microsoft Graph API (endpoints públicos Microsoft)
    │  HTTPS/TLS 1.2+
    ▼
┌─────────────────────────────────────────┐
│  Azure Virtual Network                  │
│  ┌───────────────────────────────────┐  │
│  │  Subnet: functions-subnet         │  │
│  │  Azure Functions (VNet integrated)│  │
│  │  NSG: allow outbound 443 only     │  │
│  └───────────┬───────────────────────┘  │
│              │                           │
│  ┌───────────▼───────────────────────┐  │
│  │  Subnet: private-endpoints        │  │
│  │  ┌──────────┐  ┌───────────────┐  │  │
│  │  │ Cosmos DB │  │ Blob Storage  │  │  │
│  │  │ (Private  │  │ (Private      │  │  │
│  │  │ Endpoint) │  │ Endpoint)     │  │  │
│  │  └──────────┘  └───────────────┘  │  │
│  │  ┌──────────┐  ┌───────────────┐  │  │
│  │  │ Key Vault│  │ Azure OpenAI  │  │  │
│  │  │ (Private │  │ (Private      │  │  │
│  │  │ Endpoint)│  │ Endpoint)     │  │  │
│  │  └──────────┘  └───────────────┘  │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
```

### 10.2 VNet Integration

- Azure Functions com **VNet Integration** para tráfego de saída
- Recomendado para ambiente de produção; opcional para desenvolvimento
- Route all traffic through VNet habilitado (`WEBSITE_VNET_ROUTE_ALL=1`)

### 10.3 Private Endpoints

| Recurso | Private Endpoint | DNS Zone |
|---|---|---|
| Cosmos DB | `pe-cosmos-secretario` | `privatelink.documents.azure.com` |
| Blob Storage | `pe-blob-secretario` | `privatelink.blob.core.windows.net` |
| Key Vault | `pe-kv-secretario` | `privatelink.vaultcore.azure.net` |
| Azure OpenAI | `pe-openai-secretario` | `privatelink.openai.azure.com` |

> Em produção, **desabilitar acesso público** a todos os recursos com private endpoints.

### 10.4 NSG Rules

| Regra | Direção | Porta | Origem | Destino | Ação |
|---|---|---|---|---|---|
| Allow HTTPS Outbound | Outbound | 443 | functions-subnet | Internet | Allow |
| Allow Private Endpoints | Outbound | 443 | functions-subnet | private-endpoints-subnet | Allow |
| Deny All Other Outbound | Outbound | * | functions-subnet | * | Deny |
| Deny All Inbound | Inbound | * | * | functions-subnet | Deny |

### 10.5 Azure Firewall (Enterprise)

Para ambientes enterprise com Azure Firewall:

- FQDN filtering para permitir apenas domínios necessários:
  - `graph.microsoft.com`
  - `login.microsoftonline.com`
  - `*.openai.azure.com`
  - `*.documents.azure.com`
  - `*.blob.core.windows.net`
  - `*.vaultcore.azure.net`
- Threat Intelligence habilitado em modo Alert & Deny
- Logs de tráfego integrados ao Log Analytics

---

## 11. Incident Response

### 11.1 Plano de Resposta a Incidentes

#### Classificação de Incidentes

| Severidade | Descrição | Exemplo | SLA Resposta |
|---|---|---|---|
| **Crítica** | Vazamento de dados confirmado | Transcrição acessada por terceiro não autorizado | 1 hora |
| **Alta** | Vulnerabilidade explorada ou tentativa de acesso | Certificate comprometido, anomalia de acesso | 4 horas |
| **Média** | Falha de segurança potencial | Permissão excessiva descoberta, log gap | 24 horas |
| **Baixa** | Melhoria de segurança identificada | Recomendação de hardening | 1 semana |

#### Fluxo de Resposta

```
1. DETECÇÃO
   ├── Alerta do Azure Monitor / Sentinel
   ├── Relatório de usuário
   └── Revisão periódica de logs

2. TRIAGEM (até 1h)
   ├── Classificação de severidade
   ├── Identificação do escopo
   └── Acionamento da equipe responsável

3. CONTENÇÃO (imediata)
   ├── Revogar certificados/tokens comprometidos
   ├── Desabilitar App Registration se necessário
   ├── Bloquear acesso via Conditional Access
   └── Preservar evidências (snapshots de logs)

4. ERRADICAÇÃO
   ├── Identificar causa raiz
   ├── Corrigir vulnerabilidade
   └── Verificar se há outros vetores afetados

5. RECUPERAÇÃO
   ├── Restaurar operação normal
   ├── Emitir novos certificados
   └── Verificar integridade dos dados

6. PÓS-INCIDENTE
   ├── Root Cause Analysis (RCA)
   ├── Lições aprendidas
   └── Atualização de controles
```

### 11.2 Notificação de Data Breach (LGPD)

Em caso de incidente de segurança que envolva dados pessoais:

| Ação | Prazo | Destinatário |
|---|---|---|
| Notificação interna (DPO + CISO) | Imediata | Encarregado de Dados, CISO |
| Avaliação de risco aos titulares | Até 48 horas | Equipe de resposta a incidentes |
| Notificação à ANPD | Prazo razoável (Art. 48 LGPD) | Autoridade Nacional de Proteção de Dados |
| Notificação aos titulares afetados | Prazo razoável (Art. 48 LGPD) | Titulares de dados afetados |

Conteúdo da notificação (Art. 48, §1º):
- Descrição da natureza dos dados pessoais afetados
- Informações sobre os titulares envolvidos
- Medidas técnicas e de segurança utilizadas
- Riscos relacionados ao incidente
- Medidas adotadas para reverter ou mitigar o incidente
- Motivos da demora, se não comunicado imediatamente

### 11.3 Procedimento de Quarentena

Quando um incidente é detectado, o sistema pode ser colocado em quarentena:

1. **Parar processamento**: desabilitar Azure Functions (Application Setting: `FUNCTIONS_EXTENSION_VERSION` → vazio ou desabilitar via portal)
2. **Revogar acesso Graph**: remover certificado do App Registration
3. **Isolar dados**: alterar NSG para bloquear todo acesso
4. **Preservar evidências**: exportar logs do Application Insights e Activity Log
5. **Comunicar stakeholders**: notificar equipe de segurança, DPO e gestão

---

## 12. Checklist de Segurança para Deploy

### Pré-Produção

#### Identidade e Acesso
- [ ] App Registration criado com certificate-based authentication (sem client secrets)
- [ ] Certificado armazenado no Key Vault com auto-rotation configurada
- [ ] Managed Identity habilitada nas Azure Functions
- [ ] RBAC configurado com least privilege em todos os recursos
- [ ] Application Access Policy configurada para limitar escopo do Graph
- [ ] Admin consent concedido e documentado
- [ ] Conditional Access policies verificadas

#### Graph API
- [ ] Apenas permissões application-only necessárias configuradas
- [ ] Application Access Policy restringindo acesso ao grupo autorizado
- [ ] Nenhuma permissão delegated desnecessária
- [ ] Token caching apenas em memória (sem persistência)

#### Proteção de Dados
- [ ] TLS 1.2+ configurado como mínimo em todos os serviços
- [ ] Encryption at rest habilitado em Cosmos DB e Blob Storage
- [ ] Key Vault com soft-delete e purge protection habilitados
- [ ] Nenhum secret/connection string em código ou configuração plain-text
- [ ] Data classification definida para todos os tipos de dados

#### LGPD
- [ ] RIPD (Relatório de Impacto) concluído e aprovado pelo DPO
- [ ] Base legal definida e documentada
- [ ] Registro de atividades de tratamento atualizado
- [ ] Notificação aos participantes implementada e testada
- [ ] Mecanismo de opt-out funcional
- [ ] Processo para atendimento de direitos dos titulares definido
- [ ] Política de retenção implementada (TTL no Cosmos DB, Lifecycle no Blob)

#### Retenção e Exclusão
- [ ] TTL configurado no Cosmos DB (90 dias)
- [ ] Blob Storage Lifecycle Management configurado (30 dias)
- [ ] Processo de exclusão sob demanda testado
- [ ] Exclusão em cascata validada

#### Auditoria e Logging
- [ ] Application Insights configurado com telemetria de auditoria
- [ ] Log Analytics Workspace com retenção de 365 dias
- [ ] Nenhum PII em logs (transcrições, conteúdo de atas)
- [ ] Alertas configurados para anomalias
- [ ] Azure Activity Log exportado para Log Analytics

#### Purview (se aplicável)
- [ ] Sensitivity labels configuradas e aplicáveis
- [ ] DLP policies ativas para detecção de conteúdo sensível
- [ ] Auto-labeling rules configuradas
- [ ] eDiscovery validado para atas no SharePoint

#### Rede
- [ ] VNet integration habilitada nas Azure Functions (produção)
- [ ] Private endpoints configurados para Cosmos DB, Storage, Key Vault, OpenAI
- [ ] NSG rules aplicadas e testadas
- [ ] Acesso público desabilitado em recursos com private endpoint
- [ ] DNS privado configurado para private endpoints

#### Incident Response
- [ ] Plano de resposta a incidentes documentado
- [ ] Contatos de emergência definidos (CISO, DPO, equipe de operações)
- [ ] Procedimento de quarentena testado
- [ ] Processo de notificação ANPD/titulares definido
- [ ] Runbooks de incidentes criados

#### Validação Final
- [ ] Pen test / security review realizado
- [ ] Revisão de código focada em segurança concluída
- [ ] Scan de vulnerabilidades em dependências (npm audit / pip audit)
- [ ] Aprovação formal do CISO e/ou DPO
- [ ] Documentação de segurança revisada e atualizada

---

## Referências

- [LGPD — Lei nº 13.709/2018](http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm)
- [ANPD — Autoridade Nacional de Proteção de Dados](https://www.gov.br/anpd/)
- [Microsoft Graph API Security Best Practices](https://learn.microsoft.com/en-us/graph/security-concept-overview)
- [Azure Security Baseline](https://learn.microsoft.com/en-us/security/benchmark/azure/)
- [Azure Key Vault Best Practices](https://learn.microsoft.com/en-us/azure/key-vault/general/best-practices)
- [Microsoft Purview Information Protection](https://learn.microsoft.com/en-us/purview/information-protection)
- [Azure Functions Networking Options](https://learn.microsoft.com/en-us/azure/azure-functions/functions-networking-options)

---

> **Próximos passos:**
> 1. Revisão deste documento pelo CISO e DPO da organização
> 2. Elaboração do RIPD (Relatório de Impacto à Proteção de Dados Pessoais)
> 3. Definição dos valores específicos de configuração por tenant
> 4. Implementação dos controles técnicos descritos
> 5. Teste de penetração e security review antes do go-live
