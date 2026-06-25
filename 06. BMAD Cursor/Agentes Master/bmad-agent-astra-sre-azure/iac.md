---
name: iac
description: Gera Terraform, Bicep ou ARM Templates
menu-code: IC
---

**Language:** Use `{communication_language}` for all output.

# IaC (Infrastructure as Code)

Gere artefatos IaC prontos para produção.

## Processo

1. **Entenda o escopo** — Que recursos provisionar? Qual ambiente?
2. **Escolha a ferramenta** — Terraform (padrão) ou Bicep (se preferência do time)
3. **Carregue** `references/iac-cicd.md` para padrões de estrutura e boas práticas
4. **Carregue** `references/security.md` para garantir segurança desde o início
5. **Gere o código** seguindo:
   - Naming convention CAF
   - Módulos reutilizáveis
   - Backend remoto configurado
   - Variables com validation blocks
   - Tags obrigatórias (CostCenter, Env, App, Owner, ManagedBy)
6. **Security scan** — Inclua instrução para rodar tfsec/checkov
7. **Responda no formato completo** — `references/standard-output.md`

## Entregáveis
- Código Terraform/Bicep pronto para `terraform plan` ou `az deployment`
- README do módulo com inputs/outputs
- Instrução de backend remoto (Storage Account)
- Comando de validação (fmt, validate, plan, tfsec)
