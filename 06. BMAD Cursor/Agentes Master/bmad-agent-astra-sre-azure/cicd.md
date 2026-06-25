---
name: cicd
description: Configura pipelines Azure DevOps ou GitHub Actions
menu-code: CI
---

**Language:** Use `{communication_language}` for all output.

# CI/CD & Deployment

Configure pipelines de entrega contínua com segurança integrada.

## Processo

1. **Entenda o contexto** — ADO ou GitHub Actions? Qual workload (app, IaC, ambos)?
2. **Carregue** `references/iac-cicd.md` para padrões de pipeline
3. **Defina os stages:**
   - Build → Lint → Security Scan (tfsec/checkov) → Test → Plan/Preview → Approval → Apply/Deploy
4. **Configure autenticação segura:**
   - ADO: Service Connection com Workload Identity Federation
   - GHA: OIDC com federated credentials (sem secrets)
5. **Configure environments:**
   - Approval gates para produção
   - Variable Groups integrados com Key Vault
6. **Defina estratégia de deploy** — Blue/Green, Canary ou Rolling
7. **Configure rollback** — Automático baseado em métricas de erro
8. **Responda no formato completo** — `references/standard-output.md`

## Entregáveis
- YAML de pipeline pronto (multi-stage)
- Instrução de Service Connection / OIDC setup
- Estratégia de rollback documentada
