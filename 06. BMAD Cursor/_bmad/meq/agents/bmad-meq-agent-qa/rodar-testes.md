---
name: rodar-testes
description: Guia execução de testes
menu-code: RT
---

# Rodar Testes

Guie a execução de testes e análise de resultados.

## Processo

1. **Identifique o que rodar:**
   - Suite completa
   - Testes de uma feature
   - Testes específicos (por nome ou tag)

2. **Comandos típicos:**
   - npm test / yarn test
   - pytest / jest / vitest
   - Playwright / Cypress para E2E

3. **Análise de resultados:**
   - Falhas — qual teste? qual assertion?
   - Flaky — teste instável? investigar
   - Tempo — suite lenta? considerar paralelização

4. **Regras:**
   - Nunca dar por pronto com testes falhando
   - Corrigir ou marcar como skip com motivo
   - Documentar falhas para o Felipe corrigir

5. **Output** — Resuma: passou/falhou, quantos, tempo. Sugira salvar (SM).

## Regras

- Testes passam 100% ou não está pronto
- Nunca mentir sobre testes — devem existir e passar
- Rodar suite após cada mudança significativa
