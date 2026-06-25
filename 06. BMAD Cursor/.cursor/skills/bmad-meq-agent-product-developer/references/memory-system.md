# Memory System for Paula

**Memory location:** `_bmad/_memory/bmad-meq-agent-product-developer-sidecar/`

## Core Principle

Só lembre do que importa. Condense decisões de produto ao essencial.

## File Structure

### `index.md` — Primary Source

**Load on activation.** Contains:
- Produto/projeto atual
- Escopo e requisitos definidos
- Backlog e prioridades
- Próximos passos

### `access-boundaries.md` — Required

**Load on activation.** Structure:
```markdown
# Access Boundaries for Paula

## Read Access
- {project-root}/_bmad/meq/
- {project-root}/_bmad-output/
- {project-root}/docs/

## Write Access
- {project-root}/_bmad/_memory/bmad-meq-agent-product-developer-sidecar/
- {project-root}/_bmad-output/meq/

## Deny Zones
- node_modules/
- .git/
```

### `patterns.md` — Learned Patterns

Preferências do usuário, convenções de produto, padrões recorrentes.

### `chronology.md` — Timeline

Decisões significativas, mudanças de escopo, evolução do backlog.

## Save Triggers

- Decisões de escopo ou prioridade
- Definição de MVP
- Mudança no backlog
- Usuário solicita salvar (SM)
- Fim de sessão com trabalho relevante
