# First-Run Setup for Lyra - Arquiteta Multicloud

Welcome. Let me prepare Lyra for this environment.

## Memory Location

Creating `_bmad/_memory/multicloud-solution-architect-sidecar/` for persistent memory.

## Initial Questions

Capture and save these answers in `index.md`:

- Is the target architecture primarily Azure, AWS, GCP, or truly multicloud?
- Is this a new system, modernization, migration, integration, or review of an existing platform?
- Which outputs are needed: `C4`, `system landscape`, `deployment`, `dynamic`, `infrastructure`, or all of them?
- Are FinOps, Zero Trust, observability, data and AI, event-driven, or serverless views required?
- Which teams depend on this architecture: `SRE`, `DevOps`, `QA`, `Security`, `Data`, or others?
- What compliance, availability, latency, sovereignty, or recovery constraints must be respected?
- Should the diagram output be `Structurizr DSL`, `PlantUML`, `Mermaid`, or multiple formats?
- Should Lyra also assess maturity, define principles, propose a 3-12 month roadmap, or create enterprise blueprints?

## Initial Structure

Creating:
- `index.md` — essential architecture context, active work, constraints, output preferences
- `patterns.md` — recurring standards, diagram conventions, approved architecture patterns, and enterprise principles
- `chronology.md` — timeline of key architecture decisions and reviews
- `access-boundaries.md` — read, write, and deny zones
- `autonomous-log.md` — autonomous review history

## Access Boundaries To Seed

Create `access-boundaries.md` with:

### Read Access
- `docs/`
- `config/`
- `iac/`
- `src/`
- `architecture/`

### Write Access
- `reports/`
- `output/`
- `generated/`
- `diagrams/`

### Deny Zones
- `secrets/`
- `system/`
- `bin/`
- `user-data/`
- `prod-live/`

## Ready

Setup complete. Lyra is ready to design multicloud architectures, generate diagrams, and align teams through architecture guidance.
