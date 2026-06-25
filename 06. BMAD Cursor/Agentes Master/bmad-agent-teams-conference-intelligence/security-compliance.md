# Security & Compliance

## Purpose

Assess, configure and advise on security, privacy and compliance for Teams meetings, conference intelligence, transcriptions, recordings and AI-generated content.

## Process

1. **Gather compliance context** — Ask the user:
   - What industry? (financial, healthcare, government, education, general enterprise)
   - What regulations apply? (LGPD, GDPR, HIPAA, SOX, industry-specific)
   - What is the data classification? (public, internal, confidential, highly confidential)
   - What compliance tools are available? (Purview, DLP, eDiscovery, Insider Risk)
   - What is the current compliance posture?

2. **Assess meeting data compliance**:

   ### Data Classification & Protection
   - Meeting recordings: sensitivity labels, DLP policies
   - Transcripts: classification, access control, encryption
   - AI-generated content (minutes, summaries): inherit classification from source
   - Chat messages: DLP scanning, compliance recording
   - Shared files: sensitivity labels, information barriers

   ### Retention & Lifecycle
   - Recording retention policies (Teams admin + Purview)
   - Transcript retention (storage location: OneDrive/SharePoint)
   - Chat message retention (Exchange-based)
   - AI-generated content retention
   - Legal hold and preservation
   - Deletion policies and user-initiated deletion

   ### eDiscovery
   - Meeting recordings in eDiscovery scope
   - Transcript searchability
   - Chat message discovery
   - Compliance recording for regulated industries
   - Content search across meeting artifacts
   - Premium eDiscovery capabilities

   ### DLP (Data Loss Prevention)
   - DLP policies for meeting chat
   - DLP for shared files in meetings
   - DLP for transcripts (when supported)
   - Endpoint DLP for downloaded recordings
   - DLP policy tips for end users

   ### Insider Risk
   - Anomalous meeting patterns
   - Sensitive content sharing in meetings
   - Unusual recording or transcript access
   - Integration with Insider Risk Management

   ### Access Control
   - Meeting recording access (organizer, participants, specified users)
   - Transcript access permissions
   - External participant data handling
   - Guest access to meeting artifacts
   - Conditional Access policies for Teams
   - MFA enforcement

   ### Zero Trust Alignment
   - Identity verification (Entra ID, Conditional Access)
   - Device compliance (Intune)
   - Network security (named locations, compliant network)
   - Application access (app permission policies)
   - Data protection (sensitivity labels, DLP)
   - Monitoring and audit (audit logs, alert policies)

3. **Configure compliance controls**:
   - Admin Center policy settings
   - Purview portal configurations
   - Compliance Manager assessments
   - Audit log queries for meeting events
   - Alert policies for policy violations

4. **Address AI-specific compliance**:
   - Data residency for AI processing (where does OpenAI process data?)
   - AI-generated content governance
   - Copilot data usage and privacy
   - Agent data access boundaries
   - Consent management for AI processing of meeting content

5. **Deliver** with:
   - Compliance assessment summary
   - Gap analysis
   - Configuration recommendations
   - Policy templates
   - Licensing requirements (Purview, eDiscovery, DLP tiers)
   - Monitoring and audit plan
   - Risk register

## Key Rules

- Never ignore compliance when discussing meeting intelligence
- Always specify which Purview capabilities require additional licensing
- Distinguish built-in audit from advanced audit
- eDiscovery Standard vs Premium have different capabilities and licensing
- LGPD/GDPR requirements may conflict with some monitoring approaches
- AI-generated content inherits but may also require its own governance
- External participant data has additional privacy considerations
- Compliance recording (for regulated industries) is different from standard meeting recording
