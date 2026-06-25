# Memory System for Felipe

**Memory location:** `_bmad/_memory/bmad-meq-agent-fullstack-sidecar/`

## Core Principle

Só lembre do que importa. Condense contexto de implementação ao essencial.

## File Structure

### `index.md` — Primary Source

**Load on activation.** Contains:
- Features/stories em andamento
- O que foi implementado
- Próximos passos
- Referências úteis (paths, ACs)

### `access-boundaries.md` — Required

**Load on activation.** Structure:
```markdown
# Access Boundaries for Felipe

## Read Access
- {project-root}/_bmad/meq/
- {project-root}/_bmad-output/
- {project-root}/docs/
- {project-root}/src/ (ou estrutura do projeto)

## Write Access
- {project-root}/_bmad/_memory/bmad-meq-agent-fullstack-sidecar/
- {project-root}/_bmad-output/meq/
- {project-root}/src/ (ou estrutura do projeto)

## Deny Zones
- node_modules/
- .git/
```

### `patterns.md` — Learned Patterns

Convenções do projeto, padrões de código, preferências do usuário.

### `chronology.md` — Timeline

Implementações concluídas, milestones, progresso.

## Save Triggers

- Story/feature concluída
- Progresso significativo
- Descoberta de padrão ou convenção
- Usuário solicita salvar (SM)
- Fim de sessão com trabalho relevante
