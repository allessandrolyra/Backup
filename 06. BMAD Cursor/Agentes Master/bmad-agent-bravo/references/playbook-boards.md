# Playbook: Boards & Process Customization

This playbook covers the management and standardization of Azure Boards and Process templates.

## Process TO-BE (Standardization)
1. **Inherited Process:** Always prefer creating a new process inherited from Agile/Scrum/Basic rather than modifying the system process.
2. **Work Item Types (WIT):**
   - **Epic:** Portfolio level (multi-team).
   - **Feature:** Deliverable level (single team).
   - **PBI / User Story:** Unit of work.
   - **Task / Bug:** Technical/Defect tracking.
3. **Custom Fields:**
   - Prefix fields with `Org.` (e.g., `Org.ReflectedWorkItemId`, `Org.BusinessValue`).
   - Use correct data types (Picklist, Boolean, Integer, HTML/Rich text).
4. **States & Rules:**
   - Standardize states (New, Active, Resolved, Closed).
   - Add rules for automation (e.g., "Set Resolved By when state changes to Resolved").

## Board Configuration
- **Columns:** Map columns to WIT States accurately.
- **Swimlanes:** Use for priority (Expedite) or work streams.
- **Card Styling:** Highlight stale items (e.g., "Changed Date > 30 days").
- **Tags:** Use tags for temporary metadata (e.g., `Phase-1`, `Migration-Batch-A`).

## References
- [Customize an inherited process](https://learn.microsoft.com/en-us/azure/devops/boards/process/customize-process?view=azure-devops)
- [Configure and customize Azure Boards](https://learn.microsoft.com/en-us/azure/devops/boards/get-started/plan-track-work?view=azure-devops)
