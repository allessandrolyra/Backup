# Analise das Calculadoras Azure v2 — Projeto Atento ASR Cloud

> **Data**: 14 de Abril de 2026  
> **Fonte**: 4 exportacoes da Azure Pricing Calculator (v2 corrigida)  
> **Moeda base**: USD (Dolar americano)  
> **Taxa de conversao referencia**: USD 1.00 = BRL 5.80  
> **Versao**: v2.0 — Calculadoras revisadas com correcoes  

---

## 1. Resumo Executivo

Todas as 4 calculadoras estao agora **consistentes com a arquitetura do projeto Atento**.

| # | Cenario | Total USD/mes | Total BRL/mes | Status |
|---|---------|---------------|---------------|--------|
| 1 | MVP — 10 chamadas/min | **$1,712.19** | **R$ 9,931** | VALIDO |
| 2 | 100 chamadas/min | **$6,061.19** | **R$ 35,155** | VALIDO |
| 3 | 1.000 chamadas/min | **$48,283.49** | **R$ 280,044** | VALIDO |
| 4 | 5.000 chamadas/min | **$227,663.62** | **R$ 1,320,449** | VALIDO |

### Correcoes aplicadas (vs versao anterior)

- **Speech Hours corrigidas**: 1.000/min: 8,000h -> 44,000h | 5.000/min: 20,000h -> 220,000h | 100/min: 4,000h -> 4,400h
- **SKUs MVP atualizados**: App Service Basic B2 -> Premium V3 P1V3 | APIM Basic -> Standard | Redis Basic -> Standard
- **Reserved Instances (AKS)**: Todos os cenarios com AKS usam Reserved 3 anos (economia ~55%)

---

## 2. Detalhamento por Cenario

### 2.1 Cenario 10/min (MVP) — $1,712.19/mes

| Servico | SKU / Tier | USD/mes | % |
|---------|-----------|---------|---|
| VPN Gateway | VpnGw1AZ, 100 GB transfer | $156.95 | 9% |
| Speech Services STT | S0 — 440h audio + 1 Custom endpoint | $463.65 | 27% |
| App Service | Premium V3 P1V3 (2 vCPU, 8GB), Linux | $162.06 | 9% |
| API Management | Standard — 1 unidade | $686.71 | 40% |
| Redis Cache | Standard C1 (1 GB) | $100.74 | 6% |
| Azure Monitor + App Insights | ~0.4 GB/dia logs | $128.90 | 8% |
| Key Vault | Standard | $13.18 | 1% |
| **TOTAL** | | **$1,712.19** | **100%** |

### 2.2 Cenario 100/min — $6,061.19/mes

| Servico | SKU / Tier | USD/mes | % |
|---------|-----------|---------|---|
| VPN Gateway | VpnGw2AZ, 1.2 TB transfer | $458.45 | 8% |
| Speech Services STT | S0 — 4,400h audio + 1 Custom endpoint | $4,423.65 | 73% |
| AKS | 1 cluster, 2x D4as v4, Reserved 3yr | $249.56 | 4% |
| API Management | Standard — 1 unidade | $686.71 | 11% |
| Redis Cache | Standard C1 (1 GB) | $100.74 | 2% |
| Azure Monitor + App Insights | ~0.4 GB/dia logs | $128.90 | 2% |
| Key Vault | Standard | $13.18 | <1% |
| **TOTAL** | | **$6,061.19** | **100%** |

### 2.3 Cenario 1.000/min — $48,283.49/mes

| Servico | SKU / Tier | USD/mes | % |
|---------|-----------|---------|---|
| VPN Gateway | VpnGw3AZ, 3 TB transfer | $1,153.65 | 2% |
| Speech Services STT | S0 — 44,000h audio + 1 Custom endpoint | $44,023.65 | 91% |
| AKS | 2 clusters, 4x D8as v4, Reserved 3yr | $961.25 | 2% |
| API Management | Standard — 2 unidades | $1,373.42 | 3% |
| Redis Cache | Standard C2 x 2 | $327.04 | 1% |
| Azure Monitor + App Insights | ~4 GB/dia logs | $431.30 | 1% |
| Key Vault | Standard | $13.18 | <1% |
| **TOTAL** | | **$48,283.49** | **100%** |

### 2.4 Cenario 5.000/min — $227,663.62/mes

| Servico | SKU / Tier | USD/mes | % |
|---------|-----------|---------|---|
| VPN Gateway | VpnGw4AZ, 3 TB transfer | $1,774.15 | 1% |
| Speech Services STT | S0 — 220,000h audio + 1 Custom endpoint | $220,023.65 | 97% |
| AKS | 3 clusters, 8x D8as v4, Reserved 3yr | $1,849.50 | 1% |
| API Management | Standard — 4 unidades | $2,746.84 | 1% |
| Redis Cache | Standard C3 x 2 | $657.00 | <1% |
| Azure Monitor + App Insights | ~6 GB/dia logs | $599.30 | <1% |
| Key Vault | Standard | $13.18 | <1% |
| **TOTAL** | | **$227,663.62** | **100%** |

---

## 3. Validacao das Horas de Speech

