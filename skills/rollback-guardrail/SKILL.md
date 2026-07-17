---
name: rollback-guardrail
description: Hard-stop guardrail for rollback, revert, reset, remove, undo, discard, back out, delete-feature, strip-integration, or mid-work direction changes. Use when a user asks to rollback/revert/remove/undo code or says ถอยกลับ, ย้อนกลับ, rollback, revert, เอาออก, ลบออก, ถอด, กลับไปก่อนหน้า, เปลี่ยนทิศกลางคัน, especially while implementation, Claude/prototype UI, uncommitted work, or release/deploy work is in progress.
---

# Rollback Guardrail

Protect in-progress work from being silently lost or orphaned. This skill is a
hard stop before risky rollback-like operations.

## Trigger

Use this skill before acting when the request can remove, undo, or abandon work,
including:

- rollback, revert, reset, undo, discard, remove, delete, back out, strip,
  "go back", "restore previous", "take it out"
- Thai equivalents such as ถอยกลับ, ย้อนกลับ, เอาออก, ลบออก, ถอด,
  กลับไปก่อนหน้า, เปลี่ยนทิศกลางคัน
- stopping or changing direction while implementation is partially complete
- replacing live UI with a prototype, or removing a Claude/Figma/reference UI
  integration
- commit/push/deploy after any rollback-like action

## Hard Stop Protocol

Do not perform the rollback-like operation until these steps are complete.

1. Inspect current state.
   - Run `git status --short --branch`.
   - Inspect changed filenames and relevant recent diff.
   - Identify uncommitted work, untracked files, generated artifacts, and
     partially wired features.

2. Create a recoverable checkpoint before changing files.
   - Prefer a non-mutating checkpoint outside the repo, such as:
     `/tmp/codex-rollback-checkpoints/<repo-name>-<timestamp>/`
   - Save status, changed filenames, `git diff --binary`, staged diff if any,
     and an inventory/copy of relevant untracked files.
   - If the operation affects committed history, also create a local branch
     pointer such as `checkpoint/before-rollback-YYYYMMDD-HHMM`.
   - Do not create a normal WIP commit containing unrelated user changes unless
     the user explicitly asks for that checkpoint style.

3. Write a restore note.
   - If the repo has `docs/`, use `docs/rollback-parking-lot.md`.
   - Otherwise use a short project-local markdown note or the checkpoint folder.
   - Record:
     - timestamp and request
     - checkpoint path/branch
     - features or files being parked
     - what will be removed from live routes
     - what remains as prototype/component/docs
     - restore checklist and verification needed

4. Explain impact and get confirmation.
   - State the exact behavior or UI that will disappear, remain parked, or need
     rewiring later.
   - Ask for confirmation unless the user has already explicitly accepted this
     same concrete impact in the current turn.

5. After rollback, verify the intended surface.
   - Run the smallest relevant build/test/smoke.
   - For UI, capture evidence from the live route, not only a prototype.
   - Update or close the parking-lot item only when the feature is restored,
     intentionally abandoned, or explicitly accepted as parked.

## Release Guard

Before commit, push, deploy, or handoff after rollback-like work:

- Stop if the parking lot has unresolved items that affect the requested
  release surface and the user has not accepted them.
- Stop if a new/prototype UI component exists but there is no live-route
  snapshot or smoke evidence proving it is wired into the app.
- Stop if the rollback removed tests/smoke coverage for a feature that remains
  expected product behavior.
- Report the checkpoint path and restore note in the release summary.

## Impact Statement Template

```text
Rollback guardrail:
- Checkpoint:
- Restore note:
- Will remove from live app:
- Will keep parked as:
- Must restore later:
- Verification after rollback:

Proceed with this rollback?
```
