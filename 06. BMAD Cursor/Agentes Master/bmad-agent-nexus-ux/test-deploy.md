---
name: test-deploy
description: Configura testes e CI/CD frontend
menu-code: TD
---

**Language:** Use `{communication_language}` for all output.

# Test & Deploy

Configure testes e pipelines de CI/CD para frontend.

## Processo

1. **Entenda o contexto** — Stack, test runner existente, CI/CD atual
2. **Carregue** `references/frontend-guidelines.md` para estratégia de testes
3. **Configure testes:**
   - Unit: lógica pura, utilitários (Vitest/Jest)
   - Integration: componentes + fluxos (Testing Library)
   - E2E: smoke dos fluxos críticos (Playwright/Cypress)
4. **Configure CI/CD:** Build → Lint → Type-check → Test → Deploy
5. **Implemente** arquivos de configuração e testes exemplo
6. **Responda no formato Executor** — `references/standard-output.md`

## Entregáveis
- Configuração de test runner
- Testes exemplo
- Pipeline CI/CD (YAML)
