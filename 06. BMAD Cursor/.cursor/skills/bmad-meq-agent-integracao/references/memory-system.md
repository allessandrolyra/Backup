# Memory System for Igor

**Memory location:** `_bmad/_memory/bmad-meq-agent-integracao-sidecar/`

## Core Principle

Só lembre do que importa. Condense decisões de integração ao essencial.

## File Structure

### `index.md` — Primary Source

**Load on activation.** Contains:
- Contratos de API definidos
- Integrações planejadas
- Decisões de autenticação e resiliência
- Próximos passos

### `access-boundaries.md` — Required

**Load on activation.** Structure:
```markdown
# Access Boundaries for Igor

## Read Access
- {project-root}/_bmad/meq/
- {project-root}/_bmad-output/
- {project-root}/docs/

## Write Access
- {project-root}/_bmad/_memory/bmad-meq-agent-integracao-sidecar/
- {project-root}/_bmad-output/meq/

## Deny Zones
- node_modules/
- .git/
```

### `patterns.md` — Learned Patterns

Convenções de integração, padrões de API, preferências do usuário.

### `chronology.md` — Timeline

Contratos definidos, integrações implementadas, evolução.

## Save Triggers

- Contratos de API definidos
- Decisões de autenticação ou resiliência
- Integrações planejadas
- Usuário solicita salvar (SM)
- Fim de sessão com trabalho relevante
