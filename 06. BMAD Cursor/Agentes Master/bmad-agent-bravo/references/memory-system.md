# Bravo: Memory System

Bravo uses a memory sidecar to track long-running migrations, project-specific TO-BE processes, and "Freeze" windows.

## Sidecar Structure
Location: `{project-root}/_bmad/memory/bmad-agent-bravo-sidecar/`

### index.md
The entry point for memory. It should link to:
- `active-migrations.md`: Ongoing work, batches, and progress.
- `de-para-mappings.md`: AS-IS to TO-BE mapping history.
- `freeze-calendar.md`: Scheduled windows and impacted projects.
- `audit-history.md`: Results of previous Auditor runs.

## Access Boundaries
Bravo has Read/Write access to:
- `{project-root}/_bmad/`
- Current ADO configuration files.

Bravo has Read-Only access to:
- Source code in `{project-root}/` (for Pipeline review).
