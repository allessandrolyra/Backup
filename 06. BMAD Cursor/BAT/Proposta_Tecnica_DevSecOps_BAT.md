# Proposta Técnica: Implementação de DevSecOps no Ambiente Azure DevOps (ADO)

**Cliente:** BAT Latam South (Souza Cruz)
**Assunto:** Solicitação de Proposta (RFP) -- Serviços Especializados de DevSecOps
**Data:** 02 de Junho de 2026
**Versão:** 3.0 (Revisada com base no Questionário Técnico)
**Referência:** PT-BAT-DEVSECOPS-2026-001
**Status:** Versão Final para Submissão

---

## 0. Resumo Executivo

### O Desafio

A BAT Latam South (Souza Cruz) necessita padronizar e automatizar suas práticas de DevSecOps no Azure DevOps, garantindo segurança, governança corporativa e conformidade com o Global COE -- tudo isso em um ambiente com restrições de acesso administrativo e interface obrigatória com times globais em inglês.

### Nossa Solução

Propomos a construção de uma **esteira DevSecOps completa, parametrizável e reutilizável** -- projetada como template para ser replicada em múltiplas aplicações -- que cobre os 15 itens obrigatórios do edital, desde a criação de repositórios até observabilidade avançada em produção. A solução utiliza Azure Container Apps como plataforma de compute, Terraform para infraestrutura como código, e uma cadeia de segurança Shift-Left integrada a cada commit. A camada de integração com APIs externas e genérica e adaptável a qualquer provedor (Serasa, Sefaz, Salesforce, SAP ou outros), conforme esclarecido no questionário técnico da RFP.

### Valor Entregue

- **Redução estimada de 70-80% no tempo de onboarding** de novas aplicações (de semanas para dias via templates reutilizáveis)
- **Template replicável:** esteira construída uma vez, parametrizada para N aplicações futuras sem reconstrução
- **Cobertura de segurança automatizada de 100%** no ciclo CI (SAST, SCA, Secrets Detection, DAST)
- **Zero deploys manuais** em produção -- todo deploy via pipeline automatizado com Approval Gates e rollback automático
- **Observabilidade ponta a ponta** com SLOs definidos e alertas integrados
- **Integração adaptável:** camada de APIs genérica suportando qualquer provedor externo (REST, SOAP, OData)

### Investimento e Prazo

| | Frente A (Setup) | Frente B (Sob Demanda) |
|:--|:--|:--|
| O que é | Esteira template para aplicação de referência, replicável para projetos futuros | Horas de suporte técnico especializado |
| Investimento | R$ 41.800 fixo (detalhes na proposta comercial) | R$ 110-280/hora por senioridade |
| Prazo | 6 fases + Fase 0 de pré-requisitos | Contínuo após implantação |
| Pagamento | Na entrega, com critérios de aceite | 60 dias após execução |

---

## 1. Introdução e Visão Geral do Projeto

A presente proposta técnica tem como objetivo apresentar a abordagem da nossa equipe para a estruturação, padronização, evolução e sustentação de práticas de **DevSecOps** na nuvem **Microsoft Azure**, utilizando como plataforma central o **Azure DevOps (ADO)**, para atender as iniciativas de **IDT** da **BAT Latam South (Souza Cruz)**.

Compreendemos que o desafio central vai além da simples automação de pipelines: trata-se de garantir a **estabilidade, disponibilidade, segurança da informação e governança corporativa** em um ambiente altamente regulado, onde a interface com times globais e a conformidade com as regras estabelecidas pelo **Global COE (Center of Excellence)** da BAT são fatores críticos de sucesso.

### Principais Objetivos do Engajamento

> **Visão de Plataforma:** Conforme esclarecido no questionário técnico (Item 7), não há uma aplicação-alvo fixa -- cada novo projeto solicitará a criação de uma esteira completa. Por isso, a Frente A entrega um **template de esteira parametrizável**, projetado para ser replicado em N aplicações futuras com esforço mínimo de customização.

