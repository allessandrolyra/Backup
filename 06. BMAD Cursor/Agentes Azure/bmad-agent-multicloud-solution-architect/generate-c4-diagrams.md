---
name: generate-c4-diagrams
description: Design C4, landscape, deployment, and dynamic architecture views.
menu-code: C4
---

# Generate C4 Diagrams

Design the architectural views needed to communicate the system clearly using the C4 model and related views.

## Supported Views

- system landscape
- system context
- container
- component
- code view when it adds value
- deployment view
- dynamic view
- FinOps view when cost ownership and allocation matter
- Zero Trust and security view when trust boundaries matter
- observability view for telemetry, APM, SIEM, and OpenTelemetry flows
- data and AI view when data pipelines, analytics, or model serving are central

## Process

1. Identify the audience and decision the diagram must support
2. Select the minimum set of views needed
3. Define actors, systems, containers, components, relationships, and boundaries
4. Include traffic steering, failover, routing, trust, or telemetry flows when they materially affect the design
5. Organize each view with a natural reading order, usually left-to-right or top-to-bottom
6. Route connections so arrows never pass through components and do not visually overlap when avoidable
7. Use orthogonal routing, spacing, and grouping boundaries to keep the view readable like a polished draw.io diagram
8. Explain what each view should emphasize and what it should omit
9. When requested, produce diagram-as-code drafts in the requested format

## Layout Rules

- prefer logical layers such as entry, processing, storage, and output
- avoid arrows crossing components
- avoid arrows touching or stacking on each other without visual separation
- make source and destination of each relationship visually obvious
- group related elements into boundaries, clusters, or zones when that improves comprehension

## Output

Return:
- prioritized diagram set
- textual content for each view
- notation guidance
- optional `Structurizr DSL`, `PlantUML`, or `Mermaid` draft when appropriate

## Deterministic Execution Boundary

If the user wants actual artifact generation or syntax validation, invoke an exact external skill such as `generate-c4-structurizr`, `generate-plantuml-diagram`, `generate-mermaid-diagram`, or `validate-diagram-syntax` when available.
