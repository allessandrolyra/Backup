# Memory System for Quinn

**Memory location:** `_bmad/_memory/bmad-meq-agent-qa-sidecar/`

## Core Principle

Só lembre do que importa. Condense plano de testes e cobertura ao essencial.

## File Structure

### `index.md` — Primary Source

**Load on activation.** Contains:
- Plano de testes e cenários
- Cobertura atual
- Gaps identificados
- Próximos passos

### `access-boundaries.md` — Required

**Load on activation.** Structure:
```markdown
# Access Boundaries for Quinn

## Read Access
- {project-root}/_bmad/meq/
- {project-root}/_bmad-output/
- {project-root}/docs/
- {project-root}/src/
- {project-root}/tests/

## Write Access
- {project-root}/_bmad/_memory/bmad-meq-agent-qa-sidecar/
- {project-root}/_bmad-output/meq/
- {project-root}/tests/

## Deny Zones
- node_modules/
- .git/
```

### `patterns.md` — Learned Patterns

Convenções de teste, padrões do projeto, preferências do usuário.

### `chronology.md` — Timeline

Testes criados, cobertura evoluída, bugs encontrados.

## Save Triggers

- Plano de testes definido
- Cobertura revisada
- Gaps identificados
- Usuário solicita salvar (SM)
- Fim de sessão com trabalho relevante
