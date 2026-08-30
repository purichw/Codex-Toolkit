---
name: usage-budget-gate
description: Thin compatibility router for proportional effort and usage-budget decisions now owned by efficient-execution. Use when the user asks to avoid high usage, make work cheaper/faster, decide fast versus deep mode, set stop rules, define escalation triggers, or prevent broad audits from running unnecessarily.
---

# Usage Budget Gate

This skill remains so existing prompts that mention `$usage-budget-gate` still
route correctly. The actual proportional-effort workflow now lives in
`$efficient-execution`.

## Workflow

1. Read and apply `$efficient-execution`.
2. Use its depth modes, preflight gate, stop rules, reuse rules, and escalation
   triggers.
3. Return here only to preserve the user-facing name `$usage-budget-gate` in a
   closeout or docs update.

## Closeout

Report the depth used, evidence collected, checks skipped with reasons,
escalations triggered or avoided, residual risk, and the next cheapest safe
step, following `$efficient-execution`.
