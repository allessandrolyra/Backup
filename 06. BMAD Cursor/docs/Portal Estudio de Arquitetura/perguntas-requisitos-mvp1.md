# Portal de Arquitetura e DevOps — Perguntas para Levantamento de Requisitos Funcionais (MVP1)

**Data:** 22/05/2026
**Objetivo:** Guia de perguntas para conduzir sessões de descoberta com stakeholders e definir os requisitos funcionais do MVP1.
**Como usar:** Conduza essas perguntas com o time do Studio, Tech Leads e potenciais usuários. As respostas alimentam diretamente o PRD.

---

## 1. Catálogo de Templates

### 1.1 Conteúdo e Organização

| # | Pergunta | Por que importa |
|---|---|---|
| 1.1.1 | Quais tipos de template existem hoje? (Terraform, Helm charts, Dockerfiles, pipelines YAML, ARM/Bicep, scripts, outros) | Define as categorias iniciais do catálogo |
| 1.1.2 | Quantos templates existem prontos para catalogar agora? (5? 20? 50?) | Dimensiona o esforço de carga inicial e valida se o portal já nasce com conteúdo útil |
| 1.1.3 | Onde esses templates estão hoje? (repos Azure DevOps, máquinas pessoais, wikis, SharePoint) | Define o esforço de migração e se a integração com Azure DevOps cobre tudo |
| 1.1.4 | Existe versionamento dos templates? (v1, v2, etc.) Ou sempre se usa o "último"? | Define se o portal precisa gerenciar versões ou se basta apontar para a branch main |
| 1.1.5 | Os templates são genéricos ou específicos por cliente? (ex: "Terraform VPC genérico" vs "Terraform infra Cliente X") | Define se precisa de visibilidade restrita por cliente/projeto |
| 1.1.6 | Existe alguma classificação por cloud provider? (Azure, AWS, GCP, multi-cloud) | Define filtros e organização do catálogo |
| 1.1.7 | Os templates têm documentação hoje? (README, diagramas, pré-requisitos) | Define se o portal precisa de um campo obrigatório de documentação ou se aceita templates "crus" |

### 1.2 Busca e Descoberta

| # | Pergunta | Por que importa |
|---|---|---|
| 1.2.1 | Como as pessoas buscam templates hoje? (perguntam para alguém? procuram no DevOps? não procuram?) | Valida a dor real e define a UX de busca |
| 1.2.2 | Quais filtros seriam mais úteis? (categoria, cloud, linguagem, autor, squad, tags livres) | Define os filtros prioritários da interface |
| 1.2.3 | O usuário precisa ver o código antes de baixar? (preview inline do repo) | Define se a integração com Azure DevOps API precisa renderizar arquivos |
| 1.2.4 | Precisa de busca full-text dentro do conteúdo dos templates? Ou busca por título/tag é suficiente? | Impacta a complexidade da busca (PostgreSQL full-text vs Elasticsearch futuro) |

### 1.3 Consumo e Download

| # | Pergunta | Por que importa |
|---|---|---|
| 1.3.1 | O usuário prefere baixar um ZIP ou clonar diretamente do repo? | Define se o Blob Storage é necessário no MVP ou se basta um link para o Azure DevOps |
| 1.3.2 | Precisa rastrear quem baixou o quê? (para métricas e auditoria) | Define a tabela de downloads e a política de privacidade |
| 1.3.3 | Após baixar, o usuário precisa de instruções de uso? (um "getting started" passo a passo) | Define se cada template precisa de um campo estruturado de instruções |
| 1.3.4 | Existe algum processo de aprovação antes de um template ser publicado? | Define se precisa de workflow de aprovação (draft -> review -> publicado) |

### 1.4 Contribuição

| # | Pergunta | Por que importa |
|---|---|---|
| 1.4.1 | Quem pode publicar templates? Só o Studio ou qualquer Tech Lead pode contribuir? | Define os perfis de acesso (Admin vs Contribuidor) |
| 1.4.2 | Se qualquer pessoa pode contribuir, precisa de revisão/aprovação antes de publicar? | Define workflow de moderação |
| 1.4.3 | O que acontece quando alguém encontra um bug num template? Abre issue? Edita direto? | Define o fluxo de feedback e correção |

---

## 2. Repositório de POCs

### 2.1 Conteúdo e Estrutura

