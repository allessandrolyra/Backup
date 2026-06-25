# Portal de Arquitetura e DevOps — C4 Model (N1 e N2)

**Data:** 22/05/2026
**Autor:** Studio de Arquitetura e DevOps — Foursys
**Status:** Rascunho para discussão
**Versão:** 0.1

---

## C4 Model — Nível 1: Diagrama de Contexto

> **Objetivo:** Mostrar o sistema como uma "caixa preta" e seus relacionamentos com pessoas e sistemas externos. Responde à pergunta: *quem usa o sistema e com o que ele se comunica?*

```mermaid
graph TB
    subgraph personas [Personas]
        AdminStudio["<b>Administrador do Studio</b><br/>(Arquitetos, Eng. DevOps)<br/>Publica templates, POCs,<br/>responde issues, analisa métricas"]
        TechLead["<b>Tech Lead / Arquiteto de Torre</b><br/>Busca templates, abre issues,<br/>contribui com POCs"]
        Dev["<b>Desenvolvedor de Squad</b><br/>Consome templates, baixa POCs,<br/>avalia artefatos"]
        Gestor["<b>Gestor / Head Studio</b><br/>Acompanha métricas de impacto,<br/>adoção e SLA"]
        ClienteExterno["<b>Cliente Externo (futuro)</b><br/>Acessa catálogo de soluções<br/>e assets disponibilizados"]
    end

    Portal["<b>Portal de Arquitetura e DevOps</b><br/><i>Sistema Web</i><br/><br/>Hub centralizado para<br/>descoberta, consumo e<br/>contribuição de assets técnicos,<br/>gestão de issues e<br/>métricas de impacto do CoE"]

    subgraph external [Sistemas Externos]
        AzureAD["<b>Microsoft Entra ID</b><br/><i>(Azure AD)</i><br/>Autenticação SSO corporativa"]
        AzureDevOps["<b>Azure DevOps</b><br/><i>(Repos + Pipelines)</i><br/>Fonte dos repositórios<br/>de código e templates"]
        BlobStorage["<b>Azure Blob Storage</b><br/><i>(Object Storage)</i><br/>Armazenamento de artefatos<br/>(ZIPs, docs, diagramas)"]
        Email["<b>Sistema de E-mail</b><br/><i>(SMTP / SendGrid)</i><br/>Notificações de issues,<br/>SLA e atualizações"]
    end

    AdminStudio -->|"Publica, gerencia,<br/>responde issues"| Portal
    TechLead -->|"Busca, contribui,<br/>abre issues"| Portal
    Dev -->|"Busca, baixa,<br/>avalia"| Portal
    Gestor -->|"Visualiza dashboards<br/>e métricas"| Portal
    ClienteExterno -.->|"Acessa catálogo<br/>(futuro MVP2+)"| Portal

    Portal -->|"Autentica usuários<br/>via OAuth 2.0 / OIDC"| AzureAD
    Portal -->|"Consulta repos, lê READMEs,<br/>sincroniza templates"| AzureDevOps
    Portal -->|"Upload/download de<br/>artefatos via SAS tokens"| BlobStorage
    Portal -.->|"Envia notificações<br/>(futuro)"| Email
```

### Legenda do Diagrama de Contexto

| Elemento | Tipo | Descrição |
|---|---|---|
| **Administrador do Studio** | Persona | Arquitetos e Eng. DevOps do Studio que publicam e gerenciam conteúdo |
| **Tech Lead / Arquiteto de Torre** | Persona | Consumidores avançados que também contribuem com assets |
| **Desenvolvedor de Squad** | Persona | Consumidor principal — busca e baixa templates/POCs |
| **Gestor / Head Studio** | Persona | Visualiza métricas de impacto e adoção |
| **Cliente Externo** | Persona (futuro) | Acesso externo quando o portal virar produto |
| **Portal de Arquitetura e DevOps** | Sistema (nosso) | O sistema sendo construído |
| **Microsoft Entra ID** | Sistema externo | Autenticação corporativa SSO |
| **Azure DevOps** | Sistema externo | Repositórios de código fonte existentes |
| **Azure Blob Storage** | Sistema externo | Armazenamento de artefatos para download |
| **Sistema de E-mail** | Sistema externo (futuro) | Notificações assíncronas |

### Fluxos Principais (N1)

