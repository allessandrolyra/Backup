---
name: observabilidade-sre
description: SLIs/SLOs, Error Budget, OpenTelemetry e dashboards
menu-code: OS
---

**Language:** Use `{communication_language}` for all output.

# Observabilidade & SRE

Configure monitoramento centrado em confiabilidade e cultura SRE.

## Processo

1. **Entenda o escopo** — Quais serviços monitorar?
2. **Carregue** `references/sre-observability.md` para padrões
3. **Configure Golden Signals** por serviço: Latência, Tráfego, Erros, Saturação
4. **Defina SLIs/SLOs e Error Budget Policy**
5. **Configure instrumentação:** OpenTelemetry, CloudWatch, X-Ray
6. **Configure alertas e dashboards**
7. **Responda no formato completo** — `references/standard-output.md`

## Entregáveis
- SLIs/SLOs com Error Budget Policy
- CloudWatch Dashboards e Alarms (IaC)
- Instrumentação OpenTelemetry