| # | Pergunta | Por que importa |
|---|---|---|
| 2.1.1 | O que define uma POC no contexto do Studio? (código + documentação? só documentação? apresentação?) | Define os campos obrigatórios do cadastro |
| 2.1.2 | Quantas POCs já foram realizadas que poderiam ser catalogadas? | Dimensiona o conteúdo inicial |
| 2.1.3 | Quais informações são essenciais sobre cada POC? (problema, solução, resultado, lições aprendidas, custo, tempo) | Define os metadados do modelo |
| 2.1.4 | Uma POC tem ciclo de vida? (Em andamento -> Concluída -> Produtizada -> Arquivada) | Define os status e transições |
| 2.1.5 | POCs podem ter múltiplos artefatos? (código, slides, vídeo de demo, relatório) | Define o modelo de anexos e tipos de arquivo aceitos |
| 2.1.6 | POCs são sempre internas ou algumas são feitas em conjunto com clientes? | Define visibilidade e restrições de acesso |

### 2.2 Reutilização

| # | Pergunta | Por que importa |
|---|---|---|
| 2.2.1 | O objetivo principal é que alguém pegue o código da POC e replique em outro ambiente? | Valida se o foco é no download ou na documentação |
| 2.2.2 | Precisa de um guia de "como replicar esta POC"? | Define se há um campo estruturado de replicação |
| 2.2.3 | Quando uma POC vira solução produtizada, o que muda no portal? (muda de seção? recebe selo?) | Define a relação POC -> Template/Solução |

---

## 3. Sistema de Issues / Solicitações ao CoE

### 3.1 Abertura e Classificação

| # | Pergunta | Por que importa |
|---|---|---|
| 3.1.1 | Quais tipos de solicitação o CoE recebe hoje? (consultoria, revisão arquitetural, apoio a incidente, dúvida técnica, suporte a proposta comercial) | Define as categorias de issue |
| 3.1.2 | O modelo de severidade com 5 dimensões (da apresentação) já está validado com as torres? | Confirma se o modelo é aceito ou precisa de ajuste |
| 3.1.3 | Quem faz a triagem das issues? O sistema atribui automaticamente ou alguém do Studio distribui? | Define se precisa de auto-assign por skill ou triagem manual |
| 3.1.4 | Precisa de SLA diferenciado por tipo de solicitação (além da severidade)? | Refina as regras de SLA |
| 3.1.5 | O que acontece quando o SLA estoura? Escalonamento automático? Notificação? Para quem? | Define regras de escalonamento |
| 3.1.6 | O solicitante precisa acompanhar o progresso? (comentários, status, estimativa de resolução) | Define a interface do solicitante |

### 3.2 Resolução e Histórico

| # | Pergunta | Por que importa |
|---|---|---|
| 3.2.1 | Como a issue é resolvida? O especialista responde no portal? Anexa documentos? Agenda reunião? | Define o fluxo de resolução e os campos necessários |
| 3.2.2 | Precisa de base de conhecimento? (issues resolvidas viram FAQ/artigos) | Define se issues fechadas alimentam uma base consultável |
| 3.2.3 | O solicitante avalia a resolução? (NPS, satisfação) | Define se o NPS Técnico é coletado por issue |
| 3.2.4 | Issues podem gerar templates? (ex: uma dúvida recorrente vira um template padrão) | Define a relação issue -> template |

### 3.3 Integração

| # | Pergunta | Por que importa |
|---|---|---|
| 3.3.1 | As issues do portal substituem outro canal? (Teams, e-mail, Azure DevOps Boards) Ou coexistem? | Define se precisa de integração bidirecional com outras ferramentas |
| 3.3.2 | Precisa de integração com Azure DevOps Boards para tracking no backlog do Studio? | Define se o portal cria work items no DevOps automaticamente |
| 3.3.3 | Notificações vão por onde? (e-mail, Teams, só no portal) | Define os canais de notificação do MVP |

---

## 4. Dashboard de Métricas

### 4.1 Métricas de Consumo

| # | Pergunta | Por que importa |
|---|---|---|
| 4.1.1 | Quais métricas de consumo são mais importantes? (downloads, visualizações, clones, favoritos) | Prioriza o que rastrear no MVP |
| 4.1.2 | Precisa saber quais squads usaram cada template? Ou basta o total? | Define o nível de granularidade (anônimo vs rastreado) |
| 4.1.3 | Como calcular "horas economizadas"? Tempo estimado de criar do zero vs usar o template? Quem define esse número? | Define a fórmula e quem alimenta o dado (admin? auto-estimativa?) |
| 4.1.4 | O cálculo de horas economizadas é por template (fixo) ou por download (o usuário informa)? | Define se é input do admin ou do consumidor |

### 4.2 Métricas do CoE

| # | Pergunta | Por que importa |
|---|---|---|
| 4.2.1 | Das 5 métricas core da apresentação (SLA Compliance, NPS Técnico, Knowledge Distribution, Cost per Request, Adoção de Padrões), quais entram no MVP1? | Evita escopo excessivo no dashboard |
| 4.2.2 | Quem visualiza o dashboard? Todos ou só gestores/admins? | Define controle de acesso ao dashboard |
| 4.2.3 | Precisa de exportação? (PDF, Excel, PowerPoint para apresentações) | Define funcionalidades de relatório |
| 4.2.4 | Qual o período de análise? (último mês, trimestre, ano, personalizado) | Define os filtros temporais |

