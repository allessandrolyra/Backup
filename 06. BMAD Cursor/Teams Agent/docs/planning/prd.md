# PRD — Teams Meeting Secretary Agent

**Versão:** 1.0
**Última atualização:** 08/06/2026
**Autor:** Paula — Product Developer, Squad MEQ
**Status:** Rascunho para validação

---

## 1. Visão do Produto

| Campo | Descrição |
|---|---|
| **Nome** | Teams Meeting Secretary Agent |
| **Descrição** | Agente inteligente que participa de reuniões no Microsoft Teams e, ao final, gera automaticamente uma Ata de Reunião estruturada e um Resumo Executivo com os pontos-chave discutidos. |
| **Proposta de Valor** | Eliminar o trabalho manual de documentação de reuniões, garantindo que decisões, ações e responsáveis sejam capturados de forma consistente, rastreável e imediata — transformando reuniões em registros acionáveis. |

### Declaração de Visão

> Toda reunião corporativa no Teams gera documentação estruturada automaticamente, sem esforço humano — decisões nunca se perdem, ações sempre têm dono, e a informação certa chega à pessoa certa no momento certo.

---

## 2. Problema

### Contexto

Reuniões corporativas são o principal mecanismo de tomada de decisão em organizações. No entanto, a documentação dessas reuniões é sistematicamente negligenciada ou feita de forma precária.

### Problemas Identificados

| # | Problema | Impacto |
|---|---|---|
| P-01 | **Decisões se perdem** — sem registro formal, decisões tomadas em reunião são esquecidas ou contestadas posteriormente | Retrabalho, conflitos, atraso em projetos |
| P-02 | **Atas manuais são inconsistentes** — dependem de quem anota, cada pessoa registra de forma diferente | Falta de padronização, informação incompleta |
| P-03 | **Atas são demoradas** — redigir uma ata consome 20-40 minutos por reunião | Perda de produtividade; profissionais evitam a tarefa |
| P-04 | **Atas são esquecidas** — a tarefa de redigir é delegada e frequentemente não realizada | Reuniões sem registro, zero rastreabilidade |
| P-05 | **Falta de rastreabilidade de ações** — responsáveis e prazos definidos em reunião não são acompanhados | Ações não executadas, falta de accountability |
| P-06 | **Executivos não leem atas longas** — líderes precisam de resumos rápidos, mas recebem documentos extensos | Decisões desinformadas, gargalo de comunicação |

### Evidência Qualitativa

- Profissionais participam em média de 8-12 reuniões por semana (Microsoft Work Trend Index)
- Apenas ~30% das reuniões corporativas geram ata formal
- Tempo médio para redigir uma ata: 25 minutos por reunião

---

## 3. Solução Proposta

### Visão Geral

Agente inteligente baseado em IA que automaticamente:

1. **Captura** a transcrição da reunião via Microsoft Graph API após o encerramento
2. **Processa** a transcrição usando Azure OpenAI para extrair informação estruturada
3. **Gera** dois artefatos: Ata de Reunião completa e Resumo Executivo
4. **Distribui** os artefatos via Adaptive Cards no chat, email e SharePoint
5. **Armazena** dados estruturados em Cosmos DB para consulta e auditoria

### Fluxo Principal

```
Reunião encerra (com transcrição habilitada)
    ↓
Webhook / Event Grid detecta encerramento
    ↓
Azure Function captura transcrição via Graph API
    ↓
Azure OpenAI processa e extrai informação
    ↓
Gera Ata + Resumo Executivo
    ↓
┌─────────────────────────────────────────────┐
│  Adaptive Card no chat da reunião (Teams)    │
│  Ata salva no SharePoint                     │
│  Email aos participantes (se configurado)    │
│  Dados estruturados no Cosmos DB             │
└─────────────────────────────────────────────┘
```

### Diferenciais

- **Zero esforço do usuário** — funciona automaticamente, sem intervenção
- **Consistência** — toda reunião gera documentação no mesmo padrão
- **Velocidade** — ata disponível em até 5 minutos após encerramento
- **Inteligência** — IA identifica decisões, ações e responsáveis no contexto da conversa

---

## 4. Personas

### 4.1 Líder de Projeto — "Renata"

| Atributo | Descrição |
|---|---|
| **Cargo** | Gerente de Projetos / Tech Lead |
| **Necessidade principal** | Rastrear decisões e ações atribuídas à equipe |
| **Dor** | Perde tempo relembrando o que foi decidido; ações definidas em reunião não são cumpridas porque ninguém registrou |
| **Expectativa** | Receber ata estruturada com lista clara de ações, responsáveis e prazos; poder consultar decisões passadas |
| **Frequência de uso** | Diária — 3 a 5 reuniões por dia |

