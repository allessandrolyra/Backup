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
2. **Carregue** `references/performance.md` para padrões de performance
3. **Defina métricas alvo:**
   - Latência: p95 e p99 por endpoint
   - Throughput: RPS esperado
   - Saturação: Limites por SKU
   - Error Rate: Threshold aceitável
4. **Planeje testes de carga:**
   - Ferramenta: k6, Locust ou Azure Load Testing
   - Cenários: Baseline, stress, spike, soak
   - Ambiente: Staging com dados representativos
5. **Capacity Planning:**
   - Auto Scaling baseado em métricas reais
   - Limits & Quotas por subscription/região
   - Reserved vs On-Demand para workloads estáveis
6. **Profile & Troubleshoot:**
   - App Insights Profiler para hot paths
   - Dependency tracking para latência de chamadas externas
   - KQL queries para endpoints lentos
7. **Responda no formato completo** — `references/standard-output.md`

## Entregáveis
- Definição de métricas alvo (SLIs de performance)
- Script de teste de carga (k6/Locust)
- Auto Scaling configuration (IaC)
- Relatório de profiling com recomendações
