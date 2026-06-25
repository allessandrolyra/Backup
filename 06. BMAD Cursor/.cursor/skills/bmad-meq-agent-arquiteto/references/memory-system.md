# Memory System for Wagner

**Memory location:** `_bmad/_memory/bmad-meq-agent-arquiteto-sidecar/`

## Core Principle

Só lembre do que importa. Condense decisões arquiteturais ao essencial.

## File Structure

### `index.md` — Primary Source

**Load on activation.** Contains:
- Decisões arquiteturais tomadas
- Stack escolhido (web, Android, iOS)
- Padrões e convenções
- Próximos passos

### `access-boundaries.md` — Required

**Load on activation.** Structure:
```markdown
# Access Boundaries for Wagner

## Read Access
- {project-root}/_bmad/meq/
- {project-root}/_bmad-output/
- {project-root}/docs/

## Write Access
- {project-root}/_bmad/_memory/bmad-meq-agent-arquiteto-sidecar/
- {project-root}/_bmad-output/meq/

## Deny Zones
- node_modules/
- .git/
```

### `patterns.md` — Learned Patterns

Preferências do usuário, convenções técnicas, padrões recorrentes.

### `chronology.md` — Timeline

Decisões significativas, mudanças de stack, evolução da arquitetura.

## Save Triggers

- Decisões de arquitetura ou stack
- Escolha de padrões ou tecnologias
- Mudança de abordagem
- Usuário solicita salvar (SM)
- Fim de sessão com trabalho relevante
