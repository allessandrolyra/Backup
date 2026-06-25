# Backlog de Epics e Stories — Secretário de Reunião Teams

> **Projeto:** Secretário de Reunião Teams (MVP)
> **Criado por:** Bob (Scrum Master — Squad MEQ)
> **Data:** 08/06/2026
> **Status:** Draft — Pronto para Refinamento
> **Total de Epics:** 7 | **Total de Stories:** 33
> **Sprints Planejados:** 6 (2 semanas cada)
> **Estimativa Total:** 119 pontos

---

## Índice

- [Sprint Plan Sugerido](#sprint-plan-sugerido)
- [Epic 1: Infraestrutura e Setup](#epic-1-infraestrutura-e-setup)
- [Epic 2: Event Capture (Graph Webhooks)](#epic-2-event-capture-graph-webhooks)
- [Epic 3: Data Ingestion (Graph API)](#epic-3-data-ingestion-graph-api)
- [Epic 4: Processamento com IA (Azure OpenAI)](#epic-4-processamento-com-ia-azure-openai)
- [Epic 5: Entrega de Resultados](#epic-5-entrega-de-resultados)
- [Epic 6: Segurança e Compliance](#epic-6-segurança-e-compliance)
- [Epic 7: Operações e Monitoramento](#epic-7-operações-e-monitoramento)

---

## Sprint Plan Sugerido

| Sprint | Foco | Epics | Pontos | Objetivo |
|--------|------|-------|--------|----------|
| **Sprint 1** | Infraestrutura | Epic 1 | 24 | Ambiente provisionado, pipeline CI/CD funcional, todos os recursos Azure prontos |
| **Sprint 2** | Eventos + Ingestão | Epic 2 + Epic 3 | 28 | Webhooks capturando eventos de reunião, dados brutos sendo coletados e armazenados |
| **Sprint 3** | Processamento IA | Epic 4 | 26 | Transcrições processadas pela IA com extração de tópicos, decisões e ações |
| **Sprint 4** | Entrega | Epic 5 | 21 | Adaptive Cards enviadas no Teams, atas geradas no SharePoint |
| **Sprint 5** | Segurança | Epic 6 | 16 | Auth por certificado, RBAC, audit logging e compliance configurados |
| **Sprint 6** | Operações + Testes | Epic 7 | 11 | Dashboards, alertas, health checks e testes integrados end-to-end |

**Velocidade estimada por sprint:** ~20-28 pontos

---

## Epic 1: Infraestrutura e Setup

**Objetivo:** Provisionar toda a infraestrutura Azure necessária para o MVP, incluindo identidade, compute, storage, IA, segurança e pipeline de entrega contínua.

**Sprint:** 1
**Total de pontos:** 24

---

### Story 1.1: Criar App Registration no Entra ID com permissões Graph necessárias

**Descrição:** Registrar aplicação no Microsoft Entra ID (Azure AD) configurando as permissões de aplicação (application permissions) necessárias para acessar transcrições, metadados de reuniões, presença e chat via Microsoft Graph API.

**Critérios de Aceitação:**
- [ ] App Registration criado no Entra ID com nome padronizado (`sec-reuniao-teams-{env}`)
- [ ] Permissões de aplicação configuradas: `OnlineMeetings.Read.All`, `OnlineMeetingTranscript.Read.All`, `CallRecords.Read.All`, `Chat.Read.All`
- [ ] Admin consent concedido para todas as permissões necessárias
- [ ] Certificado ou client secret gerado e armazenado no Key Vault

**Estimativa:** 3 pontos
**Dependências:** Nenhuma
**Sprint:** 1

---

### Story 1.2: Provisionar Azure Functions (Consumption Plan) via Bicep/Terraform

**Descrição:** Criar o recurso Azure Functions no plano Consumption usando Infrastructure as Code (Bicep ou Terraform), incluindo configuração de runtime (.NET 8 ou Node.js), application settings e integração com Application Insights.

**Critérios de Aceitação:**
- [ ] Azure Function App provisionada via IaC com código versionado no repositório
- [ ] Runtime configurado (stack escolhida) com variáveis de ambiente parametrizadas por ambiente (dev/staging/prod)
- [ ] Managed Identity habilitada e associada ao Function App
- [ ] Deploy de uma function "hello world" funcional para validação do pipeline

**Estimativa:** 5 pontos
**Dependências:** Nenhuma
**Sprint:** 1

---

### Story 1.3: Provisionar Cosmos DB (Serverless) com containers para meetings, decisions, actions

**Descrição:** Provisionar instância do Azure Cosmos DB no tier Serverless via IaC, criando os containers necessários para armazenar dados estruturados das reuniões processadas.

**Critérios de Aceitação:**
- [ ] Cosmos DB account provisionado no tier Serverless via IaC
- [ ] Containers criados: `meetings` (partition key: `/meetingId`), `decisions` (partition key: `/meetingId`), `actions` (partition key: `/meetingId`)
- [ ] Políticas de indexação configuradas para consultas por `meetingId`, `date` e `status`
- [ ] Connection string armazenada no Key Vault

**Estimativa:** 3 pontos
**Dependências:** Story 1.5 (Key Vault)
**Sprint:** 1

---

### Story 1.4: Provisionar Azure OpenAI com modelo GPT-4o

**Descrição:** Provisionar recurso Azure OpenAI Service e realizar o deployment do modelo GPT-4o, configurando limites de rate e filtros de conteúdo adequados ao caso de uso corporativo.

**Critérios de Aceitação:**
- [ ] Recurso Azure OpenAI provisionado via IaC na região com disponibilidade de GPT-4o
- [ ] Deployment do modelo GPT-4o criado com TPM (Tokens Per Minute) adequado ao volume estimado
- [ ] Content filters configurados para contexto corporativo
- [ ] Endpoint e API key armazenados no Key Vault

**Estimativa:** 3 pontos
**Dependências:** Story 1.5 (Key Vault)
**Sprint:** 1

---

### Story 1.5: Configurar Key Vault para secrets e certificates

**Descrição:** Provisionar Azure Key Vault via IaC para centralizar o gerenciamento de secrets, certificados e connection strings utilizados pela aplicação. Configurar access policies para o Function App via Managed Identity.

**Critérios de Aceitação:**
- [ ] Key Vault provisionado via IaC com soft-delete e purge protection habilitados
- [ ] Access policy configurada para a Managed Identity do Function App com permissões `Get` e `List` em secrets e certificates
- [ ] Secrets de referência configurados nas application settings do Function App usando sintaxe `@Microsoft.KeyVault(...)`

**Estimativa:** 2 pontos
**Dependências:** Story 1.2 (Function App com Managed Identity)
**Sprint:** 1

---

### Story 1.6: Configurar Application Insights para monitoramento

**Descrição:** Provisionar e configurar Application Insights integrado ao Function App para coleta de telemetria, métricas customizadas e rastreamento de dependências.

**Critérios de Aceitação:**
- [ ] Application Insights provisionado via IaC e vinculado ao Function App
- [ ] Sampling configurado para balancear custo vs. visibilidade (sugestão: 25% em produção)
- [ ] Telemetria de dependências (Cosmos DB, Graph API, OpenAI) sendo capturada automaticamente

**Estimativa:** 2 pontos
**Dependências:** Story 1.2 (Function App)
**Sprint:** 1

---

### Story 1.7: Criar pipeline CI/CD (Azure DevOps ou GitHub Actions)

**Descrição:** Implementar pipeline de integração e entrega contínua que realize build, testes unitários, e deploy automático do Function App nos ambientes configurados.

**Critérios de Aceitação:**
- [ ] Pipeline de CI configurado com build e execução de testes unitários em cada push/PR
- [ ] Pipeline de CD configurado com deploy automático para ambiente de desenvolvimento e aprovação manual para staging/produção
- [ ] IaC executado como stage separada no pipeline para provisionamento de infraestrutura
- [ ] Secrets do pipeline armazenados de forma segura (variáveis protegidas ou integração com Key Vault)

**Estimativa:** 5 pontos
**Dependências:** Story 1.2 (Function App provisionado)
**Sprint:** 1

---

## Epic 2: Event Capture (Graph Webhooks)

**Objetivo:** Implementar a captura de eventos do Microsoft Teams via Graph Webhooks para detectar automaticamente quando reuniões terminam e iniciar o pipeline de processamento.

**Sprint:** 2
**Total de pontos:** 15

---

### Story 2.1: Implementar Azure Function para webhook receiver (validação de token)

**Descrição:** Criar Azure Function HTTP-triggered que atua como endpoint de recebimento de change notifications do Microsoft Graph, implementando o fluxo de validação obrigatório (validation token challenge) e verificação de assinatura.

**Critérios de Aceitação:**
- [ ] Function HTTP-triggered responde ao `validationToken` challenge com HTTP 200 e o token no body (text/plain)
- [ ] Verificação de assinatura do payload implementada usando o certificado configurado
- [ ] Endpoint acessível publicamente via HTTPS com URL estável
- [ ] Logs estruturados registrando cada notificação recebida (correlationId, resourceType, changeType)

**Estimativa:** 3 pontos
**Dependências:** Story 1.1 (App Registration), Story 1.2 (Function App)
**Sprint:** 2

---

### Story 2.2: Criar subscription no Graph para change notifications de meetings

**Descrição:** Implementar a criação programática de subscriptions no Microsoft Graph para receber change notifications quando reuniões online são criadas, atualizadas ou finalizadas.

**Critérios de Aceitação:**
- [ ] Subscription criada programaticamente via Graph API para o resource `/communications/callRecords`
- [ ] Change types configurados para capturar eventos relevantes (created)
- [ ] Subscription registrada com expiração máxima permitida pelo Graph (4230 minutos para callRecords)

**Estimativa:** 3 pontos
**Dependências:** Story 2.1 (Webhook receiver funcional)
**Sprint:** 2

---

### Story 2.3: Implementar renovação automática de subscriptions

**Descrição:** Criar mecanismo automático (Timer-triggered Function) para renovar subscriptions do Graph antes da expiração, garantindo continuidade na captura de eventos.

**Critérios de Aceitação:**
- [ ] Timer Function executando periodicamente (sugestão: a cada 24h) verificando subscriptions ativas
- [ ] Renovação automática executada quando a subscription estiver a menos de 12h da expiração
- [ ] Alerta gerado em caso de falha na renovação
- [ ] Log de auditoria registrando cada renovação com timestamps

**Estimativa:** 3 pontos
**Dependências:** Story 2.2 (Subscription criada)
**Sprint:** 2

---

### Story 2.4: Implementar handler para evento "meeting ended"

**Descrição:** Implementar a lógica de processamento que identifica quando uma reunião foi finalizada a partir da change notification recebida, extraindo os metadados necessários e enfileirando o processamento.

**Critérios de Aceitação:**
- [ ] Handler identifica corretamente eventos de callRecord com tipo `groupCall` (reuniões Teams)
- [ ] Metadados extraídos: `callId`, `organizer`, `participants`, `startDateTime`, `endDateTime`
- [ ] Mensagem enfileirada (Azure Queue Storage ou Service Bus) com metadados para processamento assíncrono
- [ ] Reuniões duplicadas detectadas e ignoradas (idempotência por `callId`)

**Estimativa:** 3 pontos
**Dependências:** Story 2.1 (Webhook receiver)
**Sprint:** 2

---

### Story 2.5: Implementar retry e dead-letter para notificações falhadas

**Descrição:** Implementar mecanismo de retry com backoff exponencial e dead-letter queue para notificações que falharam no processamento, garantindo que nenhum evento seja perdido silenciosamente.

**Critérios de Aceitação:**
- [ ] Retry configurado com backoff exponencial (3 tentativas: 1s, 5s, 30s)
- [ ] Mensagens que excedem o retry movidas para dead-letter queue
- [ ] Alerta configurado quando mensagens entram na dead-letter queue
- [ ] Dashboard mostrando volume de retries e dead-letters por período

**Estimativa:** 3 pontos
**Dependências:** Story 2.4 (Handler de eventos)
**Sprint:** 2

---

## Epic 3: Data Ingestion (Graph API)

**Objetivo:** Implementar a coleta de todos os dados necessários de uma reunião via Microsoft Graph API — metadados, transcrição, presença e chat — armazenando os dados brutos para processamento posterior.

**Sprint:** 2
**Total de pontos:** 13

---

### Story 3.1: Implementar captura de meeting metadata via Graph API

**Descrição:** Implementar a coleta de metadados completos da reunião (organizador, assunto, horários, participantes) via Microsoft Graph API a partir do callRecord recebido.

**Critérios de Aceitação:**
- [ ] Metadados coletados: `subject`, `organizer`, `startDateTime`, `endDateTime`, `joinWebUrl`
- [ ] Lista de participantes extraída com `displayName` e `userPrincipalName`
- [ ] Dados estruturados em modelo definido e prontos para persistência
- [ ] Tratamento de erro para reuniões cujos metadados não estão disponíveis

**Estimativa:** 2 pontos
**Dependências:** Story 2.4 (Evento de meeting ended processado)
**Sprint:** 2

---

### Story 3.2: Implementar captura de transcript via Graph API (com retry para disponibilidade)

**Descrição:** Implementar a coleta da transcrição da reunião via Microsoft Graph API, considerando que a transcrição pode não estar disponível imediatamente após o término da reunião (delay de até alguns minutos).

**Critérios de Aceitação:**
- [ ] Transcrição coletada via endpoint `/communications/callRecords/{id}/transcript` ou `/me/onlineMeetings/{id}/transcripts`
- [ ] Retry com backoff implementado para aguardar disponibilidade (polling a cada 30s, máximo 10 tentativas)
- [ ] Formato da transcrição parseado (VTT ou texto) com identificação de speakers
- [ ] Caso a transcrição não esteja habilitada, o fluxo continua com flag `transcriptAvailable: false`

**Estimativa:** 5 pontos
**Dependências:** Story 3.1 (Metadados da reunião disponíveis)
**Sprint:** 2

---

### Story 3.3: Implementar captura de attendance report via Graph API

**Descrição:** Implementar a coleta do relatório de presença da reunião, incluindo horários de entrada/saída de cada participante e duração total de participação.

**Critérios de Aceitação:**
- [ ] Attendance report coletado via Graph API com `attendanceRecords`
- [ ] Dados extraídos por participante: `displayName`, `joinDateTime`, `leaveDateTime`, `totalAttendanceInSeconds`
- [ ] Tratamento para reuniões sem attendance report disponível

**Estimativa:** 2 pontos
**Dependências:** Story 3.1 (Metadados da reunião)
**Sprint:** 2

---

### Story 3.4: Implementar captura de chat messages da reunião

**Descrição:** Coletar mensagens do chat da reunião via Graph API para enriquecer o contexto disponível para o processamento de IA (links compartilhados, perguntas, comentários relevantes).

**Critérios de Aceitação:**
- [ ] Mensagens do chat coletadas via endpoint do meeting chat
- [ ] Conteúdo extraído incluindo: `sender`, `body`, `createdDateTime`, `attachments` (metadados)
- [ ] Mensagens de sistema filtradas (join/leave notifications)
- [ ] Volume limitado às últimas 200 mensagens para evitar excesso de contexto

**Estimativa:** 2 pontos
**Dependências:** Story 3.1 (Metadados da reunião)
**Sprint:** 2

---

### Story 3.5: Armazenar dados brutos no Blob Storage

**Descrição:** Implementar o armazenamento dos dados brutos coletados (transcrição, metadados, attendance, chat) no Azure Blob Storage com organização por reunião e data, servindo como fonte de verdade e auditoria.

**Critérios de Aceitação:**
- [ ] Container Blob criado com estrutura: `raw/{yyyy}/{MM}/{dd}/{meetingId}/`
- [ ] Arquivos armazenados: `metadata.json`, `transcript.vtt`, `attendance.json`, `chat.json`
- [ ] Lifecycle policy configurada para mover blobs para cool tier após 30 dias
- [ ] Referência ao blob path salva no registro do Cosmos DB

**Estimativa:** 2 pontos
**Dependências:** Story 3.1 (Dados coletados)
**Sprint:** 2

---

## Epic 4: Processamento com IA (Azure OpenAI)

**Objetivo:** Processar transcrições e dados brutos das reuniões utilizando Azure OpenAI GPT-4o para extrair informações estruturadas — tópicos discutidos, decisões tomadas, ações atribuídas — e gerar documentos de ata e resumo executivo.

**Sprint:** 3
**Total de pontos:** 26

---

### Story 4.1: Implementar integração com Azure OpenAI GPT-4o

**Descrição:** Criar módulo/serviço de integração com Azure OpenAI que encapsula chamadas à API, gerenciamento de tokens, tratamento de erros e rate limiting.

**Critérios de Aceitação:**
- [ ] Módulo criado com abstração para chamadas ao Azure OpenAI (chat completions)
- [ ] Configuração externalizada: endpoint, deployment name, API version, max tokens, temperature
- [ ] Retry com backoff exponencial para erros 429 (rate limit) e 5xx
- [ ] Telemetria de cada chamada: tokens consumidos, latência, modelo utilizado

**Estimativa:** 3 pontos
**Dependências:** Story 1.4 (Azure OpenAI provisionado)
**Sprint:** 3

---

### Story 4.2: Criar prompt de extração de tópicos

**Descrição:** Desenvolver e testar o system prompt + user prompt para extração de tópicos discutidos a partir da transcrição da reunião, retornando lista estruturada com título, descrição e speakers envolvidos.

**Critérios de Aceitação:**
- [ ] Prompt retorna lista de tópicos em formato JSON estruturado
- [ ] Cada tópico contém: `title`, `description`, `speakers`, `approximateTimeRange`
- [ ] Testado com pelo menos 3 transcrições de diferentes tamanhos e contextos
- [ ] Resultados consistentes e relevantes validados manualmente

**Estimativa:** 3 pontos
**Dependências:** Story 4.1 (Integração OpenAI)
**Sprint:** 3

---

### Story 4.3: Criar prompt de extração de decisões

**Descrição:** Desenvolver e testar o prompt para extração de decisões tomadas durante a reunião, diferenciando decisões confirmadas de propostas em aberto.

**Critérios de Aceitação:**
- [ ] Prompt retorna lista de decisões em formato JSON estruturado
- [ ] Cada decisão contém: `decision`, `context`, `decidedBy`, `status` (confirmed/proposed)
- [ ] Prompt instrui o modelo a diferenciar entre decisões firmes e sugestões/propostas
- [ ] Testado com transcrições reais e resultados validados manualmente

**Estimativa:** 3 pontos
**Dependências:** Story 4.1 (Integração OpenAI)
**Sprint:** 3

---

### Story 4.4: Criar prompt de extração de ações/tarefas com responsáveis

**Descrição:** Desenvolver e testar o prompt para extração de action items com atribuição de responsáveis, prazos mencionados e prioridade inferida.

**Critérios de Aceitação:**
- [ ] Prompt retorna lista de ações em formato JSON estruturado
- [ ] Cada ação contém: `action`, `assignee`, `deadline` (se mencionado), `priority` (high/medium/low), `context`
- [ ] Prompt instrui o modelo a inferir responsáveis pelo contexto quando não explicitamente atribuídos
- [ ] Testado com transcrições reais e resultados validados manualmente

**Estimativa:** 3 pontos
**Dependências:** Story 4.1 (Integração OpenAI)
**Sprint:** 3

---

### Story 4.5: Criar prompt de geração de Ata de Reunião completa

**Descrição:** Desenvolver o prompt que gera a ata de reunião completa em formato Markdown, compilando metadados, tópicos, decisões e ações em um documento estruturado e profissional.

**Critérios de Aceitação:**
- [ ] Prompt gera documento Markdown com seções: Informações Gerais, Participantes, Pauta/Tópicos, Decisões, Ações, Próximos Passos
- [ ] Informações da reunião (data, hora, organizador, participantes) preenchidas automaticamente dos metadados
- [ ] Tom profissional e objetivo, adequado para documentação corporativa
- [ ] Documento gerado em até 30 segundos para transcrições de tamanho médio (< 30min de reunião)

**Estimativa:** 5 pontos
**Dependências:** Stories 4.2, 4.3, 4.4 (Extrações individuais)
**Sprint:** 3

---

### Story 4.6: Criar prompt de geração de Resumo Executivo

**Descrição:** Desenvolver o prompt que gera um resumo executivo conciso (máximo 500 palavras) destacando os pontos mais relevantes da reunião para stakeholders que não participaram.

**Critérios de Aceitação:**
- [ ] Resumo executivo gerado com no máximo 500 palavras
- [ ] Estrutura: Contexto (1-2 frases), Principais Decisões, Ações Críticas, Próximas Etapas
- [ ] Tom executivo e direto, focado em impacto e próximos passos
- [ ] Adequado para envio como corpo de email ou card no Teams

**Estimativa:** 3 pontos
**Dependências:** Stories 4.2, 4.3, 4.4 (Extrações individuais)
**Sprint:** 3

---

### Story 4.7: Implementar tratamento de transcrições longas (chunking + merge)

**Descrição:** Implementar estratégia de processamento para transcrições que excedem o limite de contexto do modelo, dividindo em chunks com overlap e fazendo merge inteligente dos resultados parciais.

**Critérios de Aceitação:**
- [ ] Detecção automática de transcrições que excedem 80% do limite de tokens do modelo
- [ ] Estratégia de chunking implementada com overlap de ~200 tokens entre chunks para continuidade de contexto
- [ ] Merge dos resultados parciais com deduplicação de tópicos/decisões/ações similares
- [ ] Testado com transcrição de reunião longa (>1h) e resultados coerentes

**Estimativa:** 5 pontos
**Dependências:** Stories 4.2-4.6 (Prompts individuais implementados)
**Sprint:** 3

---

## Epic 5: Entrega de Resultados

**Objetivo:** Entregar os resultados do processamento aos participantes e stakeholders — via Adaptive Card no Teams, documento no SharePoint e, opcionalmente, por email — além de persistir os dados estruturados no Cosmos DB.

**Sprint:** 4
**Total de pontos:** 21

---

### Story 5.1: Implementar geração de Adaptive Card com resumo

**Descrição:** Implementar a geração de Adaptive Card (JSON) contendo o resumo executivo, lista de decisões, ações com responsáveis e link para a ata completa no SharePoint.

**Critérios de Aceitação:**
- [ ] Adaptive Card gerada em formato JSON válido (schema 1.5+)
- [ ] Card contém seções: Header (título da reunião, data), Resumo Executivo, Decisões (lista), Ações (tabela com responsável e prazo), Link para ata completa
- [ ] Layout responsivo e visualmente limpo no cliente Teams (desktop e mobile)
- [ ] Card renderiza corretamente no Adaptive Card Designer (validação visual)

**Estimativa:** 5 pontos
**Dependências:** Story 4.5 (Ata gerada), Story 4.6 (Resumo gerado)
**Sprint:** 4

---

### Story 5.2: Implementar envio de Adaptive Card no chat da reunião via Graph API

**Descrição:** Implementar o envio da Adaptive Card gerada diretamente no chat da reunião Teams via Microsoft Graph API, utilizando a identidade do bot/aplicação.

**Critérios de Aceitação:**
- [ ] Adaptive Card enviada no chat da reunião via endpoint `/chats/{chatId}/messages` com Graph API
- [ ] Mensagem enviada com tipo `application/vnd.microsoft.card.adaptive`
- [ ] Tratamento de erro para chats que não estão mais acessíveis
- [ ] Log de confirmação com messageId e timestamp do envio

**Estimativa:** 3 pontos
**Dependências:** Story 5.1 (Adaptive Card gerada), Story 1.1 (Permissões Graph)
**Sprint:** 4

---

### Story 5.3: Implementar geração e upload de documento de ata no SharePoint

**Descrição:** Converter a ata de reunião em documento (Markdown → DOCX ou PDF) e realizar upload em uma biblioteca do SharePoint pré-configurada, organizando por data e reunião.

**Critérios de Aceitação:**
- [ ] Ata convertida para formato DOCX com formatação profissional (cabeçalho, estilos de título, tabelas)
- [ ] Upload realizado via Graph API no SharePoint: `sites/{siteId}/drive/items/{folderId}/children`
- [ ] Estrutura de pastas: `Atas de Reunião/{yyyy}/{MM}/{NomeReunião}-{dd-MM-yyyy}.docx`
- [ ] URL do documento retornada e incluída na Adaptive Card

**Estimativa:** 5 pontos
**Dependências:** Story 4.5 (Ata gerada), Story 1.1 (Permissões Graph para SharePoint)
**Sprint:** 4

---

### Story 5.4: Implementar envio de email com ata aos participantes (opcional)

**Descrição:** Implementar envio opcional de email com a ata de reunião para todos os participantes, usando Microsoft Graph API Send Mail. Funcionalidade configurável por reunião ou tenant.

**Critérios de Aceitação:**
- [ ] Email enviado via Graph API `/users/{userId}/sendMail` com corpo HTML formatado
- [ ] Documento da ata anexado ao email como DOCX
- [ ] Feature flag para habilitar/desabilitar envio de email (configuração por tenant ou global)
- [ ] Template de email profissional com resumo executivo no corpo e ata completa em anexo

**Estimativa:** 3 pontos
**Dependências:** Story 5.3 (Ata em DOCX gerada)
**Sprint:** 4

---

### Story 5.5: Armazenar dados estruturados no Cosmos DB

**Descrição:** Persistir os resultados estruturados do processamento (tópicos, decisões, ações, referências) no Cosmos DB, habilitando consultas futuras e dashboards.

**Critérios de Aceitação:**
- [ ] Documento `meeting` salvo no container `meetings` com: metadados, referência ao blob de dados brutos, referência ao documento no SharePoint, resumo executivo
- [ ] Documentos `decision` salvos no container `decisions` vinculados ao `meetingId`
- [ ] Documentos `action` salvos no container `actions` com campos `status` (pending/done), `assignee`, `deadline`
- [ ] Índice composto configurado para consultas por `date`, `organizer` e `status`

**Estimativa:** 5 pontos
**Dependências:** Story 1.3 (Cosmos DB provisionado), Stories 4.2-4.4 (Dados estruturados extraídos)
**Sprint:** 4

---

## Epic 6: Segurança e Compliance

**Objetivo:** Implementar controles de segurança, autenticação robusta, RBAC, auditoria e conformidade com políticas corporativas para proteger dados sensíveis de reuniões.

**Sprint:** 5
**Total de pontos:** 16

---

### Story 6.1: Implementar certificate-based auth para Graph API

**Descrição:** Migrar a autenticação da aplicação com Microsoft Graph de client secret para certificate-based authentication, aumentando a segurança e eliminando a necessidade de rotação manual de secrets.

**Critérios de Aceitação:**
- [ ] Certificado X.509 gerado e armazenado no Key Vault
- [ ] App Registration configurada para aceitar autenticação por certificado
- [ ] Fluxo de autenticação client_credentials com certificado implementado e testado
- [ ] Client secret anterior removido do App Registration

**Estimativa:** 3 pontos
**Dependências:** Story 1.1 (App Registration), Story 1.5 (Key Vault)
**Sprint:** 5

---

### Story 6.2: Configurar RBAC nos recursos Azure

**Descrição:** Configurar Role-Based Access Control em todos os recursos Azure do projeto, seguindo o princípio de menor privilégio, utilizando Managed Identities e roles built-in.

**Critérios de Aceitação:**
- [ ] Managed Identity do Function App com roles mínimas: `Cosmos DB Data Contributor`, `Storage Blob Data Contributor`, `Key Vault Secrets User`, `Cognitive Services OpenAI User`
- [ ] Acesso de desenvolvedores configurado via Azure AD groups com roles adequadas por ambiente
- [ ] Nenhum recurso acessível via connection string direta (tudo via Managed Identity onde possível)
- [ ] RBAC configurado via IaC para reprodutibilidade

**Estimativa:** 5 pontos
**Dependências:** Story 1.2 (Function App com Managed Identity)
**Sprint:** 5

---

### Story 6.3: Implementar audit logging de todas as operações

**Descrição:** Implementar registro de auditoria estruturado para todas as operações do sistema, incluindo captura de eventos, acesso a dados, processamento de IA e entrega de resultados.

**Critérios de Aceitação:**
- [ ] Cada operação gera log estruturado com: `operationId`, `timestamp`, `operationType`, `resourceId`, `userId` (quando aplicável), `result`
- [ ] Logs de auditoria escritos no Application Insights com customDimensions para facilitar consultas
- [ ] Log específico para cada chamada ao Azure OpenAI incluindo: tokens consumidos, prompt hash (sem conteúdo sensível)
- [ ] Query KQL documentada para consulta de audit trail por meetingId ou período

**Estimativa:** 3 pontos
**Dependências:** Story 1.6 (Application Insights)
**Sprint:** 5

---

### Story 6.4: Configurar retention policies nos dados

**Descrição:** Configurar políticas de retenção de dados em todos os stores (Cosmos DB, Blob Storage, Application Insights) alinhadas com as políticas corporativas de retenção de dados.

**Critérios de Aceitação:**
- [ ] TTL configurado no Cosmos DB para documentos de meetings (sugestão: 365 dias, configurável)
- [ ] Lifecycle management no Blob Storage: Hot → Cool (30 dias) → Archive (90 dias) → Delete (365 dias)
- [ ] Retention period do Application Insights configurado (sugestão: 90 dias)
- [ ] Documentação das políticas de retenção aplicadas

**Estimativa:** 2 pontos
**Dependências:** Story 1.3 (Cosmos DB), Story 3.5 (Blob Storage)
**Sprint:** 5

---

### Story 6.5: Implementar notificação de processamento de IA nas reuniões

**Descrição:** Implementar mecanismo de notificação aos participantes informando que a reunião será processada por IA, atendendo requisitos de transparência e compliance (LGPD/GDPR).

**Critérios de Aceitação:**
- [ ] Mensagem automática enviada no chat da reunião informando que o conteúdo será processado por IA para geração de ata
- [ ] Mensagem inclui informações sobre: finalidade do processamento, tipo de dados coletados, política de retenção
- [ ] Opção de opt-out configurável por organizador da reunião (flag no subject ou configuração)
- [ ] Registro de consentimento/ciência armazenado no audit log

**Estimativa:** 3 pontos
**Dependências:** Story 5.2 (Envio de mensagens no chat via Graph)
**Sprint:** 5

---

## Epic 7: Operações e Monitoramento

**Objetivo:** Implementar observabilidade completa, alertas proativos, health checks e documentação operacional para garantir operação confiável e manutenibilidade do sistema em produção.

**Sprint:** 6
**Total de pontos:** 11

---

### Story 7.1: Configurar dashboards no Application Insights

**Descrição:** Criar dashboards operacionais no Application Insights (ou Azure Dashboard) que forneçam visibilidade sobre o volume de reuniões processadas, taxa de sucesso, latência e consumo de tokens de IA.

**Critérios de Aceitação:**
- [ ] Dashboard com métricas: reuniões processadas/dia, taxa de sucesso (%), latência média de processamento, tokens consumidos/dia
- [ ] Gráficos de tendência para volume de processamento (últimos 7/30 dias)
- [ ] Tabela de reuniões com erro nos últimos 7 dias com link para investigação
- [ ] Dashboard compartilhável com a equipe via Azure Dashboard ou Workbook

**Estimativa:** 3 pontos
**Dependências:** Story 1.6 (Application Insights), Story 6.3 (Audit logging)
**Sprint:** 6

---

### Story 7.2: Configurar alertas para falhas de processamento

**Descrição:** Configurar alertas no Azure Monitor / Application Insights para notificar a equipe sobre falhas de processamento, degradação de performance e anomalias operacionais.

**Critérios de Aceitação:**
- [ ] Alerta configurado para: taxa de erro > 10% em janela de 15 minutos
- [ ] Alerta configurado para: latência P95 > 120 segundos
- [ ] Alerta configurado para: mensagens na dead-letter queue > 0
- [ ] Notificações enviadas via email e/ou canal Teams da equipe de operações

**Estimativa:** 2 pontos
**Dependências:** Story 1.6 (Application Insights), Story 2.5 (Dead-letter queue)
**Sprint:** 6

---

### Story 7.3: Implementar health check endpoint

**Descrição:** Criar endpoint de health check que valide conectividade e estado de todas as dependências do sistema (Cosmos DB, Graph API, Azure OpenAI, Blob Storage, Key Vault).

**Critérios de Aceitação:**
- [ ] Endpoint HTTP GET `/api/health` retornando status de cada dependência
- [ ] Response format: `{ "status": "healthy|degraded|unhealthy", "checks": { "cosmosDb": "ok", "graphApi": "ok", ... }, "timestamp": "..." }`
- [ ] Timeout de 5 segundos por check de dependência
- [ ] Endpoint utilizável por Azure Monitor ou load balancer para probes

**Estimativa:** 3 pontos
**Dependências:** Todos os recursos provisionados (Epic 1)
**Sprint:** 6

---

### Story 7.4: Documentar runbook operacional

**Descrição:** Criar documentação operacional (runbook) cobrindo procedimentos para cenários comuns de operação, troubleshooting e recuperação de falhas.

**Critérios de Aceitação:**
- [ ] Runbook documentado em Markdown no repositório com seções: Arquitetura do Sistema, Fluxo de Processamento, Procedimentos de Troubleshooting, Procedimentos de Recovery
- [ ] Procedimentos documentados para: reprocessar reunião com erro, renovar subscription manualmente, verificar e resolver dead-letters, escalar limites de Azure OpenAI
- [ ] Diagrama de arquitetura atualizado incluindo fluxo de dados e dependências
- [ ] Contatos e escalation path documentados

**Estimativa:** 3 pontos
**Dependências:** Nenhuma (pode ser feito em paralelo)
**Sprint:** 6

---

## Resumo do Backlog

| Epic | Descrição | Stories | Pontos | Sprint |
|------|-----------|---------|--------|--------|
| Epic 1 | Infraestrutura e Setup | 7 | 24 | 1 |
| Epic 2 | Event Capture (Graph Webhooks) | 5 | 15 | 2 |
| Epic 3 | Data Ingestion (Graph API) | 5 | 13 | 2 |
| Epic 4 | Processamento com IA (Azure OpenAI) | 7 | 26 | 3 |
| Epic 5 | Entrega de Resultados | 5 | 21 | 4 |
| Epic 6 | Segurança e Compliance | 5 | 16 | 5 |
| Epic 7 | Operações e Monitoramento | 4 | 11 | 6 |
| **Total** | | **33** | **119** (*)| **6 sprints** |

(*) *Com base na estimativa de complexidade relativa. Velocidade real será ajustada após Sprint 1.*

---

## Dependências Críticas entre Epics

```
Epic 1 (Infra) ──► Epic 2 (Webhooks) ──► Epic 3 (Ingestão) ──► Epic 4 (IA) ──► Epic 5 (Entrega)
                                                                                       │
Epic 6 (Segurança) ◄──────────────────────────────────────────────────────────────────┘
                                                                                       │
Epic 7 (Operações) ◄──────────────────────────────────────────────────────────────────┘
```

## Riscos Identificados

| # | Risco | Impacto | Mitigação |
|---|-------|---------|-----------|
| R1 | Transcrição não disponível via Graph API para todas as reuniões | Alto | Validar permissões e licenciamento M365 necessário; fallback para processamento apenas com chat |
| R2 | Latência do Azure OpenAI em horários de pico | Médio | Implementar fila assíncrona; processamento pode ser diferido em até 5 minutos |
| R3 | Limite de tokens insuficiente para reuniões muito longas | Médio | Story 4.7 (chunking) mitiga; validar com reuniões de 2h+ |
| R4 | Permissões de aplicação requerem aprovação de admin global do tenant | Alto | Engajar time de Identity/Security na Sprint 0 para pré-aprovação |
| R5 | Custos de Azure OpenAI excedem orçamento | Médio | Monitorar tokens consumidos; configurar hard limits no recurso; avaliar modelo menor para resumos |

---

## Definição de Pronto (Definition of Done)

Cada story será considerada **Done** quando:

1. Código implementado, revisado (code review) e mergeado na branch principal
2. Testes unitários escritos com cobertura mínima de 80% para lógica de negócio
3. Testes de integração passando no pipeline CI/CD
4. Documentação técnica atualizada (quando aplicável)
5. Deploy realizado com sucesso no ambiente de desenvolvimento
6. Critérios de aceitação validados e marcados como concluídos

---

> **Próximos passos:** Refinamento com o time técnico para validar estimativas e dependências. Agendar Sprint Planning da Sprint 1.
