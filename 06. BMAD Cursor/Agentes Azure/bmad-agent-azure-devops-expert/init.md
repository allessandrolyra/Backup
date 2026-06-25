# First-Run Setup for Orion - DevOps Azure

Welcome! Let me prepare Orion for this environment.

## Memory Location

Creating `_bmad/_memory/azure-devops-expert-sidecar/` for persistent memory.

## Initial Questions

Capture and save these answers in `index.md`:

- What is the main application stack for this project?
- Do you use `Azure DevOps`, `GitHub Actions`, or both?
- Is infrastructure managed with `Terraform`, `Bicep`, `ARM`, or a combination?
- Which delivery environments exist today (`DEV`, `HML`, `PRD`, others)?
- What is the current release strategy and rollback model?
- Are there security, compliance, or governance requirements that must always be enforced?
- Which subscriptions, resource groups, service connections, or tenants are in scope by reference only, never by secret?

## Initial Structure

Creating:
- `index.md` — essential context, active work, saved paths, project delivery standards
- `patterns.md` — recurring conventions, approved practices, and detected team preferences
- `chronology.md` — session timeline and relevant milestones
- `access-boundaries.md` — read, write, and deny zones for this agent
- `autonomous-log.md` — autonomous task history and results

## Access Boundaries To Seed

Create `access-boundaries.md` with:

### Read Access
- `iac/`
- `pipelines/`
- `config/`
- `src/`
- `docs/`

### Write Access
- `reports/`
- `output/`
- `logs/agent/`
- `generated/`

### Deny Zones
- `secrets/`
- `system/`
- `bin/`
- `user-data/`
- `prod-live/`

## Ready

Setup complete. Orion is ready to support Azure DevOps architecture, reviews, diagnostics, and continuous improvement.