### 4.2 Executivo — "Carlos"

| Atributo | Descrição |
|---|---|
| **Cargo** | Diretor / C-Level |
| **Necessidade principal** | Resumos rápidos e acionáveis das reuniões que participa ou que deveria acompanhar |
| **Dor** | Não tem tempo de ler atas longas; precisa de contexto rápido antes da próxima reunião |
| **Expectativa** | Resumo executivo de 3-5 parágrafos com os pontos-chave, decisões críticas e riscos |
| **Frequência de uso** | Diária — consome resumos; raramente acessa ata completa |

### 4.3 Participante — "Marcos"

| Atributo | Descrição |
|---|---|
| **Cargo** | Analista / Desenvolvedor / Consultor |
| **Necessidade principal** | Saber exatamente quais ações foram atribuídas a ele e com que prazo |
| **Dor** | Sai da reunião sem clareza do que precisa fazer; não recebe follow-up formal |
| **Expectativa** | Notificação clara com suas ações específicas e contexto da decisão |
| **Frequência de uso** | Várias vezes por semana |

### 4.4 Compliance Officer — "Helena"

| Atributo | Descrição |
|---|---|
| **Cargo** | Analista de Compliance / DPO |
| **Necessidade principal** | Registro auditável de decisões corporativas para fins regulatórios |
| **Dor** | Decisões críticas são tomadas em reunião sem registro formal, gerando risco de compliance |
| **Expectativa** | Registro imutável com timestamp, participantes, decisões e trilha de auditoria |
| **Frequência de uso** | Sob demanda — consulta em auditorias e investigações |

### 4.5 Administrador de TI — "André"

| Atributo | Descrição |
|---|---|
| **Cargo** | Administrador Microsoft 365 / DevOps |
| **Necessidade principal** | Governar a solução — controlar permissões, monitorar uso e garantir segurança |
| **Dor** | Soluções de terceiros sem controle corporativo; preocupação com dados sensíveis de reuniões |
| **Expectativa** | Dashboard administrativo, logs de operação, controle de quais reuniões são processadas |
| **Frequência de uso** | Semanal — monitoramento e configuração |

---

## 5. Requisitos Funcionais (MVP)

| ID | Requisito | Prioridade | Persona |
|---|---|---|---|
| **FR-001** | Capturar transcrição da reunião via Graph API automaticamente após encerramento | Must Have | Todas |
| **FR-002** | Processar transcrição com Azure OpenAI para extrair tópicos, decisões, ações e responsáveis | Must Have | Renata, Carlos |
| **FR-003** | Gerar Ata de Reunião estruturada com: título, data/hora, participantes, pauta/tópicos discutidos, decisões tomadas, ações com responsável e prazo, próximos passos | Must Have | Renata, Helena |
| **FR-004** | Gerar Resumo Executivo com pontos-chave em formato conciso (3-5 parágrafos) | Must Have | Carlos |
| **FR-005** | Enviar Adaptive Card com resumo no chat da reunião no Teams | Must Have | Todas |
| **FR-006** | Salvar ata completa no SharePoint (site e biblioteca de documentos configuráveis) | Must Have | Helena, André |
| **FR-007** | Enviar email com ata aos participantes (funcionalidade opcional, configurável por reunião ou globalmente) | Should Have | Marcos, Renata |
| **FR-008** | Armazenar dados estruturados (decisões, ações, metadados) em Cosmos DB para consulta programática | Must Have | Helena, André |
| **FR-009** | Suportar reuniões agendadas com transcrição habilitada (não processar reuniões ad-hoc sem transcrição) | Must Have | Todas |
| **FR-010** | Dashboard administrativo básico com log de reuniões processadas, status e erros | Should Have | André |

### Detalhamento dos Requisitos

#### FR-001 — Captura de Transcrição

- A solução deve detectar o encerramento de reuniões via Microsoft Graph Subscriptions (webhooks) ou Event Grid
- Após detecção, recuperar a transcrição completa via `GET /communications/callRecords/{id}/transcript`
- Tratar cenários: transcrição não disponível, reunião sem transcrição habilitada, falha temporária na API
- Implementar retry com backoff exponencial (máximo 3 tentativas)

#### FR-002 — Processamento com IA

- Enviar transcrição ao Azure OpenAI (modelo GPT-4o) com prompt estruturado
- Extrair: tópicos discutidos, decisões tomadas, ações atribuídas (quem, o quê, quando), sentimento geral, riscos mencionados
- Tratar transcrições em Português Brasileiro e Inglês
- Output em formato JSON estruturado para consumo pelos demais módulos

