---
name: governanca
description: Multi-account, Landing Zones, SCPs, IAM e compliance
menu-code: GV
---

**Language:** Use `{communication_language}` for all output.

# Governança

Configure governança enterprise AWS.

## Processo

1. **Entenda o escopo** — Landing Zone nova ou governance em ambiente existente?
2. **Carregue** `references/finops-governance.md` para padrões
3. **Configure hierarquia:** AWS Organizations, OUs, accounts por ambiente
4. **Configure SCPs:** Guardrails de segurança globais
5. **Configure IAM:** Least privilege, IAM Roles, SSO
6. **Configure Policy as Code:** OPA/Sentinel/Conftest
7. **Tags obrigatórias:** App, Env, Team, CostCenter
8. **Responda no formato completo** — `references/standard-output.md`

## Entregáveis
- Estrutura de Organizations/OUs documentada
- SCPs definitions (JSON)
- IAM role/policy assignments
