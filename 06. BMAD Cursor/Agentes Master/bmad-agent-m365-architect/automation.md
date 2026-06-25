# Automation

## Purpose

Provide PowerShell, Microsoft Graph API and Infrastructure as Code automation for Microsoft 365 configuration, management and operations.

## Process

1. **Understand the automation need**:
   - What operation needs automating?
   - One-time configuration or ongoing management?
   - Interactive or unattended execution?
   - Scale: single tenant or multi-tenant?
   - Who will run it? (admin, service account, managed identity)

2. **Select the right approach**:

   | Scenario | Recommended Approach |
   |----------|---------------------|
   | One-time admin setup | PowerShell interactive |
   | Recurring operations | PowerShell scheduled / Azure Automation |
   | Application integration | Microsoft Graph API |
   | Infrastructure provisioning | Terraform / Bicep |
   | Policy enforcement | Azure Policy |
   | Cross-tenant management | Graph API with multi-tenant app |

3. **Provide automation** with:

   ### PowerShell
   - Module specification (Microsoft.Graph, ExchangeOnlineManagement, MicrosoftTeams, PnP.PowerShell, etc.)
   - Connection method (interactive, certificate, managed identity)
   - Complete script with error handling
   - Verification commands
   - Disconnect/cleanup

   ### Microsoft Graph API
   - Endpoint URL and HTTP method
   - Request headers and body (JSON)
   - Delegated permissions (for user context)
   - Application permissions (for daemon/service)
   - Consent type required (user, admin)
   - Rate limiting considerations
   - Pagination handling (when returning collections)

   ### Infrastructure as Code
   - Terraform provider and resource definitions
   - Bicep modules and parameters
   - ARM template structure
   - State management considerations

4. **Security considerations for every automation**:
   - Minimum permissions required (least privilege)
   - Credential management (certificate vs. secret, Key Vault)
   - Audit trail (what gets logged)
   - Excessive privilege warnings
   - Service principal vs. managed identity recommendation

5. **Deliver** with:
   - Prerequisites (modules, permissions, consent)
   - Complete code/script
   - Execution instructions
   - Expected output
   - Rollback procedure
   - Known limitations

## Key Rules

- Always specify exact permission scopes — never recommend overly broad permissions
- Prefer managed identity over service principal with secrets
- Prefer certificate-based auth over client secret
- Always include error handling in scripts
- Warn about tenant-wide impact for write operations
- Specify Graph API version (v1.0 for production, beta for preview features)
- Note when an operation requires admin consent vs. user consent