#### FR-003 — Ata de Reunião

Formato da ata gerada:

```markdown
# Ata de Reunião — {Título}

**Data:** {DD/MM/AAAA HH:MM - HH:MM}
**Organizador:** {Nome}
**Participantes:** {Lista}
**Duração:** {X}h{Y}min

## Pauta / Tópicos Discutidos
1. {Tópico 1} — {resumo}
2. {Tópico 2} — {resumo}

## Decisões
- [D-01] {Decisão} — Aprovado por {quem}
- [D-02] {Decisão}

## Ações
| # | Ação | Responsável | Prazo | Status |
|---|---|---|---|---|
| A-01 | {Descrição} | {Nome} | {DD/MM/AAAA} | Pendente |
| A-02 | {Descrição} | {Nome} | {DD/MM/AAAA} | Pendente |

## Próximos Passos
- {Passo 1}
- {Passo 2}

## Resumo Executivo
{Resumo conciso de 3-5 parágrafos}
```

#### FR-004 — Resumo Executivo

- Texto conciso (3-5 parágrafos) destacando pontos-chave
- Deve conter: contexto da reunião, principais decisões, ações críticas, riscos ou bloqueios levantados
- Linguagem executiva — direto ao ponto, sem jargão técnico desnecessário

#### FR-005 — Adaptive Card no Teams

- Card enviado no chat da reunião dentro de 5 minutos após encerramento
- Conteúdo: título, resumo executivo (truncado), contagem de decisões e ações, link para ata completa no SharePoint
- Ações no card: "Ver Ata Completa", "Ver Minhas Ações"

#### FR-006 — Armazenamento no SharePoint

- Ata salva como arquivo `.md` ou `.docx` (configurável)
- Caminho configurável: `{Site}/{Biblioteca}/{Ano}/{Mês}/{NomeDaReunião}_{Data}.md`
- Metadados do documento: organizador, data, número de participantes, quantidade de decisões e ações

#### FR-007 — Email de Notificação

- Template de email com resumo executivo no corpo e ata completa como anexo ou link
- Destinatários: todos os participantes da reunião
- Configurável: habilitado/desabilitado globalmente e por reunião (via configuração no Teams app)

#### FR-008 — Armazenamento Estruturado

- Cosmos DB com containers: `meetings`, `decisions`, `actions`, `processing-logs`
- Partition key: `/organizerId` ou `/meetingId`
- TTL configurável por container (padrão: 365 dias para meetings, sem TTL para decisions)

#### FR-009 — Escopo de Reuniões

- Processar apenas reuniões agendadas (calendar events) com transcrição habilitada
- Não processar: calls ad-hoc, reuniões de canal sem transcrição, webinars
- Permitir opt-out por organizador (configuração no Teams app)

#### FR-010 — Dashboard Administrativo

- Interface web simples (SPA) acessível via Azure App Service
- Visualização: lista de reuniões processadas, status (sucesso/erro/pendente), timestamp, duração de processamento
- Filtros: por data, status, organizador
- Autenticação via Azure AD (roles: admin)

---

## 6. Requisitos Não-Funcionais

| ID | Requisito | Categoria | Meta |
|---|---|---|---|
| **NFR-001** | Processamento em até 5 minutos após encerramento da reunião | Performance | p95 ≤ 5 min |
| **NFR-002** | Disponibilidade do serviço | Disponibilidade | 99.5% uptime mensal |
| **NFR-003** | Suporte a reuniões de até 4 horas de duração | Capacidade | Transcrições de até ~120.000 palavras |
| **NFR-004** | Suporte a até 100 participantes por reunião | Capacidade | Sem degradação de performance |
| **NFR-005** | Dados criptografados em trânsito (TLS 1.2+) e em repouso (AES-256) | Segurança | Compliance corporativo |
| **NFR-006** | Conformidade com LGPD — dados pessoais tratados com base legal, consentimento ou legítimo interesse documentado | Compliance | Adequação regulatória |
| **NFR-007** | Logs de auditoria para todas as operações (captura, processamento, distribuição, acesso) | Auditabilidade | Retenção mínima de 1 ano |
| **NFR-008** | Suporte a Português Brasileiro e Inglês na análise de transcrição | Internacionalização | Detecção automática de idioma |

### Detalhamento

#### NFR-001 — Performance

- Tempo medido desde o encerramento da reunião até a entrega do Adaptive Card no chat
- Para reuniões de até 1 hora: meta ≤ 3 minutos
- Para reuniões de 1-4 horas: meta ≤ 5 minutos
- Monitoramento via Application Insights com alertas para p95 > 5 min

#### NFR-002 — Disponibilidade

