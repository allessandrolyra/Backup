---
name: performance
description: Performance engineering — p95/p99, testes de carga, capacity planning
menu-code: PF
---

**Language:** Use `{communication_language}` for all output.

# Performance Engineering

Otimize performance e planeje capacidade.

## Processo

1. **Entenda o contexto** — Qual o workload? Existem métricas de baseline?
2. **Defina métricas alvo:** p95/p99, throughput (RPS), saturação
3. **Planeje testes de carga:** k6, Locust ou AWS-native
4. **Capacity Planning:** Auto Scaling baseado em métricas reais
5. **Profile & Troubleshoot:** X-Ray, CloudWatch Insights
6. **Responda no formato completo** — `references/standard-output.md`

## Entregáveis
- Métricas alvo definidas
- Script de teste de carga
- Auto Scaling configuration (IaC)