| # | Fluxo | Descrição |
|---|---|---|
| F1 | Publicação | Admin cria/edita template ou POC no portal, que armazena metadados no banco e artefatos no Blob Storage |
| F2 | Descoberta | Dev busca no catálogo, filtra por tags/categoria, visualiza README inline (via Azure DevOps API) |
| F3 | Consumo | Dev baixa template/POC (download via SAS token do Blob Storage), contador incrementa |
| F4 | Solicitação | Tech Lead abre issue para o CoE, sistema calcula severidade e inicia timer de SLA |
| F5 | Métricas | Gestor acessa dashboard com horas economizadas, adoção por squad, SLA compliance |

---

## C4 Model — Nível 2: Diagrama de Container

> **Objetivo:** Abrir a "caixa preta" do Nível 1 e mostrar os containers (aplicações, bases de dados, serviços) que compõem o sistema. Responde à pergunta: *quais são as peças técnicas e como se comunicam?*

```mermaid
graph TB
    subgraph personas [Personas]
        Admin["Administrador Studio"]
        TechLead["Tech Lead"]
        Dev["Desenvolvedor"]
        Gestor["Gestor"]
    end

    subgraph portalSystem ["Portal de Arquitetura e DevOps (System Boundary)"]

        WebApp["<b>Web Application</b><br/><i>Next.js 14 + TypeScript</i><br/><br/>Interface do portal:<br/>catálogo, POCs, issues,<br/>dashboard de métricas<br/><br/><i>Azure App Service</i>"]

        APIServer["<b>API Server</b><br/><i>NestJS + TypeScript</i><br/><br/>Lógica de negócio,<br/>autenticação, autorização,<br/>integrações externas<br/><br/><i>Azure App Service</i>"]

        Database[("<b>Database</b><br/><i>PostgreSQL 16</i><br/><br/>Templates, POCs, Issues,<br/>Users, Downloads,<br/>Ratings, Métricas<br/><br/><i>Azure DB Flexible Server</i>")]

        Cache["<b>Cache Layer</b><br/><i>Redis (futuro MVP2)</i><br/><br/>Cache de catálogo,<br/>sessões, rate limiting"]
    end

    subgraph external [Sistemas Externos]
        AzureAD["<b>Microsoft Entra ID</b><br/><i>OAuth 2.0 / OIDC</i>"]
        DevOpsAPI["<b>Azure DevOps API</b><br/><i>REST API v7</i>"]
        BlobStore["<b>Azure Blob Storage</b><br/><i>Containers de artefatos</i>"]
    end

    Admin -->|"HTTPS"| WebApp
    TechLead -->|"HTTPS"| WebApp
    Dev -->|"HTTPS"| WebApp
    Gestor -->|"HTTPS"| WebApp

    WebApp -->|"REST API<br/>JSON/HTTPS"| APIServer

    APIServer -->|"Prisma ORM<br/>TCP/5432"| Database
    APIServer -.->|"get/set<br/>TCP/6379 (futuro)"| Cache
    APIServer -->|"OAuth 2.0 / OIDC<br/>HTTPS"| AzureAD
    APIServer -->|"REST API<br/>PAT Token / HTTPS"| DevOpsAPI
    APIServer -->|"SDK @azure/storage-blob<br/>HTTPS + SAS"| BlobStore
```

### Detalhamento dos Containers

---

#### Container 1: Web Application (Frontend)

| Atributo | Valor |
|---|---|
| **Tecnologia** | Next.js 14+, React 18, TypeScript |
| **Hospedagem** | Azure App Service (B1) |
| **Responsabilidade** | Interface do usuário, SSR, navegação, formulários |

**Módulos da interface:**

| Módulo | Funcionalidade |
|---|---|
| **Catálogo de Templates** | Listagem com grid/cards, busca full-text, filtros por categoria/tag/cloud, preview de README, botão de download |
| **Repositório de POCs** | Listagem de POCs com status, detalhes com problema/solução/lições, download de artefatos, rating |
| **Painel de Issues** | Formulário de abertura, calculadora de severidade, kanban de status, timer SLA visível, comentários |
| **Dashboard de Métricas** | Gráficos de downloads, horas economizadas, adoção por squad, SLA compliance, ranking de contribuidores |
| **Administração** | CRUD de templates/POCs (admin), gestão de categorias/tags, gestão de usuários e perfis |