- **Template Reutilizável como Produto:** A esteira DevSecOps construída na Frente A é projetada como um template parametrizável (YAML + Terraform modules). Para cada nova aplicação, basta ajustar variáveis (nome do projeto, número de ambientes, APIs externas) sem reconstruir a esteira do zero.
- **Segurança Nativa (Shift-Left Security):** Integração automática de SAST, SCA, Secrets Detection e DAST sem impactar a agilidade de entrega.
- **Observabilidade Avançada:** Telemetria baseada em OpenTelemetry com backend Azure Monitor e dashboards Grafana, estabelecendo SLOs concretos.
- **Alinhamento e Governança Global:** Atuação fluida e colaborativa em inglês com os times globais da BAT, respeitando os três níveis de controle e o fluxo de Change Management.
- **Onboarding Acelerado:** Com o template pronto, o tempo estimado para provisionar uma nova aplicação completa cai de semanas para **2-3 dias** (Frente B sob demanda).

### Diferenciais Competitivos

1. **Experiência comprovada com Azure DevOps Enterprise** em ambientes com restrição de acesso administrativo
2. **Fluência em inglês técnico** em toda a equipe (não apenas no líder) para interface direta com o Global COE, conforme exigido no questionário (Item 9)
3. **Modelo híbrido Frente A + B** que reduz risco financeiro para a BAT
4. **Abordagem Reliability First** com SLOs, RTO/RPO e rollback automatizado desde o Day 1

---

## 2. Arquitetura de Referência

A arquitetura proposta para a aplicação de referência da BAT segue o princípio **MVC-R (Mínimo Viável Confiável)**: produzir uma solução segura e operacional sem complexidade desnecessária, com caminho de evolução documentado.

**Diagrama visual:** ver arquivo `Arquitetura_Referencia_BAT.png` em anexo.

### Componentes por Camada

| Camada | Componente | Serviço Azure | Justificativa |
|:-------|:-----------|:--------------|:--------------|
| **1. Acesso e Segurança** | WAF e ingress | Application Gateway WAF v2 | Proteção OWASP Top 10, SSL termination, routing |
| | API Gateway | Azure API Management (APIM) | Rate limiting, throttling, autenticação unificada, logging centralizado |
| **2. Compute** | Plataforma de containers | Azure Container Apps (VNet-injected) | PaaS gerenciado, scale-to-zero, Dapr nativo, traffic splitting para Blue-Green |
| | Microserviço Java A | Container App + Dapr sidecar | Spring Boot, mTLS automático, retries, observabilidade distribuída |
| | Microserviço Java B | Container App + Dapr sidecar | Spring Boot, comunicação inter-serviço via Dapr |
| | Frontend Flutter SPA/PWA | Container App (nginx) | Servindo assets estáticos com cache headers |
| **3. Dados** | Banco relacional | PostgreSQL Flexible Server (Zone-Redundant HA) | Private Endpoint, backup automático, point-in-time restore |
| | Cache | Azure Cache for Redis | Private Endpoint, sessões e cache de consultas frequentes |
| **4. Integração** | Mensageria assíncrona | Azure Service Bus | Filas para operações de escrita com APIs externas, Dead Letter Queue |
| | API externa A (ex: Serasa, SF) | Adaptável (REST/SOAP) | Via APIM, autenticação configurável (OAuth 2.0, API Key, certificado digital), Circuit Breaker |
| | API externa B (ex: Sefaz, SAP) | Adaptável (REST/SOAP/OData) | Via APIM, autenticação configurável (OAuth 2.0, X.509, mTLS), Circuit Breaker, Retry |
| **5. Observabilidade** | Telemetria | Azure Monitor + App Insights | OpenTelemetry SDK nos microserviços, Log Analytics como backend |
| | Dashboards | Grafana (Azure Monitor datasource) | Métodos RED (serviços) e USE (infra), SLOs visuais |
| | Secrets | Azure Key Vault | Managed Identity, rotação automática a cada 90 dias |
| | Registry | Azure Container Registry (ACR) | Private Endpoint, image signing com Cosign |
| **6. DevOps** | Código e CI/CD | Azure DevOps (Repos + Pipelines) | GitFlow, pipelines YAML herdados, Approval Gates |
| | Infraestrutura | Terraform (módulos reutilizáveis) | State remoto em Azure Storage, tfsec/checkov para validação |

### Networking

| Recurso | Configuração |
|:--------|:-------------|
| **VNet** | 4 subnets: Container Apps, PostgreSQL (delegated), Private Endpoints, Application Gateway |
| **Private Endpoints** | PostgreSQL, Redis, ACR, Key Vault, Service Bus -- zero exposição pública |
| **NSGs** | Regras restritivas por subnet, deny-all como default |
| **DNS Private Zones** | Resolução interna para todos os Private Endpoints |
| **Application Gateway** | WAF v2 com regras OWASP 3.2, SSL termination |

