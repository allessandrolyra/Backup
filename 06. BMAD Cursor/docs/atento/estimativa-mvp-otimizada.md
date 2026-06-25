# Atento ASR Cloud — Estimativa MVP Otimizada

> **Data**: Maio 2026  
> **Objetivo**: Reduzir custo do cenário MVP (10 chamadas/min) substituindo componentes caros por alternativas mais baratas sem comprometer latência  
> **Moeda base**: USD | Taxa referência: USD 1.00 = BRL 5.80

---

## 1. Diagnóstico do Custo Atual (MVP 10/min)

| Serviço | SKU | USD/mês | % do Total | Problema |
|---------|-----|---------|------------|----------|
| **API Management** | Standard (classic) | $686.71 | **40%** | Tier sobredimensionado para MVP |
| Speech Services STT | S0 — 440h + Custom | $463.65 | 27% | Pay-per-use, não otimizável |
| App Service | Premium V3 P1V3 | $162.06 | 9% | Pode reduzir para P0V3 |
| VPN Gateway | VpnGw1AZ | $156.95 | 9% | Zone-Redundant desnecessário para MVP |
| Azure Monitor | ~0.4 GB/dia | $128.90 | 8% | Reduzível |
| Redis Cache | Standard C1 | $100.74 | 6% | Sobredimensionado para MVP |
| Key Vault | Standard | $13.18 | 1% | Já mínimo |
| **TOTAL** | | **$1,712.19** | **100%** | |

### Conclusão: APIM é 40% do custo e pode ser eliminado ou substituído no MVP.

---

## 2. Análise de Alternativas por Componente

### 2.1 API Management — O Grande Vilão do Custo

| Opção | USD/mês | VNet Integration | SLA | WebSocket | Latência | Viável? |
|-------|---------|-----------------|-----|-----------|----------|---------|
| Standard v2 | $700 | Sim (outbound) | 99.95% | Sim | < 5ms | Sim, mas caro |
| Basic v2 | $150 | **NÃO** | 99.95% | Sim | < 5ms | Risco: sem VNet |
| Consumption | ~$0.55* | **NÃO** | 99.95% | Não | **1-2s cold start** | **NÃO** — latência inaceitável |
| Developer | $48 | Sim | **SEM SLA** | Sim | < 5ms | Só dev/test |
| **Eliminar APIM** | **$0** | N/A | N/A | N/A | **0ms (direto)** | **SIM — recomendado** |

> \* Consumption: ~158.400 requests/mês × $0.042/10K = $0.67. Mas **não suporta WebSocket** e tem **cold starts de 1-2s** — inaceitável para voz real-time.

#### Recomendação: Eliminar APIM no MVP

**Justificativa:**
- Para 10 chamadas/min com um único backend, APIM agrega pouco valor
- As funções do APIM podem ser implementadas no próprio App Service:
  - **Auth**: Middleware de API Key validation (ASP.NET Core / Node.js)
  - **Rate Limiting**: Pacote `AspNetCoreRateLimit` ou middleware customizado
  - **Logging**: Application Insights SDK (já existe)
  - **Routing**: Não necessário — um único endpoint WebSocket
- **Economia: $687/mês (40% do total)**
- Quando crescer, reintroduzir APIM Standard v2 na Fase 2

**Impacto na latência: POSITIVO** — remove um hop intermediário (~5ms de melhoria)

---

### 2.2 Compute — App Service vs VM

| Opção | Specs | USD/mês | VNet Inbound | AutoScale | Managed | Latência | HA nativa |
|-------|-------|---------|--------------|-----------|---------|----------|-----------|
| App Service P1V3 (atual) | 2 vCPU, 8GB | $162* | Private Endpoint | Sim | Sim | < 1ms | Sim (multi-AZ) |
| **App Service P0V3** | 1 vCPU, 4GB | **$80*** | Private Endpoint | Sim | Sim | < 1ms | Sim (multi-AZ) |
| VM B2ms | 2 vCPU, 8GB | $76* | IP direto na VNet | Manual (VMSS) | Não | < 1ms | Não (precisa 2 VMs) |
| VM B2s | 2 vCPU, 4GB | $44* | IP direto na VNet | Manual (VMSS) | Não | < 1ms | Não (precisa 2 VMs) |
| VM B2als_v2 | 2 vCPU, 4GB | $38* | IP direto na VNet | Manual (VMSS) | Não | < 1ms | Não (precisa 2 VMs) |

> \* Preços estimados para Brazil South (premium ~30% sobre US East)

#### Análise de Latência (compute)

