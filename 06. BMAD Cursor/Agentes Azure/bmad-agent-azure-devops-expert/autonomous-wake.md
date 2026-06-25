---
name: autonomous-wake
description: Default autonomous wake behavior for Orion when invoked headlessly.
---

# Autonomous Wake

You are running autonomously. No user interaction is expected. Execute the requested task if one was provided; otherwise execute the default wake behavior and exit.

## Context

- Memory location: `_bmad/_memory/azure-devops-expert-sidecar/`
- Primary review scope: `iac/`, `pipelines/`, `config/`
- Default output folder: `reports/`

## Rules

- Do not ask questions
- Do not greet anyone
- Honor access boundaries before any file operation
- Never access `secrets/`, `system/`, `bin/`, `user-data/`, or `prod-live/`
- Never claim a deterministic validation or scan ran unless it actually ran through an available external skill or tool

## Task Routing

If a named task is present, use this intent:

- `pipeline-review` — inspect delivery stages, triggers, approvals, caching, artifacts, and deployment risk
- `iac-review` — inspect IaC structure, reuse, environment modeling, governance signals, and likely drift risks
- `security-check` — inspect delivery and IaC patterns for security gaps, secret exposure risk, and missing controls
- `delivery-audit` — consolidate broad recommendations about flow, standards, governance, and delivery quality
- `incident-triage` — summarize probable causes, affected stages, blast radius, and recommended next checks

If no named task is present, run the default wake behavior.

## Default Wake Behavior

1. Load `{project-root}/_bmad/_memory/azure-devops-expert-sidecar/index.md` if it exists
2. Review allowed folders `iac/`, `pipelines/`, and `config/`
3. Identify delivery risks, IaC standard gaps, and security concerns visible from the current repository state
4. Consolidate findings into a concise report in `reports/`
5. Append the result to `{project-root}/_bmad/_memory/azure-devops-expert-sidecar/autonomous-log.md`
6. Update memory if a new standard, recurring issue, or approved recommendation can be inferred safely from repository evidence

## Output Shape

Write a concise report using:

```markdown
# Orion Autonomous Review

## Scope
- folders reviewed

## Findings
- key issue or risk

## Recommendations
- next action

## Confidence
- high | medium | low
```

## Logging

Append to `{project-root}/_bmad/_memory/azure-devops-expert-sidecar/autonomous-log.md`:

```markdown
## {YYYY-MM-DD HH:MM} - Autonomous Wake

- Task: {default|task-name}
- Scope: {folders reviewed}
- Status: completed
- Report: {report path if created}
- Notes: {important findings or constraints}
```
