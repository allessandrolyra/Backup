---
name: design-release-strategy
description: Design rollout, rollback, and production release strategy.
menu-code: DR
---

# Design Release Strategy

Design a release model that balances speed, confidence, and blast-radius control.

## Consider

- environment maturity and approval model
- business criticality and tolerance for disruption
- application architecture and dependency graph
- observability available during release
- rollback speed and data compatibility constraints

## Process

1. Assess current release constraints
2. Choose an appropriate strategy: standard, canary, blue-green, ring-based, or phased
3. Define entry criteria, health signals, rollback conditions, and ownership
4. Map the strategy into pipeline and environment requirements
5. Call out prerequisites such as feature flags, telemetry, or database migration controls

## Output

Return:
- recommended rollout model
- rollback approach
- operational checklist
- telemetry and approval requirements
