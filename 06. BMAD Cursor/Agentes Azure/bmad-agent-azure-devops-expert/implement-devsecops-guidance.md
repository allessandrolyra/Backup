---
name: implement-devsecops-guidance
description: Recommend practical DevSecOps controls for Azure delivery.
menu-code: DS
---

# Implement DevSecOps Guidance

Recommend security controls that fit the current delivery flow without sacrificing maintainability.

## Focus Areas

- secret handling and secret exposure risk
- dependency and code scanning
- branch protection and PR policy
- least privilege for service connections and identities
- artifact trust, provenance, and pinned versions
- compliance gates and auditable approvals

## Process

1. Review the current delivery and IaC context
2. Identify missing controls and risky defaults
3. Prioritize fixes that move security left with low operational friction
4. Recommend where checks belong in the flow
5. Separate architectural guidance from actual scan execution

## Output

Return:
- prioritized DevSecOps recommendations
- where each control should live in the pipeline or platform
- rollout order
- optional external checks to execute when exact skills are available

## Autonomous Use

This capability can run headlessly for broad security posture review within allowed folders.