Para o caso de uso ASR:
- O processamento pesado é feito pelo **Azure Speech Services** (200-800ms)
- O App Service / VM apenas orquestra: recebe WebSocket → converte codec → chama Speech → valida → responde
- **Qualquer opção acima atende** — a latência de compute é < 5ms para todas

#### Recomendação: App Service P0V3

**Justificativa:**
- 1 vCPU / 4GB é suficiente para orquestrar 10 chamadas/min (~0.17 chamadas/segundo)
- Cada sessão WebSocket usa ~50MB RAM max → 4GB suporta ~80 sessões simultâneas (mais que suficiente)
- VNet Integration nativa + Private Endpoint para inbound
- Zero overhead operacional (vs VM que exige patching, backup, monitoramento de OS)
- AutoScale disponível se precisar
- **Economia vs P1V3: ~$82/mês**

#### Quando usar VM?
- Apenas se orçamento for absolutamente crítico E houver equipe para operar
- Uma única VM B2ms é mais barata ($76 vs $80), mas sem HA
- Para HA com VM, precisa de 2 VMs + Load Balancer → ~$160+ (mais caro que P0V3!)

---

### 2.3 VPN Gateway

| Opção | USD/mês | Bandwidth | Zone-Redundant | BGP | S2S Tunnels |
|-------|---------|-----------|----------------|-----|-------------|
| Basic | ~$27 | 100 Mbps | Não | Não | 10 |
| VpnGw1 | $138 | 650 Mbps | Não | Sim | 30 |
| **VpnGw1AZ** (atual) | $157 | 650 Mbps | **Sim** | Sim | 30 |

#### Recomendação: VpnGw1 (non-AZ) para MVP

- Zone-Redundancy não é crítica para PoC/MVP
- Se o gateway cair, há fallback para operador humano (arquitetura já prevê)
- **Economia: ~$19/mês** (pouco impacto, mas contribui)
- Na Fase 2, migrar para VpnGw1AZ ou VpnGw2AZ

**Impacto na latência: ZERO** — mesma performance, mesma região

---

### 2.4 Redis Cache

| Opção | USD/mês | Capacidade | SLA | Replicação |
|-------|---------|-----------|-----|-----------|
| Standard C1 (atual) | $100.74 | 1 GB | 99.9% | Sim |
| Basic C1 | $53 | 1 GB | Sem SLA | Não |
| **Basic C0** | **$16** | 250 MB | Sem SLA | Não |
| **Eliminar Redis** | **$0** | N/A | N/A | N/A |

#### Recomendação: Eliminar Redis OU Basic C0

**Opção A — Eliminar Redis ($0):**
- Sessões de chamada duram 10-30 segundos
- Para 10 chamadas/min, no máximo ~5 sessões simultâneas
- In-memory session state no App Service é suficiente
- Se instância reiniciar, chamadas ativas (< 5) falham com fallback para operador
- **Risco aceitável para MVP**

**Opção B — Basic C0 ($16):**
- Mantém cache externalizado (mais seguro)
- 250MB é suficiente para centenas de sessões simultâneas
- Sem SLA formal, mas uptime real é > 99.5%

**Impacto na latência: ZERO** — in-memory é até mais rápido que Redis

---

### 2.5 Observabilidade

| Opção | USD/mês | Retenção | Features |
|-------|---------|----------|----------|
| Full (atual) | $128.90 | 30 dias | App Insights + Log Analytics + Alerts |
| **Reduzido MVP** | **$50-70** | 30 dias | App Insights basic + alertas essenciais |

- Reduzir ingestão de logs para ~0.2 GB/dia
- Manter App Insights (essencial para monitorar latência ASR)
- Desligar alertas secundários, manter apenas: VPN down, latência > 2s, error rate > 5%

---

## 3. Estimativas MVP Otimizadas — 3 Cenários

### Cenário A: Ultra-MVP (PoC — custo mínimo absoluto)

| Serviço | SKU | USD/mês |
|---------|-----|---------|
| VPN Gateway | VpnGw1 (non-AZ) | $138.00 |
| App Service | **P0V3** (1 vCPU, 4GB) | $80.00 |
| API Management | **Eliminado** (middleware no app) | $0.00 |
| Speech Services STT | S0 — 440h + 1 Custom endpoint | $463.65 |
| Redis Cache | **Eliminado** (in-memory) | $0.00 |
| Azure Monitor | Reduzido (~0.2 GB/dia) | $60.00 |
| Key Vault | Standard | $13.18 |
| Private Endpoint (App Service) | 1 PE | $7.30 |
| Private Endpoint (Speech) | 1 PE | $7.30 |
| **TOTAL** | | **$769.43** |
| **TOTAL BRL** | | **R$ 4.463** |

