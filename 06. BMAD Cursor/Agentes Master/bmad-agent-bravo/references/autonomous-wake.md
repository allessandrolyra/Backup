# Bravo: Autonomous Wake

When Bravo runs in headless mode (`--headless` or `-H`), it follows this autonomous logic.

## Named Tasks

### `-H:audit`
1. Load memory and configuration.
2. Run `Auditor` mode on all projects defined in scope.
3. Generate a report in `{project-root}/_bmad/reports/bravo-audit-{date}.md`.
4. Update memory with new findings.

### `-H:pulse`
1. Check for active migrations in memory.
2. Query ADO for the status of recent batches.
3. Report progress and any blocked items to the user via notification/log.

### `-H:validate`
1. Review all recently modified YAML pipelines or WIQL queries in the project.
2. Run `validate-wiql.py` on any new queries found.
3. Log inconsistencies in `{project-root}/_bmad/logs/bravo-validation.log`.

## Default Managed Behavior
If run with `-H` and no task, Bravo will perform a `pulse` check on all active projects in memory.