### Decisões Arquiteturais (ADRs)

| Decisão | Escolha | Alternativa Descartada | Motivo |
|:--------|:--------|:-----------------------|:-------|
| Plataforma de compute | Container Apps | AKS | Menor complexidade operacional para 2-3 microserviços; migração para AKS viável se escalar para 10+ |
| Estrategia de deploy PRD | Blue-Green (revision-based) | Canary | Mais simples de governar no modelo 3 níveis; binário (old/new) facilita aprovação CAB |
| Stack de observabilidade | OTel SDK + Azure Monitor + Grafana | Prometheus + Loki auto-hospedado | Zero-ops para a BAT; Grafana preserva experiência visual sem operar infra adicional |
| Framework E2E | Playwright | Cypress | Suporte nativo a múltiplos browsers e PWA; melhor para pipelines CI headless |
| Service mesh | Dapr (nativo Container Apps) | Istio / Linkerd | Integrado, sem instalação adicional; mTLS, retries e observabilidade out-of-box |
| Mensageria | Azure Service Bus | Event Grid / Kafka | Adequado para volume moderado; managed, sem cluster; Dead Letter Queue nativa |

---

## 3. Arquitetura de Governança e Integração no Azure DevOps (ADO)

Um dos pontos mais críticos do escopo da BAT é a **restrição de acessos administrativos (Admin)** nos portais do Azure DevOps. Como fornecedor parceiro, nossa atuação respeitará rigorosamente a estrutura de três níveis definida pela BAT:

### Modelo de 3 Níveis

| Nível | Responsável | Escopo | Impacto |
|:------|:------------|:-------|:--------|
| **Nível 1: Plataforma** | COE Global BAT | Políticas globais, templates herdados, organização ADO | Alterações requerem aprovação global |
| **Nível 2: Organização** | BATDIGITAL | Change Management via CAB, Service Connections, Variable Groups | Alterações via RFC formal |
| **Nível 3: Projeto** | Aplicação Local (PO + Fornecedor) | Repositórios, pipelines, builds, testes | Autonomia local dentro das políticas herdadas |

**Atuação do fornecedor:** Nível 3 com autonomia local, e RFCs estruturadas para Níveis 2 e 1.

### Estrategia de Operação sem Acesso Admin

1. **Design e Engenharia:** Desenhamos localmente os arquivos de infraestrutura como código (IaC - Terraform) e os arquivos de configuração de pipelines (YAML).
2. **Validação:** Validamos os artefatos nos limites do Nível 3 (Projeto).
3. **Change Management (RFC):** Para alterações que exijam provisionamento no Nível 2 ou Nível 1, estruturaremos RFCs detalhadas com categorização formal:
   - **Standard Changes:** Pré-aprovadas pelo COE (ex: criação de branch policies em repos existentes)
   - **Normal Changes:** Submetidas ao CAB com antecedência mínima de 1 sprint (ex: nova Service Connection, Variable Group)
   - **Emergency Changes:** Procedimento acelerado para incidentes críticos em PRD
4. **Interface Técnica Fluente:** Nosso Líder Técnico / Arquiteto DevOps conduzirá as interações com o time global em reuniões internacionais em inglês, acelerando a aprovação das RFCs.

**SLA esperado para RFCs:** Consideramos 2-3 semanas para aprovação de Normal Changes pelo COE. Nosso cronograma inclui buffer de contingência para mitigar atrasos.

---

## 4. Escopo Técnico Detalhado: Implementação da Esteira DevSecOps

Para fins de estimativa de esforço e custo (Frente A), consideramos a aplicação de referência descrita no item 1.1 do edital. Conforme esclarecido no questionário técnico (Item 8), o edital descreve um exemplo representativo do porte médio de uma aplicação, e as APIs externas não são necessariamente fixas -- a esteira é projetada para suportar qualquer provedor.

- **2 Microserviços Backend:** Java (Spring Boot), autocontidos em containers
- **1 Frontend SPA/PWA:** Flutter (conforme definido pela BAT para compartilhar codebase com mobile futuro)
- **1 Banco de Dados Relacional:** PostgreSQL (Azure Database for PostgreSQL Flexible Server)
- **1 Cache NoSQL:** Redis (Azure Cache for Redis)
- **2 APIs Externas:** Camada genérica adaptável -- exemplos do edital: Serasa e Sefaz; conforme Q&A: pode ser Salesforce, SAP ou outros. A esteira suporta REST, SOAP, OData com autenticação configurável (OAuth 2.0, API Key, certificado digital ICP-Brasil, mTLS)

