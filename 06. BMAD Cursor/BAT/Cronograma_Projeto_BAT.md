# Cronograma do Projeto -- DevSecOps BAT Latam South

**Cliente:** BAT Latam South (Souza Cruz)
**Duracao Total:** 14 semanas (pior cenario com dependencias externas)
**Esforco Total:** 400 horas
**Equipe:** 3 profissionais

---

## Equipe do Projeto

| Perfil | Senioridade | Responsabilidades Principais | Dedicacao |
|:-------|:------------|:-----------------------------|:----------|
| Lider Tecnico / Arquiteto DevOps | Especialista | Arquitetura, IaC Terraform, interface com COE Global em ingles, defesa tecnica, decisoes de design | Parcial (~15-20h/semana) |
| Engenheiro DevSecOps Senior | Senior | Pipelines CI/CD, seguranca Shift-Left, observabilidade, deploys multi-ambiente | Integral (~35-40h/semana) |
| Engenheiro DevSecOps Pleno | Pleno | Dockerfiles, testes E2E, mocks, documentacao tecnica, automacoes de suporte | Integral (~35-40h/semana) |

---

## Premissas do Pior Cenario

Este cronograma considera os seguintes riscos materializados:

| Risco | Impacto no Cronograma |
|:------|:----------------------|
| RFC do COE Global demora 3-4 semanas para aprovacao (ao inves de 2) | +2 semanas de espera na Fase 1 e Fase 4 |
| BAT atrasa 1 semana para fornecer acessos iniciais ao ADO | +1 semana na Fase 0 |
| Integracao com SonarQube corporativo exige troubleshooting | +8h na Fase 2 |
| Sandbox Salesforce/SAP nao disponivel no prazo | +1 semana na Fase 3 (trabalho com mocks enquanto aguarda) |
| Problemas de conectividade de rede (VNet, firewall corporativo) | +8h na Fase 5 |
| Retrabalho apos revisao do time BAT | +16h distribuidos nas Fases 4-6 |
| Reunioes de alinhamento, status reports, ceremonias | ~4h/semana para o Lider Tecnico |

---

## Visao Geral por Fase

| Fase | Semanas | Horas | Valor (R$) | Entregaveis |
|:-----|:--------|:------|:-----------|:------------|
| Fase 0: Pre-requisitos e Discovery | S1-S2 | 25h | R$ 4.750 | Checklist de acessos, discovery Salesforce/SAP, validacao de ambiente, RFCs submetidas |
| Fase 1: Setup, Repos e Versionamento | S2-S3 | 30h | R$ 5.700 | Repos ADO, GitFlow, Branch Protection, acessos de terceiros configurados |
| Fase 2: Integracao Continua e Qualidade | S4-S6 | 60h | R$ 11.400 | Pipelines CI (Java x2 + Flutter), Sonar corporativo integrado, Quality Gates |
| Fase 3: Empacotamento, Artefatos e E2E | S6-S8 | 55h | R$ 10.450 | Dockerfiles, ACR, Playwright E2E, WireMock mocks validados |
| Fase 4: Continuous Delivery | S8-S10 | 65h | R$ 12.350 | Pipelines CD (UAT/REG/PRD), Blue-Green, rollback, Flyway, Approval Gates |
| Fase 5: Observabilidade e IaC | S9-S12 | 65h | R$ 12.350 | Terraform completo (networking + compute + dados), OpenTelemetry, Grafana, SLOs |
| Fase 6: Handover e Onboarding | S12-S14 | 45h | R$ 8.550 | Documentacao em ingles, 3 sessoes hands-on, runbooks, video, suporte pos-handover |
| Gestao do Projeto | S1-S14 | 55h | R$ 10.450 | Reunioes BAT, status reports, alinhamentos COE, gestao de RFCs, impedimentos |
| **TOTAL** | **14 semanas** | **400h** | **R$ 76.000** | |

---

## Cronograma Semana a Semana

### SEMANA 1 -- Kick-off e Discovery

| Profissional | Horas | Atividades |
|:-------------|:------|:-----------|
| Lider Tecnico | 12h | Reuniao de kick-off com BAT. Discovery de integracoes: mapear tipo de API Salesforce (REST/Bulk/Streaming), SAP (OData/RFC), volumes, autenticacao. Elaborar primeiras RFCs (Service Connections, Variable Groups, acessos terceiros). Submeter RFCs ao COE. |
| Senior | 6h | Mapear ambiente existente: ADO org structure, policies herdadas, networking, firewalls. Validar conectividade com Azure (subscriptions, resource groups). |
| Pleno | 4h | Preparar checklist de pre-requisitos. Documentar dependencias (acessos, licencas, credenciais). Enviar formalmente para BAT. |
| **Total** | **22h** | **Fase 0 iniciada. RFCs submetidas (aguardando aprovacao COE).** |

