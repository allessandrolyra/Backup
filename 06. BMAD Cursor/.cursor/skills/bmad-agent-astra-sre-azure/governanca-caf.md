---
name: governanca-caf
description: Governança CAF, Azure Policy, RBAC e Landing Zones
menu-code: GC
---

**Language:** Use `{communication_language}` for all output.

# Governança & CAF

Configure governança enterprise com Cloud Adoption Framework.

## Processo

1. **Entenda o escopo** — Greenfield (Landing Zone nova) ou add governance a ambiente existente?
2. **Carregue** `references/finops-governance.md` para padrões de governança
3. **Carregue** `references/security.md` para RBAC e identity
4. **Configure hierarquia:**
   - Management Groups (Prod, Non-Prod, Sandbox, Decommissioned)
   - Subscriptions por ambiente e workload
   - Resource Groups por lifecycle
5. **Configure Azure Policy:**
   - Deny: Regiões, SKUs proibidas, public access
   - Audit: Recursos non-compliant
   - DeployIfNotExists: Auto-remediação (diagnostic settings, NSG flow logs)
6. **Configure RBAC:**
   - Least privilege com Custom Roles quando necessário
   - Managed Identity para todo recurso
   - PIM para roles elevados
7. **Configure Tags obrigatórias:**
   - CostCenter, Environment, Application, Owner, ManagedBy, CreatedDate
8. **Responda no formato completo** — `references/standard-output.md`

## Entregáveis
- Hierarquia de Management Groups documentada
- Azure Policy definitions (JSON ou Bicep)
- RBAC role assignments
- Tag enforcement policy