- Calculada como: `(tempo_total - tempo_indisponível) / tempo_total × 100`
- Exclui janelas de manutenção planejada (máximo 2h/mês)
- Recuperação automática via Azure Functions retry policies

#### NFR-005 — Segurança

- Comunicação entre serviços via Managed Identity (sem secrets em código)
- Key Vault para armazenamento de configurações sensíveis
- Network security: VNet integration onde aplicável
- Princípio do menor privilégio nas permissões do Graph API

#### NFR-006 — LGPD

- Transcrições são dados pessoais — base legal deve ser documentada
- Direito de exclusão: mecanismo para remover dados de um participante
- Retenção de dados configurável com exclusão automática
- Registro de atividades de tratamento (ROPA)

#### NFR-007 — Auditoria

- Eventos auditados: reunião detectada, transcrição capturada, processamento iniciado/concluído, ata gerada, card enviado, email enviado, ata salva no SharePoint, acesso ao dashboard, erros
- Formato: JSON estruturado no Application Insights / Log Analytics
- Retenção: mínimo 12 meses

---

## 7. Fora do Escopo (MVP)

| Item | Justificativa | Considerado para |
|---|---|---|
| Analytics de reuniões (dashboard Power BI) | Complexidade adicional; MVP foca em gerar ata | V1.1 |
| RAG / base de conhecimento de reuniões | Requer indexação e busca semântica; alto esforço | V2.0 |
| Integração com Jira, Azure DevOps, Planner | Depende de mapeamento de workflows por cliente | V2.0 |
| Bot interativo durante a reunião | Requer presença em real-time na reunião; complexidade de UX | V1.1 |
| Processamento de reuniões retroativas | Requer acesso a gravações passadas; questões de consentimento | V1.1 |
| Multi-tenant | MVP atende single-tenant; multi-tenant requer arquitetura diferente | V2.0 |
| Customização de templates de ata | Template fixo no MVP; customização por tenant no futuro | V1.1 |
| Suporte a idiomas além de PT-BR e EN | Expansão de idiomas conforme demanda | V2.0 |
| Processamento de gravações de áudio/vídeo | MVP usa apenas transcrição textual disponível via Graph API | V2.0 |

---

## 8. User Stories (MVP)

### Captura e Processamento

| ID | User Story | Requisitos Relacionados |
|---|---|---|
| **US-001** | Como **Líder de Projeto**, quero que a transcrição da minha reunião seja capturada automaticamente após o encerramento, para que eu não precise lembrar de iniciar nenhum processo manual. | FR-001, FR-009 |
| **US-002** | Como **Líder de Projeto**, quero que a IA identifique automaticamente os tópicos discutidos, decisões e ações na transcrição, para que eu tenha uma ata estruturada sem esforço. | FR-002 |

### Geração de Documentos

| ID | User Story | Requisitos Relacionados |
|---|---|---|
| **US-003** | Como **Líder de Projeto**, quero receber uma ata de reunião com título, data, participantes, pauta, decisões e ações com responsável e prazo, para que eu tenha um registro completo e padronizado. | FR-003 |
| **US-004** | Como **Executivo**, quero receber um resumo executivo conciso com os pontos-chave da reunião, para que eu entenda rapidamente o que foi discutido e decidido sem ler a ata completa. | FR-004 |
| **US-005** | Como **Participante**, quero ver claramente quais ações foram atribuídas a mim, com descrição e prazo, para que eu saiba exatamente o que preciso fazer após a reunião. | FR-003, FR-005 |

### Distribuição e Armazenamento

| ID | User Story | Requisitos Relacionados |
|---|---|---|
| **US-006** | Como **Participante**, quero receber um Adaptive Card no chat da reunião com o resumo e link para a ata completa, para que eu acesse a informação sem sair do Teams. | FR-005 |
| **US-007** | Como **Compliance Officer**, quero que a ata seja salva automaticamente no SharePoint com metadados estruturados, para que eu tenha um repositório auditável e pesquisável de registros de reuniões. | FR-006 |
| **US-008** | Como **Líder de Projeto**, quero receber a ata por email (quando configurado), para que participantes externos ou que preferem email tenham acesso. | FR-007 |
| **US-009** | Como **Compliance Officer**, quero que decisões e ações sejam armazenadas de forma estruturada em banco de dados, para que eu possa consultar e auditar decisões corporativas programaticamente. | FR-008 |

### Administração

