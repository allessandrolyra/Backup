# Tenant Readiness Assessment

## Purpose

Perform comprehensive tenant readiness assessments to evaluate maturity, identify gaps, and generate implementation roadmaps.

## Process

1. **Gather tenant information**:
   - Organization name and size (user count)
   - Tenant type (Commercial, Government, Education, 21Vianet)
   - Purchase channel and contract type
   - Cloud model (cloud-only, hybrid with on-premises AD, multi-cloud)
   - Primary geographic locations
   - Industry and regulatory requirements

2. **Assess current state across dimensions**:

   ### Identity & Access
   - Entra ID edition (Free, P1, P2)
   - MFA adoption percentage
   - Conditional Access policies deployed
   - PIM enabled for privileged roles
   - Guest access governance
   - Identity Protection configured

   ### Security
   - Defender suite components deployed
   - Secure Score current vs. target
   - Endpoint protection coverage
   - Email protection (Defender for O365 plan)
   - Cloud App Security deployed
   - Security alerting and response process

   ### Compliance
   - Purview components enabled
   - DLP policies active
   - Retention policies configured
   - Sensitivity labels deployed
   - eDiscovery readiness
   - Audit log retention period

   ### Device Management
   - Intune enrollment status
   - Device compliance policies
   - Application management (MAM)
   - Windows Autopilot readiness
   - BYOD vs. corporate device strategy

   ### Collaboration
   - Exchange Online configuration maturity
   - Teams governance policies
   - SharePoint information architecture
   - OneDrive adoption and protection
   - External sharing controls

   ### Operations
   - Monitoring and alerting setup
   - Change management process maturity
   - Documentation and runbooks
   - Disaster recovery planning
   - License management processes

3. **Generate assessment output**:

   ### Maturity Assessment
   For each dimension, evaluate:
   - **Initial** — Ad-hoc, minimal configuration
   - **Developing** — Basic policies, inconsistent enforcement
   - **Defined** — Documented standards, consistent application
   - **Managed** — Measured, monitored, continuously improved
   - **Optimized** — Automated, proactive, best-in-class

   Present qualitatively unless quantitative data supports scoring.

   ### Gap Analysis
   - Current state vs. desired state per dimension
   - Critical gaps (security/compliance risks)
   - Important gaps (operational efficiency)
   - Nice-to-have improvements

   ### Roadmap
   - **Quick Wins** (0-30 days): High impact, low effort
   - **Short-term** (1-3 months): Foundation building
   - **Medium-term** (3-6 months): Advanced capabilities
   - **Long-term** (6-12 months): Optimization and maturity

   ### Risk Register
   - Identified risks with likelihood and impact
   - Mitigation recommendations
   - Dependencies and blockers

4. **Deliver** using the Decision Matrix format when comparing options, and standard response format for the full assessment.

## Key Rules

- Do not assign numerical maturity scores without sufficient evidence
- Always flag assumptions explicitly
- Roadmap must be achievable with identified licensing
- Quick wins should demonstrate immediate value to build momentum
- Assessment scope should match the user's decision-making needs
- Recommend involving Microsoft or certified partner for formal assessments
