---
name: release-gate
description: Verify changes before commit, push, deploy, release, or handoff. Use when the user asks to commit, push, deploy, ship, release, merge, open a PR, check readiness, or make sure a feature is safe; also use after substantial code, UI, data, auth, or configuration changes before publishing.
---

# Release Gate

Block avoidable releases by collecting evidence before publishing. Keep the gate
proportional to risk, but do not skip checks silently.

## Scope

1. Confirm the intended release target: branch, PR, production, preview, package,
   static artifact, or docs-only.
2. Inspect `git status --short`, staged files, unstaged files, and recent diff.
   Do not include unrelated user changes without explicit intent.
3. Identify affected surfaces: UI, API, data model, auth, build config,
   deployment config, docs, tests, generated assets.

## Required Checks

- Run formatting/lint/typecheck/tests/build commands that the repo defines or
  that match the touched risk.
- For frontend changes, run the app and verify with a browser automation skill
  when available. Capture screenshots or interaction evidence for visual work.
- For deploy work, use the platform's deployment skill/tooling when available
  and verify the resulting URL, not only the local build.
- Check browser console and failed network/asset requests for web releases.
- Confirm environment variables, migrations, cron jobs, storage, or feature
  flags when touched.

## Decision

Proceed only when:

- diffs match the requested scope;
- tests/builds pass or failures are unrelated and disclosed;
- key interactions still work;
- visual changes have browser evidence when relevant;
- deploy target is known and reachable;
- rollback or recovery path is obvious for risky changes.

If a check cannot run, state exactly why and decide whether the remaining
evidence is enough for the user's requested release action.

## Commit And Deploy Hygiene

- Use concise commit messages describing the behavior or docs changed.
- Push the current branch only when asked or when repo policy requires it.
- Deploy only when asked or already authorized by the task.
- After deploy, verify production/preview URL and report commit SHA, deploy URL,
  checks run, and any skipped coverage.
