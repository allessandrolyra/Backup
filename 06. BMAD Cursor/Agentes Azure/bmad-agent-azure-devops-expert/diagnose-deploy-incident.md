---
name: diagnose-deploy-incident
description: Diagnose deployment failures and pipeline incidents.
menu-code: DI
---

# Diagnose Deploy Incident

Help the user triage a failed pipeline, deployment, or post-deploy incident with a fast, evidence-oriented approach.

## Gather

- failing stage, job, or environment
- recent change window
- visible logs, error messages, and affected services
- whether the issue is build, release, infrastructure, configuration, or runtime

## Process

1. Frame the incident precisely
2. Identify likely failure domain and blast radius
3. Build a short hypothesis list ordered by probability and impact
4. Recommend the next safest checks and rollback options
5. Distinguish evidence from assumption
6. Capture reusable lessons if the root cause becomes clear

## Output

Use this structure:

```markdown
# Incident Triage

## Current Signal
- what is failing

## Most Likely Causes
- hypothesis with evidence

## Next Checks
- immediate diagnostic action

## Containment
- rollback, freeze, or mitigation
```

## Deterministic Execution Boundary

If the user wants log parsing or exact scan execution, invoke a registered external skill such as `review-logs` when available.
