# Troubleshooting

## Purpose

Diagnose and resolve issues related to Teams meetings, recordings, transcriptions, Graph API integration, agents and conference intelligence solutions.

## Process

1. **Identify the symptom** — Ask the user:
   - What is happening? (or not happening)
   - When did it start? (always, recently, after a change)
   - Who is affected? (all users, specific users, specific meeting types)
   - What was the expected behavior?
   - What has been tried so far?

2. **Apply systematic diagnosis**:

   ### Layer 1 — Licensing Verification
   - Verify base license (E3, E5, Business Premium)
   - Verify add-ons (Teams Premium, Copilot, Phone, Audio Conferencing, Rooms)
   - Check license assignment to affected users
   - Verify feature availability for the license tier

   ### Layer 2 — Policy Verification
   - Teams meeting policies (recording, transcription, Copilot)
   - Teams messaging policies
   - Teams app permission policies
   - Conditional Access policies affecting Teams
   - Information barrier policies
   - DLP policies impacting meeting content

   ### Layer 3 — Permission Verification
   - Graph API permissions (delegated and application)
   - Admin consent status
   - App registration configuration
   - Service principal permissions
   - RBAC assignments in Azure resources
   - Teams admin roles

   ### Layer 4 — Configuration Verification
   - Teams Admin Center settings
   - Meeting options (per-meeting settings by organizer)
   - Tenant-level vs user-level vs group-level policies
   - PowerShell verification of effective policies
   - Graph API settings verification

   ### Layer 5 — Technical Verification
   - API endpoint availability and response codes
   - Webhook/change notification subscription status
   - Azure Function health and execution logs
   - Logic App run history
   - Network connectivity (proxies, firewalls)
   - Certificate validity for app authentication

   ### Layer 6 — Data Verification
   - Recording storage location and accessibility
   - Transcript availability timeline
   - Recap generation status
   - OneDrive/SharePoint permissions
   - Retention policy impact on data availability

3. **Common issue patterns**:

   ### Recording Issues
   - Recording not starting → policy, license, organizer role, compliance recording conflict
   - Recording not available → processing time, storage quota, retention policy, permissions
   - Recording access denied → sharing settings, OneDrive permissions, external user

   ### Transcription Issues
   - Transcription not available → policy disabled, language not supported, Teams Premium required
   - Transcript quality → audio quality, multiple speakers, background noise, language detection
   - Transcript not in Graph API → processing delay, permission scope, meeting type limitation

   ### Recap/Copilot Issues
   - Intelligent recap not showing → Teams Premium or Copilot license missing, policy disabled
   - Copilot not available in meeting → license, policy, meeting type, tenant rollout
   - Facilitator not appearing → preview availability, policy, meeting type, license

   ### Graph API Issues
   - 403 Forbidden → missing permissions, missing admin consent, scope mismatch
   - 404 Not Found → incorrect endpoint, resource not yet available, processing delay
   - 429 Too Many Requests → rate limiting, missing retry logic
   - Empty transcript → processing still in progress, meeting too short, no speech detected
   - Webhook not firing → subscription expired, endpoint unreachable, validation token failure

   ### Agent Issues
   - Bot not responding → app registration, messaging endpoint, SSL certificate
   - Agent not processing transcripts → Graph permissions, webhook subscription, function timeout
   - Output not delivered → Adaptive Card schema error, channel permissions, bot conversation scope

4. **Deliver** with structured format:
   - **Symptom** — What the user reports
   - **Probable Cause** — Most likely based on symptom pattern
   - **Root Cause** — Confirmed after investigation
   - **Correction** — Step-by-step fix
   - **Validation** — How to confirm the fix works
   - **Prevention** — How to avoid recurrence

## Key Rules

- Always check licensing first — most issues trace back to missing license or add-on
- Policies override user settings — always verify effective policy
- Graph API processing is not instant — transcripts and recordings have processing delays
- Always verify admin consent for application permissions
- Webhook subscriptions expire and must be renewed
- Different meeting types have different feature availability
- Tenant rollout for new features is gradual — not all tenants get features simultaneously
- Check Service Health Dashboard for known Microsoft-side issues before deep debugging
