# Proposta Comercial: Servicos de DevSecOps (Azure DevOps)

**Cliente:** BAT Latam South (Souza Cruz)
**Assunto:** RFP -- Servicos Especializados de DevSecOps
**Data:** 02 de Junho de 2026
**Versao:** 2.0 (Revisada)
**Referencia:** PT-BAT-DEVSECOPS-2026-002
**Status:** Versao Final para Submissao

---

## 0. Resumo Executivo Comercial

| | Frente A (Setup) | Frente B (Sob Demanda) | Frente A-Ext (Replicacao) |
|:--|:--|:--|:--|
| **Descricao** | Esteira DevSecOps completa para 1 app | Horas de suporte tecnico especializado | Replicacao para novas apps similares |
| **Investimento** | R$ 41.800 fixo | R$ 110-280/hora | R$ 14.000 por esteira |
| **Faturamento** | Por entrega com aceite | 60 dias apos execucao | Por entrega com aceite |
| **Escopo** | 15 itens do edital + handover | Manutencao, evolucao, reunioes COE | Template + parametrizacao + validacao |

**Projecao de economia:** A partir da 2a aplicacao, o custo cai 66% (de R$ 41.800 para R$ 14.000) gracas aos templates reutilizaveis. Para 5 aplicacoes no primeiro ano, o investimento total seria R$ 97.800 (vs R$ 209.000 sem reuso).

---

## 1. Modelo de Cobranca e Premissas

Com base no edital da RFP e nas respostas oficiais aos questionamentos tecnicos, adotamos uma abordagem comercial transparente e orientada a resultados:

- **Faturamento por Entrega (Frente A):** A BAT nao fara faturamento mensal recorrente (conforme Item 11 do questionario). O faturamento ocorrera por aplicacao/esteira implantada com sucesso, conforme criterios de aceite definidos na proposta tecnica (Secao 11).
- **Tabela de Precos (Frente B):** Valores fixos de hora por senioridade para suporte tecnico, reunioes internacionais ou melhorias evolutivas.
- **Prazo de Faturamento:** 60 dias apos emissao da NFS-e (com suporte a Confirming/Santander corporativo).

### Criterios de Aceite (Definicao de Pronto) — Frente A

A Frente A sera considerada concluida quando:

1. Todos os 15 itens do edital estiverem implementados e demonstrados em UAT
2. Quality Gate Matrix configurada e operacional
3. Documentacao tecnica em ingles entregue e aprovada
4. 3 sessoes de handover realizadas com time BAT
5. Runbooks de operacao entregues

---

## 2. Estimativa de Custos: Frente A (Setup Completo)

Preco fechado para a configuracao completa da esteira DevSecOps para a aplicacao de referencia (2 Microservicos Java, 1 Frontend Flutter SPA/PWA, PostgreSQL, Redis, 2 APIs externas).

| Fase | Escopo / Entregaveis | Horas | Valor (R$) |
|:-----|:---------------------|:---:|:---:|
| **Fase 0: Pre-requisitos e Discovery** | Checklist de acessos BAT, discovery de integracoes Salesforce/SAP, validacao de ambiente | 15h | R$ 2.850 |
| **Fase 1: Setup, Repos e Versionamento** | Repositorios ADO, Branch Protection, GitFlow, acessos terceiros, RFCs iniciais | 25h | R$ 4.750 |
| **Fase 2: Integracao Continua e Qualidade** | Pipelines CI (Java x2 + Flutter), SonarQube, Linting, Integration Tests (Testcontainers) | 50h | R$ 9.500 |
| **Fase 3: Empacotamento, Artefatos e E2E** | Dockerfiles multi-stage, ACR, Artifacts, Playwright E2E, WireMock mocks | 45h | R$ 8.550 |
| **Fase 4: Continuous Delivery** | Pipelines multi-ambiente (UAT/REG/PRD), Approval Gates, Blue-Green, rollback automatizado, Flyway migrations | 55h | R$ 10.450 |
| **Fase 5: Observabilidade e IaC** | Terraform (compute + networking + Private Endpoints), OpenTelemetry, Azure Monitor, Grafana dashboards, SLOs | 55h | R$ 10.450 |
| **Fase 6: Handover e Onboarding** | Documentacao em ingles, 3 sessoes hands-on, runbooks, troubleshooting guide, video walkthrough | 35h | R$ 6.650 |
| **TOTAL** | **Solucao completa DevSecOps (Itens 1-15 + Handover)** | **280h** | **R$ 53.200** |

> **Nota sobre estimativa:** A tabela acima representa o escopo completo com todas as melhorias identificadas na revisao tecnica (networking, resiliencia, integration tests, discovery de integracoes). Se a BAT optar por um escopo reduzido (sem networking IaC completo e sem discovery de integracoes), a estimativa retorna a **220h / R$ 41.800**.

### Custo por Nova Aplicacao (Frente A -- Extensao)

Uma vez construidos os templates reutilizaveis (YAML herdados e modulos Terraform), o onboarding de novas aplicacoes similares tera custo de **R$ 14.000 por nova esteira**, incluindo:

- Parametrizacao dos templates para a nova aplicacao
- Configuracao de repositorios e branch policies
- Ajuste de pipelines CI/CD
- Validacao end-to-end em UAT
- Documentacao especifica

**Nota:** Aplicacoes com stack diferente da referencia (ex: .NET, Python, Node.js) podem exigir estimativa customizada via Frente B.

---

## 3. Tabela de Servicos Especializados: Frente B (Sob Demanda)

Para demandas que fujam da esteira padrao, melhorias evolutivas, correcoes e suporte em reunioes internacionais de Change Management (CAB).

| Perfil Profissional | Atuacao Principal | Horario Comercial (R$/h) | Fora do Horario (R$/h) |
|:--------------------|:------------------|:---:|:---:|
| **Engenheiro DevOps Junior** | Scripts basicos, parametrizacao simples | R$ 110 | R$ 165 |
| **Engenheiro DevSecOps Pleno** | Pipelines YAML, Dockerfiles, automacao | R$ 160 | R$ 240 |
| **Engenheiro DevSecOps Senior** | SAST/DAST, OpenTelemetry, Terraform | R$ 220 | R$ 330 |
| **Lider Tecnico / Arquiteto DevOps** | Arquitetura, alinhamento em ingles com COE | R$ 280 | R$ 420 |

**Horario comercial:** Segunda a sexta, 09h-18h (horario de Brasilia).
**Fora do horario:** Acrescimo de 50% sobre o valor hora comercial.

### Projecao de Consumo Frente B (Primeiros 6 Meses Pos-Implantacao)

| Periodo | Cenario Otimista | Cenario Realista | Cenario Pessimista |
|:--------|:---:|:---:|:---:|
| Meses 1-3 (estabilizacao) | 30h/mes (~R$ 6.600) | 60h/mes (~R$ 13.200) | 100h/mes (~R$ 22.000) |
| Meses 4-6 (operacao estavel) | 15h/mes (~R$ 3.300) | 30h/mes (~R$ 6.600) | 60h/mes (~R$ 13.200) |
| **Total 6 meses** | **R$ 29.700** | **R$ 59.400** | **R$ 105.600** |

*Estimativa baseada em engajamentos similares. Valores calculados com mix medio de senioridade (60% Pleno + 30% Senior + 10% Arquiteto).*

---

## 4. Projecao TCO -- Total Cost of Ownership (12 Meses)

### Cenario: 1 Aplicacao de Referencia + 2 Replicacoes

| Componente | Valor Estimado (12 meses) |
|:-----------|:---:|
| Frente A -- Setup esteira referencia | R$ 41.800 - R$ 53.200 |
| Frente A-Ext -- 2 replicacoes (R$ 14.000 cada) | R$ 28.000 |
| Frente B -- Suporte 12 meses (cenario realista) | R$ 95.000 |
| Custo Azure PRD (R$ 17.000/mes medio) | R$ 204.000 |
| Custo Azure UAT+REG (R$ 8.000/mes medio) | R$ 96.000 |
| **TCO Total Estimado (12 meses)** | **R$ 465.000 - R$ 476.200** |

**Nota:** Custos Azure sao responsabilidade direta da BAT e estao incluidos apenas para visao completa de TCO. Oportunidades de reducao: Reserved Instances (economia de 30-40% no compute), Dev/Test pricing para ambientes nao-PRD, autoscaling em horario nao-comercial.

---

## 5. Condicoes Comerciais e Operacionais

1. **Acionamento Frente B:** Mediante envio de cronograma simples e aprovacao formal da estimativa por e-mail ou sistema corporativo.
2. **Reunioes Globais:** Horas de reunioes internacionais conduzidas em ingles pelo Arquiteto Tecnico serao faturadas pela Frente B.
3. **Impedimentos:** Horas consumidas durante bloqueios por dependencias externas (acessos, aprovacoes COE, liberacoes de rede) nao contabilizam contra o budget fixo da Frente A. Retomaremos a contagem apos liberacao formal.
4. **Prazo de Pagamento:** 60 dias apos emissao da NFS-e, aceitando Santander Confirming.
5. **Validade da Proposta:** 90 dias a partir da data de emissao.
6. **Reajuste:** Apos os 90 dias de validade, valores sujeitos a reajuste pelo IPCA acumulado no periodo.
7. **Change Requests:** Alteracoes de escopo durante a execucao da Frente A serao formalizadas via Change Request com re-estimativa e aprovacao previa.

---

## 6. Proximos Passos

1. **Submissao via Coupa** ate 08/06/2026
2. **Chamada de alinhamento** para validacao de premissas e esclarecimento de duvidas
3. **Kick-off pos-awarding** com Fase 0 e discovery de integracoes
4. **Contato:** [inserir nome e e-mail]

---

> **Confidencialidade:** Todas as informacoes contidas nesta proposta sao tratadas com sigilo absoluto, respeitando o Codigo de Conduta Etica da BAT Brasil e os termos de confidencialidade do edital.

---

*Proposta elaborada pela equipe de Engenharia DevSecOps.*