| ID | User Story | Requisitos Relacionados |
|---|---|---|
| **US-010** | Como **Administrador de TI**, quero um dashboard com log de reuniões processadas e seus status, para que eu monitore a saúde da solução e identifique problemas rapidamente. | FR-010 |
| **US-011** | Como **Administrador de TI**, quero configurar em qual site e biblioteca do SharePoint as atas são salvas, para que a solução se integre à estrutura de governança existente. | FR-006 |
| **US-012** | Como **Administrador de TI**, quero habilitar ou desabilitar o envio de email globalmente, para que eu controle como a solução se comunica com os usuários. | FR-007 |

### Qualidade e Conformidade

| ID | User Story | Requisitos Relacionados |
|---|---|---|
| **US-013** | Como **Compliance Officer**, quero que todas as operações (captura, processamento, distribuição) gerem logs de auditoria, para que eu tenha rastreabilidade completa em caso de investigação. | NFR-007 |
| **US-014** | Como **Executivo**, quero que a solução processe reuniões em Português Brasileiro e Inglês, para que funcione em reuniões com equipes internacionais. | NFR-008 |
| **US-015** | Como **Líder de Projeto**, quero que a ata esteja disponível em até 5 minutos após o encerramento da reunião, para que eu possa agir imediatamente sobre decisões e ações. | NFR-001 |

---

## 9. Critérios de Aceitação

### FR-001 — Captura de Transcrição

| # | Critério | Tipo |
|---|---|---|
| AC-001.1 | Dado que uma reunião agendada com transcrição habilitada foi encerrada, quando o evento de encerramento é detectado, então a transcrição completa é recuperada via Graph API em até 2 minutos | Funcional |
| AC-001.2 | Dado que a transcrição não está disponível imediatamente, quando a primeira tentativa falha, então o sistema executa até 3 retries com backoff exponencial (30s, 60s, 120s) | Resiliência |
| AC-001.3 | Dado que uma reunião foi encerrada sem transcrição habilitada, quando o evento é detectado, então o sistema registra o evento como "sem transcrição" e não processa | Negativo |

### FR-002 — Processamento com IA

| # | Critério | Tipo |
|---|---|---|
| AC-002.1 | Dado que uma transcrição foi capturada, quando processada pelo Azure OpenAI, então o output contém: lista de tópicos, decisões com contexto, ações com responsável identificado e prazo (quando mencionado) | Funcional |
| AC-002.2 | Dado que a transcrição está em Português Brasileiro, quando processada, então todos os campos extraídos são em Português Brasileiro | i18n |
| AC-002.3 | Dado que a transcrição está em Inglês, quando processada, então a ata é gerada no idioma detectado | i18n |
| AC-002.4 | Dado que a transcrição contém ambiguidade sobre responsáveis, quando processada, então a IA marca a ação como "Responsável: A definir" em vez de atribuir incorretamente | Qualidade |

### FR-003 — Ata de Reunião

| # | Critério | Tipo |
|---|---|---|
| AC-003.1 | Dado que o processamento foi concluído, quando a ata é gerada, então contém obrigatoriamente: título, data/hora, organizador, lista de participantes, tópicos, decisões e ações | Estrutura |
| AC-003.2 | Dado que ações foram identificadas, quando listadas na ata, então cada ação possui: descrição, responsável e prazo (ou "A definir") | Completude |
| AC-003.3 | Dado que decisões foram identificadas, quando listadas na ata, então cada decisão possui identificador único (D-01, D-02...) e contexto resumido | Rastreabilidade |

### FR-004 — Resumo Executivo

| # | Critério | Tipo |
|---|---|---|
| AC-004.1 | Dado que a ata foi gerada, quando o resumo executivo é criado, então possui entre 3 e 5 parágrafos com no máximo 500 palavras | Formato |
| AC-004.2 | Dado que a reunião teve decisões críticas, quando o resumo é gerado, então as decisões são destacadas no primeiro ou segundo parágrafo | Relevância |

### FR-005 — Adaptive Card

| # | Critério | Tipo |
|---|---|---|
| AC-005.1 | Dado que a ata foi gerada, quando o Adaptive Card é enviado, então aparece no chat da reunião em até 5 minutos após o encerramento | Performance |
| AC-005.2 | Dado que o card foi enviado, quando o usuário visualiza, então contém: título da reunião, resumo truncado (máx. 280 caracteres), contagem de decisões e ações, botões "Ver Ata Completa" e "Ver Minhas Ações" | UX |
| AC-005.3 | Dado que o usuário clica em "Ver Ata Completa", quando redirecionado, então abre a ata no SharePoint | Navegação |

### FR-006 — SharePoint

| # | Critério | Tipo |
|---|---|---|
| AC-006.1 | Dado que a ata foi gerada, quando salva no SharePoint, então está no caminho configurado com nome no formato `{TítuloDaReunião}_{AAAAMMDD}.md` | Organização |
| AC-006.2 | Dado que a ata foi salva, quando consultada no SharePoint, então possui metadados: organizador, data, número de participantes, decisões, ações | Metadados |

