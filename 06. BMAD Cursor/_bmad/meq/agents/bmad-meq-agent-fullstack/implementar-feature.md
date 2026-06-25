---
name: implementar-feature
description: Implementa feature ou mudança
menu-code: IF
---

# Implementar Feature

Implemente a feature ou mudança solicitada seguindo a arquitetura e padrões do projeto.

## Processo

1. **Entenda o pedido** — O que implementar?
   - **Feature nova** — Seguir spec e AC
   - **Bugfix** — Reproduzir, isolar causa, corrigir, testar
   - **Refactor** — Manter comportamento, melhorar estrutura
   - **Debug** — Identificar causa raiz, propor correção

2. **Consulte contexto:**
   - Arquitetura definida (Wagner) — stack, padrões, project-context
   - Escopo do produto (Paula) — requisitos, prioridades
   - Memória — o que já foi implementado
   - Código existente — reutilizar interfaces e padrões

3. **Especifique antes de codar:**
   - Quais arquivos serão alterados/criados?
   - Quais critérios de aceite?
   - Há testes a escrever?

4. **Implemente:**
   - Siga a arquitetura existente
   - Reutilize componentes/interfaces
   - Código limpo, testável
   - Testes passando

5. **Resuma** — Formato succinto: "AC-X implementado em `path/to/file`. Testes: OK."

6. **Memória** — Se progresso relevante, sugira salvar (SM).

## Regras

- Story Context e AC são fonte da verdade
- Não inventar — seguir spec e arquitetura
- Toda mudança mapeia a AC
- Testes 100% antes de dar por pronto
