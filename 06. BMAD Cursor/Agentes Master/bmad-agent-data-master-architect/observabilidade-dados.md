---
name: observabilidade-dados
description: Observabilidade — monitoramento, SLA/SLO, alertas, logs, tracing, freshness
menu-code: OB
---

**Language:** Use `{communication_language}` for all output.

# Observabilidade de Dados

Projete e implante observabilidade para plataformas de dados: monitoramento, alertas, SLA/SLO, métricas, logs e tracing.

## Escopo

- **Ferramentas:** Azure Monitor, Log Analytics, CloudWatch, Datadog, Grafana, Prometheus, OpenTelemetry
- **Métricas:** SLA, SLO, throughput, latência, freshness, utilização, crescimento
- **Logs:** SQL execution, Spark jobs, ETL pipelines, API calls, Power BI refresh
- **Tracing:** Dependências entre pipelines, lineage operacional, gargalos
- **Data Observability:** Monte Carlo, Bigeye, Elementary, Great Expectations + dashboards

## Processo

Ao receber um pedido de observabilidade:

### NÍVEL 1 — Estratégia

1. **Definir pilares:**

| Pilar | O que Monitorar | Ferramentas |
|---|---|---|
| Métricas | SLA/SLO, throughput, latência, volume | Prometheus, Azure Monitor, CloudWatch |
| Logs | Execuções, erros, warnings, SQL queries | Log Analytics, CloudWatch Logs, ELK |
| Tracing | Dependências, flow, gargalos | OpenTelemetry, Jaeger, App Insights |
| Data Quality | Freshness, completude, anomalias | Elementary, Great Expectations, custom |

2. **Definir SLIs/SLOs:**

| SLI | SLO Exemplo |
|---|---|
| Pipeline freshness | Dados disponíveis até 07:00 (99.5%) |
| Query latency p95 | < 5s para dashboards principais |
| Data completude | > 99.9% de registros esperados |
| Pipeline success rate | > 99% de execuções bem-sucedidas |

### NÍVEL 2 — Implementação

1. **Instrumentação** — OpenTelemetry SDK, logging estruturado
2. **Dashboards:**
   - Pipeline health (success rate, duration trends, volume)
   - Data quality (freshness, completude, anomalias)
   - Infrastructure (CPU, memory, storage, network)
   - Cost tracking (compute hours, storage growth)
3. **Alertas** — Configuração de alertas com severidade e routing

### NÍVEL 3 — Automação

1. **Alert rules** — Terraform/Bicep para alertas como código
2. **Runbooks** — Playbooks automatizados para incidentes comuns
3. **Auto-remediation** — Retry automático, autoscaling, cleanup

### NÍVEL 4 — Operação

1. **Incident response** — Processo de resposta a incidentes de dados
2. **Error budget** — Tracking de budget de erros por SLO
3. **Capacity planning** — Projeções de crescimento e capacidade
4. **Review** — Revisão periódica de SLOs e alertas

## Progressão

- **NÍVEL 1 → 2:** Após confirmar pilares e SLIs/SLOs com o usuário, prosseguir para implementação
- **NÍVEL 2 → 3:** Após o usuário aprovar dashboards e alertas, prosseguir para automação
- **NÍVEL 3 → 4:** Após entregar automação, perguntar se deseja configurar operação e incident response
- **A qualquer momento:** O usuário pode solicitar apenas um nível específico — respeitar o escopo pedido

## Saída

Sempre carregar `references/standard-output.md` e seguir o formato padrão de resposta.

Incluir:
- Definição de SLIs/SLOs
- Queries de monitoramento (KQL, SQL, PromQL)
- Configuração de alertas
- Dashboard layouts
