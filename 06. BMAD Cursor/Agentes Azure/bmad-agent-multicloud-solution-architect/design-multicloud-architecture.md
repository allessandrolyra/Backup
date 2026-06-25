---
name: design-multicloud-architecture
description: Design a complete multicloud architecture with rationale and trade-offs.
menu-code: MA
---

# Design Multicloud Architecture

Design a complete solution architecture across Azure, AWS, GCP, or a hybrid combination.

## Gather

- business goals and critical user journeys
- functional and non-functional requirements
- cloud constraints, sovereignty, compliance, and integration needs
- resilience, latency, cost, and operational targets
- team boundaries and ownership model
- whether FinOps, Zero Trust, observability, data and AI, event-driven, or serverless concerns need dedicated views

## Process

1. Define the system scope and major domains
2. Propose the target architecture and major components
3. Explain how the solution addresses reliability, security, cost, performance, and operations
4. Apply cloud-agnostic principles first, then map provider-specific choices and service equivalences where useful
5. Call out trade-offs, risks, and alternatives
6. Recommend which diagrams and documents should accompany the design

## Output

Return:
- architecture overview
- major components and responsibilities
- core integrations and data flow
- trade-offs and risks
- recommended next diagrams and deliverables
- major service equivalence or provider-specific mapping notes when relevant
