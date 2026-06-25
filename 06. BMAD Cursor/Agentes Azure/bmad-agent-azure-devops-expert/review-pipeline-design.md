---
name: review-pipeline-design
description: Review pipeline architecture, gates, and delivery risk.
menu-code: RP
---

# Review Pipeline Design

Review the existing delivery pipeline and identify structural, security, and reliability issues.

## Focus Areas

- triggers and branch strategy
- stage separation and job dependencies
- test and quality gates
- artifact handling and environment promotion
- approvals, rollback, and failure containment
- caching, parallelism, and execution efficiency
- platform correctness: Azure Pipelines vs GitHub Actions

## Process

1. Inspect the allowed pipeline files and supporting config
2. Identify risky patterns, anti-patterns, and missing controls
3. Prioritize findings by deployment risk and delivery impact
4. Recommend concrete improvements with rationale
5. If helpful, provide corrected YAML fragments in the right syntax

## Output

Use this structure:

```markdown
# Pipeline Review

## Findings
- risk and impact

## Recommendations
- concrete fix

## Suggested Next Checks
- deterministic validation or testing to run
```

## Autonomous Use

This capability is suitable for autonomous review. If invoked headlessly, produce a concise report and log the outcome to memory.