| Cenario | Chamadas/mes | Horas esperadas @10s | Horas na calculadora | Status |
|---------|-------------|---------------------|---------------------|--------|
| 10/min | 158,400 | 440h | 440h | CORRETO |
| 100/min | 1,584,000 | 4,400h | 4,400h | CORRETO |
| 1.000/min | 15,840,000 | 44,000h | 44,000h | CORRETO |
| 5.000/min | 79,200,000 | 220,000h | 220,000h | CORRETO |

---

## 4. Conformidade com a Arquitetura

| Requisito | 10/min | 100/min | 1.000/min | 5.000/min |
|-----------|--------|---------|-----------|-----------|
| VNet Integration | P1V3 | AKS | AKS | AKS |
| Private Endpoints | Suportado | Suportado | Suportado | Suportado |
| APIM c/ VNet | Standard | Standard | Standard | Standard |
| Redis c/ SLA | Standard | Standard | Standard | Standard |
| Zone-Redundant VPN | Gw1AZ | Gw2AZ | Gw3AZ | Gw4AZ |
| Speech Hours Corretas | 440h | 4,400h | 44,000h | 220,000h |
| Reserved Instances | — | AKS 3yr | AKS 3yr | AKS 3yr |

### Itens pendentes (nao na calculadora)

| Item | Impacto | Cenarios | Prioridade |
|------|---------|----------|------------|
| Private Endpoints (4 PEs) | $40-100/mes | Todos | Incluir |
| Bandwidth outbound | $0 a $200+ | 1.000/min, 5.000/min | Incluir |
| DDoS Protection | ~$2,944/mes | Somente 5.000/min | Avaliar |

---

## 5. Comparativo: Calculadora v1 vs v2 vs Estimativa Original

| Cenario | Estimativa Original | Calc v1 (erros) | Calc v2 (corrigida) | Desvio v2 vs Original |
|---------|--------------------|-----------------|--------------------|----------------------|
| 10/min | R$ 8,370 | R$ 5,857 | **R$ 9,931** | +19% |
| 100/min | R$ 33,150 | R$ 34,100 | **R$ 35,155** | +6% |
| 1.000/min | R$ 267,050 | R$ 77,712 | **R$ 280,044** | +5% |
| 5.000/min | — | R$ 173,385 | **R$ 1,320,449** | Novo cenario |

---

## 6. TCO — 12 Meses

| Metrica | 10/min | 100/min | 1.000/min | 5.000/min |
|---------|--------|---------|-----------|-----------|
| Mensal USD | $1,712 | $6,061 | $48,283 | $227,664 |
| Mensal BRL | R$ 9,931 | R$ 35,155 | R$ 280,044 | R$ 1,320,449 |
| **Anual USD** | **$20,546** | **$72,734** | **$579,402** | **$2,731,963** |
| **Anual BRL** | **R$ 119,169** | **R$ 421,859** | **R$ 3,360,530** | **R$ 15,845,387** |
| Custo/chamada | $0.0108 | $0.0038 | $0.0030 | $0.0029 |
| Custo/chamada BRL | R$ 0,063 | R$ 0,022 | R$ 0,018 | R$ 0,017 |

---

## 7. Economia com Reserved Instances (AKS)

| Cenario | Pay-as-you-go | Reserved 3yr | Economia mensal | Economia 3 anos |
|---------|--------------|-------------|----------------|----------------|
| 100/min | $528 | $250 | $279 (53%) | $10,028 |
| 1.000/min | $2,076 | $961 | $1,115 (54%) | $40,151 |
| 5.000/min | $4,080 | $1,850 | $2,230 (55%) | $80,290 |

---

## 8. Veredito

- **10/min (MVP)**: VALIDO — SKUs adequados, VNet suportada, custo razoavel
- **100/min**: VALIDO — Speech corrigido, AKS Reserved, bem alinhado
- **1.000/min**: VALIDO — Correcao critica de 8.000h->44.000h aplicada, confirma estimativa original
- **5.000/min**: VALIDO com ressalvas — Exige EA ou alternativa self-hosted para viabilidade financeira

---

## 9. Recomendacoes

1. **Confirmar volume real** com a Atento (dados historicos de chamadas/min)
2. **Validar quota Speech** em Brazil South para cenarios 1.000+ (167-833 sessoes concorrentes)
3. **Incluir Private Endpoints e Bandwidth** na estimativa final (~$50-300/mes)
4. **Negociar Enterprise Agreement** para Speech Services (70-97% do custo)
5. **Avaliar Whisper self-hosted** para cenarios 1.000+/min
6. **Iniciar com pay-as-you-go** no MVP, Reserved apos validar volume

### Cenario recomendado para proposta

| Fase | Cenario | Custo Azure | Periodo | Objetivo |
|------|---------|-------------|---------|----------|
| PoC | 10/min | $1,712/mes | 2-3 meses | Validar integracao Avaya + ASR |
| Producao | 100/min | $6,061/mes | 6-12 meses | Volume inicial real |
| Escala | 1.000/min | $48,283/mes | Sob demanda | Expansao conforme crescimento |

---

> **Squad MEQ — Foursys** | v2.0 — 14 Abril 2026 | Confidencial
