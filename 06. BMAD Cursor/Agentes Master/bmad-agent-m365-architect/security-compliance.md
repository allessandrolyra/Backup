# Security & Compliance

## Purpose

Assess, design and configure Microsoft security and compliance solutions including Defender, Purview, DLP, eDiscovery, and identity protection.

## Process

1. **Understand the requirement**:
   - Is this a security concern, compliance mandate, or both?
   - What regulatory frameworks apply? (LGPD, GDPR, SOX, HIPAA, etc.)
   - What data types need protection?
   - What threats need addressing?
   - Current security posture and maturity?

2. **Security Assessment** (when applicable):

   ### Identity Security
   - Entra ID P1/P2 capabilities needed
   - MFA enforcement strategy
   - Conditional Access policy design
   - Identity Protection risk policies
   - PIM for privileged access

   ### Endpoint Security
   - Defender for Endpoint deployment
   - Device compliance policies
   - Attack surface reduction rules
   - EDR capabilities

   ### Email & Collaboration Security
   - Defender for Office 365 (Plan 1 vs Plan 2)
   - Safe Attachments, Safe Links
   - Anti-phishing policies
   - Teams security considerations

   ### Cloud App Security
   - Defender for Cloud Apps
   - Shadow IT discovery
   - App governance
   - Session controls

3. **Compliance Assessment** (when applicable):

   ### Information Protection
   - Sensitivity labels design
   - Auto-labeling policies
   - Encryption and rights management

   ### Data Loss Prevention
   - DLP policy design (Exchange, SharePoint, Teams, Endpoints)
   - Sensitive information types
   - Policy tips and user notifications

   ### Retention & Records
   - Retention policies and labels
   - Records management
   - Regulatory records (immutable)
   - Disposition reviews

   ### eDiscovery & Audit
   - Standard vs. Premium eDiscovery
   - Case management
   - Legal holds
   - Audit Standard vs. Premium
   - Audit log retention

   ### Insider Risk
   - Insider Risk Management policies
   - Communication Compliance
   - Information barriers

4. **Licensing mapping** — Clearly state what's included in base SKU vs. what requires add-ons or premium capabilities

5. **Deliver** with implementation steps covering all 5 layers

## Key Rules for Purview & eDiscovery

- Always distinguish: licensing needed, who needs to be licensed, premium add-ons required
- Clarify billing: included vs. pay-as-you-go vs. additional charges
- Specify: current portal experience vs. legacy (retired)
- Note limitations by region, cloud, data type, API, or preview status
- Identify dependencies: Exchange, SharePoint, OneDrive, Teams, specific permissions