| Métrica | Valor |
|---------|-------|
| Economia vs atual | **$942.76/mês (55%)** |
| Economia anual | **$11.313 / R$ 65.617** |
| Custo/chamada | $0.0049 (vs $0.0108 atual) |

---

### Cenário B: MVP Produção (equilíbrio custo × confiabilidade)

| Serviço | SKU | USD/mês |
|---------|-----|---------|
| VPN Gateway | VpnGw1AZ (zone-redundant) | $156.95 |
| App Service | **P0V3** (1 vCPU, 4GB) | $80.00 |
| API Management | **Eliminado** (middleware no app) | $0.00 |
| Speech Services STT | S0 — 440h + 1 Custom endpoint | $463.65 |
| Redis Cache | **Basic C0** (250MB) | $16.00 |
| Azure Monitor | Padrão (~0.4 GB/dia) | $100.00 |
| Key Vault | Standard | $13.18 |
| Private Endpoints | 3 PEs (App, Speech, Redis) | $21.90 |
| **TOTAL** | | **$851.68** |
| **TOTAL BRL** | | **R$ 4.940** |

| Métrica | Valor |
|---------|-------|
| Economia vs atual | **$860.51/mês (50%)** |
| Economia anual | **$10.326 / R$ 59.891** |
| Custo/chamada | $0.0054 |

---

### Cenário C: MVP com APIM Basic v2 (se APIM for mandatório)

| Serviço | SKU | USD/mês | Observação |
|---------|-----|---------|------------|
| VPN Gateway | VpnGw1 (non-AZ) | $138.00 | |
| App Service | **P0V3** (1 vCPU, 4GB) | $80.00 | |
| API Management | **Basic v2** | $150.01 | Sem VNet integration |
| Speech Services STT | S0 — 440h + 1 Custom endpoint | $463.65 | |
| Redis Cache | Basic C0 (250MB) | $16.00 | |
| Azure Monitor | Reduzido | $70.00 | |
| Key Vault | Standard | $13.18 | |
| Private Endpoints | 2 PEs (Speech, Redis) | $14.60 | |
| **TOTAL** | | **$945.44** |
| **TOTAL BRL** | | **R$ 5.483** |

| Métrica | Valor |
|---------|-------|
| Economia vs atual | **$766.75/mês (45%)** |
| Economia anual | **$9.201 / R$ 53.366** |

> **ALERTA**: APIM Basic v2 **não suporta VNet Integration**. O App Service precisaria expor endpoint público (com IP restriction via NSG) ou usar Private Link. Isso quebra o requisito ADR-006 (zero exposição pública). Use este cenário **apenas se APIM for mandatório pelo cliente** e aceitar relaxar o requisito de rede.

---

## 4. Comparativo Resumo

| Métrica | Atual | Cenário A | Cenário B | Cenário C |
|---------|-------|-----------|-----------|-----------|
| USD/mês | $1,712 | **$769** | **$852** | **$945** |
| BRL/mês | R$ 9.931 | **R$ 4.463** | **R$ 4.940** | **R$ 5.483** |
| Economia | — | 55% | 50% | 45% |
| APIM | Standard | Eliminado | Eliminado | Basic v2 |
| Compute | P1V3 | P0V3 | P0V3 | P0V3 |
| VPN | Gw1AZ | Gw1 | Gw1AZ | Gw1 |
| Redis | Std C1 | Eliminado | Basic C0 | Basic C0 |
| SLA esperado | ~99.9% | ~99.5% | ~99.7% | ~99.5% |
| Latência E2E | 300-900ms | **280-880ms** | **280-880ms** | 300-900ms |
| Prod-ready? | Sim | PoC only | **Sim** | Parcial |

---

## 5. Análise de Latência — Impacto das Mudanças

| Etapa | Atual | Cenário A/B (sem APIM) | Diferença |
|-------|-------|------------------------|-----------|
| VPN → Azure | 2-5ms | 2-5ms | = |
| APIM processing | 3-5ms | **0ms (eliminado)** | **-5ms** |
| App Service processing | < 10ms | < 10ms | = |
| Speech STT (streaming) | 200-800ms | 200-800ms | = |
| CNPJ Parse + Validate | < 5ms | < 5ms | = |
| Response return | 2-5ms | 2-5ms | = |
| **Total E2E** | **~300-900ms** | **~280-880ms** | **-20ms (melhor)** |

**Conclusão: Eliminar APIM MELHORA a latência** (um hop a menos no caminho do áudio).

