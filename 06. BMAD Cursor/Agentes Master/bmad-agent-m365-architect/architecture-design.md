# Architecture Design

## Purpose

Design Microsoft 365 solution architectures, blueprints and reference architectures for any scenario involving M365 workloads.

## Process

1. **Understand business objective** — What is the desired outcome? What problem is being solved?

2. **Gather technical context**:
   - Current environment (cloud-only, hybrid, multi-cloud)
   - User count and distribution (geographic, profile-based)
   - Existing Microsoft investments and licenses
   - Identity model (Entra ID, hybrid AD, federation)
   - Security and compliance requirements
   - Integration requirements (third-party systems, custom apps)

3. **Design the architecture** covering:

   ### Logical Architecture
   - Component diagram showing all M365 services involved
   - Data flow between components
   - Integration points

   ### Identity & Access
   - Authentication flow (Entra ID, Conditional Access)
   - Authorization model (RBAC, PIM)
   - Identity governance

   ### Security
   - Defense-in-depth layers
   - Defender components applicable
   - Zero Trust alignment
   - Data protection (Purview, DLP)

   ### Compliance
   - Regulatory framework mapping
   - Retention and records management
   - Audit and investigation capabilities

   ### Resilience
   - Service availability considerations
   - Backup and recovery strategy
   - Multi-region considerations

4. **Map licensing requirements** — Which SKUs and add-ons are needed to support the architecture

5. **Identify risks** — Technical, operational, financial and compliance risks

6. **Deliver** using Architect Mode format:
   - Business objective
   - Logical architecture
   - Components
   - Flows
   - Security
   - Compliance
   - Licensing
   - Costs
   - Risks
   - Recommendations

## Key Rules

- Architecture must be achievable with the licensing identified
- Always consider identity as the foundation layer
- Security and compliance are not optional add-ons — they're integral
- Specify when architecture varies by cloud/segment/region
