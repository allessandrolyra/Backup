---
name: resiliencia-dr
description: Resiliência, HA, DR e Chaos Engineering
menu-code: RD
---

**Language:** Use `{communication_language}` for all output.

# Resiliência & Disaster Recovery

Projete para falha controlada e recuperação.

## Processo

1. **Mapeie workloads críticos** — Quais são mission-critical?
2. **Carregue** `references/sre-observability.md` para padrões de resiliência
3. **Defina RTO/RPO** por workload
4. **Escolha estratégia de DR** — 2 opções:
   - Backup & Restore, Pilot Light, Warm Standby, Active-Active
5. **Aplique padrões de resiliência:** Retry, Circuit Breaker, Bulkhead, Fallback
6. **Planeje Chaos Engineering:** AWS Fault Injection Simulator (FIS), GameDays
7. **Responda no formato completo** — `references/standard-output.md`

## Entregáveis
- Mapeamento RTO/RPO por workload
- IaC para recursos multi-AZ
- Plano de GameDay documentado
