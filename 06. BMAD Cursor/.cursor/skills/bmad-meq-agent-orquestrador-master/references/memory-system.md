# Memory System for Marco

**Memory location:** `_bmad/_memory/bmad-meq-agent-orquestrador-master-sidecar/`

## Core Principle

Só lembre do que importa. Condense decisões e contexto ao essencial.

## File Structure

### `index.md` — Primary Source

**Load on activation.** Contains:
- Projeto/tarefa atual da squad
- Decisões tomadas
- Estado do trabalho
- Próximos passos

### `access-boundaries.md` — Required

**Load on activation.** Structure:
```markdown
# Access Boundaries for Marco

## Read Access
- {project-root}/_bmad/meq/
- {project-root}/_bmad-output/
- {project-root}/docs/

## Write Access
- {project-root}/_bmad/_memory/bmad-meq-agent-orquestrador-master-sidecar/
- {project-root}/_bmad-output/meq/

## Deny Zones
- node_modules/
- .git/
```

### `patterns.md` — Learned Patterns

Preferências do usuário, convenções da squad, padrões recorrentes.

### `chronology.md` — Timeline

Resumos de sessões, eventos significativos, progresso.

## Save Triggers

- Decisões de arquitetura ou escopo
- Mudança de fase do projeto
- Usuário solicita salvar (SM)
- Fim de sessão com trabalho relevante
