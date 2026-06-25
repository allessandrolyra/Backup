# Portal de Arquitetura e DevOps — Diagramas C4 Model + Arquitetura Alto Nível

**Projeto:** Portal de Arquitetura e DevOps — MVP1
**Data:** 26/05/2026
**Autor:** Winston (Agente Arquiteto) — Studio Foursys
**Versão:** 1.0

---

## 1. C4 Model — Nível 1: Diagrama de Contexto

> Mostra quem interage com o sistema e com quais sistemas externos ele se comunica.
> Responde: *"Qual é o panorama geral?"*

```mermaid
graph TB
    subgraph personas ["Personas"]
        direction LR
        P1["👤 Administrador do Studio<br/><i>Arquitetos, Eng. DevOps</i><br/>───────────────<br/>Publica templates e POCs<br/>Responde issues<br/>Gerencia catálogo"]
        P2["👤 Tech Lead / Arq. Torre<br/><i>Líderes técnicos das torres</i><br/>───────────────<br/>Busca templates<br/>Contribui com POCs<br/>Abre solicitações ao CoE"]
        P3["👤 Desenvolvedor de Squad<br/><i>Devs das squads de delivery</i><br/>───────────────<br/>Consome templates<br/>Baixa POCs<br/>Avalia artefatos"]
        P4["👤 Gestor / Head Studio<br/><i>Head do Studio, Diretoria</i><br/>───────────────<br/>Acompanha métricas<br/>Monitora SLA<br/>Avalia impacto do CoE"]
        P5["👤 Cliente Externo<br/><i>Futuro — MVP2+</i><br/>───────────────<br/>Acessa catálogo público<br/>Consome soluções<br/>comercializadas"]
    end

    PORTAL["🏢 PORTAL DE ARQUITETURA E DEVOPS<br/><i>Sistema Web — MVP1</i><br/>═══════════════════════════<br/>Hub centralizado para descoberta,<br/>consumo e contribuição de assets<br/>técnicos, gestão de issues ao CoE<br/>e métricas de impacto"]

    subgraph externals ["Sistemas Externos"]
        direction LR
        E1["🔐 Microsoft Entra ID<br/><i>Azure AD</i><br/>───────────────<br/>Autenticação SSO<br/>OAuth 2.0 / OIDC<br/>MFA corporativo"]
        E2["📦 Azure DevOps<br/><i>Repos + Pipelines</i><br/>───────────────<br/>Repositórios de código<br/>Templates fonte<br/>CI/CD Pipelines"]
        E3["💾 Azure Blob Storage<br/><i>Object Storage</i><br/>───────────────<br/>Artefatos para download<br/>ZIPs, docs, diagramas<br/>SAS Tokens temporários"]
        E4["📧 Sistema de Notificação<br/><i>SMTP / SendGrid</i><br/>───────────────<br/>Alertas de SLA<br/>Notificações de issues<br/>Updates de templates"]
    end

    P1 -->|"Publica, gerencia,<br/>responde issues"| PORTAL
    P2 -->|"Busca, contribui,<br/>abre issues"| PORTAL
    P3 -->|"Busca, baixa,<br/>avalia"| PORTAL
    P4 -->|"Visualiza dashboards<br/>e métricas"| PORTAL
    P5 -.->|"Acessa catálogo<br/>(futuro MVP2+)"| PORTAL

    PORTAL -->|"Autentica usuários<br/>OAuth 2.0 / OIDC"| E1
    PORTAL -->|"Consulta repos,<br/>lê READMEs, sync"| E2
    PORTAL -->|"Upload/download<br/>artefatos via SAS"| E3
    PORTAL -.->|"Envia notificações<br/>(futuro)"| E4
```

### Legenda N1

| Cor/Estilo | Significado |
|---|---|
| Linha sólida (→) | Interação ativa no MVP1 |
| Linha tracejada (- - →) | Planejado para versões futuras |
| Personas (topo) | Quem usa o sistema |
| Sistema central | O que estamos construindo |
| Sistemas externos (base) | Com o que nos integramos |

---

## 2. C4 Model — Nível 2: Diagrama de Container

> Abre o sistema e mostra as peças técnicas internas: aplicações, bancos, serviços.
> Responde: *"Quais são os blocos de construção e como se conectam?"*

