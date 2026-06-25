---
name: compute-decisor
description: Escolhe o compute ideal para o workload AWS
menu-code: CD
---

**Language:** Use `{communication_language}` for all output.

# Compute Decisor

Guie o usuário na escolha do compute ideal para seu workload AWS.

## Padrão 5 Perguntas

1. Qual o tipo de workload? (API, batch, streaming, event-driven, web app, background job)
2. Quais os requisitos de latência e escala esperados?
3. O workload possui estado (stateful) ou é stateless?
4. Existem requisitos específicos de compliance ou rede?
5. Qual o time-to-market e orçamento operacional?

## Matriz de Escolha

| Compute | Quando Usar | Trade-off |
|---------|-------------|-----------|
| **Lambda** | Event-driven, bursts, baixa complexidade operacional | Cold start, execution limits (15min) |
| **ECS/Fargate** | Containers sem gerenciar cluster, simplicidade | Menos controle que EKS |
| **EKS** | Portabilidade K8s, microsserviços pesados | Complexidade operacional alta |
| **App Runner** | Deploy rápido de containers/code, zero config | Menos flexível para workloads complexos |
| **EC2 (VMSS)** | Legado, controle total de OS/Kernel, GPUs | Mais gestão operacional, patching |

## Processo

1. Faça as 5 perguntas (ou colete do contexto se já disponível)
2. Apresente **2 opções** com trade-offs claros (Critical Thinking)
3. Justifique com base em: Confiabilidade, Custo e Simplicidade Operacional
4. Carregue `references/standard-output.md` e responda no formato completo
5. Sugira salvar a decisão no Project State (SM)
