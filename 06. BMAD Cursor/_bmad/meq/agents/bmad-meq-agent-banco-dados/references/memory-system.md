# Memory System for Diana

**Memory location:** `_bmad/_memory/bmad-meq-agent-banco-dados-sidecar/`

## Core Principle

Só lembre do que importa. Condense decisões de dados ao essencial.

## File Structure

### `index.md` — Primary Source

**Load on activation.** Contains:
- Modelagem e schemas definidos
- Decisões de índices e otimizações
- Migrations planejadas
- Próximos passos

### `access-boundaries.md` — Required

**Load on activation.** Structure:
```markdown
# Access Boundaries for Diana

## Read Access
- {project-root}/_bmad/meq/
- {project-root}/_bmad-output/
- {project-root}/docs/

## Write Access
- {project-root}/_bmad/_memory/bmad-meq-agent-banco-dados-sidecar/
- {project-root}/_bmad-output/meq/

## Deny Zones
- node_modules/
- .git/
```

### `patterns.md` — Learned Patterns

Convenções de modelagem, padrões de schema, preferências do usuário.

### `chronology.md` — Timeline

Decisões significativas, evolução do schema, migrations aplicadas.

## Save Triggers

- Decisões de modelagem ou schema
- Otimizações aplicadas
- Migrations planejadas
- Usuário solicita salvar (SM)
- Fim de sessão com trabalho relevante
