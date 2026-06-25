---
name: review-iac-strategy
description: Review infrastructure as code strategy and governance patterns.
menu-code: RI
---

# Review IaC Strategy

Review Terraform, Bicep, or ARM usage for structure, reuse, environment modeling, governance, and operational risk.

## Focus Areas

- module structure and composition
- environment separation and promotion model
- naming, tagging, and policy alignment
- state management and drift exposure
- dependency clarity and deploy ordering
- version pinning and repeatability

## Process

1. Identify the IaC technology in scope
2. Review the current structure in allowed paths
3. Surface design issues, likely drift risks, and governance gaps
4. Recommend target-state patterns and migration steps when needed
5. Distinguish clearly between conceptual advice and deterministic validation

## Output

Return:
- current-state assessment
- key risks
- recommended structure or standard
- validation steps to run through external skills if available

## Deterministic Execution Boundary

When the user asks for actual validation, lint, build, or diff execution, route to exact external skills such as `validate-iac` or `compare-iac-diff` if they exist.
