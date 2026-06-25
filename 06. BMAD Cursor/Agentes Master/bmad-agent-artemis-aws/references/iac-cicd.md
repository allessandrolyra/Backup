# Infra as Code & CI/CD Patterns

Padronização de entrega e automação.

## 1. Terraform (Padrão)
Estrutura sugerida:
- `/modules`: Componentes reaproveitáveis.
- `/envs`: Pastas `dev`, `stg`, `prd` para instanciar os módulos.
- Arquivos padrão: `versions.tf`, `providers.tf`, `main.tf`, `variables.tf`, `outputs.tf`.

### Boas Práticas:
- Backend remoto (S3 + DynamoDB).
- Uso extensivo de `locals`.
- Validation blocks nas variáveis.
- Sempre rodar `terraform fmt` e `validate`.

## 2. CloudFormation (Alternativo)
- Seguir Lifecycle de Stacks.
- Usar Change Sets para previews.
- Recomendar `cfn-lint`.

## 3. Pipelines & Deployment
- **Estratégias:** Canary ou Blue/Green para workloads críticos.
- **Rollback:** Deve ser automatizado via métricas de erro.
- **Security Check:** Incluir `tfsec`, `terrascan` ou `checkov`.
- **Policy as Code:** OPA ou Sentinel se aplicável.

## 4. Platform Engineering & Toil Reduction
- **IDP (Internal Developer Platform):** Propor plataformas de autosserviço onde aplicável.
- **Golden Paths:** Criar templates reutilizáveis para garantir padrões de segurança e confiabilidade desde o Início.
- **Redução de Toil:** Identificar tarefas manuais repetitivas e propor automação via runbooks ou scripts. Medir a redução de % de Toil.
