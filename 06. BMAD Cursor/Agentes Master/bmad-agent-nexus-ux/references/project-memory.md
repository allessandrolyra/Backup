# Project Memory Structure

## Location
`{project-root}/_bmad/memory/bmad-agent-nexus-ux-ledger/`

## index.md Structure

```markdown
# Nexus — Project Memory

## A. Projeto
- Nome, stack, design system, objetivo

## B. Design Decisions
- Decisões de UX/UI com data e justificativa
- Componentes criados/refatorados

## C. Padrões Adotados
- Convenções de naming, scaffolding, estados
- Tokens e variáveis customizadas

## D. Auditorias
- Resultados de auditorias anteriores
- Issues pendentes e resolvidas

## E. Tech Stack
- Framework, versão, dependências chave
- Build tool, test runner, linter config

## F. Pendências
- TODOs técnicos, debt, melhorias futuras
```

## Access Boundaries
- Read/Write: `{project-root}/_bmad/`
- Read-Only: source code in `{project-root}/` (para análise)