### Plataforma de Compute: Azure Container Apps

Recomendamos **Azure Container Apps** como plataforma principal de compute para esta aplicação, pelos seguintes motivos:

| Critério | Container Apps | AKS |
|:---------|:---------------|:----|
| Complexidade operacional | Baixa (PaaS gerenciado) | Alta (upgrades, node pools, RBAC K8s) |
| Custo para 2-3 microserviços | Proporcional ao uso (scale-to-zero) | Over-provisioned (mínimo 3 nodes) |
| Canary/Blue-Green | Nativo (revision-based traffic splitting) | Requer Flagger/Argo Rollouts |
| VNet integration | Suportado | Total |
| Dapr (service mesh) | Integrado nativamente | Requer instalação manual |

**Nota:** Caso a BAT já possua cluster AKS provisionado ou o COE Global exija AKS, adaptaremos a solução sem impacto funcional. A migração de Container Apps para AKS é direta se a aplicação crescer para 10+ microserviços.

### Tabela de Solução de Engenharia

#### Fase 1: Setup, Repositórios e Versionamento (Itens 1-3)

| Item | Requisito do Edital | Abordagem Técnica |
|:-----|:--------------------|:------------------|
| **1** | Criação e configuração de repositórios no ADO | Estruturação de repositórios Git no Azure Repos seguindo nomenclatura corporativa BAT (ex: `bat-latamsouth-<app>-<tier>`). Configuração de Branch Protection Rules (PRs obrigatórios, revisão de código, aprovação por pares). |
| **2** | GitFlow Workflow como Software Versioning | Modelo GitFlow com branches `main`, `develop`, `feature/*`, `release/*`, `hotfix/*`. Automação de merges e pull requests via triggers de pipeline. |
| **3** | Criar usuários para provedores terceiros | Levantamento e mapeamento de perfis de acesso. RFCs de segurança para Azure AD/Entra ID com privilégio mínimo. Processo de offboarding e revisão periódica documentado. |

#### Fase 2: Integração Contínua e Qualidade (Itens 4-5)

| Item | Requisito do Edital | Abordagem Técnica |
|:-----|:--------------------|:------------------|
| **4** | Pipeline para execução dos Unit Tests | CI disparada por Pull Requests. Java: Maven/Gradle com JUnit 5. Flutter: flutter test. **Quality Gate: merge bloqueado se cobertura < 80% ou testes falharem.** |
| **5** | Sonar e Lint para Code Quality | Integração com instância SonarQube/SonarCloud corporativa da BAT. Conforme questionário técnico (Item 5), os Quality Gates serão os **definidos pelo time da BAT** (trabalho em andamento). A esteira será configurada para aplicar os Quality Gates corporativos assim que entregues. Caso necessário, sugerimos como complemento: duplicação < 3%, debt ratio < 5%, zero Critical/Blocker issues. |

#### Fase 3: Empacotamento, Artefatos e E2E (Itens 6-7)

| Item | Requisito do Edital | Abordagem Técnica |
|:-----|:--------------------|:------------------|
| **6** | Pipeline para empacotar aplicações | Backend (Java): Dockerfiles multi-stage otimizados, publicação no ACR. Frontend (Flutter): Builds para SPA/PWA web e APK/AAB. **Artifact promotion:** mesmo artefato Docker promovido entre ambientes (build once, deploy everywhere). |
| **7** | Pipeline para execução dos E2E Tests | Framework: **Playwright** (suporte nativo a múltiplos browsers e PWA). Ambiente efêmero via Container Apps revision dedicada. Mocks de APIs externas via **WireMock** com contratos OpenAPI. Cenários de erro incluídos (timeout, 500, rate limit). |

#### Fase 4: Continuous Delivery Multi-Ambiente (Itens 8-10)

> **Nota sobre ambientes:** Conforme questionário técnico (Item 3), a BAT esclareceu que para alguns projetos haverá apenas UAT e PRD (sem REG). A esteira e parametrizável para suportar **2 ambientes (UAT + PRD)** ou **3 ambientes (UAT + REG + PRD)**, conforme definido no início de cada projeto.

