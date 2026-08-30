---
name: efficient-execution
description: Choose, explain, and execute the smallest quality-preserving workflow across coding, docs, QA, assets, project discovery, UI/UX audit, commit, push, deploy, and handoff work. Use when the user asks to go faster, reduce usage, avoid over-auditing, choose fast/standard/deep/release depth, batch or parallelize checks, reuse prior evidence, define stop rules, or optimize release workflows without increasing risk.
---

# Efficient Execution

Move faster by removing waste, not by removing evidence. Use this skill as a
thin operating layer with domain skills such as `$project-onboarding`,
`$release-gate`, `$claude-to-a-tee`, `$mobile-web-qa`, `$uat-environment`, or
project-specific skills.

## Core Rule

Keep the acceptance bar unchanged. Speed comes from cutting repeated discovery,
irrelevant checks, stale ceremony, serial reads that can run in parallel, and
verification that does not cover the changed risk.

Never hide skipped checks. If a check is not run, say why and what risk remains.

## Depth Modes

- **Fast pass:** tiny answer or edit. Read owner files and nearby selectors only,
  run `git diff --check`, and use one targeted browser/computed-style/snapshot
  check only when the change is visible.
- **Standard pass:** one component, one route, one flow, one asset batch, or
  narrow runtime logic. Read relevant source and run targeted checks for the
  touched risk.
- **Deep pass:** architecture, auth, data/admin/CMS contracts, cache/fallback
  behavior, routing, broad shared logic, migrations, destructive actions,
  Claude-to-a-tee parity, or broad redesign. Build wider evidence before editing
  or shipping.
- **Release pass:** commit, push, deploy, PR, merge, release, or handoff. Verify
  the diff and target environment with `$release-gate`; do not repeat unrelated
  discovery.

Before expensive discovery, broad test suites, multi-route QA, or many
screenshots, state:

```text
Proposed depth:
Why:
Evidence needed:
Stop rule:
Escalate only if:
Checks intentionally skipped:
User-visible risk:
```

## Fast Loop

1. Restate the user target and the deliverable: answer, edit, commit, push,
   deploy, UAT, visual proof, handoff, or docs.
2. Classify the highest touched risk: docs/static, narrow code, runtime code,
   frontend UI, auth/data/API/config, generated assets, or production deploy.
3. Reuse trustworthy context only when the source still matches: same commit or
   diff, same reference hash, same build/version, same URL, same viewport, same
   auth/data state, or same generated manifest.
4. Choose the smallest evidence path that could catch a real failure for that
   risk. Prefer repo-defined targeted commands, affected-package filters,
   nearest tests, extractor manifests, and focused browser checks before broad
   suites.
5. Parallelize independent reads and checks. Use `rg`/`rg --files` for search,
   batch file reads, and keep long-running servers only when they are useful.
6. Stop discovery once you know the owner files, data/runtime surface, relevant
   commands, verification path, and likely rollback. Implement instead of
   continuing to tour the project.
7. Verify the riskiest surface, then report evidence, skips, and residual risk.

## Fast Path Matrix

- **Docs/static:** inspect diff, run lightweight lint/checks only if defined or
  publishing docs as an artifact.
- **Narrow code:** read the owner files and nearest tests; run targeted
  lint/type/test first.
- **Runtime/shared code:** add or run focused regression coverage, then escalate
  to broader build/typecheck when shared contracts changed.
- **Frontend UI:** verify the changed route and primary interaction first; add
  viewport and screenshot coverage for responsive or visual-risk changes.
- **Auth/data/API/config/admin:** test allow and deny paths, persistence/reload,
  migrations/rules/env boundaries, and rollback before release.
- **Generated assets:** audit mappings and representative rendered usage before
  broad regeneration.
- **Deploy:** use `$release-gate` and verify the deployed URL or artifact; use
  `$uat-environment` for production-like evidence only when it reduces risk.

## Escalation Triggers

Run the deeper path when any of these appear:

- unknown ownership, stale docs, or conflicting handoffs;
- lockfile/dependency/build config changes;
- auth, permissions, secrets, billing, destructive operations, migrations, or
  production data risk;
- shared helpers, cross-client contracts, or generated manifests;
- visual parity, Claude-to-a-tee, mobile layout, or accessibility claims;
- flaky targeted results or missing focused tests for a risky change;
- production deploy, PR merge, or user-visible release.

Stop verification when the highest-risk touched surface is covered and skipped
broader checks are disclosed. Do not keep running broad checks just because they
exist.

## Do Not Save Time By

- skipping a selected skill's `SKILL.md`;
- ignoring unrelated user changes or staging unrelated files;
- using screenshots, dev servers, manifests, or build logs from stale source;
- treating UI-hidden controls as security;
- bypassing auth when auth or permissions are the feature under test;
- using production as UAT;
- shipping inert mock controls where the product needs real behavior;
- lowering safety, compliance, visual parity, or data integrity requirements.

## Closeout

Use this compact shape when speed decisions matter:

```text
Target:
Depth chosen:
Evidence reused:
Checks run:
Checks skipped and why:
Escalations triggered:
Residual risk:
Next fastest safe step:
```
