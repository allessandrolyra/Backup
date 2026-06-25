---
name: iac
description: Gera Terraform ou CloudFormation prontos para produção
menu-code: IC
---

**Language:** Use `{communication_language}` for all output.

# IaC (Infrastructure as Code)

Gere artefatos IaC prontos para produção.

## Processo

1. **Entenda o escopo** — Que recursos provisionar? Qual ambiente?
2. **Escolha a ferramenta** — Terraform (padrão) ou CloudFormation
3. **Carregue** `references/iac-cicd.md` para padrões de estrutura
4. **Gere o código** seguindo:
   - Estrutura: `/modules` + `/envs` (dev, stg, prd)
   - Backend remoto (S3 + DynamoDB)
   - Variables com validation blocks
   - Tags obrigatórias (App, Env, Team, CostCenter)
5. **Security scan** — Inclua instrução para rodar tfsec/checkov/terrascan
6. **Responda no formato completo** — `references/standard-output.md`

## Entregáveis
- Código Terraform/CFN pronto para `terraform plan` ou `aws cloudformation deploy`
- Instrução de backend remoto (S3 + DynamoDB lock)
- Comando de validação (fmt, validate, plan, tfsec)
