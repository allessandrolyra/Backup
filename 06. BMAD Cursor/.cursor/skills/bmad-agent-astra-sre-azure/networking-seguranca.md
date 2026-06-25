---
name: networking-seguranca
description: VNet design, Private Endpoints, NSG e segurança
menu-code: NS
---

**Language:** Use `{communication_language}` for all output.

# Networking & Segurança

Projete a topologia de rede e segurança do perímetro.

## Processo

1. **Entenda o escopo** — Greenfield ou brownfield? On-premises? Multi-região?
2. **Carregue** `references/networking.md` para topologia e padrões
3. **Carregue** `references/security.md` para segurança e identidade
4. **Defina topologia:**
   - Hub-Spoke (padrão CAF) ou Virtual WAN
   - CIDR planning sem overlap
   - Subnets por tier (web/app/data) e workload
5. **Configure conectividade:**
   - Private Endpoints para todo PaaS (Zero Trust)
   - VNet Integration para App Service/Functions
   - VPN Gateway ou ExpressRoute para hybrid
6. **Configure segurança:**
   - NSG com deny-all inbound como baseline
   - Azure Firewall centralizado no hub
   - Front Door + WAF para workloads web
   - DDoS Protection Standard para exposição pública
7. **Responda no formato completo** — `references/standard-output.md`

## Entregáveis
- Diagrama de rede (VNets, Subnets, peerings)
- CIDR allocation table
- IaC para VNet, Subnets, NSG, Private Endpoints
- NSG rules documentadas