### SEMANA 2 -- Aguardando Acessos + Inicio dos Repos

| Profissional | Horas | Atividades |
|:-------------|:------|:-----------|
| Lider Tecnico | 8h | Follow-up com COE sobre RFCs. Reuniao de alinhamento tecnico com time BAT. Definir nomenclatura de repos e branching strategy com PO local. |
| Senior | 8h | Criar repositorios Git no Azure Repos (assim que acessos liberados). Configurar Branch Protection Rules iniciais. |
| Pleno | 6h | Configurar GitFlow (main/develop/feature/release/hotfix). Documentar convencoes de commit e PR. |
| **Total** | **22h** | **Fase 0 concluida. Fase 1 em andamento (dependente de acessos).** |

**Risco ativo:** Se acessos ADO nao liberados ate final da S2, Senior e Pleno ficam bloqueados. Lider Tecnico escala para BAT.

### SEMANA 3 -- Repos Operacionais + Preparacao CI

| Profissional | Horas | Atividades |
|:-------------|:------|:-----------|
| Lider Tecnico | 6h | Validar repos criados. Definir arquitetura dos pipelines YAML (template base herdavel). Alinhar Quality Gate Matrix com time BAT. Status report semanal. |
| Senior | 10h | Finalizar Branch Protection (aprovadores, checks obrigatorios). Configurar grupos de seguranca no Azure AD/Entra ID. Testar fluxo de PR completo. |
| Pleno | 8h | Preparar estrutura base dos pipelines CI (YAML template). Configurar Variable Groups por ambiente (dev/uat/reg/prd). |
| **Total** | **24h** | **Fase 1 concluida. Preparacao para Fase 2.** |

### SEMANA 4 -- Pipelines CI: Java (Parte 1)

| Profissional | Horas | Atividades |
|:-------------|:------|:-----------|
| Lider Tecnico | 6h | Reuniao com time BAT para acesso ao SonarQube corporativo. Definir Quality Gates (cobertura 80%, zero Critical/Blocker). Status report. |
| Senior | 14h | Pipeline CI do Microservico Java A: build Maven/Gradle, JUnit 5, cobertura com JaCoCo, integracao com Sonar corporativo. Troubleshooting de conectividade com Sonar (firewall, tokens). |
| Pleno | 10h | Pipeline CI do Microservico Java B: replicar padrao do Java A. Configurar Checkstyle/PMD para linting. Testar gate de bloqueio de merge. |
| **Total** | **30h** | **Fase 2 (50%). 2 pipelines CI Java operacionais.** |

### SEMANA 5 -- Pipelines CI: Flutter + Seguranca

| Profissional | Horas | Atividades |
|:-------------|:------|:-----------|
| Lider Tecnico | 4h | Validar pipelines Java em funcionamento. Revisar configuracao de seguranca. Status report. |
| Senior | 12h | Pipeline CI do Flutter: flutter test, flutter analyze (lint), cobertura. Configurar OWASP Dependency Check (SCA para JARs Java). Testar integracao SCA no pipeline. |
| Pleno | 10h | Configurar Gitleaks (secrets detection) em todos os repos. Integration Tests com Testcontainers (Java + PostgreSQL + Redis). Ajustar gates de seguranca nos PRs. |
| **Total** | **26h** | **Fase 2 (85%). 3 pipelines CI + seguranca basica.** |

### SEMANA 6 -- Finalizacao CI + Inicio Empacotamento

| Profissional | Horas | Atividades |
|:-------------|:------|:-----------|
| Lider Tecnico | 6h | Revisao final de todas as pipelines CI. Aprovar Quality Gate Matrix. Definir estrategia de containers e ACR. Status report. |
| Senior | 10h | Troubleshooting de issues encontrados nas pipelines CI (falsos positivos Sonar, timeout de testes). Dockerfile multi-stage para Microservico Java A (build + runtime otimizado com distroless). |
| Pleno | 10h | Dockerfile multi-stage para Microservico Java B. Configuracao do ACR (Azure Container Registry). Pipeline de build + push para ACR. |
| **Total** | **26h** | **Fase 2 concluida. Fase 3 (25%).** |

### SEMANA 7 -- Containers + Setup E2E