---

#### Container 2: API Server (Backend)

| Atributo | Valor |
|---|---|
| **Tecnologia** | NestJS, Node.js 20 LTS, TypeScript |
| **Hospedagem** | Azure App Service (B1) |
| **Responsabilidade** | Lógica de negócio, autenticação, autorização, integrações |

**Módulos do backend:**

```mermaid
graph LR
    subgraph apiModules ["API Server — Módulos NestJS"]
        AuthModule["<b>Auth Module</b><br/>Login Azure AD<br/>JWT tokens<br/>Guards RBAC"]
        TemplateModule["<b>Template Module</b><br/>CRUD templates<br/>Busca e filtros<br/>Sync Azure DevOps"]
        POCModule["<b>POC Module</b><br/>CRUD POCs<br/>Upload artefatos<br/>Gestão de status"]
        IssueModule["<b>Issue Module</b><br/>Abertura/triagem<br/>Cálculo severidade<br/>Timer SLA<br/>Workflow status"]
        MetricsModule["<b>Metrics Module</b><br/>Downloads tracking<br/>Horas economizadas<br/>Adoção por squad<br/>SLA compliance"]
        StorageModule["<b>Storage Module</b><br/>Upload Blob<br/>Geração SAS tokens<br/>Gestão containers"]
        DevOpsModule["<b>DevOps Integration</b><br/>Listar repos<br/>Ler READMEs<br/>Sync metadados"]
    end
```

| Módulo | Endpoints principais | Integrações |
|---|---|---|
| **AuthModule** | `POST /auth/login`, `GET /auth/me`, `POST /auth/refresh` | Azure AD (OIDC) |
| **TemplateModule** | `GET /templates`, `POST /templates`, `GET /templates/:id`, `GET /templates/:id/download` | Azure DevOps API, Blob Storage |
| **POCModule** | `GET /pocs`, `POST /pocs`, `PATCH /pocs/:id`, `GET /pocs/:id/download` | Blob Storage |
| **IssueModule** | `GET /issues`, `POST /issues`, `PATCH /issues/:id/status`, `POST /issues/:id/comments` | PostgreSQL |
| **MetricsModule** | `GET /metrics/downloads`, `GET /metrics/hours-saved`, `GET /metrics/adoption`, `GET /metrics/sla` | PostgreSQL |
| **StorageModule** | (interno) Upload, geração SAS, limpeza | Blob Storage |
| **DevOpsModule** | (interno) Sync repos, leitura README | Azure DevOps API |

---

#### Container 3: Database

| Atributo | Valor |
|---|---|
| **Tecnologia** | PostgreSQL 16 |
| **Hospedagem** | Azure Database for PostgreSQL — Flexible Server (B1ms) |
| **ORM** | Prisma |
| **Responsabilidade** | Persistência de todos os dados do sistema |

**Tabelas principais:**

| Schema/Tabela | Propósito | Relações |
|---|---|---|
| `users` | Perfis sincronizados do Azure AD | Referenciado por todas as tabelas |
| `templates` | Metadados dos templates (título, categoria, tags, repo_url) | `author -> users` |
| `pocs` | Metadados das POCs (problema, solução, status, tecnologias) | `author -> users` |
| `issues` | Solicitações ao CoE (severidade, SLA, status, workflow) | `requester -> users`, `assignee -> users` |
| `issue_comments` | Histórico de comentários nas issues | `issue -> issues`, `author -> users` |
| `downloads` | Registro de cada download (quem, o quê, quando) | `user -> users`, `template/poc` |
| `ratings` | Avaliações dos usuários sobre templates/POCs | `user -> users`, `template/poc` |
| `categories` | Categorias dos templates (Terraform, K8s, CI/CD...) | Referenciado por `templates` |
| `tags` | Tags livres para classificação flexível | Many-to-many com `templates`, `pocs` |
| `audit_log` | Log de ações para auditoria e compliance | `user -> users` |

---

#### Container 4: Cache Layer (futuro MVP2)

| Atributo | Valor |
|---|---|
| **Tecnologia** | Redis |
| **Hospedagem** | Azure Cache for Redis (Basic C0) |
| **Responsabilidade** | Cache de listagens, sessões, rate limiting |
| **Quando** | MVP2 — quando a base de usuários crescer para 50+ |

