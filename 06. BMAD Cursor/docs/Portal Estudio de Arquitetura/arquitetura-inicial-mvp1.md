# Portal de Arquitetura e DevOps — Arquitetura Inicial MVP1

**Data:** 22/05/2026
**Autor:** Studio de Arquitetura e DevOps — Foursys
**Status:** Proposta para discussão com a equipe
**Versão:** 0.1 (Draft)

---

## 1. O Problema

Hoje os assets técnicos do Studio (templates Terraform, POCs de Kubernetes, pipelines CI/CD, arquiteturas de referência) estão **dispersos** — em máquinas pessoais, repositórios isolados no Azure DevOps, ou na cabeça das pessoas. Isso causa:

- **Retrabalho:** squads recriando do zero o que já foi feito
- **Perda de conhecimento:** quando alguém sai, o conhecimento vai junto
- **Sem visibilidade de impacto:** não sabemos quantas horas economizamos, quem usa o quê, nem quais padrões estão sendo adotados
- **Sem canal estruturado:** as torres não sabem o que podem pedir ao CoE

## 2. A Solução

Um **portal web centralizado** onde o time do Studio publica e as squads consomem: templates prontos, POCs documentadas, solicitações de apoio técnico e métricas de impacto.

---

## 3. Decisões de Arquitetura e Justificativas

### 3.1 Frontend — Next.js (React + TypeScript)

| Aspecto | Decisão |
|---|---|
| **Framework** | Next.js 14+ |
| **Linguagem** | TypeScript |

**Por que Next.js?**

- **SSR (Server-Side Rendering):** páginas carregam rápido e são indexáveis — importante se no futuro o portal virar produto comercial com landing page pública
- **React:** maior ecossistema de componentes, mais fácil encontrar devs no mercado
- **TypeScript full-stack:** usando TypeScript no front e no back, a equipe de 2-3 devs não precisa alternar entre linguagens diferentes
- **App Router:** estrutura de rotas moderna com layouts aninhados, ideal para um portal com múltiplas seções

**Alternativas consideradas:**

| Alternativa | Por que não? |
|---|---|
| Angular | Curva de aprendizado mais alta, ecossistema menor para prototipação rápida |
| Vue/Nuxt | Viável, mas ecossistema de componentes enterprise menor que React |
| Blazor (.NET) | Limitaria o pool de devs e a interoperabilidade com o backend Node |

---

### 3.2 Backend — NestJS (Node.js + TypeScript)

| Aspecto | Decisão |
|---|---|
| **Framework** | NestJS |
| **Runtime** | Node.js 20 LTS |
| **API** | REST (GraphQL como evolução futura) |

**Por que NestJS?**

- **Estrutura enterprise-grade:** injeção de dependência, módulos, guards, interceptors — não é um "Express solto", tem padrão arquitetural desde o início
- **TypeScript nativo:** mesma linguagem do frontend, contratos de tipo compartilhados
- **Integração Azure:** SDKs do Azure (Blob Storage, Azure AD, DevOps API) todos disponíveis nativamente em Node.js
- **Produtividade:** para 2-3 devs em 3-6 meses, a velocidade de desenvolvimento é crítica

**Alternativas consideradas:**

| Alternativa | Por que não? |
|---|---|
| Spring Boot (Java) | Robusto, mas overhead maior para equipe pequena, dois ecossistemas de linguagem |
| .NET Minimal API | Boa opção se a equipe fosse .NET, mas perdemos o TypeScript unificado |
| FastAPI (Python) | Excelente para APIs, mas menos maduro para aplicações enterprise complexas |

---

### 3.3 Banco de Dados — PostgreSQL

| Aspecto | Decisão |
|---|---|
| **SGBD** | PostgreSQL 16 |
| **Hosting** | Azure Database for PostgreSQL — Flexible Server |
| **ORM** | Prisma (TypeScript) |

**Por que PostgreSQL?**

