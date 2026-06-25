---
name: observabilidade-sre
description: Observabilidade, SLIs/SLOs, Error Budget e alertas
menu-code: OS
---

**Language:** Use `{communication_language}` for all output.

# Observabilidade & SRE

Configure monitoramento centrado em confiabilidade e cultura SRE.

## Processo

1. **Entenda o escopo** — Quais serviços monitorar? Existe App Insights configurado?
2. **Carregue** `references/observability.md` para padrões de observabilidade
3. **Configure Golden Signals** por serviço:
   - Latência (p95/p99), Tráfego (RPS), Erros (5xx rate), Saturação (CPU/mem/IOPS)
4. **Defina SLIs/SLOs** com o usuário:
   - SLI: Métrica concreta (ex: % requests < 200ms)
   - SLO: Alvo (ex: 99.9% mensal)
   - Error Budget: Quanto erro é tolerável
   - Error Budget Policy: Ações quando budget ≤ 20% e ≤ 0%
5. **Configure instrumentação:**
   - OpenTelemetry preferível para tracing distribuído
   - App Insights para auto-instrumentation
   - Correlation IDs para rastreabilidade cross-service
6. **Configure alertas e dashboards:**
   - Alert rules baseados em sintomas (user-impacting), não em métricas de infra
   - KQL queries para Log Analytics
   - Azure Dashboard ou Grafana Managed
7. **Responda no formato completo** — `references/standard-output.md`

## Entregáveis
- Definição de SLIs/SLOs com Error Budget Policy
- KQL queries prontas para alertas e dashboards
- IaC para Alert Rules e Action Groups
- Dashboard template (JSON ou Bicep)
