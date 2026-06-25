---
name: arquitetura-design
description: Design de arquitetura Azure com WAF e trade-offs
menu-code: AD
---

**Language:** Use `{communication_language}` for all output.

# Arquitetura & Design

Guie o usuário no design de arquitetura Azure seguindo o Well-Architected Framework.

## Processo

1. **Entenda o contexto** — Qual o workload? Requisitos de escala, latência, compliance?
2. **Carregue o Ledger** — Se existe projeto ativo, leia o contexto atual
3. **Aplique WAF Checklist** — Revise contra os 5 pilares:
   - Reliability, Security, Cost Optimization, Operational Excellence, Performance Efficiency
4. **Apresente 2 opções** — Com trade-offs em Confiabilidade, Custo e Complexidade
5. **Carregue references conforme necessidade:**
   - Compute → `references/performance.md`
   - Rede → `references/networking.md`
   - Segurança → `references/security.md`
   - Resiliência → `references/azure-reliability.md`
6. **Responda no formato completo** — `references/standard-output.md`
7. **Sugira salvar decisões** no Ledger (SM)

## Entregáveis
- Diagrama descritivo da arquitetura (componentes e fluxos)
- Justificativa técnica com trade-offs documentados
- IaC skeleton (estrutura de módulos Terraform/Bicep)
- Composite SLA calculation
