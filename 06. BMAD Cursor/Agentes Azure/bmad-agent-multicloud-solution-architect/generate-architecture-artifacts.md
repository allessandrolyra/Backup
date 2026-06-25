---
name: generate-architecture-artifacts
description: Generate ADRs, architecture guides, boilerplates, and reusable blueprints.
menu-code: GA
---

# Generate Architecture Artifacts

Generate reusable architecture artifacts that help teams operationalize the target design.

## Artifact Types

- Architecture Decision Records
- architecture guides
- reference boilerplates
- golden templates and blueprints
- baseline diagram templates

## Process

1. Identify which artifact best fits the current decision or delivery stage
2. Gather the minimum context required to make the artifact useful and reusable
3. Produce a structured draft with clear assumptions and intended audience
4. Connect the artifact to related diagrams, standards, and implementation guidance
5. Call out what still needs validation or stakeholder approval

## Output

Return:
- selected artifact type
- draft content
- intended audience and usage guidance
- follow-up actions needed to operationalize it

## Deterministic Execution Boundary

If the user wants boilerplate files or diagram templates generated in a strict format, invoke an exact external skill such as `generate-adr-template` or `generate-enterprise-blueprint` when available.
