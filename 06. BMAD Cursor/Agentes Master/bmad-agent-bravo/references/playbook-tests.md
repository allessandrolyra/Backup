# Playbook: Test Plans & Suites

Guidelines for managing and migrating Test Plans, Suites, and Cases in Azure DevOps.

## Structure Best Practices
1. **Test Plans:** One per Sprint or Major Release.
2. **Test Suites:**
   - **Static Suites:** Manual organization.
   - **Query-based Suites:** Dynamic (e.g., "All Priority 1 PBI bugs").
   - **Requirement-based Suites:** Linked directly to PBIs/User Stories (Recommended for traceability).
3. **Test Cases:**
   - Use **Shared Steps:** For common actions (Login, Logout).
   - Use **Parameters:** For data-driven testing.

## Reconstruction after Migration
When migrating WITs, Test Plans and Suites often need manual reconstruction or scripted reconnection:
1. Migrate **Test Cases** first as standard WITs.
2. Reconect **Shared Steps** (they have unique IDs).
3. Re-create **Test Plans** and **Suites** in the Target.
4. Bulk-add Test Cases to Suites using the UI or REST API.

## Traceability Validation
Check if the following links are preserved:
- **Tested By:** PBI -> Test Case.
- **Tests:** Test Case -> Parent Requirement.
- **Shared Step:** Test Case -> Shared Step.

## References
- [Create test plans and test suites](https://learn.microsoft.com/en-us/azure/devops/test/create-a-test-plan?view=azure-devops)
- [Add test cases to test suites](https://learn.microsoft.com/en-us/azure/devops/test/add-test-cases-to-test-suites?view=azure-devops)
