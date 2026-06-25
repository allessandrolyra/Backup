---
name: resiliencia-dr
description: Resiliência, HA, DR e Chaos Engineering
menu-code: RD
---

**Language:** Use `{communication_language}` for all output.

# Resiliência & Disaster Recovery

Projete para falha controlada e recuperação.

## Processo

1. **Mapeie workloads críticos** — Quais são mission-critical? Quais toleram downtime?
2. **Carregue** `references/azure-reliability.md` para padrões de resiliência
3. **Defina RTO/RPO** por workload com o usuário
4. **Escolha estratégia de DR** — Apresente 2 opções:
   - Backup & Restore (custo baixo, RTO/RPO alto)
   - Pilot Light (core ativo, infra mínima)
   - Warm Standby (infra funcional reduzida)
   - Active-Active (máxima disponibilidade, custo alto)
5. **Aplique padrões de resiliência:**
   - Retry, Circuit Breaker, Bulkhead, Graceful Degradation
   - Zone Redundancy para recursos críticos
6. **Planeje Chaos Engineering:**
   - Azure Chaos Studio experiments
   - GameDay com hipótese, blast radius e métricas de sucesso
7. **Responda no formato completo** — `references/standard-output.md`

## Entregáveis
- Mapeamento RTO/RPO por workload
- Configuração ASR (se aplicável)
- IaC para recursos zone-redundant
- Plano de GameDay documentado