| Item | Requisito do Edital | Abordagem Técnica |
|:-----|:--------------------|:------------------|
| **8** | Deploy em ambiente UAT | Deploy automatizado em Container Apps após merge em `develop`. Notificação automática para o PO realizar homologação. |
| **9** | Deploy em ambiente REG (quando aplicável) | Deploy automatizado no ambiente de Regressão após branch `release/*`. Testes de regressão executados automaticamente. Em projetos com apenas UAT+PRD, os testes de regressão são executados em UAT antes da promoção para PRD. |
| **10** | Deploy em ambiente PRD | Deploy via tags de versão (`v*`). **Estrategia: Blue-Green** com revision-based traffic splitting. Approval Gates (PO local + equipe de segurança). **Rollback automatizado em < 5 minutos** acionado por health check failure ou manualmente via Approval Gate reverso. Database migrations via Flyway com rollback script obrigatório. Smoke tests automáticos pós-deploy. |

#### Fase 5: Observabilidade e IaC (Itens 11-15)

| Item | Requisito do Edital | Abordagem Técnica |
|:-----|:--------------------|:------------------|
| **11** | Monitoramento Uptime e Health Checks | Probes nativos Container Apps/Kubernetes: Liveness, Readiness e Startup Probes para os microserviços Java. |
| **12** | Monitoramento Links/Endpoints Uptime | Azure Monitor Availability Tests (Standard Tests) com frequência de 5 minutos, 3 localizações geográficas. Alertas para latência > 2s ou status != 200. |
| **13** | Observabilidade com Logs, Metrics e Traces | **Stack híbrida:** OpenTelemetry SDK nos microserviços Java (vendor-neutral) exportando para Azure Monitor (App Insights + Log Analytics). Correlação ponta a ponta de traces entre frontend Flutter e backend Java. |
| **14** | Provisionamento de Infraestrutura IaC | Terraform modular: Resource Group, Container Apps Environment, PostgreSQL Flexible Server, Redis Cache, ACR, Key Vault, **VNet com 4 subnets, Private Endpoints para PG/Redis/ACR, NSGs, DNS Private Zones, Application Gateway WAF v2.** |
| **15** | Monitoramento dos componentes | Dashboards **Grafana com Azure Monitor datasource**: métodos RED (Rate, Errors, Duration) para microserviços e USE (Utilization, Saturation, Errors) para PostgreSQL e Redis. **SLOs iniciais:** availability 99.9%, p99 latency < 500ms, error rate < 0.1%. Alertas via Teams. |

#### Fase 6: Handover, Runbooks e Onboarding

- Documentação técnica completa em inglês
- 3 sessões de treinamento hands-on com o time BAT
- Runbook por pipeline (CI, CD, rollback, DR)
- Troubleshooting guide com cenários comuns
- Video walkthrough gravado das esteiras
- **Guia de replicação do template:** documentação passo a passo para provisionar novas aplicações a partir do template (parâmetros configurar, RFCs necessárias, checklist de onboarding)

### Quality Gate Matrix

| Verificação | Bloqueia Merge? | Bloqueia UAT? | Bloqueia REG? | Bloqueia PRD? |
|:------------|:---:|:---:|:---:|:---:|
| Unit tests falhando | Sim | Sim | Sim | Sim |
| Coverage < 80% | Sim | Não | Não | Não |
| Sonar Quality Gate fail | Sim | Não | Não | Não |
| SAST Critical/High | Sim | Sim | Sim | Sim |
| SCA CVE CVSS >= 7.0 | Sim | Sim | Sim | Sim |
| Secrets detectados | Sim | Sim | Sim | Sim |
| Integration tests falhando | N/A | Sim | Sim | Sim |
| E2E tests falhando | N/A | Não | Sim | Sim |
| DAST Critical | N/A | Não | Sim | Sim |
| Aprovação humana (PO) | Não | Não | Não | Sim |
| Smoke test pós-deploy | N/A | Sim | Sim | Sim |

---

## 5. Arquitetura de Integração

> **Nota sobre APIs Externas:** Conforme resposta ao questionário técnico (Item 8), a BAT esclareceu que as APIs mencionadas no edital (Serasa e Sefaz) são exemplos representativos. As APIs reais podem ser Salesforce, SAP, ou quaisquer outros provedores. Por isso, projetamos uma **camada de integração genérica e adaptável**.

### APIs Externas -- Camada Adaptável

