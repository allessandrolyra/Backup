---
name: networking-seguranca
description: VPC design, Security Groups, PrivateLink e segurança
menu-code: NS
---

**Language:** Use `{communication_language}` for all output.

# Networking & Segurança

Projete topologia de rede e segurança.

## Processo

1. **Entenda o escopo** — Greenfield ou brownfield? Multi-account? Hybrid?
2. **Defina topologia:** VPC com subnets públicas/privadas, Transit Gateway
3. **Configure segurança:** Security Groups, NACLs, PrivateLink, WAF
4. **DNS:** Route53 para zonas públicas e privadas
5. **Conectividade híbrida:** VPN ou Direct Connect
6. **Responda no formato completo** — `references/standard-output.md`

## Entregáveis
- Diagrama VPC (subnets, routing tables, NAT)
- CIDR allocation table
- IaC para VPC, SGs, PrivateLink
