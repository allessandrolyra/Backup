# Azure Networking

Base de conhecimento para design de rede, conectividade e segurança de perímetro.

## 1. Topologia de Rede
- **Hub-Spoke:** Padrão CAF para enterprise. Hub centraliza firewall, VPN, DNS.
- **VNet Peering:** Conectividade entre spokes via hub (transit) ou direct.
- **CIDR Planning:** Planejar sem overlap entre ambientes e on-premises.
- **Subnets:** Separação por tier (web/app/data) e por workload.

## 2. Resolução DNS
- **Azure Private DNS Zones:** Resolução para Private Endpoints (privatelink.*.core.windows.net).
- **Custom DNS:** Conditional forwarders para integração com on-premises.
- **Azure DNS:** Zonas públicas para domínios externos.

## 3. Conectividade Híbrida
- **VPN Gateway:** Site-to-Site para conectividade on-premises.
- **ExpressRoute:** Conexão dedicada para latência previsível e alta bandwidth.
- **Virtual WAN:** Hub gerenciado para topologias complexas multi-região.

## 4. Balanceamento & Distribuição
- **Azure Front Door:** Global L7 load balancer + WAF + CDN + SSL offload.
- **Application Gateway:** Regional L7 com WAF, path routing, SSL termination.
- **Azure Load Balancer:** L4 para distribuição intra-região (Standard SKU sempre).
- **Traffic Manager:** DNS-based routing para failover cross-region.

## 5. Segurança de Rede
- **NSG:** Regras stateful por subnet e NIC. Deny-all inbound como baseline.
- **ASG (Application Security Groups):** Agrupamento lógico para regras simplificadas.
- **Azure Firewall:** Centralizado no hub, regras DNAT/Network/Application.
- **DDoS Protection:** Standard plan para workloads expostos à internet.

## 6. Private Connectivity (Zero Trust)
- **Private Endpoints:** Acesso privado para todo PaaS (SQL, Storage, ACR, Key Vault).
- **Service Endpoints:** Alternativa mais simples mas menos segura que Private Link.
- **VNet Integration:** App Service/Functions com acesso outbound via VNet.
- **AKS Private Cluster:** API server acessível apenas via rede privada.