| Aspecto | Configuração | Exemplos Suportados |
|:--------|:-------------|:--------------------|
| **Protocolos** | REST, SOAP, OData V4 | Serasa (REST), Sefaz (SOAP/REST), Salesforce (REST), SAP (OData) |
| **Autenticação** | Configurável por API via Key Vault | OAuth 2.0 (JWT Bearer, Client Credentials), API Key, certificado digital (ICP-Brasil A1/A3), X.509/mTLS |
| **Resiliência** | Padrão aplicado a todas as APIs | Circuit Breaker (Resilience4j), Retry com exponential backoff + jitter, Timeout configurável (10-15s), Bulkhead |
| **Compliance** | Conforme regulamentação da API | LGPD (Serasa/consulta de crédito), legislação fiscal (Sefaz/NF-e), políticas corporativas (SF/SAP) |

**API Gateway:** Azure API Management (APIM) como camada centralizada para rate limiting, throttling, logging e autenticação unificada. Cada API externa é registrada como backend no APIM com políticas de resiliência independentes.

**Mensageria assíncrona:** Azure Service Bus para operações de escrita/comandos com APIs externas. Padrão: API síncrona para leitura, fila para escrita. Dead Letter Queue para mensagens falhadas após 3 retries.

**Flexibilidade:** Na Fase 0 (Discovery), mapearemos com a BAT quais APIs reais serão integradas na aplicação de referência, definindo protocolo, autenticação e volumes específicos. A esteira suporta adição de novas APIs sem refatoração estrutural.

### Comunicação entre Microserviços

Os 2 microserviços Java comunicam-se via REST síncrono com contratos OpenAPI/Swagger gerados automaticamente no build CI. Dapr sidecar (nativo Container Apps) fornece mTLS, retries e observabilidade distribuída. Backward compatibility obrigatória -- deploy independente sem quebra de contrato.

### Contratos de API

Todos os microserviços Java geram spec OpenAPI/Swagger automaticamente como artefato do build CI e publicam no Azure Artifacts. Mocks WireMock são gerados a partir dos contratos para ambientes inferiores.

---

## 6. Compliance e Segurança da Informacao (Shift-Left)

A segurança é integrada organicamente a cada commit atraves da seguinte cadeia:

### Pipeline de Segurança

| Etapa | Ferramenta | Momento | Gate |
|:------|:-----------|:--------|:-----|
| 1. Linter e Unit Tests | ESLint/Checkstyle + JUnit/Flutter test | PR | Bloqueia merge |
| 2. SAST (Análise Estática) | SonarQube corporativo BAT | PR | Bloqueia merge (Critical/High) |
| 3. SCA (Vulnerabilidades em Libs) | OWASP Dependency Check (Java) + Trivy (containers) | PR | Bloqueia merge (CVSS >= 7.0) |
| 4. Secrets Detection | Gitleaks | PR | Bloqueia merge (qualquer finding) |
| 5. Build e Image Signing | Docker multi-stage + Cosign (Sigstore) | Merge | Artefato assinado |
| 6. DAST (Teste Dinâmico) | OWASP ZAP | UAT/REG | Bloqueia deploy PRD (Critical) |
| 7. Deploy Seguro PRD | Blue-Green + Approval Gates | Tag v* | Aprovação PO + Security |

### Práticas de Segurança

- **Gerenciamento de Secrets:** Azure Key Vault com Managed Identity (zero credentials em código). Rotacao automática de secrets a cada 90 dias.
- **Escaneamento de Containers:** Trivy/Grype para vulnerabilidades + OPA/Gatekeeper para policy enforcement em runtime (se AKS).
- **Compliance de Auditoria (SOC 2 / ISO 27001):** Rastreabilidade absoluta ponta a ponta. Cada alteração em PRD associada ao PR aprovado. Trilhas de auditoria imutáveis com retenção de 12 meses no Log Analytics.
- **Networking:** Private Endpoints para PostgreSQL, Redis e ACR. NSGs restritivos. Application Gateway WAF v2 com regras OWASP Top 10.

---

## 7. Metas de Confiabilidade

### SLOs (Service Level Objectives)

| Métrica | Target | Método de Medição |
|:--------|:-------|:------------------|
| Availability | 99.9% (8.7h downtime/ano) | Azure Monitor Availability Tests |
| Latência p99 | < 500ms | App Insights (OpenTelemetry) |
| Error rate | < 0.1% | App Insights custom metrics |
| Deploy lead time | < 30 minutos (commit to PRD) | ADO Pipeline analytics |
| Rollback time | < 5 minutos | Automação Blue-Green |

