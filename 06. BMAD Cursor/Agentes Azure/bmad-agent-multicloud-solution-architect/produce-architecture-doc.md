---
name: produce-architecture-doc
description: Produce architecture documentation with views, rationale, and guidance.
menu-code: AD
---

# Produce Architecture Document

Produce a coherent architecture document that combines narrative, decisions, risks, and recommended diagram views.

## Include

- executive summary
- system context and scope
- architecture overview
- key components and integrations
- security, resilience, and operational notes
- ADR-worthy decisions and reusable standards
- recommended diagrams and implementation guidance
- diagram guidance with explicit readability and routing expectations when visual artifacts are included

## Process

1. Gather the current architectural context
2. Organize the document for both decision-makers and engineering teams
3. Write concise but technically grounded explanations
4. Link each major section to the diagram or artifact that should support it
5. When recommending diagrams, specify layout expectations such as logical layers, natural reading order, and non-overlapping routed connections
6. Surface unresolved risks, assumptions, and next decisions

## Output

Return:
- architecture document draft
- diagram checklist
- ADR-worthy decisions
- open issues and follow-up actions