```mermaid
graph TB
    subgraph users ["Usuários"]
        direction LR
        U1["👤 Admin Studio"]
        U2["👤 Tech Lead"]
        U3["👤 Desenvolvedor"]
        U4["👤 Gestor"]
    end

    subgraph systemBoundary ["Portal de Arquitetura e DevOps — System Boundary"]

        WEBAPP["🌐 Web Application<br/>───────────────<br/><b>Next.js 14 + TypeScript</b><br/>───────────────<br/>Interface do portal:<br/>• Catálogo de Templates<br/>• Repositório de POCs<br/>• Painel de Issues/SLA<br/>• Dashboard de Métricas<br/>• Área de Administração<br/>───────────────<br/><i>Azure App Service (B1)</i>"]

        APISERVER["⚙️ API Server<br/>───────────────<br/><b>NestJS + TypeScript</b><br/>───────────────<br/>Lógica de negócio:<br/>• Auth Module (JWT/RBAC)<br/>• Template Service<br/>• POC Service<br/>• Issue Service (SLA)<br/>• Metrics Service<br/>• Storage Module<br/>• DevOps Integration<br/>───────────────<br/><i>Azure App Service (B1)</i>"]

        DATABASE[("🗄️ Database<br/>───────────────<br/><b>PostgreSQL 16</b><br/>───────────────<br/>Persistência:<br/>• users, templates<br/>• pocs, issues<br/>• downloads, ratings<br/>• audit_log<br/>───────────────<br/><i>Azure DB Flexible (B1ms)</i>")]

        CACHE["⚡ Cache Layer<br/>───────────────<br/><b>Redis</b><br/>───────────────<br/>Futuro MVP2:<br/>• Cache de catálogo<br/>• Sessões<br/>• Rate limiting<br/>───────────────<br/><i>Azure Cache for Redis</i>"]
    end

    subgraph externals ["Sistemas Externos"]
        direction LR
        EXT1["🔐 Microsoft Entra ID<br/><i>OAuth 2.0 / OIDC</i>"]
        EXT2["📦 Azure DevOps API<br/><i>REST API v7 + PAT</i>"]
        EXT3["💾 Azure Blob Storage<br/><i>SDK + SAS Tokens</i>"]
    end

    U1 & U2 & U3 & U4 -->|"HTTPS<br/>Browser"| WEBAPP

    WEBAPP -->|"REST API<br/>JSON / HTTPS"| APISERVER

    APISERVER -->|"Prisma ORM<br/>TCP :5432"| DATABASE
    APISERVER -.->|"get/set<br/>TCP :6379<br/>(futuro)"| CACHE
    APISERVER -->|"OAuth 2.0 / OIDC<br/>HTTPS"| EXT1
    APISERVER -->|"REST API<br/>PAT Token / HTTPS"| EXT2
    APISERVER -->|"@azure/storage-blob<br/>HTTPS + SAS"| EXT3
```

### Detalhamento dos Containers

| Container | Tecnologia | Hospedagem | Responsabilidade |
|---|---|---|---|
| **Web Application** | Next.js 14, React 18, TypeScript | Azure App Service B1 | SSR, UI, formulários, navegação |
| **API Server** | NestJS, Node.js 20 LTS, TypeScript | Azure App Service B1 | Regras de negócio, auth, integrações |
| **Database** | PostgreSQL 16, Prisma ORM | Azure DB Flexible B1ms | Persistência de dados, full-text search |
| **Cache** (futuro) | Redis | Azure Cache for Redis | Cache, sessões, rate limit |

### Comunicação entre Containers

| De | Para | Protocolo | Autenticação |
|---|---|---|---|
| Browser | Web App | HTTPS (443) | Cookie/Session |
| Web App | API Server | REST/JSON (HTTPS) | JWT Bearer Token |
| API Server | PostgreSQL | TCP (5432) | Connection string + SSL |
| API Server | Azure AD | HTTPS (OAuth 2.0) | Client ID + Secret |
| API Server | Azure DevOps | HTTPS (REST) | PAT (Personal Access Token) |
| API Server | Blob Storage | HTTPS (SDK) | Storage Account Key + SAS |

---

## 3. Arquitetura de Alto Nível — MVP1