### 4.3 Métricas de Contribuição

| # | Pergunta | Por que importa |
|---|---|---|
| 4.3.1 | Quer um ranking de squads/pessoas que mais contribuíram? (gamificação leve) | Define se há elementos de incentivo à contribuição |
| 4.3.2 | Contribuição é medida como? (templates publicados, POCs criadas, issues respondidas, ratings dados) | Define o cálculo do score de contribuição |
| 4.3.3 | Esse ranking é público (visível a todos) ou restrito a gestores? | Define a política de transparência |

---

## 5. Usuários, Perfis e Acesso

| # | Pergunta | Por que importa |
|---|---|---|
| 5.1 | Quantos perfis de acesso no MVP? Sugestão: Admin, Contribuidor, Consumidor. Faz sentido? | Define a matriz de permissões |
| 5.2 | Os perfis são atribuídos manualmente ou baseados em grupos do Azure AD? | Define se sincroniza com AD groups |
| 5.3 | Precisa de auditoria? (log de quem fez o quê e quando) | Define o nível de compliance exigido |
| 5.4 | Usuários externos (clientes) acessam no MVP1 ou isso fica para depois? | Delimita o escopo de multi-tenancy |
| 5.5 | Precisa de funcionalidade de "favoritos" ou "minha biblioteca"? | Define personalização do portal por usuário |

---

## 6. Perguntas Transversais

| # | Pergunta | Por que importa |
|---|---|---|
| 6.1 | Qual o nome oficial do portal? (Portal de Arquitetura, Hub do CoE, Studio Assets, outro) | Define o branding e a URL |
| 6.2 | Existe algum portal ou ferramenta similar na Foursys hoje que devemos integrar ou substituir? | Evita duplicação e conflito com iniciativas existentes |
| 6.3 | Quem é o Product Owner deste portal? Quem aprova o que entra no MVP? | Define a cadeia de decisão |
| 6.4 | O portal precisa funcionar offline ou em rede interna restrita? | Impacta a arquitetura de hosting |
| 6.5 | Existe requisito de compliance específico? (LGPD para dados de usuários, ISO 27001, SOC2) | Define requisitos de segurança e auditoria |
| 6.6 | Qual a tolerância a downtime? (portal pode ficar fora no fim de semana?) | Refina o SLA de disponibilidade |
| 6.7 | Existe budget definido para infra e desenvolvimento? | Restringe ou amplia opções técnicas |

---

## 7. Funcionalidades Futuras (para NÃO entrar no MVP1, mas validar interesse)

Estas perguntas ajudam a mapear o roadmap sem inflacionar o MVP.

| # | Funcionalidade | Pergunta |
|---|---|---|
| 7.1 | **IA Analysis** | Qual caso de uso? Análise de código? Sugestão de templates? Review automatizado de arquitetura? |
| 7.2 | **Marketplace** | Quando o portal virar produto, será self-service (cliente sobe o próprio portal) ou SaaS multi-tenant? |
| 7.3 | **CLI** | Seria útil um CLI para baixar templates direto do terminal? (ex: `studio pull terraform-vpc-azure`) |
| 7.4 | **Integração Teams** | Bot no Teams para buscar templates ou receber notificações de issues? |
| 7.5 | **ADR Repository** | O portal deve hospedar os ADRs (Architecture Decision Records) das torres também? |
| 7.6 | **Runbooks** | Os runbooks de incidentes mencionados na apresentação ficam no portal ou na Wiki separada? |
| 7.7 | **Technology Radar** | O Technology Radar do CoE (Adotar/Experimentar/Avaliar/Abandonar) é publicado pelo portal? |

---

## Como Conduzir as Sessões

**Formato sugerido:** 3 sessões de 1h com grupos diferentes

| Sessão | Participantes | Foco | Seções deste doc |
|---|---|---|---|
| **Sessão 1** | Time do Studio (admins do portal) | Conteúdo, publicação, issues, métricas do CoE | 1.1, 1.4, 2.1, 3.1, 4.2 |
| **Sessão 2** | Tech Leads e Arquitetos das torres (consumidores) | Busca, consumo, solicitações, o que falta hoje | 1.2, 1.3, 2.2, 3.2, 4.1 |
| **Sessão 3** | Gestores (Head Studio, Diretoria) | Métricas de impacto, compliance, budget, roadmap | 4.2, 4.3, 5, 6, 7 |

**Dica:** Priorize as perguntas marcando com o time quais são "must have" para o MVP1 e quais podem esperar.

---

*Após as sessões, consolide as respostas e volte para transformá-las em requisitos funcionais formais no PRD.*
