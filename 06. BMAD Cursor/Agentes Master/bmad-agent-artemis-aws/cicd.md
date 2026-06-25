---
name: cicd
description: Configura pipelines CI/CD com security scans e rollback
menu-code: CI
---

**Language:** Use `{communication_language}` for all output.

# CI/CD & Deployment

Configure pipelines de entrega contínua com segurança integrada.

## Processo

1. **Entenda o contexto** — GitHub Actions, CodePipeline ou outro? Qual workload?
2. **Carregue** `references/iac-cicd.md` para padrões de pipeline
3. **Defina os stages:** Build → Lint → Security Scan → Test → Plan → Approval → Apply/Deploy
4. **Configure autenticação segura:** OIDC para GitHub Actions (sem access keys)
5. **Defina estratégia de deploy** — Canary, Blue/Green ou Rolling
6. **Configure rollback** — Automatizado baseado em métricas de erro
7. **Responda no formato completo** — `references/standard-output.md`

## Entregáveis
- YAML/workflow de pipeline pronto
- Estratégia de rollback documentada
- Security checks integrados