| Profissional | Horas | Atividades |
|:-------------|:------|:-----------|
| Lider Tecnico | 6h | Definir arquitetura do ambiente efemero para E2E. Alinhar com BAT sobre sandbox Salesforce/SAP. Status report. Follow-up de RFCs pendentes com COE. |
| Senior | 12h | Dockerfile Flutter (nginx + assets estaticos). Image signing com Cosign. Trivy/Grype scan integrado no pipeline de build. Corrigir vulnerabilidades encontradas nos scans. |
| Pleno | 12h | Setup Playwright: instalacao, configuracao de browsers headless, primeiros testes de smoke. Criar contratos OpenAPI/Swagger para mocks. Configurar WireMock com contratos Salesforce/SAP. |
| **Total** | **30h** | **Fase 3 (70%). Containers prontos, E2E em configuracao.** |

**Risco ativo:** Se sandbox Salesforce/SAP nao disponivel, E2E roda 100% com mocks. Validacao com APIs reais fica para Fase 4.

### SEMANA 8 -- Finalizacao E2E + Inicio CD

| Profissional | Horas | Atividades |
|:-------------|:------|:-----------|
| Lider Tecnico | 8h | Design dos ambientes CD (UAT/REG/PRD). Definir Approval Gates e fluxo de aprovacao com PO BAT. Elaborar RFC para Service Connections dos ambientes de deploy. Status report. |
| Senior | 12h | Finalizar cenarios E2E (happy path + cenarios de erro: timeout, 500, rate limit). Integrar pipeline E2E no fluxo CI (trigger em merge para develop). |
| Pleno | 10h | Artifact promotion: garantir que a mesma imagem Docker promove entre ambientes. Configurar Variable Groups por ambiente. Iniciar pipeline CD para UAT. |
| **Total** | **30h** | **Fase 3 concluida. Fase 4 (20%).** |

### SEMANA 9 -- CD Multi-ambiente + Inicio IaC

