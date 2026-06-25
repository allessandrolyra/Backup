---
name: seguranca-dados
description: Segurança — IAM, encryption, compliance, redes, Private Endpoints
menu-code: SD
---

**Language:** Use `{communication_language}` for all output.

# Segurança de Dados

Projete e implante segurança para plataformas de dados: identity, access control, encryption, networking, compliance e auditoria.

## Escopo

- **Identity:** Entra ID, AWS IAM, service principals, managed identities, federated access
- **Access Control:** RBAC, ABAC, RLS, OLS, column masking, dynamic data masking
- **Encryption:** At rest (CMK/PMK), in transit (TLS), column-level, tokenization
- **Networking:** Private Endpoints, Service Endpoints, VNet integration, firewall rules, NSG
- **Compliance:** LGPD, GDPR, SOX, PCI-DSS, HIPAA, audit trails
- **Ferramentas:** Key Vault, AWS KMS, Defender for Cloud, GuardDuty, Purview, Lake Formation

## Processo

Ao receber um pedido de segurança:

### NÍVEL 1 — Assessment

1. **Inventário de dados sensíveis** — PII, PCI, PHI, dados financeiros
2. **Classificação** — Nível de sensibilidade por dataset
3. **Superfície de ataque** — Endpoints públicos, credenciais, acessos
4. **Compliance requirements** — Regulamentações aplicáveis

### NÍVEL 2 — Design

1. **Zero Trust para dados:**

| Princípio | Implementação |
|---|---|
| Least privilege | RBAC granular, just-in-time access |
| Verify explicitly | MFA, conditional access, token validation |
| Assume breach | Encryption, logging, segmentation |

2. **Modelo de acesso:**

| Camada | Controle |
|---|---|
| Network | Private Endpoints, VNet, firewall, NSG |
| Identity | Entra ID / IAM, MFA, service principals |
| Data | RLS, column masking, encryption |
| Application | API keys, OAuth, managed identity |
| Audit | Logging, monitoring, alerting |

### NÍVEL 3 — Implementação

1. **IAM** — Configuração de roles, groups, policies
2. **Networking** — Private Endpoints, DNS private zones, NSG rules
3. **Encryption** — Key Vault/KMS setup, CMK rotation
4. **Data masking** — Dynamic masking, RLS rules
5. **Audit** — Diagnostic settings, audit logs, retention

### NÍVEL 4 — Operação

1. **Monitoramento de segurança** — Defender, GuardDuty, SIEM
2. **Incident response** — Playbooks para violação de dados
3. **Compliance auditing** — Relatórios periódicos
4. **Key rotation** — Rotação automática de chaves e secrets
5. **Access reviews** — Revisão periódica de acessos

## Progressão

- **NÍVEL 1 → 2:** Após confirmar inventário de dados sensíveis e compliance requirements com o usuário, prosseguir para design
- **NÍVEL 2 → 3:** Após o usuário aprovar modelo de segurança, prosseguir para implementação
- **NÍVEL 3 → 4:** Após entregar IAM, networking e encryption, perguntar se deseja configurar operação contínua
- **A qualquer momento:** O usuário pode solicitar apenas um nível específico — respeitar o escopo pedido

## Saída

Sempre carregar `references/standard-output.md` e seguir o formato padrão de resposta.

Incluir:
- Assessment de segurança
- Configuração de IAM e networking
- IaC para segurança (Terraform/Bicep)
- Checklist de compliance
