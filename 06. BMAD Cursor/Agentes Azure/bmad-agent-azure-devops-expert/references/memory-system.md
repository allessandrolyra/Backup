# Memory System for Orion - DevOps Azure

**Memory location:** `_bmad/_memory/azure-devops-expert-sidecar/`

## Core Principle

Memoria deve guardar apenas o que melhora futuras decisoes do agente: padroes do projeto, preferencias do time, limites de acesso, incidentes recorrentes e recomendacoes aprovadas.

## File Structure

### `index.md` — Primary Source

**Load on activation.** Contains:
- essential project context
- active delivery concerns and current work
- environments, tools, and standards in force
- quick pointers to patterns and chronology when needed

**Update immediately when:**
- core stack or platform changes
- environment model changes
- an approved recommendation changes the operating standard

### `access-boundaries.md` — Access Control

**Load on activation before any file operation.** Contains:

```markdown
# Access Boundaries for Orion - DevOps Azure

## Read Access
- iac/
- pipelines/
- config/
- src/
- docs/

## Write Access
- reports/
- output/
- logs/agent/
- generated/

## Deny Zones
- secrets/
- system/
- bin/
- user-data/
- prod-live/
```

If a path is outside these boundaries or appears to contain credentials, tokens, keys, sensitive data, or live production artifacts, stop and ask before proceeding.

### `patterns.md` — Learned Patterns

**Load when needed.** Contains:
- pipeline conventions by repository or stack
- naming, tagging, and versioning rules
- reusable delivery patterns
- recurring issues and accepted fixes
- preferred Azure and GitHub/Azure DevOps workflows

### `chronology.md` — Timeline

**Load when needed.** Contains:
- significant sessions
- major design decisions
- incidents diagnosed
- notable improvements adopted by the team

### `autonomous-log.md` — Headless History

**Load when needed.** Contains:
- autonomous reviews executed
- files or folders analyzed
- reports generated
- major risks detected

## Memory Persistence Strategy

### Write-Through

Persist immediately when:
1. a project standard or operating constraint changes
2. a new recurring pattern is identified
3. an incident is diagnosed with a credible root-cause hypothesis
4. the user explicitly approves a recommendation or asks to save memory

### Checkpoint

Update periodically after:
- a capability completes
- an autonomous review generates a report
- enough new findings accumulate to improve future guidance

### Save Triggers

Always update memory after:
- each completed analysis
- identifying a new project pattern
- diagnosing an incident
- approval of a recommendation

## Write Discipline

Before writing to memory, ask:

1. Is this likely to improve a future DevOps decision?
2. Can it be reduced to the smallest useful summary?
3. Does it belong in `index.md`, `patterns.md`, `chronology.md`, or `autonomous-log.md`?
4. Does `index.md` need a condensed pointer to keep activation fast?

## Memory Maintenance

Regularly:
1. condense repeated recommendations into a single standard
2. prune stale environment details
3. merge similar incident lessons into reusable playbook notes
4. keep `index.md` short enough to load quickly every session

## First Run

If the sidecar does not exist, load `init.md` and create the memory structure before any operational work.
