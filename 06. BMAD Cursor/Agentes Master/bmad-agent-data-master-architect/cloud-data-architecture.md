---
name: cloud-data-architecture
description: Cloud Data Architecture — Azure, AWS, Fabric, Synapse, Redshift, multi-cloud
menu-code: CA
---

**Language:** Use `{communication_language}` for all output.

# Cloud Data Architecture

Projete arquiteturas de plataforma de dados em cloud (Azure, AWS, multi-cloud) com foco em escalabilidade, segurança e custo-efetividade.

## Escopo

- **Azure:** Fabric, Synapse, ADF, Azure SQL, Storage Account, Event Hubs, Purview
- **AWS:** Redshift, Glue, Athena, Lake Formation, EMR, S3, Kinesis, DataZone
- **Multi-cloud:** Databricks (Azure + AWS), Snowflake (multi-cloud), Iceberg (portable)
- **Networking:** VNet/VPC, Private Endpoints, Service Endpoints, VPN, ExpressRoute/Direct Connect
- **Identity:** Entra ID, AWS IAM, federated access, service principals, managed identities

## Processo

Ao receber um pedido de cloud data architecture:

### NÍVEL 1 — Arquitetura

1. **Requisitos** — Workloads, latência, volume, compliance, multi-region
2. **Cloud selection:**

| Critério | Azure | AWS | Multi-cloud |
|---|---|---|---|
| Ecossistema Microsoft forte | Fabric + Power BI | - | Databricks/Snowflake |
| Big Data / ML first | Databricks on Azure | EMR + SageMaker | Databricks |
| Data Sharing | Fabric/Purview | Clean Rooms | Snowflake |
| Cost-sensitive | Fabric capacity | Serverless (Athena/Glue) | Snowflake credits |

3. **Landing Zone** — Resource groups, subscriptions, networking, tagging
4. **Data flow** — Ingestão → Storage → Processing → Serving → Consumption

### NÍVEL 2 — Configuração

1. **Recursos** — SKUs, tiers, regions, HA configuration
2. **Networking** — VNet/VPC peering, private endpoints, DNS
3. **Identity** — Managed identity, RBAC, least privilege
4. **Encryption** — At rest (CMK), in transit (TLS), column-level

### NÍVEL 3 — Automação

1. **IaC** — Terraform ou Bicep para toda infraestrutura
2. **CI/CD** — Pipelines de deploy para recursos e dados
3. **Policy as Code** — Azure Policy, AWS Config, guardrails

### NÍVEL 4 — Operação

1. **Monitoramento** — Azure Monitor / CloudWatch / Datadog
2. **Cost management** — Budgets, alertas, rightsizing
3. **Disaster Recovery** — RPO/RTO, replicação cross-region
4. **Compliance** — Audit logs, data residency, retention policies

## Progressão

- **NÍVEL 1 → 2:** Após confirmar cloud selection e arquitetura com o usuário, prosseguir para configuração
- **NÍVEL 2 → 3:** Após o usuário aprovar configurações de recursos, prosseguir para automação IaC
- **NÍVEL 3 → 4:** Após entregar IaC e policy as code, perguntar se deseja configurar operação
- **A qualquer momento:** O usuário pode solicitar apenas um nível específico — respeitar o escopo pedido

## Saída

Sempre carregar `references/standard-output.md` e seguir o formato padrão de resposta.

Incluir:
- Diagrama de arquitetura cloud (mermaid)
- IaC (Terraform/Bicep) para componentes principais
- Configuração de networking e segurança
- Estimativa qualitativa de custos
