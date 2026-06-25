---
name: scaffold-build
description: Cria componentes, páginas, layouts e features completas
menu-code: SB
---

**Language:** Use `{communication_language}` for all output.

# Scaffold & Build

Crie estruturas completas de componentes, páginas e features.

## Processo

1. **Detecte ambiente** — Load `references/environment-detection.md`
2. **Leia estrutura existente** — Identificar padrões de scaffolding do projeto
3. **Leia design system** — Tokens, componentes base, naming conventions
4. **Pergunte apenas se necessário** — Se o contexto for suficiente, implemente direto (Executor-First)
5. **Crie os arquivos** seguindo `references/frontend-guidelines.md` (scaffolding padrão)
6. **Garanta estados** — loading, empty, error, sucesso, retry
7. **Garanta A11y** — Checklist WCAG 2.2 AA obrigatório
8. **Valide** — Rode lint/typecheck se terminal disponível
9. **Responda no formato Executor** — `references/standard-output.md`

## Entregáveis
- Arquivos criados com código funcional
- Lista de arquivos criados/modificados
- Decisões tomadas (trade-offs)
- Validação (lint/types)
