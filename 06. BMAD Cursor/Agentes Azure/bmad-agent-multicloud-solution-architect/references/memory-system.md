# Memory System for Lyra - Arquiteta Multicloud

**Memory location:** `_bmad/_memory/multicloud-solution-architect-sidecar/`

## Core Principle

Remember only the architecture context that improves future design quality: system boundaries, business constraints, approved patterns, diagram conventions, dependencies, and architectural decisions that affect multiple teams.

## File Structure

### `index.md` — Primary Source

**Load on activation.** Contains:
- essential solution context
- active architecture scope and current goals
- chosen cloud posture and major constraints
- quick references to patterns, dependencies, and outputs

Update immediately when:
- target architecture scope changes
- a major architecture decision is approved
- output format or review goals change materially

### `access-boundaries.md` — Access Control

**Load on activation before any file operation.** Contains:

```markdown
# Access Boundaries for Lyra - Arquiteta Multicloud

## Read Access
- docs/
- config/
- iac/
- src/
- architecture/

## Write Access
- reports/
- output/
- generated/
- diagrams/

## Deny Zones
- secrets/
- system/
- bin/
- user-data/
- prod-live/
```

If a path falls outside these boundaries or appears to expose secrets or live production artifacts, stop and ask before proceeding.

### `patterns.md` — Learned Patterns

**Load when needed.** Contains:
- preferred diagram conventions
- approved architecture standards
- cloud maturity observations and enterprise principles
- recurring integration and topology patterns
- service equivalence mappings and preferred cloud patterns
- cross-team communication preferences
- repeated risks and accepted mitigations

### `chronology.md` — Timeline

**Load when needed.** Contains:
- architecture reviews
- major design decisions
- modernization or migration milestones
- important diagram refresh events

### `autonomous-log.md` — Headless History

**Load when needed.** Contains:
- autonomous architecture reviews
- files and folders analyzed
- reports or diagram artifacts created
- major gaps detected

## Memory Persistence Strategy

### Write-Through

Persist immediately when:
1. an architecture decision is approved
2. a new recurring system pattern is identified
3. an important dependency or cross-team constraint is discovered
4. a maturity assessment, roadmap direction, or enterprise principle is approved
5. the user explicitly asks to save memory

### Checkpoint

Update periodically after:
- a major capability completes
- an autonomous review produces a report
- the architecture model becomes materially clearer

### Save Triggers

Always update memory after:
- each completed architecture analysis
- identifying a new system pattern or dependency
- approval of a design recommendation
- delivery of a significant architecture artifact or diagram set
- approval of a roadmap, blueprint, or enterprise standard

## Write Discipline

Before writing to memory, ask:

1. Will this improve a future architecture decision?
2. Can it be expressed in fewer tokens without losing meaning?
3. Does it belong in `index.md`, `patterns.md`, `chronology.md`, or `autonomous-log.md`?
4. Does `index.md` need a short pointer to keep startup fast?

## Memory Maintenance

Regularly:
1. condense repeated design rationales into shared patterns
2. prune obsolete constraints and stale alternatives
3. merge similar architecture lessons into reusable guidance
4. keep `index.md` concise and current

## First Run

If the sidecar does not exist, load `init.md` and create the structure before doing architecture work.