- **Gratuito e open-source:** sem custo de licença, reduz risco se precisar migrar de cloud
- **JSON nativo:** campos como `tags[]` e `technologies[]` podem usar `jsonb` sem precisar de tabelas auxiliares no MVP
- **Maturidade:** o banco mais confiável do ecossistema open-source, com suporte nativo no Azure
- **Prisma ORM:** type-safe, migrations automáticas, excelente DX para equipe pequena

**Por que não MongoDB?** Para um portal com entidades bem definidas (templates, POCs, issues, métricas), o modelo relacional é mais adequado. Sem necessidade de flexibilidade de schema no MVP.

---

### 3.4 Autenticação — Azure AD / Entra ID

| Aspecto | Decisão |
|---|---|
| **Provider** | Microsoft Entra ID (Azure AD) |
| **Protocolo** | OAuth 2.0 / OpenID Connect |
| **Biblioteca** | NextAuth.js com provider Azure AD |

**Por que Azure AD?**

- **Já existe na Foursys:** todos os colaboradores já têm conta Microsoft corporativa
- **SSO transparente:** login com um clique, sem criar senha nova
- **Segurança enterprise:** MFA, conditional access, auditoria — tudo gerenciado pelo Azure
- **Multi-tenant ready:** quando o portal virar produto, cada cliente pode usar seu próprio Azure AD (ou outro IdP via OIDC)

---

### 3.5 Armazenamento de Artefatos — Azure Blob Storage

| Aspecto | Decisão |
|---|---|
| **Serviço** | Azure Blob Storage |
| **Uso** | ZIPs de templates, código de POCs, documentação, diagramas |

**Por que Blob Storage?**

- **Custo baixíssimo:** ~R$ 0,10/GB/mês para armazenamento, ideal para artefatos que são baixados esporadicamente
- **SAS Tokens:** links temporários de download com expiração — segurança sem complexidade
- **Integração nativa:** SDK `@azure/storage-blob` no Node.js

**Alternativa:** Servir tudo direto do Azure DevOps Repos via API. Viável, mas limita a tipos de artefato que não são código (diagramas, docs, binários).

---

### 3.6 Integração — Azure DevOps API

| Aspecto | Decisão |
|---|---|
| **API** | Azure DevOps REST API v7 |
| **Uso** | Listar repos, buscar templates, sincronizar código |

**Por que integrar com Azure DevOps?**

- **Fonte da verdade:** os repositórios já estão lá — o portal não duplica código, aponta para ele
- **Sincronização:** o portal pode ler o README.md direto do repo e exibir inline
- **Sem migração:** nenhum esforço de mover repositórios, o portal é uma camada de descoberta

---

### 3.7 Hosting — Azure App Service (MVP) → Container Apps (escala)

| Aspecto | MVP1 | Evolução |
|---|---|---|
| **Frontend** | Azure App Service (Node.js) | Azure Static Web Apps ou Container Apps |
| **Backend** | Azure App Service (Node.js) | Azure Container Apps |
| **Banco** | Azure DB for PostgreSQL Flexible | Mesmo |

**Por que App Service no MVP?**

- **Simplicidade:** deploy via push para branch, sem necessidade de Docker/K8s no dia 1
- **Custo controlado:** plano B1 (~US$ 13/mês) é suficiente para 15 usuários
- **SSL gratuito e custom domain** inclusos
- **Escala futura:** quando precisar, migrar para Container Apps é simples (mesma runtime Node.js, só containeriza)

---

## 4. Visão Geral da Arquitetura

