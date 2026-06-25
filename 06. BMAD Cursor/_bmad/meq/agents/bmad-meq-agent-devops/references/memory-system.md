# Memory System for Davi

**Memory location:** `_bmad/_memory/bmad-meq-agent-devops-sidecar/`

## Core Principle

Só lembre do que importa. Condense pipelines e decisões de infra ao essencial.

## File Structure

### `index.md` — Primary Source

**Load on activation.** Contains:
- Pipelines configurados
- Ambientes e variáveis
- Decisões de infra
- Próximos passos

### `access-boundaries.md` — Required

**Load on activation.** Structure:
```markdown
# Access Boundaries for Davi

## Read Access
- {project-root}/_bmad/meq/
- {project-root}/_bmad-output/
- {project-root}/docs/
- {project-root}/.github/
- {project-root}/.gitlab-ci.yml
- {project-root}/Dockerfile*

## Write Access
- {project-root}/_bmad/_memory/bmad-meq-agent-devops-sidecar/
- {project-root}/_bmad-output/meq/
- {project-root}/.github/
- {project-root}/.gitlab-ci.yml
- {project-root}/Dockerfile*

## Deny Zones
- node_modules/
- .git/
```

### `patterns.md` — Learned Patterns

Convenções de pipeline, ambientes, preferências do usuário.

### `chronology.md` — Timeline

Pipelines criados, deploys configurados, mudanças de infra.

## Save Triggers

- Pipeline configurado
- Ambientes definidos
- Decisões de infra
- Usuário solicita salvar (SM)
- Fim de sessão com trabalho relevante
