---
name: usage-budget-gate
description: Choose and communicate the right work depth before spending heavily on project discovery, UI/UX audit, Claude-to-a-tee parity, regression hunts, release checks, UAT, screenshots, test suites, or deploy verification. Use when the user asks to avoid high usage, make work cheaper/faster, decide fast versus deep mode, set stop rules, define escalation triggers, or prevent broad audits from running unnecessarily.
---

# Usage Budget Gate

Use this skill before work that could expand into a large audit or long
verification loop. The goal is to cap waste while keeping quality proportional
to risk.

Use `$efficient-execution` for the execution loop after choosing depth,
`$release-gate` before commit/push/deploy, `$project-onboarding` for repo
intake, `$claude-to-a-tee` for strict parity, `$ui-ux-orchestrator` for UI/UX
routing, and `$uat-environment` when production-like evidence is needed.

## Depth Modes

- **Fast pass:** narrow answer or edit. Read owner files only, run targeted
  checks, disclose skipped broader checks.
- **Standard pass:** normal implementation. Read relevant docs/source, run
  targeted tests/build/browser evidence for touched risk.
- **Deep pass:** architecture, Claude parity, UX contract inventory, regression
  family, auth/data/admin risk, or broad refactor. Build ledgers and wider
  evidence before editing or shipping.
- **Release pass:** commit/push/deploy/PR/handoff. Verify the diff and target
  environment with `$release-gate`; do not repeat unrelated discovery.

## Preflight

Before heavy work, state this compact gate:

```text
Proposed depth:
Why:
Evidence needed:
Stop rule:
Escalate only if:
Checks intentionally skipped:
User-visible risk:
```

For tiny obvious tasks, this can be one sentence. For high-risk work, make it an
explicit plan before spending the tokens.

## Risk Classifier

- **Low:** docs/copy/static metadata, tiny style tweak, isolated non-runtime
  change. Prefer fast pass.
- **Medium:** narrow runtime logic, one UI component, one route, one asset batch,
  one form or flow with known ownership. Prefer standard pass.
- **High:** auth, permissions, data migrations, admin/destructive operations,
  payment/financial logic, deploy config, shared contracts, native/web parity,
  Claude-to-a-tee, broad redesign, or production release. Use deep or release
  pass.

## Stop Rules

Stop discovery and act when you know:

- owner files and nearby tests;
- data/auth/runtime surface touched;
- relevant commands and dev server path;
- verification evidence required for the risk;
- rollback or recovery path when applicable.

Stop verification when the highest-risk touched surface is covered and skipped
checks are disclosed. Do not keep running broad checks just because they exist.

## Escalation Triggers

Escalate depth only when evidence demands it:

- docs conflict with code or ownership is unclear;
- targeted checks fail or are flaky;
- touched files are shared primitives/contracts;
- auth/data/admin/destructive/deploy risk appears;
- UI work affects product UX contracts, mobile, accessibility, or visual parity;
- generated assets/manifests or lockfiles changed;
- user asks to commit, push, deploy, merge, or release.

## Reuse Rules

Reuse previous evidence only when source identity still matches: same commit or
diff, same reference hash, same build/version, same URL, same viewport, same
auth/data state, and no relevant edits since capture. Stale screenshots, old
test runs, and old preview URLs do not save budget.

## Closeout

Report the depth used, evidence collected, checks skipped with reasons,
escalations triggered or avoided, residual risk, and the next cheapest safe
step.
