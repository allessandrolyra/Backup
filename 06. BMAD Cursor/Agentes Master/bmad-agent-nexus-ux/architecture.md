---
name: architecture
description: Decisões de arquitetura frontend
menu-code: AR
---

**Language:** Use `{communication_language}` for all output.

# Architecture

Tome decisões de arquitetura frontend com trade-offs explícitos.

## Processo

1. **Entenda o contexto** — Escala, requisitos, stack atual
2. **Carregue** `references/frontend-guidelines.md` para guidelines de arquitetura
3. **Apresente 2 opções** (Critical Thinking):
   - Trade-offs em Usabilidade, Performance e Complexidade
4. **Recomende 1 default** com justificativa
5. **Se aprovado, implemente** a estrutura base
6. **Responda no formato** — `references/standard-output.md`

## Temas Comuns
- SSR vs CSR vs ISR vs SSG
- State management (local vs server-state vs global)
- Mono-repo vs multi-repo
- Micro-frontends vs monolith
- Component composition patterns
- Data fetching strategy

## Entregáveis
- Decisão documentada com trade-offs
- Estrutura de diretórios proposta
- IaC/config skeleton (se aplicável)
