# Azure Security & Identity

Base de conhecimento para segurança, identidade e proteção de workloads Azure.

## 1. Identidade & Acesso (IAM)
- **Managed Identity:** Sempre preferir System-assigned ou User-assigned sobre secrets.
- **RBAC:** Least privilege com Custom Roles quando built-in é amplo demais.
- **Conditional Access:** MFA e políticas baseadas em risco para admin.
- **PIM (Privileged Identity Management):** Just-in-time access para roles elevados.

## 2. Secrets & Chaves
- **Azure Key Vault:** Centralizar secrets, certificados e chaves de criptografia.
- **Referências do Key Vault:** App Service, Functions e AKS leem direto do Key Vault.
- **Rotation:** Rotação automática de secrets com Event Grid triggers.
- **Nunca:** Hardcode de connection strings, access keys ou passwords em código ou pipelines.

## 3. Rede & Perímetro
- **Private Endpoints:** Acesso privado para PaaS (SQL, Storage, Key Vault, ACR).
- **NSG (Network Security Groups):** Deny-all default, allow explícito por porta/IP.
- **Azure Firewall / Front Door WAF:** Proteção L7 contra OWASP Top 10.
- **Service Endpoints vs Private Link:** Private Link preferível (tráfego fora da VNet pública).

## 4. Proteção de Dados
- **Encryption at Rest:** Padrão com Microsoft-managed keys; BYOK para compliance.
- **Encryption in Transit:** TLS 1.2+ obrigatório em todos endpoints.
- **Azure Disk Encryption / SSE:** VMs e discos gerenciados.
- **Soft Delete + Purge Protection:** Key Vault e Storage para proteção contra exclusão.

## 5. Detecção & Resposta
- **Microsoft Defender for Cloud:** Secure Score, recomendações e proteção de workloads.
- **Defender for Containers/SQL/Storage:** Proteção runtime por tipo de recurso.
- **Azure Sentinel (SIEM):** Análise de ameaças e automação de resposta.
- **Activity Log + Diagnostic Settings:** Auditoria completa de operações.

## 6. Compliance & Policy
- **Azure Policy:** Deny, Audit, DeployIfNotExists para enforcement automático.
- **Regulatory Compliance:** Dashboards para ISO 27001, SOC 2, LGPD, PCI-DSS.
- **Resource Locks:** CanNotDelete em recursos críticos de produção.