### SLA Composto da Arquitetura

```
Container Apps (99.95%) x PostgreSQL Flex HA (99.99%) x Redis (99.9%) x Front Door (99.99%)
= 99.83% (~1.5h downtime permitido/mes)
```

Com Circuit Breaker isolando APIs externas (independente do provedor), o SLA do caminho crítico interno fica desacoplado das dependências terceiras.

### RTO/RPO

| Cenário | RTO | RPO |
|:--------|:----|:----|
| Falha de container/pod | < 30 segundos | 0 (stateless) |
| Falha de zona | < 15 minutos | 0 (zone-redundant) |
| Corrupção de dados | < 2 horas | < 15 minutos (point-in-time restore PG) |
| Rollback de deploy | < 5 minutos | 0 (Blue-Green) |

---

## 8. Equipe Técnica e Modelo de Atuação Internacional

> **Nota sobre inglês:** Conforme questionário técnico (Item 9), a BAT esclareceu que **todo profissional que trabalhar na criação do ambiente precisa ter capacidade de comunicação em inglês** para interagir com o time global. Caso o Líder Técnico não domine todos os componentes, será necessário mais de um profissional com fluência.

### Perfis da Equipe

| Perfil | Papel no Projeto | Inglês | Diferencial |
|:-------|:-----------------|:-------|:------------|
| **Líder Técnico / Arquiteto DevOps** | Arquitetura, RFCs, interface primaria com COE | Fluente (C1+) | Experiência com ADO Enterprise, conduz reuniões globais |
| **Engenheiro DevSecOps Senior** | IaC Terraform, observabilidade, segurança | Fluente (B2+) | Certificações Azure, capaz de discutir issues técnicos diretamente com COE |
| **Engenheiro DevSecOps Pleno** | Pipelines YAML, Dockerfiles, automação | Intermediário (B1+) | CI/CD multi-ambiente, documenta em inglês |

### Atuação Internacional

- **Inglês Técnico em toda a equipe:** O Líder Técnico conduz discussoes de arquitetura e negocia prazos com o COE. O Engenheiro Senior atua como segundo ponto de contato para temas de IaC e segurança, garantindo que não hajá dependência de uma única pessoa. Todos os profissionais documentam Playbooks/Runbooks em inglês e participam de reuniões globais quando necessário.
- **Cultura SRE:** Automação sistematica, redução de trabalho repetitivo, e Análise de Incidentes sem atribuição de culpa individual (Blameless Post-Mortems).

---

## 9. Matriz de Riscos

| ID | Risco | Probabilidade | Impacto | Mitigação |
|:---|:------|:---:|:---:|:----------|
| R1 | Atraso na aprovação de RFCs pelo COE Global | Alta | Alto | Buffer de 2 semanas por fase; RFCs antecipadas na Fase 0 |
| R2 | Incompatibilidade de versoes das ferramentas BAT (Sonar, ADO) | Média | Médio | Discovery técnico na Fase 1; contingência de 16h |
| R3 | Mudança de escopo pela BAT durante execução | Média | Alto | Change Request formal com re-estimativa e aprovação |
| R4 | Indisponibilidade de sandbox das APIs externas | Média | Alto | Mocks WireMock como fallback; discovery na Fase 0 para definir APIs reais |
| R5 | Restricoes de rede corporativa bloqueando deploys | Média | Alto | Mapeamento de networking na Fase 0; RFC antecipada para liberações |
| R6 | Turnover de pessoal-chave BAT (PO, SPOC técnico) | Baixa | Alto | Documentação completa; handover independente de indivíduos |

---

## 10. Matriz RACI

| Atividade | Foursys | BAT LATAM (IDT) | COE Global |
|:----------|:---:|:---:|:---:|
| Design de pipelines YAML | R/A | I | I |
| Desenvolvimento IaC Terraform | R/A | I | I |
| Aprovação de RFCs (Nível 2) | I | C | R/A |
| Provisionamento Service Connections | C | I | R/A |
| Configuração Quality Gates | R | A | C |
| Integração Sonar corporativo | R | A | C |
| Testes E2E e validação | R/A | I | I |
| Handover e documentação | R/A | A | I |
| Fornecimento de acessos e licenças | I | R/A | C |
| Aprovação de deploy PRD | C | R/A | I |

