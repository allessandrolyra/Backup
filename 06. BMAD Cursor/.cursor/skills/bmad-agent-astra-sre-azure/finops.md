---
name: finops
description: Cost Management, Budgets, Rightsizing e otimização
menu-code: FO
---

**Language:** Use `{communication_language}` for all output.

# FinOps

Otimize custos Azure com visibilidade e governança financeira.

## Processo

1. **Entenda o escopo** — Análise de custos existentes ou planejamento de novos workloads?
2. **Carregue** `references/finops-governance.md` para padrões FinOps
3. **Analise custos:**
   - Rightsizing: VMs, AKS node pools, database SKUs (Azure Advisor)
   - Waste: Recursos orphaned, discos não attachados, IPs públicos sem uso
   - Schedules: Auto-shutdown de Non-Prod fora do horário
4. **Configure guardrails:**
   - Budgets com alertas (50%, 80%, 100%, 120%)
   - Anomaly detection no Cost Management
   - Tags obrigatórias para showback/chargeback
5. **Otimize:**
   - Reserved Instances / Savings Plans para workloads estáveis
   - Spot Instances para batch/tolerante a interrupção
   - Tier optimization (Storage, Database)
6. **Reporte:**
   - Custo por CostCenter tag
   - FinOps KPIs: cost per transaction, unit economics, waste %
7. **Responda no formato completo** — `references/standard-output.md`

## Entregáveis
- Análise de rightsizing com recomendações
- Budget configuration (IaC)
- Relatório de waste/orphaned resources
- FinOps dashboard ou KQL queries
