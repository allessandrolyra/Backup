# Playbook: AI & Agentic DevOps

This playbook covers the integration of AI assistance and managed infrastructure in Azure DevOps.

## ADO MCP Server (AI Assistance)
- **Concept:** Expose Azure DevOps data (Boards, Work Items) to AI assistants.
- **Prerequisites:**
    - ADO Organization & Project.
    - Personal Access Token (PAT) with `Read/Write` permission to Work Items.
    - MCP Server configured with the PAT.
- **Capabilities:**
    - Create/Update/Query Work Items via Natural Language.
    - Summarize Backlogs or Sprint progress.
    - Generate Child tasks from a PBI description.

## GitHub Copilot & Managed DevOps Pools
- **Managed DevOps Pools:** Use for scalable, Microsoft-managed agent infrastructure.
    - Pro: Zero maintenance, secure by default.
    - Use case: Large CI/CD pipelines with high concurrency.
- **Agentic DevOps:** Use AI to:
    - Review PRs (GitHub Copilot).
    - Suggest YAML pipeline optimizations.
    - Auto-generate test cases from requirement descriptions.

## References
- [MCP Server for Azure DevOps](https://github.com/microsoft/mcp-server-azure-devops)
- [Managed DevOps Pools documentation](https://learn.microsoft.com/en-us/azure/devops/managed-devops-pools/?view=azure-devops)
