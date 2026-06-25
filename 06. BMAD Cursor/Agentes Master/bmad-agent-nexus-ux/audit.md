---
name: audit
description: Auditoria de UX, acessibilidade e performance
menu-code: AU
---

**Language:** Use `{communication_language}` for all output.

# Audit

Auditoria completa de UX, Acessibilidade (WCAG 2.2 AA) e Performance (Core Web Vitals).

## Processo

1. **Defina escopo** — Componente, página ou aplicação inteira?
2. **Carregue** `references/frontend-guidelines.md` para checklists
3. **Execute audit por dimensão:**
   - **UX**: Fluxos, estados, microcopy, feedback
   - **A11y**: Checklist WCAG 2.2 AA completo
   - **Performance**: Core Web Vitals (LCP, INP, CLS)
   - **Tech Debt**: Código legado, padrões inconsistentes
4. **Classifique findings** por severidade: Critical | Major | Minor
5. **Proponha fixes** para cada finding
6. **Implemente quick wins** diretamente (se modo Executor)
7. **Responda no formato** — `references/standard-output.md`

## Entregáveis
- Relatório de findings (tabela com severidade)
- Fixes implementados (quick wins)
- Plano para findings estruturais
