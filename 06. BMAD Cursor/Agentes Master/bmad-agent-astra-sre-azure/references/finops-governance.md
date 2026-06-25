# Azure Governance, CAF & FinOps

Cloud Adoption Framework (CAF), governança enterprise e eficiência financeira.

## 1. Cloud Adoption Framework (CAF)
- **Management Groups:** Organização hierárquica (Prod, Non-Prod, Sandbox, Decommissioned).
- **Subscriptions:** Separação por ambiente e workload (isolation boundary).
- **Landing Zones:** Hub-spoke networking, Shared Services, baseline security.
- **ALZ (Azure Landing Zone):** Terraform/Bicep modules da Microsoft para bootstrap.

## 2. Azure Policy (Policy as Code)
- **Deny Policies:** Restrição de regiões, SKUs proibidas, public access deny.
- **Audit Policies:** Detecção de recursos non-compliant sem bloquear.
- **DeployIfNotExists:** Auto-remediação (ex: habilitar diagnostic settings automaticamente).
- **Policy Sets (Initiatives):** Agrupamento lógico (Security Baseline, CIS, NIST).
- **Exemptions:** Exceções documentadas e com data de expiração.

## 3. RBAC & Identity Governance
- **Least Privilege:** Custom Roles quando built-in é amplo demais.
- **PIM:** Just-in-time activation para roles sensíveis.
- **Managed Identity:** Eliminar credentials — System-assigned para recursos únicos, User-assigned para compartilhados.
- **Service Principals:** Apenas quando Managed Identity não é possível (ex: ferramentas externas).

## 4. Tagging (Obrigatório)
Tags mínimas para governança e FinOps:
- `CostCenter` — Centro de custo para showback/chargeback.
- `Environment` — dev, staging, prod.
- `Application` — Nome do sistema/aplicação.
- `Owner` — Responsável técnico.
- `ManagedBy` — terraform, bicep, manual.
- `CreatedDate` — Data de criação para lifecycle management.

## 5. FinOps
- **Rightsizing:** Análise periódica de VMs/AKS com Azure Advisor.
- **Schedules:** Auto-shutdown de recursos Non-Prod fora do horário.
- **Reserved Instances / Savings Plans:** Workloads estáveis com commitment 1-3 anos.
- **Spot Instances:** Batch processing e workloads tolerantes a interrupção.
- **Cost Management:** Alertas de budget e detecção de anomalias.
- **Showback/Chargeback:** Relatórios por CostCenter tag para stakeholders.
- **FinOps KPIs:** Cost per transaction, unit economics, waste %.

## 6. Resource Locks & Lifecycle
- **CanNotDelete:** Recursos críticos de produção.
- **ReadOnly:** Infraestrutura que não deve ser alterada manualmente.
- **Resource Groups:** Organizar por lifecycle (deploy e delete juntos).
- **Decommission Process:** Tag → Schedule → Backup → Delete.
