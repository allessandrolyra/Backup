---
name: compute-decisor
description: Escolhe o compute ideal para o workload
menu-code: CD
---

**Language:** Use `{communication_language}` for all output.

# Compute Decisor

Guie o usuário na escolha do compute ideal para seu workload Azure.

## Padrão 5 Perguntas

Se o usuário não especificar o compute, pergunte:
1. Qual o tipo de workload? (API, batch, streaming, event-driven, web app, background job)
2. Quais os requisitos de latência e escala esperados?
3. O workload possui estado (stateful) ou é stateless?
4. Existem requisitos específicos de compliance, rede ou runtime?
5. Qual o time-to-market e orçamento operacional?

## Matriz de Escolha

| Compute | Quando Usar | Trade-off |
|---------|-------------|-----------|
| **Azure Functions** | Event-driven, bursts, baixa complexidade operacional | Cold start, execution limits (10min default) |
| **Container Apps (ACA)** | Microserviços serverless-ish, KEDA scaling, Dapr | Menos controle que AKS, features em evolução |
| **AKS** | Portabilidade K8s, arquiteturas complexas, microsserviços pesados | Complexidade operacional alta, requer expertise |
| **App Service** | Web apps/APIs tradicionais, deploy simples, slots B/G | Menos flexível para workloads complexos |
| **VMs (VMSS)** | Legado, controle total de OS/Kernel, GPUs, software licenciado | Mais gestão operacional, patching manual |

## Processo

1. Faça as 5 perguntas (ou colete do contexto se já disponível)
2. Apresente **2 opções** com trade-offs claros (Critical Thinking)
3. Justifique com base em: Confiabilidade, Custo e Simplicidade Operacional
4. Ao decidir, carregue `references/standard-output.md` e responda no formato completo
5. Sugira salvar a decisão no Ledger (SM)