```
┌─────────────────────────────────────────────────────────┐
│                     USUÁRIOS                            │
│   Time Studio │ Tech Leads │ Squads │ (Clientes futuro) │
└───────────────────────┬─────────────────────────────────┘
                        │ HTTPS
                        ▼
┌─────────────────────────────────────────────────────────┐
│               FRONTEND — Next.js (SSR)                  │
│                                                         │
│  ┌──────────┐ ┌──────────┐ ┌────────┐ ┌─────────────┐  │
│  │ Catálogo │ │   POCs   │ │ Issues │ │  Dashboard  │  │
│  │Templates │ │          │ │  /SLA  │ │  Métricas   │  │
│  └──────────┘ └──────────┘ └────────┘ └─────────────┘  │
└───────────────────────┬─────────────────────────────────┘
                        │ REST API
                        ▼
┌─────────────────────────────────────────────────────────┐
│               BACKEND — NestJS                          │
│                                                         │
│  ┌──────┐ ┌──────────┐ ┌───────┐ ┌────────┐ ┌───────┐  │
│  │ Auth │ │Templates │ │ POCs  │ │Issues  │ │Metrics│  │
│  │Module│ │ Service  │ │Service│ │Service │ │Service│  │
│  └──┬───┘ └────┬─────┘ └───┬───┘ └───┬────┘ └───┬───┘  │
│     │          │           │         │           │      │
└─────┼──────────┼───────────┼─────────┼───────────┼──────┘
      │          │           │         │           │
      ▼          ▼           ▼         ▼           ▼
┌──────────┐ ┌──────────┐ ┌──────────────┐ ┌───────────┐
│ Azure AD │ │  Azure   │ │  Azure Blob  │ │PostgreSQL │
│ Entra ID │ │  DevOps  │ │   Storage    │ │  (Azure)  │
│  (SSO)   │ │  API     │ │ (artefatos)  │ │  (dados)  │
└──────────┘ └──────────┘ └──────────────┘ └───────────┘
```

---

## 5. Resumo das Decisões (ADR Rápido)

| # | Decisão | Escolha | Motivo principal |
|---|---|---|---|
| ADR-P01 | Frontend framework | Next.js + TypeScript | SSR para futuro comercial, ecossistema React, TypeScript unificado |
| ADR-P02 | Backend framework | NestJS + TypeScript | Estrutura enterprise, mesma linguagem do front, SDKs Azure nativos |
| ADR-P03 | Banco de dados | PostgreSQL (Azure) | Open-source, relacional, jsonb para flexibilidade, Prisma ORM |
| ADR-P04 | Autenticação | Azure AD / Entra ID | Já existe na Foursys, SSO, multi-tenant ready |
| ADR-P05 | Storage de artefatos | Azure Blob Storage | Custo baixo, SAS tokens, integração nativa |
| ADR-P06 | Fonte de código | Azure DevOps API | Repos já estão lá, sem duplicação, sincronização |
| ADR-P07 | Hosting MVP | Azure App Service | Simples, barato, deploy rápido, escala futura fácil |
| ADR-P08 | ORM | Prisma | Type-safe, migrations, DX excelente para equipe pequena |

---

## 6. Estimativa de Custo Azure (MVP — 15 usuários)

| Recurso | Tier | Custo estimado/mês |
|---|---|---|
| App Service (front) | B1 | ~US$ 13 |
| App Service (back) | B1 | ~US$ 13 |
| PostgreSQL Flexible | Burstable B1ms | ~US$ 12 |
| Blob Storage | Hot, ~10 GB | ~US$ 1 |
| Azure AD | Incluído (P1 se já existente) | US$ 0 |
| **Total estimado** | | **~US$ 39/mês** |

---

## 7. Pontos para Discussão com a Equipe

1. **Stack:** a equipe tem experiência com TypeScript/React/Node? Ou prefere outra stack?
2. **Azure vs. outra cloud:** existe budget ou conta Azure já provisionada para o Studio?
3. **Azure DevOps como fonte:** os templates e POCs existentes já estão em repos organizados, ou será preciso um esforço de catalogação antes?
4. **Escopo do MVP:** começamos com catálogo de templates + issues, ou todas as 4 features em paralelo?
5. **Design/UX:** temos designer disponível ou usamos um design system pronto (ex: Shadcn/UI)?
6. **IA Analysis:** entra no MVP1 ou fica para MVP2? Qual o caso de uso prioritário?
7. **Multi-tenancy:** já pensamos na arquitetura de isolamento por cliente desde o MVP, ou tratamos depois?

---

*Este documento é um ponto de partida para alinhar a equipe. Após a discussão, evoluímos para um PRD detalhado e iniciamos o desenvolvimento.*