---

### Fluxos Detalhados (N2)

#### Fluxo 1: Autenticação SSO

```mermaid
sequenceDiagram
    participant User as Usuário
    participant Web as WebApp (Next.js)
    participant API as API Server (NestJS)
    participant AAD as Azure AD (Entra ID)
    participant DB as PostgreSQL

    User->>Web: Acessa o portal
    Web->>AAD: Redirect para login Microsoft
    AAD->>User: Tela de login corporativo (MFA)
    User->>AAD: Credenciais
    AAD->>Web: Authorization code
    Web->>API: POST /auth/login (code)
    API->>AAD: Troca code por tokens (access + id token)
    AAD->>API: Tokens JWT + perfil do usuário
    API->>DB: Upsert user (sync perfil Azure AD)
    API->>Web: JWT do portal + perfil + role
    Web->>User: Portal autenticado
```

#### Fluxo 2: Download de Template

```mermaid
sequenceDiagram
    participant User as Desenvolvedor
    participant Web as WebApp (Next.js)
    participant API as API Server (NestJS)
    participant DB as PostgreSQL
    participant Blob as Azure Blob Storage
    participant DevOps as Azure DevOps API

    User->>Web: Busca "terraform vpc azure"
    Web->>API: GET /templates?search=terraform+vpc+azure
    API->>DB: Query templates com full-text search
    DB->>API: Lista de templates encontrados
    API->>Web: JSON com resultados
    Web->>User: Exibe cards dos templates

    User->>Web: Clica no template
    Web->>API: GET /templates/:id
    API->>DevOps: GET README.md do repositório
    DevOps->>API: Conteúdo do README
    API->>Web: Detalhes + README renderizado
    Web->>User: Página do template com preview

    User->>Web: Clica "Download"
    Web->>API: GET /templates/:id/download
    API->>Blob: Gera SAS token (expira em 5min)
    Blob->>API: URL assinada
    API->>DB: INSERT download (user, template, timestamp)
    API->>DB: UPDATE template download_count +1
    API->>Web: Redirect para URL com SAS token
    Web->>User: Download inicia automaticamente
```

#### Fluxo 3: Abertura de Issue com Cálculo de Severidade

```mermaid
sequenceDiagram
    participant User as Tech Lead
    participant Web as WebApp (Next.js)
    participant API as API Server (NestJS)
    participant DB as PostgreSQL

    User->>Web: Clica "Abrir Solicitação"
    Web->>User: Formulário com 5 dimensões de severidade

    Note over User,Web: Impacto negócio (0-4)<br/>Usuários afetados (0-4)<br/>Ambiente (0-4)<br/>Impacto financeiro (0-4)<br/>Segurança (0-4)<br/>Workaround (0-3)

    User->>Web: Preenche formulário
    Web->>Web: Calcula score em tempo real
    Web->>User: Exibe "Severidade: ALTA (score 12)"

    User->>Web: Confirma envio
    Web->>API: POST /issues (dados + score)
    API->>API: Valida score, define SLA deadline
    API->>DB: INSERT issue (status=ABERTA, sla_deadline)
    API->>Web: Issue criada com ID e SLA
    Web->>User: "Issue #42 criada — SLA: 8h úteis"
```

---

## Decisões Arquiteturais no C4

| ADR | Decisão | Justificativa no contexto C4 |
|---|---|---|
| **Separação Front/Back** | WebApp e API Server como containers separados | Permite escalar independentemente; API pode servir futuros clientes mobile ou integrações |
| **API REST (não BFF)** | API genérica, não acoplada ao frontend | Futuro: outros consumers (CLI, integração com outras ferramentas) |
| **Blob Storage separado** | Artefatos fora do banco e fora do DevOps | Banco leve (só metadados); downloads diretos via SAS sem sobrecarregar a API |
| **Azure DevOps como fonte** | Portal não armazena código, apenas referencia | Evita duplicação, garante que o repo é sempre a fonte da verdade |
| **PostgreSQL único** | Um banco para todo o MVP | Simplicidade operacional; particionamento lógico por schema se necessário no futuro |

---

*Documento preparado para discussão com a equipe. Próximo passo: validar decisões, ajustar baseado no feedback, e evoluir para implementação.*