### FR-007 — Email

| # | Critério | Tipo |
|---|---|---|
| AC-007.1 | Dado que o envio de email está habilitado, quando a ata é gerada, então todos os participantes recebem email com resumo executivo no corpo e link para ata no SharePoint | Distribuição |
| AC-007.2 | Dado que o envio de email está desabilitado globalmente, quando a ata é gerada, então nenhum email é enviado | Configuração |

### FR-008 — Cosmos DB

| # | Critério | Tipo |
|---|---|---|
| AC-008.1 | Dado que a ata foi gerada, quando os dados são salvos no Cosmos DB, então os containers `meetings`, `decisions` e `actions` contêm os registros correspondentes | Persistência |
| AC-008.2 | Dado que uma consulta por meetingId é executada, quando os dados existem, então retorna todas as decisões e ações associadas em menos de 100ms | Performance |

### FR-009 — Escopo de Reuniões

| # | Critério | Tipo |
|---|---|---|
| AC-009.1 | Dado que uma reunião agendada com transcrição foi encerrada, quando detectada, então é processada automaticamente | Escopo |
| AC-009.2 | Dado que uma call ad-hoc sem transcrição foi encerrada, quando detectada, então não é processada e o evento é registrado como ignorado | Escopo |

### FR-010 — Dashboard

| # | Critério | Tipo |
|---|---|---|
| AC-010.1 | Dado que reuniões foram processadas, quando o admin acessa o dashboard, então visualiza lista com: data, título, organizador, status, duração do processamento | Funcional |
| AC-010.2 | Dado que o admin aplica filtro por data, quando os resultados são exibidos, então contêm apenas reuniões no período selecionado | Filtro |

---

## 10. Dependências Técnicas

### Serviços Microsoft

| Dependência | Uso | Permissões Graph API Necessárias |
|---|---|---|
| **Microsoft Graph API** | Captura de transcrições, metadados de reuniões, lista de participantes, envio de emails | `OnlineMeetings.Read.All`, `CallRecords.Read.All`, `OnlineMeetingTranscript.Read.All`, `Mail.Send`, `Sites.ReadWrite.All`, `User.Read.All` |
| **SharePoint Online** | Armazenamento das atas em bibliotecas de documentos | Acesso via Graph API com `Sites.ReadWrite.All` |
| **Microsoft Teams** | Envio de Adaptive Cards, bot presence | Bot Framework registration, `ChatMessage.Send` |

### Serviços Azure

| Dependência | Uso | SKU Recomendado |
|---|---|---|
| **Azure OpenAI Service** | Processamento de linguagem natural (extração de tópicos, decisões, ações) | Standard S0, modelo GPT-4o |
| **Azure Functions** | Orquestração do pipeline (event-driven, serverless) | Consumption Plan (MVP), Premium Plan (produção) |
| **Cosmos DB** | Armazenamento de dados estruturados (decisões, ações, metadados) | Serverless (MVP) |
| **Azure Key Vault** | Gestão de secrets e configurações sensíveis | Standard |
| **Application Insights** | Monitoramento, logs, métricas de performance | — |
| **Azure Event Grid** | Roteamento de eventos de encerramento de reuniões | — |
| **Azure App Service** | Hosting do dashboard administrativo | B1 (MVP) |

### Infraestrutura e Configuração

| Dependência | Descrição |
|---|---|
| **App Registration (Azure AD)** | Registro da aplicação com admin consent para permissões do Graph API |
| **Bot Framework Registration** | Registro do bot para envio de mensagens no Teams |
| **Teams App Manifest** | Pacote da app para instalação no Teams Admin Center |
| **Service Principal / Managed Identity** | Autenticação entre serviços Azure sem secrets |

---

## 11. Requisitos de Licenciamento

### Microsoft 365

| Licença | Necessidade | Observação |
|---|---|---|
| **Microsoft Teams E3/E5** ou **Teams Premium** | Obrigatória para transcrição de reuniões | Transcrição é feature de Teams Premium ou M365 E3+ com Compliance add-on |
| **SharePoint Online (Plan 1+)** | Armazenamento de atas | Incluído em M365 E3/E5 |
| **Exchange Online** | Envio de emails de notificação | Incluído em M365 E3/E5 |

### Azure

