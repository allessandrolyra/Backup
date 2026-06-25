# Implementation Guide

## Purpose

Generate comprehensive implementation plans following the 5-layer framework: Licensing, Architecture, Configuration, Automation, and Operations.

## Process

1. **Clarify scope** — What is being implemented?
   - Specific workload (Teams, Purview, Intune, etc.)
   - Security feature (Defender, Conditional Access, etc.)
   - Compliance control (DLP, Retention, eDiscovery, etc.)
   - Full environment setup (greenfield or migration)

2. **Apply the 5-Layer Framework**:

### Layer 1 — Licensing
- Required SKU(s) and add-ons
- Dependencies and prerequisites
- Eligibility validation
- Applicable contracts and channels
- Restrictions and limitations
- Additional billing considerations

### Layer 2 — Architecture
- Components involved and their relationships
- Dependencies (service-to-service)
- Integrations required
- Authentication and authorization flows
- Data flows and residency
- Security and compliance implications
- Resilience considerations

### Layer 3 — Configuration
- Admin center paths (step-by-step)
- Settings and policies to configure
- RBAC roles and permissions needed
- Minimum configuration checklist
- Best practices and hardening

### Layer 4 — Automation
Provide scripts and commands when applicable:

**Portal path:** Admin center → Menu → Setting

**PowerShell:**
- Module to use (Microsoft.Graph, ExchangeOnlineManagement, etc.)
- Connection commands
- Configuration commands
- Verification commands

**Microsoft Graph:**
- Endpoint (e.g., `POST /policies/conditionalAccessPolicies`)
- Method and headers
- Request body example
- Required permissions (Delegated and Application)
- Scopes needed

**IaC (when applicable):**
- Terraform, Bicep, or ARM template snippets

### Layer 5 — Operations
- Monitoring setup (alerts, dashboards)
- Audit log configuration
- Troubleshooting guidance
- KPIs and success metrics
- Ongoing maintenance tasks
- Change management considerations

3. **Deliver** with:
   - Pre-implementation checklist
   - Implementation steps (ordered)
   - Post-implementation validation
   - Rollback plan
   - Official source references

## Key Rules

- Never skip Layer 1 (licensing) — it gates everything else
- Always provide rollback guidance for critical changes
- Inform permissions and RBAC requirements before any automation
- Warn about tenant-wide vs. scoped impact
- Differentiate production-ready configs from pilot/test configs