> Visão em camadas da solução completa, mostrando tecnologias, protocolos e o fluxo vertical.
> Responde: *"Como tudo se encaixa de ponta a ponta?"*

```mermaid
graph TB
    subgraph camada1 ["CAMADA DE APRESENTAÇÃO"]
        direction LR
        Browser["🖥️ Browser<br/><i>Chrome, Edge, Firefox</i>"]
        Mobile["📱 Mobile Browser<br/><i>Responsivo (futuro)</i>"]
    end

    subgraph camada2 ["CAMADA DE FRONTEND — Next.js 14 + TypeScript"]
        direction LR
        SSR["SSR Engine<br/><i>Server-Side Rendering</i>"]
        Pages["App Router<br/><i>Pages & Layouts</i>"]
        UILib["UI Components<br/><i>Shadcn/UI + Tailwind</i>"]
        AuthClient["Auth Client<br/><i>NextAuth.js</i>"]
    end

    subgraph camada3 ["CAMADA DE API — NestJS + TypeScript"]
        direction LR

        subgraph authLayer ["Auth & Security"]
            AuthGuard["Auth Guard<br/><i>JWT + RBAC</i>"]
        end

        subgraph businessLayer ["Serviços de Negócio"]
            TemplateSvc["Template<br/>Service"]
            POCSvc["POC<br/>Service"]
            IssueSvc["Issue<br/>Service"]
            MetricsSvc["Metrics<br/>Service"]
        end

        subgraph integrationLayer ["Integrações"]
            StorageSvc["Storage<br/>Module"]
            DevOpsSvc["DevOps<br/>Integration"]
        end
    end

    subgraph camada4 ["CAMADA DE DADOS E INFRAESTRUTURA"]
        direction LR
        PG[("PostgreSQL 16<br/><i>Azure DB Flexible</i><br/>Dados do sistema")]
        BLOB["Azure Blob Storage<br/><i>Artefatos, ZIPs</i><br/>Downloads"]
        AAD["Microsoft Entra ID<br/><i>SSO Corporativo</i><br/>Identidade"]
        DEVOPS["Azure DevOps<br/><i>Repos & Pipelines</i><br/>Código fonte"]
    end

    subgraph camada5 ["CAMADA DE OPERAÇÃO — Azure"]
        direction LR
        AppInsights["Application Insights<br/><i>Monitoramento</i>"]
        CICD["Azure Pipelines<br/><i>CI/CD Deploy</i>"]
        AppService["App Service Plan<br/><i>B1 — 2 instâncias</i>"]
    end

    Browser & Mobile -->|"HTTPS"| camada2
    camada2 -->|"REST API / JSON"| AuthGuard
    AuthGuard --> businessLayer
    AuthGuard --> integrationLayer
    TemplateSvc & POCSvc & IssueSvc & MetricsSvc -->|"Prisma ORM"| PG
    StorageSvc -->|"SDK Azure"| BLOB
    DevOpsSvc -->|"REST API v7"| DEVOPS
    AuthGuard -->|"OAuth 2.0"| AAD
    camada3 -->|"Telemetry"| AppInsights
    CICD -->|"Deploy"| AppService
```

### Resumo de Tecnologias por Camada

| Camada | Tecnologias | Propósito |
|---|---|---|
| **Apresentação** | Browser moderno (Chrome, Edge) | Acesso do usuário |
| **Frontend** | Next.js 14, React 18, TypeScript, Tailwind, Shadcn/UI, NextAuth.js | Interface, SSR, autenticação client-side |
| **API** | NestJS, Node.js 20, TypeScript, Prisma, JWT, RBAC | Lógica de negócio, autorização, integrações |
| **Dados** | PostgreSQL 16, Azure Blob Storage | Persistência relacional + artefatos binários |
| **Identidade** | Microsoft Entra ID (Azure AD), OAuth 2.0, OIDC | SSO corporativo, MFA |
| **Integração** | Azure DevOps REST API v7 | Repositórios fonte, sincronização |
| **Operação** | App Service B1, Application Insights, Azure Pipelines | Hosting, monitoramento, CI/CD |

---

*Estes diagramas estão disponíveis também no formato Draw.io (.drawio) para edição visual no arquivo `diagramas-c4-mvp1.drawio`.*