| Recurso | Modelo de Custo | Estimativa Mensal (MVP — 500 reuniões/mês) |
|---|---|---|
| **Azure OpenAI (GPT-4o)** | Pay-per-token (input + output) | ~R$ 1.500 - R$ 3.000 |
| **Azure Functions** | Consumption (execuções + GB-s) | ~R$ 50 - R$ 150 |
| **Cosmos DB** | Serverless (RU/s consumidos + storage) | ~R$ 100 - R$ 300 |
| **Application Insights** | Ingestão de dados (GB/mês) | ~R$ 50 - R$ 100 |
| **Azure App Service (B1)** | Plano fixo mensal | ~R$ 80 |
| **Key Vault** | Operações + secrets | < R$ 10 |
| **Estimativa Total** | — | **~R$ 1.800 - R$ 3.600/mês** |

> **Nota:** Valores estimados com base em pricing de junho/2026. Custos reais variam conforme volume e duração das reuniões.

---

## 12. Riscos

| ID | Risco | Probabilidade | Impacto | Mitigação |
|---|---|---|---|---|
| **R-01** | **Transcrição indisponível ou incompleta** — Graph API pode não retornar transcrição imediatamente ou pode estar incompleta | Alta | Alto | Implementar retry com backoff; validar completude da transcrição antes de processar; alertar admin em caso de falha após retries |
| **R-02** | **Qualidade da extração por IA** — GPT-4o pode interpretar incorretamente decisões, atribuir ações ao responsável errado ou omitir informações | Média | Alto | Prompt engineering iterativo; testes com transcrições reais diversas; incluir disclaimer na ata ("gerado por IA — verifique as informações"); feedback loop para melhoria contínua |
| **R-03** | **Resistência organizacional** — usuários podem resistir à adoção por desconfiança na IA ou medo de monitoramento | Média | Médio | Comunicação clara sobre propósito; opt-out por organizador; demonstração de valor com pilotos; política de uso transparente |
| **R-04** | **Custos de Azure OpenAI acima do esperado** — transcrições longas geram alto consumo de tokens | Média | Médio | Monitorar custo por reunião; implementar truncamento inteligente de transcrições longas; definir budget alerts no Azure; avaliar modelos menores para reuniões simples |
| **R-05** | **Mudanças na Graph API** — Microsoft pode alterar endpoints, permissões ou comportamento da API de transcrições | Baixa | Alto | Abstrair integrações em camada de serviço; monitorar changelog da Graph API; manter versão da API fixada; testes de integração automatizados |
| **R-06** | **Violação de LGPD / privacidade** — processamento de transcrições pode expor dados pessoais ou sensíveis | Baixa | Crítico | DPIA (Data Protection Impact Assessment) antes do go-live; base legal documentada; mecanismo de exclusão de dados; comunicação transparente; consultoria jurídica |
| **R-07** | **Latência no processamento de reuniões longas** — reuniões de 4 horas podem exceder o SLA de 5 minutos | Média | Médio | Chunking da transcrição para processamento paralelo; otimização do prompt; monitoramento de latência por duração de reunião |
| **R-08** | **Admin consent bloqueado** — equipe de segurança pode rejeitar permissões do Graph API (especialmente `CallRecords.Read.All`) | Média | Crítico | Engajar equipe de segurança/compliance no início do projeto; documentar justificativa para cada permissão; oferecer escopo mínimo de permissões; POC com ambiente de desenvolvimento |
| **R-09** | **Limites de rate da Graph API** — volume alto de reuniões simultâneas pode atingir throttling | Baixa | Médio | Implementar queue (Service Bus) para processamento sequencial; respeitar headers de retry-after; distribuir processamento ao longo do tempo |

---

## 13. Métricas de Sucesso

### KPIs Primários

| Métrica | Meta (MVP) | Meta (6 meses) | Como Medir |
|---|---|---|---|
| **% de reuniões processadas com sucesso** | ≥ 90% | ≥ 98% | `reuniões processadas / reuniões elegíveis × 100` — Application Insights |
| **Tempo médio de processamento** | ≤ 5 min (p95) | ≤ 3 min (p95) | Timestamp: encerramento → card entregue — Application Insights |
| **Satisfação do usuário (CSAT)** | ≥ 3.5/5 | ≥ 4.0/5 | Survey in-app trimestral (via Forms) |
| **Redução de tempo em atas manuais** | ≥ 50% | ≥ 80% | Survey comparativo antes/depois com grupo piloto |

### KPIs Secundários

| Métrica | Meta | Como Medir |
|---|---|---|
| **Precisão da extração de ações** | ≥ 85% de ações corretamente identificadas | Amostragem manual mensal (20 reuniões) |
| **Precisão da atribuição de responsáveis** | ≥ 80% de responsáveis corretamente atribuídos | Amostragem manual mensal (20 reuniões) |
| **Taxa de adoção** | ≥ 60% dos organizadores com transcrição habilitada utilizam a solução | Telemetria de uso / reuniões elegíveis vs processadas |
| **Taxa de erro** | ≤ 5% de falhas no pipeline | Logs de processamento — Application Insights |
| **Custo por reunião processada** | ≤ R$ 7,00 | Custos Azure / número de reuniões processadas |