| Profissional | Horas | Atividades |
|:-------------|:------|:-----------|
| Lider Tecnico | 10h | Terraform: modulo de networking (VNet, 4 subnets, Private Endpoints, NSGs, DNS Private Zones). Validar com equipe de infra BAT. Status report. |
| Senior | 14h | Pipeline CD UAT (trigger em merge develop). Pipeline CD REG (trigger em branch release/*). Flyway: configurar migrations de banco no pipeline. Smoke tests pos-deploy. |
| Pleno | 10h | Terraform: modulo de compute (Container Apps Environment). Terraform: modulo de dados (PostgreSQL Flexible, Redis Cache). Configurar state remoto (Azure Storage). |
| **Total** | **34h** | **Fase 4 (55%). Fase 5 (25%).** |

### SEMANA 10 -- CD Producao + IaC

| Profissional | Horas | Atividades |
|:-------------|:------|:-----------|
| Lider Tecnico | 10h | Terraform: Application Gateway WAF v2, Key Vault, APIM, Service Bus. Revisao de seguranca de toda a IaC (tfsec/checkov). Status report. |
| Senior | 14h | Pipeline CD PRD: tags v*, Blue-Green com revision splitting, Approval Gates (PO + Security), rollback automatico por health check failure (< 5 min), smoke tests pos-deploy. |
| Pleno | 8h | Terraform: ACR com Private Endpoint, Service Bus, configuracoes de DNS. Troubleshooting de conectividade de Private Endpoints (problema frequente em ambientes corporativos). |
| **Total** | **32h** | **Fase 4 (90%). Fase 5 (55%).** |

**Risco ativo:** Private Endpoints frequentemente exigem liberacoes de rede que dependem do time de infra BAT. Possivel atraso de 3-5 dias uteis.

### SEMANA 11 -- Finalizacao CD + Observabilidade

| Profissional | Horas | Atividades |
|:-------------|:------|:-----------|
| Lider Tecnico | 8h | OWASP ZAP: configurar DAST no ambiente UAT. Definir SLOs com PO BAT (availability 99.9%, p99 < 500ms). Configurar alertas no Teams. Status report. |
| Senior | 10h | Teste end-to-end do fluxo CD completo: commit -> CI -> UAT -> REG -> PRD com Blue-Green. Corrigir issues encontrados. Validar rollback em cenario de falha simulada. |
| Pleno | 10h | OpenTelemetry SDK nos microservicos Java (instrumentacao de traces, metricas, logs). Configurar exportacao para Azure Monitor (App Insights + Log Analytics). |
| **Total** | **28h** | **Fase 4 concluida. Fase 5 (80%).** |

### SEMANA 12 -- Dashboards + Inicio Handover

| Profissional | Horas | Atividades |
|:-------------|:------|:-----------|
| Lider Tecnico | 10h | Dashboards Grafana: RED (Rate, Errors, Duration) para microservicos, USE (Utilization, Saturation, Errors) para PostgreSQL e Redis. Definir thresholds de alerta. |
| Senior | 10h | Azure Monitor Availability Tests (Standard Tests, 5 min, 3 localizacoes). Probes de Container Apps (Liveness, Readiness, Startup). Validar traces ponta a ponta (Flutter -> Java A -> Java B -> PostgreSQL). |
| Pleno | 10h | Iniciar documentacao tecnica em ingles: arquitetura, pipelines, IaC, integrações. Criar indice de runbooks. |
| **Total** | **30h** | **Fase 5 concluida. Fase 6 (25%).** |

### SEMANA 13 -- Handover: Sessoes e Documentacao

| Profissional | Horas | Atividades |
|:-------------|:------|:-----------|
| Lider Tecnico | 12h | **Sessao hands-on 1:** Arquitetura, IaC Terraform e networking (2h apresentacao + 1h pratica + 1h Q&A). **Sessao hands-on 2:** Pipelines CI/CD, Blue-Green e rollback (2h + 1h + 1h). Defesa tecnica para stakeholders BAT. |
| Senior | 8h | **Sessao hands-on 3:** Observabilidade, SLOs, Grafana e troubleshooting (2h + 1h + 1h). Gravar video walkthrough das esteiras (screencast completo ~45min). |
| Pleno | 10h | Finalizar documentacao: runbooks de operacao (CI, CD, rollback, DR), troubleshooting guide com cenarios comuns, FAQ tecnico. |
| **Total** | **30h** | **Fase 6 (85%).** |

### SEMANA 14 -- Suporte Pos-Handover e Encerramento

| Profissional | Horas | Atividades |
|:-------------|:------|:-----------|
| Lider Tecnico | 8h | Reuniao de encerramento com BAT. Apresentacao de resultados e metricas. Recomendacoes para evolucao (Frente B). Assinatura de aceite formal. |
| Senior | 6h | Suporte a duvidas do time BAT apos handover. Correcoes pontuais de configuracao. Validacao final de todos os pipelines em execucao real. |
| Pleno | 6h | Revisao final de toda documentacao. Entrega formal dos artefatos (repos, pipelines, IaC, docs, videos). Checklist de encerramento. |
| **Total** | **20h** | **Fase 6 concluida. Projeto encerrado.** |

---

## Resumo de Horas por Profissional

| Profissional | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 | S13 | S14 | Total | % |
|:-------------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:---:|:---:|:---:|:---:|:---:|:------|:--|
| Lider Tecnico | 12 | 8 | 6 | 6 | 4 | 6 | 6 | 8 | 10 | 10 | 8 | 10 | 12 | 8 | **114h** | 29% |
| Senior | 6 | 8 | 10 | 14 | 12 | 10 | 12 | 12 | 14 | 14 | 10 | 10 | 8 | 6 | **146h** | 36% |
| Pleno | 4 | 6 | 8 | 10 | 10 | 10 | 12 | 10 | 10 | 8 | 10 | 10 | 10 | 6 | **124h** | 31% |
| **Contingencia** | | | | | | | | | | | | | | | **16h** | 4% |
| **Total Semana** | **22** | **22** | **24** | **30** | **26** | **26** | **30** | **30** | **34** | **32** | **28** | **30** | **30** | **20** | **400h** | 100% |

---

## Custo por Profissional

| Profissional | Horas | Valor/Hora (R$) | Custo Total (R$) |
|:-------------|:------|:----------------|:-----------------|
| Lider Tecnico / Arquiteto DevOps | 114h | R$ 280 | R$ 31.920 |
| Engenheiro DevSecOps Senior | 146h | R$ 220 | R$ 32.120 |
| Engenheiro DevSecOps Pleno | 124h | R$ 160 | R$ 19.840 |
| Contingencia (mix de perfis) | 16h | R$ 190 (media) | R$ 3.040 |
| **TOTAL** | **400h** | | **R$ 86.920** |

---

## Marcos do Projeto (Milestones)

| Marco | Semana | Criterio de Aceite | Risco de Atraso |
|:------|:-------|:-------------------|:----------------|
| M0 -- Kick-off Realizado | S1 | Reuniao feita, RFCs submetidas, checklist enviado | Baixo |
| M1 -- Acessos e Ambiente Prontos | S2 | Todos os acessos ADO Nivel 3 liberados | Alto (depende BAT) |
| M2 -- Repos Operacionais | S3 | 3 repos com GitFlow, PRs funcionando | Medio (depende M1) |
| M3 -- CI Completo | S6 | 3 pipelines CI com Quality Gates, Sonar integrado | Medio (Sonar corporativo) |
| M4 -- Artefatos e E2E | S8 | Imagens Docker no ACR, E2E passando | Medio (sandbox APIs) |
| M5 -- CD Multi-Ambiente | S11 | Deploy UAT/REG/PRD com Blue-Green e rollback testado | Alto (RFCs + networking) |
| M6 -- Observabilidade Completa | S12 | Dashboards, SLOs, alertas, IaC 100% aplicado | Medio (Private Endpoints) |
| M7 -- Projeto Encerrado | S14 | Handover concluido, aceite formal assinado | Baixo |

---

## Dependencias e Caminho Critico

```
S1-S2: Fase 0 (Discovery + Acessos BAT)  <<<< BLOQUEANTE >>>>
   |
   v
S2-S3: Fase 1 (Repos + GitFlow)
   |
   v
S4-S6: Fase 2 (Pipelines CI) ----------> S6-S8: Fase 3 (Docker + E2E)
                                              |
                                              v
                                     S8-S10: Fase 4 (CD Multi-Ambiente)
                                              |
                              S9-S12: Fase 5 (IaC + Observabilidade)  <-- parcialmente paralelo
                                              |
                                              v
                              S12-S14: Fase 6 (Handover + Encerramento)
```

**Gargalos do pior cenario:**
1. **S1-S2:** BAT demora para liberar acessos ADO e credenciais --> tudo atrasa
2. **S4-S5:** Sonar corporativo com problemas de conectividade --> Fase 2 estoura
3. **S7-S8:** Sandbox Salesforce/SAP indisponivel --> E2E roda so com mocks
4. **S9-S10:** RFCs de Service Connection para PRD demoram no COE --> Fase 4 atrasa
5. **S10-S11:** Private Endpoints bloqueados por firewall corporativo --> Fase 5 atrasa

---

## Custo Acumulado por Semana

| Semana | Horas | Custo (R$) | Acumulado (R$) | % Concluido |
|:-------|:------|:-----------|:---------------|:------------|
| S1 | 22h | R$ 4.840 | R$ 4.840 | 6% |
| S2 | 22h | R$ 4.840 | R$ 9.680 | 11% |
| S3 | 24h | R$ 5.280 | R$ 14.960 | 17% |
| S4 | 30h | R$ 6.600 | R$ 21.560 | 25% |
| S5 | 26h | R$ 5.720 | R$ 27.280 | 31% |
| S6 | 26h | R$ 5.720 | R$ 33.000 | 38% |
| S7 | 30h | R$ 6.600 | R$ 39.600 | 46% |
| S8 | 30h | R$ 6.600 | R$ 46.200 | 53% |
| S9 | 34h | R$ 7.480 | R$ 53.680 | 62% |
| S10 | 32h | R$ 7.040 | R$ 60.720 | 70% |
| S11 | 28h | R$ 6.160 | R$ 66.880 | 77% |
| S12 | 30h | R$ 6.600 | R$ 73.480 | 85% |
| S13 | 30h | R$ 6.600 | R$ 80.080 | 92% |
| S14 | 20h | R$ 3.800 | R$ 83.880 | 97% |
| Contingencia | 16h | R$ 3.040 | R$ 86.920 | 100% |

---

## Comparativo: Cenario Otimista vs Pior Cenario

| Indicador | Cenario Otimista | Pior Cenario |
|:----------|:-----------------|:-------------|
| Duracao | 10 semanas | 14 semanas |
| Horas totais | 280h | 400h |
| Custo Frente A | R$ 53.200 | R$ 86.920 |
| Horas de gestao/reunioes | 20h (7%) | 55h (14%) |
| Buffer/contingencia | 20h (7%) | 16h (4%) -- absorvido pelos riscos |
| Maior risco | Acessos BAT | Acessos BAT + RFCs COE + networking |

**Recomendacao:** Apresentar ao cliente o cenario otimista (R$ 53.200 / 10 semanas) como proposta base, e manter o pior cenario (R$ 86.920 / 14 semanas) como referencia interna para negociacao e gestao de expectativas. Se o cliente questionar prazos, a clausula de impedimentos protege o budget fixo contra atrasos causados pela BAT.

---

*Cronograma elaborado pela equipe de Engenharia DevSecOps.*
*Valores calculados com base na tabela Frente B. Sujeito a ajustes apos validacao de premissas com a BAT.*
