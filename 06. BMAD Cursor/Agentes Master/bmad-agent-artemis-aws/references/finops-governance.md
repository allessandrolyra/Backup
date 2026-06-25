# FinOps & Governance

Controle de custos e conformidade.

## 1. FinOps & Trade-offs
- **Tagging:** Obrigatório (App, Env, Team, CostCenter).
- **Showback:** Sempre reportar custo estimado na proposta.
- **Rightsizing:** Analisar CPU/Memória antes de escalar.
- **Savings:** Recomendar Savings Plans/Reserved Instances para workloads estáveis.
- **Custo vs Performance:** Analisar se o ganho de latência ou disponibilidade justifica o custo adicional.

## 2. Segurança, Governança & Multi-account
- **Multi-account:** Arquitetura baseada em AWS Organizations e Landing Zone.
- **SCPs (Service Control Policies):** Definir guardrails de segurança globais.
- **Ambientes:** Separação física e lógica (Blast Radius Control) entre Dev/Stg/Prd.
- **IAM:** Least Privilege e uso de IAM Roles.

## 3. Policy as Code & Compliance
- **Validação de Políticas:** Implementar Sentinel, OPA ou Conftest para IaC.
- **Compliance Automatizado:** Usar AWS Config Rules para auditoria contínua em tempo real.
- **Guardrails:** Impedir deploys que não atendam aos requisitos de segurança via pipeline.
