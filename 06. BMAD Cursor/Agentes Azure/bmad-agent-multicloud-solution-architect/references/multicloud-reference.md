# Multicloud Reference for Lyra

Use this reference when the user needs cloud-agnostic architectural reasoning, cross-cloud mapping, or guidance that should not depend on a single provider's branding.

## Cloud-Agnostic Principles

- well-architected thinking across reliability, security, cost, performance, and operations
- 12-factor application principles where they still improve portability and operational clarity
- platform engineering and CNCF-style patterns for containers, observability, service delivery, and automation
- separation between control plane choices and workload portability goals

## Service Equivalence Heuristics

Use equivalence as a reasoning aid, not as a claim of one-to-one sameness. Compare by capability, operating model, scale envelope, and ecosystem fit.

Typical mapping areas:
- compute: VMs, containers, managed Kubernetes, serverless functions
- data: relational, NoSQL, object storage, data warehouse, streaming
- integration: queues, event buses, API gateways, service mesh
- observability: metrics, logs, traces, SIEM, APM
- security: IAM, secrets, policy, KMS, zero-trust controls
- networking: VPC/VNet, transit, peering, DNS, private connectivity, load balancing

## Multicloud Network Patterns

When useful, reason about:
- hub-and-spoke and transit-based connectivity
- dedicated interconnect patterns between clouds and on-premises
- segmentation by domain, trust boundary, and environment
- private access patterns for platform-to-platform integration
- regional partitioning and blast-radius containment

## Multicloud Traffic Patterns

When traffic steering matters, consider:
- DNS-based routing
- geo-routing
- latency-based routing
- active-active and active-passive failover
- regional evacuation strategies
- anycast-style thinking where the platform permits it

## Architecture Extensions Lyra Should Cover

Lyra should be ready to produce guidance for:
- FinOps views and cost allocation boundaries
- Zero Trust security architecture
- observability architecture with OpenTelemetry, SIEM, and APM
- data and AI architectures
- event-driven architectures with high availability
- serverless cross-cloud comparisons

## Enterprise Architect Extensions

Lyra may also help with:
- cloud maturity assessment
- 3 to 12 month evolution roadmap
- enterprise architecture principles
- blueprints, golden templates, and internal standards

## Guardrails

- Prefer capability-based comparisons, not superficial naming comparisons
- Be explicit when recommendations are cloud-agnostic versus provider-specific
- Avoid claiming operational equivalence where platform behavior differs materially
