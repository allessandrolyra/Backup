# Playbook: Migration & Cloning

Strategies and tools for moving data between Azure DevOps Organizations or Projects.

## Tool Selection Strategy
- **Azure DevOps Migration Tools (recommended):** Use for WITs, history, links, and attachments.
- **OpsHub Migration Manager:** Best for Enterprise SLA, zero-downtime, and complex transformations.
- **Data Migration Tool:** Use only for full collection imports (Server to Services).

## Migration Lifecycle (Azure DevOps Migration Tools)
1. **Setup:** Install via `winget install -e --id NKDAgility.AzureDevOpsMigrationTools`.
2. **Configuration:**
   - Define `Source` and `Target` endpoints.
   - Map `WorkItemType` and `Field` mappings (AS-IS -> TO-BE).
   - Enable `NodeStructuresMigrationConfig` for Area/Iteration paths.
3. **Dry-Run:**
   - Run with `dry-run: true` or migration batch of 5 items.
   - Check `Result` and `ReflectedWorkItemId` mapping.
4. **Execution:** Run in batches (by Team or Area Path).
5. **Hyper-care:** Validate links (Parent/Child) and Test Plan associations.

## Common Pitfalls
- **Identity Mismatch:** Ensure users exist in the Target Org with the same email/UPN.
- **Max History:** History migration can be slow; consider migrating only the latest 10 revisions.
- **Attachments Size:** Use chunked upload for files > 60MB via REST API.

## References
- [Azure DevOps Migration Tools Wiki](https://nkdagility.github.io/azure-devops-migration-tools/)
- [OpsHub Migration Manager](https://www.opshub.com/azure-devops-migration-manager/)
