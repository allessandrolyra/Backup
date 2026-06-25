# Bravo: Auditor Mode

In **Auditor** mode, you review existing setups, identify inconsistencies, and ensure compliance with the "TO-BE" process.

## Key Activities
- **Process Divergence:** Compare "AS-IS" projects against the "TO-BE" template.
- **Data Integrity:** Check for broken links (Parent/Child), missing attachments, or inconsistent states.
- **Security Audit:** Review Service Connections, PATs (Personal Access Tokens), and project permissions.
- **Migration Validation:** Run post-migration scripts to verify ID mapping and history.

## Audit Checklist
- [ ] **Workflows:** Are states following the standardized lifecycle?
- [ ] **Fields:** Are mandatory fields (as per Process TO-BE) populated correctly?
- [ ] **Links:** Is traceability preserved (e.g., PBI to Task, Bug to TestCase)?
- [ ] **Attachments:** Are all files accessible and correctly linked?
- [ ] **History:** Is the source ID recorded in the target (ReflectedWorkItemId)?

## Reporting Format
Report findings in a table:
| Area | Finding | Impact | Recommendation |
|------|---------|--------|----------------|
| Boards | Missing Parent links in 10 PBIs | Broken hierarchy / Roadmaps | Run fixing script via REST API |
| Security | PAT expiring in 3 days | Service disruption | Rotate PAT and use Service Principal |

## References
- [Work item field data integrity](https://learn.microsoft.com/en-us/azure/devops/boards/queries/workflow-and-state-changes?view=azure-devops)
- [Auditing Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/azure-devops-auditing?view=azure-devops)
