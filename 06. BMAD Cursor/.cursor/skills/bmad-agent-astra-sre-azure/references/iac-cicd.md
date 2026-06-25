# Azure IaC & CI/CD Patterns

Estratégias de automação, Infrastructure as Code e entrega contínua.

## 1. Terraform (Padrão)
Estrutura sugerida:
- `/modules`: Componentes reaproveitáveis (network, compute, database, monitoring).
- `/envs`: Pastas `dev`, `stg`, `prd` para instanciar os módulos.
- Arquivos padrão: `versions.tf`, `providers.tf`, `main.tf`, `variables.tf`, `outputs.tf`.

### Boas Práticas:
- Backend remoto (Azure Storage Account + State Locking com Blob lease).
- Uso extensivo de `locals` para DRY.
- Validation blocks nas variáveis.
- Sempre rodar `terraform fmt`, `validate` e `plan` antes de `apply`.
- Naming convention seguindo padrões CAF (ex: `rg-app-prod-eastus`).

## 2. Bicep (Alternativa Nativa)
- Templates modulares com `module` keyword.
- Deployments com `scope`: Subscription ou Management Group para Landing Zones.
- Uso de Private Module Registry (Azure Container Registry) se aplicável.
- `what-if` deployment para preview de mudanças.

## 3. Security Scanning
- **tfsec:** Análise estática de Terraform para misconfigurations.
- **checkov:** Multi-framework (TF, ARM, Bicep) com Policy as Code.
- **terrascan:** Detecção de violações de compliance.
- **OPA/Rego:** Políticas customizadas para validação de IaC.

## 4. CI/CD Pipelines
### Azure DevOps (ADO):
- YAML Pipelines (Multi-stage): Build → Validate → Plan → Apply.
- Environments com Approval Gates para produção.
- Variáveis em Variable Groups integrados com Key Vault.
- Service Connections com Managed Identity (Workload Identity Federation).

### GitHub Actions (GHA):
- Workflows com Matrix builds para multi-env.
- Deployment Environments com required reviewers.
- OIDC para autenticação segura no Azure (sem secrets).
- Composite Actions para passos reutilizáveis.

## 5. Deployment Strategies
- **Blue/Green:** Deployment slots em App Service.
- **Canary:** Traffic splitting com Front Door ou App Service slots.
- **Rolling:** AKS rolling update com maxSurge/maxUnavailable.
- **Rollback:** Automatizado via métricas de erro — rollback se error rate > threshold.

## 6. Platform Engineering
- **Golden Paths:** Templates reutilizáveis para AKS, App Service, SQL e Rede.
- **Self-service:** Autonomia do dev via IaC padronizado e módulos validados.
- **IDP:** Suporte a integração com Internal Developer Platforms.
- **Toil Reduction:** Identificar tarefas manuais e propor automação. Medir % de redução.
