---
name: design-infrastructure-landscape
description: Design infrastructure topology, network, security, and platform landscape.
menu-code: IL
---

# Design Infrastructure Landscape

Design the infrastructure topology for a distributed or multicloud platform, including network, security, platform, and regional concerns.

## Focus Areas

- network topology and segmentation
- hybrid or cross-cloud connectivity
- traffic steering, global routing, and failover patterns
- identity and zero-trust boundaries
- compute, data, messaging, and API layers
- multi-region, disaster recovery, and failover patterns
- observability and operational touchpoints

## Process

1. Clarify the platform and environment model
2. Define the major infrastructure layers and trust boundaries
3. Explain how connectivity, resilience, governance, and multicloud traffic negotiation are handled
4. Identify platform dependencies and failure domains
5. Organize the view in logical layers with a clear flow from entry to processing to output
6. Route all connections around components, never through them, using orthogonal paths or smooth curves
7. Keep parallel flows separated with visible spacing so they do not appear glued together
8. Recommend the infrastructure views that best communicate the design
9. Map cross-cloud connectivity options such as transit, interconnect, DNS routing, and failover models when relevant

## Layout Rules

- preserve a natural reading order, usually left-to-right or top-to-bottom
- use zones, clusters, or boundary boxes to group related services
- define clear source and destination points for each connection
- prioritize readability over compactness when placement trade-offs exist
- avoid visual overlap between arrows, labels, and infrastructure components

## Output

Return:
- infrastructure topology summary
- network and trust model
- resiliency and recovery notes
- platform gaps and recommended next actions
