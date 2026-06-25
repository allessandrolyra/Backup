---
name: create-cicd-pipeline
description: Design a CI/CD pipeline for Azure delivery workflows.
menu-code: CP
---

# Create CI/CD Pipeline

Design a delivery pipeline for the user's stack and platform without mixing Azure Pipelines syntax with GitHub Actions syntax.

## Gather

- application stack and runtime
- repository model and branching strategy
- build, test, packaging, and deployment requirements
- environments and approval gates
- security or compliance controls
- target platform: `Azure DevOps`, `GitHub Actions`, or hybrid

## Process

1. Confirm the target orchestration platform
2. Propose the pipeline shape: stages, jobs, dependencies, approvals, artifacts, environments
3. Recommend optimization opportunities such as caching, parallelism, and smart triggers
4. Embed security by default: secret handling, pinned versions, least privilege, and required scans
5. Provide a concrete pipeline example in the correct YAML flavor
6. Call out assumptions, rollout path, and rollback path

## Output

Return:
- recommended pipeline architecture
- example YAML
- environment and secret strategy
- risks and follow-up validations

## Deterministic Execution Boundary

If the user wants the YAML linted or validated, invoke an exact registered external skill such as `pipeline-linter` when available. If it is unavailable, say so explicitly.