### Metodologia de Medição

- **Dashboard de métricas** via Application Insights / Azure Monitor
- **Relatório mensal** consolidado pelo Administrador de TI
- **Survey trimestral** com usuários piloto via Microsoft Forms
- **Amostragem de qualidade** mensal: revisão manual de 20 atas para validar precisão

---

## 14. Roadmap

### MVP — Sprints 1 a 3 (6 semanas)

| Sprint | Foco | Entregas |
|---|---|---|
| **Sprint 1** | Infraestrutura e captura | App Registration, permissões Graph API, Azure Functions scaffold, webhook de encerramento de reunião, captura de transcrição (FR-001), armazenamento bruto |
| **Sprint 2** | Processamento e geração | Integração Azure OpenAI, prompt engineering, extração de dados (FR-002), geração de ata (FR-003), geração de resumo executivo (FR-004), Cosmos DB (FR-008) |
| **Sprint 3** | Distribuição e administração | Adaptive Card (FR-005), SharePoint storage (FR-006), email opcional (FR-007), dashboard administrativo básico (FR-010), testes end-to-end, deploy em staging |

**Marco: MVP validado com grupo piloto (5-10 organizadores, 2 semanas de piloto)**

### V1.1 — Sprints 4 a 5 (4 semanas)

| Sprint | Foco | Entregas |
|---|---|---|
| **Sprint 4** | Bot interativo e refinamentos | Bot que pode ser adicionado à reunião (presença visual), refinamentos de UX no Adaptive Card, customização básica de templates de ata, processamento de reuniões retroativas (últimos 30 dias) |
| **Sprint 5** | Analytics e configurações | Dashboard de analytics básico (frequência de reuniões, ações pendentes), configurações por equipe/departamento, notificações de ações pendentes (follow-up automático) |

**Marco: V1.1 em produção com rollout para departamento inteiro**

### V2.0 — Sprints 6 a 8 (6 semanas)

| Sprint | Foco | Entregas |
|---|---|---|
| **Sprint 6** | RAG e busca semântica | Indexação de atas em Azure AI Search, busca semântica ("O que decidimos sobre X?"), base de conhecimento de reuniões |
| **Sprint 7** | Integrações externas | Criação automática de tasks no Planner/Azure DevOps/Jira a partir de ações, sincronização de status |
| **Sprint 8** | Multi-tenant e escala | Arquitetura multi-tenant, onboarding self-service, dashboard Power BI avançado, suporte a idiomas adicionais |

**Marco: V2.0 — produto escalável, pronto para múltiplos clientes/departamentos**

### Visão de Longo Prazo (V3.0+)

- Participação ativa na reunião (sugestões em tempo real, alertas de pauta)
- Integração com Copilot for Microsoft 365
- Análise de sentimento e dinâmica de reuniões
- Recomendações de eficiência ("esta reunião poderia ter sido um email")
- API pública para integrações customizadas

---

## Apêndice A — Glossário

| Termo | Definição |
|---|---|
| **Ata de Reunião** | Documento formal que registra o que foi discutido, decidido e as ações atribuídas em uma reunião |
| **Resumo Executivo** | Versão concisa da ata focada em pontos-chave para leitura rápida |
| **Adaptive Card** | Componente visual interativo do Microsoft Teams para exibir informações estruturadas |
| **Graph API** | API da Microsoft para acessar dados do Microsoft 365 (calendário, reuniões, transcrições, SharePoint) |
| **Transcrição** | Texto gerado automaticamente pelo Teams a partir do áudio da reunião |
| **Admin Consent** | Aprovação do administrador do tenant para conceder permissões de aplicação |

## Apêndice B — Referências

- [Microsoft Graph API — Online Meetings](https://learn.microsoft.com/en-us/graph/api/resources/onlinemeeting)
- [Microsoft Graph API — Call Records](https://learn.microsoft.com/en-us/graph/api/resources/callrecords-callrecord)
- [Azure OpenAI Service](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Bot Framework — Adaptive Cards](https://learn.microsoft.com/en-us/microsoftteams/platform/task-modules-and-cards/cards/cards-reference)
- [LGPD — Lei Geral de Proteção de Dados](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm)

---

*Documento gerado por Paula — Product Developer, Squad MEQ*
*Para dúvidas ou sugestões, entre em contato com a squad de produto.*