**Legenda:** R = Responsável, A = Aprovador, C = Consultado, I = Informado

---

## 11. Premissas e Dependências

### Premissas

- A BAT fornecerá acessos de Nível 3 no ADO em até 5 dias úteis após kick-off
- A BAT designará um SPOC (Single Point of Contact) técnico com disponibilidade de 4h/semana
- Instancia SonarQube/SonarCloud corporativa já ativa e acessível
- Ambiente Container Apps ou AKS já provisionado (ou provisionamento via RFC na Fase 0)
- Sandbox ou ambiente de homologação das APIs externas disponível para testes de integração (a ser definido na Fase 0 em conjunto com a BAT, conforme Q&A Item 8)

### Dependências Externas (responsabilidade BAT)

| Dependência | Responsável | SLA Esperado | Impacto se Atrasar |
|:------------|:------------|:-------------|:--------------------|
| Acessos ADO Nível 3 | BAT LATAM | 5 dias úteis | Bloqueia Fase 1 |
| Service Connections (RFC) | COE Global | 2-3 semanas | Bloqueia Fase 4 |
| Credenciais APIs externas (sandbox) | BAT LATAM | 10 dias úteis | Bloqueia Fase 3 (E2E) |
| Liberações de rede (VNet, NSG) | COE Global | 2-3 semanas | Bloqueia Fase 5 |

**Cláusula de impedimentos:** Horas consumidas durante bloqueios por dependências externas não contabilizam contra o budget fixo da Frente A. Retomaremos a contagem após liberação formal pela BAT.

---

## 12. Modelo Comercial e Timeline

### Timeline de Entrega

- **08/06/2026:** Submissão das Propostas Técnica e Comercial via Coupa
- **08/06 a 12/06/2026:** Chamadas de Alinhamento Técnico e Defesa de Proposta
- **22/06 a 26/06/2026:** Rodadas de Negociação e Leilao Eletrônico
- **Pós-Awarding:** Início dos serviços conforme disponibilidade de acessos

### Estrutura Comercial (detalhes em documento separado: PT-BAT-DEVSECOPS-2026-002)

1. **Frente A (Valor Fixo):** Setup completo da esteira DevSecOps para a aplicação de referência
2. **Frente B (Sob Demanda):** Tabela de valores hora por senioridade para manutenção evolutiva e suporte

### Definição de Pronto (Frente A)

Considera-se concluída a entrega da Frente A quando:

1. Todos os 15 itens do edital estiverem implementados e demonstrados em ambiente UAT
2. Quality Gate Matrix configurada e operacional em todos os níveis
3. Documentação técnica em inglês entregue e aprovada pelo SPOC BAT
4. 3 sessões de handover realizadas com time BAT
5. Runbooks de operação e troubleshooting entregues
6. **Template parametrizável validado:** demonstração de que a esteira pode ser replicada para uma segunda aplicação com ajuste de variáveis

---

## 13. Próximos Passos

1. **Submissão via Coupa** até 08/06/2026
2. **Chamada de alinhamento técnico** para esclarecer dúvidas e validar premissas
3. **Kick-off pós-awarding** com Fase 0 (pré-requisitos) e discovery de integracoes
4. **Contato direto:** [inserir nome e e-mail do Líder Técnico]

---

## Glossário

| Termo | Definição |
|:------|:----------|
| ADO | Azure DevOps -- plataforma de desenvolvimento da Microsoft |
| CAB | Change Advisory Board -- comite de aprovação de mudanças |
| COE | Center of Excellence -- centro global de excelência da BAT |
| DAST | Dynamic Application Security Testing -- teste dinâmico de segurança |
| IaC | Infrastructure as Code -- infraestrutura como código |
| RFC | Request for Change -- requisição formal de mudança |
| RTO/RPO | Recovery Time/Point Objective -- metas de recuperação |
| SAST | Static Application Security Testing -- teste estatico de segurança |
| SCA | Software Composition Analysis -- análise de composição de software |
| SLO | Service Level Objective -- meta de nível de serviço |

---

> **Confidencialidade:** Todas as informações contidas nesta proposta são tratadas com sigilo absoluto, respeitando o Código de Conduta Etica da BAT Brasil e os termos de confidencialidade do edital.

---

*Proposta elaborada pela equipe de Engenharia DevSecOps.*