A escolha entre P0V3 e P1V3 **não afeta latência** — o processamento é I/O-bound (Speech SDK), não CPU-bound.

---

## 6. Cenário 100/min — Substituindo AKS

A estimativa atual para 100/min usa AKS ($249.56 Reserved 3yr). Alternativas:

| Opção | USD/mês | Sessões simultâneas | AutoScale | Operacional |
|-------|---------|--------------------:|-----------|-------------|
| AKS (atual) | $249.56 | ~50-100 | HPA/KEDA | Médio |
| **App Service P2V3** | **$248** | ~60 | Nativo | **Baixo** |
| **App Service P1V3 × 2** | **$248** | ~80 | Nativo | **Baixo** |
| VM D4as_v4 × 2 | ~$280 | ~80 | VMSS | Alto |
| VM B4ms × 2 | ~$200 | ~60 | VMSS | Alto |

#### Recomendação para 100/min: App Service P2V3 ou P1V3 × 2 instâncias

- Custo similar ao AKS Reserved, mas **zero overhead de cluster Kubernetes**
- AutoScale nativo do App Service
- Sem necessidade de gerenciar node pools, helm charts, ingress controllers
- **Latência idêntica ao AKS** (mesma VNet, mesmo datapath)

### Estimativa 100/min Otimizada

| Serviço | SKU (otimizado) | USD/mês |
|---------|-----------------|---------|
| VPN Gateway | VpnGw2AZ | $458.45 |
| App Service | P1V3 × 2 instâncias | $248.00 |
| API Management | **Eliminado** (ou Basic v2 $150 se necessário) | $0.00 |
| Speech Services STT | S0 — 4,400h + Custom | $4,423.65 |
| Redis Cache | Standard C1 | $100.74 |
| Azure Monitor | Padrão | $128.90 |
| Key Vault | Standard | $13.18 |
| Private Endpoints | 4 PEs | $29.20 |
| **TOTAL** | | **$5,402.12** |
| **TOTAL BRL** | | **R$ 31.332** |

| vs Atual ($6,061) | Economia |
|--------------------|----------|
| Diferença | **$659/mês (11%)** |
| Anual | **$7.908 / R$ 45.867** |

> Nota: No cenário 100/min, Speech Services domina (82% do custo). A otimização de compute/APIM tem impacto relativo menor.

---

## 7. Recomendação Final

### Para proposta comercial ao cliente:

| Fase | Cenário | Custo Azure | Período | Arquitetura |
|------|---------|-------------|---------|-------------|
| **PoC** | 10/min — Cenário B | **$852/mês** | 2-3 meses | P0V3 + sem APIM + Basic Redis |
| **MVP Produção** | 10/min — Cenário B (scale up) | **$900-1.000/mês** | 3-6 meses | P1V3 + sem APIM + Standard Redis |
| **Crescimento** | 100/min | **$5.400/mês** | 6-12 meses | P1V3×2 + APIM Standard v2 |
| **Escala** | 1.000/min | $48.000/mês | On-demand | AKS + APIM Premium |

### ADRs Atualizadas para MVP

| ID | Decisão Original | Decisão MVP | Justificativa |
|----|-----------------|-------------|---------------|
| ADR-005 | App Service P2V3 → AKS | **App Service P0V3** | 1 vCPU suficiente para 10/min; scale up conforme demanda |
| ADR-NEW | APIM Standard | **Eliminar APIM** | Middleware no app para auth/rate-limit; reintroduzir em Fase 2 |
| ADR-002 | VPN Gateway Zone-Redundant | **VpnGw1 (non-AZ)** para PoC | Zone-Redundancy desnecessária para validação; upgrade posterior |
| ADR-NEW | Redis Standard C1 | **Redis Basic C0 ou in-memory** | Sessões curtas (10-30s); volume baixo (< 10 simultâneas) |

---

## 8. Riscos da Otimização

| # | Risco | Impacto | Mitigação |
|---|-------|---------|-----------|
| 1 | Sem APIM: falta de rate limiting centralizado | Baixo (volume é baixo no MVP) | Middleware no app + NSG para whitelist IP |
| 2 | Redis Basic sem SLA | Baixo (fallback para operador se cache falhar) | Upgrade para Standard C0 ($50) se necessário |
| 3 | VPN non-AZ: sem redundância de zona | Médio (se zona cair, VPN cai) | Aceitar para PoC; migrar para AZ em produção |
| 4 | P0V3 insuficiente sob carga inesperada | Baixo (autoscale ativado) | Monitorar CPU; scale up para P1V3 se > 70% |

---

> **Squad MEQ — Foursys** | v1.0 — Maio 2026 | Confidencial
