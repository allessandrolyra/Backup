# Playbook: Governance & Security

The "Golden Rules" for managing Azure DevOps in large corporate environments.

## The Sandbox Strategy
- **NEVER** dry-run in production if a sandbox Org/Project is available.
- **Cloning:** Use for destructive tests (e.g., deleting fields, changing process models).
- **Validation:** Run 100% of the migration in Sandbox before scheduling Production.

## Freeze Windows & Change Management
- **Short Freeze:** A brief period (2-4 hours) where no one edits Work Items during the final migration run.
- **Communication:** Notify teams clearly about the freeze and the TO-BE process changes.
- **Rollback Plan:** Have a "Kill Switch" (e.g., stop the migration tool, restore from a manual backup if applicable).

## Data Preservation (E2E Validation)
- **ReflectedWorkItemId:** Always store the Source ID in the Target Work Item.
- **History Logs:** Keep a JSON log of every item migrated (Source ID -> Target ID).
- **Acceptance (UAT):** Have the PO/Lead of the area sign off on a sample of 20 items after the Sandbox run.

## References
- [Security best practices for Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/organizations/security/security-best-practices?view=azure-devops)
- [Plan a migration to Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/migrate/migration-overview?view=azure-devops)
