---
name: rollback-guardrail
description: Risk-tiered guardrail for rollback, revert, reset, remove, undo, discard, or direction changes that could lose work, rewrite history, remove product behavior, or affect data. Classify routine reversible edits and pauses without unnecessary checkpoints; require recovery and concrete authorization for destructive or ambiguous work-loss operations.
---

# Rollback Guardrail

Protect in-progress work from being silently lost or orphaned. This skill is a
hard stop before risky rollback-like operations.

## Trigger

Classify actual effects before acting on rollback-like wording, including:

- rollback, revert, reset, undo, discard, remove, delete, back out, strip,
  "go back", "restore previous", "take it out"
- Thai equivalents such as ถอยกลับ, ย้อนกลับ, เอาออก, ลบออก, ถอด,
  กลับไปก่อนหน้า, เปลี่ยนทิศกลางคัน
- changing direction in a way that might discard partially complete work
- replacing live UI with a prototype, or removing a Claude/Figma/reference UI
  integration
- commit/push/deploy after a risky rollback-like action

## Risk Routing

- **Pause or discussion only:** stop as requested, preserve files, and report
  unfinished work if useful. No checkpoint or confirmation is needed merely to
  pause. A new priority does not authorize discarding the previous work.
- **Routine reversible edit:** a clearly requested, localized adjustment whose
  exact diff is understood, such as restoring one CSS value just changed by the
  agent. Inspect status and the owner diff, preserve unrelated work, make the
  scoped edit, and run targeted verification. No parking-lot file or checkpoint
  is required when no work, feature, data, or history can be lost.
- **Risky or uncertain loss:** broad rollback, destructive commands, deleting
  files/features/tests, overwriting others' edits, history rewrites, data loss,
  partially wired integration removal, or unclear ownership/impact. Use the hard
  stop below. Uncertainty does not qualify for the routine path.

These tiers do not override project/user safety rules. When those require exact
command disclosure and fresh approval for deletion or other destructive work,
obtain it even for a small change. A checkpoint never grants authorization.

## Hard Stop Protocol

Do not perform a risky rollback-like operation until these steps are complete.

1. Inspect current state.
   - Run `git status --short --branch`.
   - Inspect changed filenames and relevant recent diff.
   - Identify uncommitted work, untracked files, generated artifacts, and
     partially wired features.

2. Explain exact impact, action, and checkpoint location before mutation.
   - State the files, behavior, UI, data, or history that will disappear or be
     parked and the exact command/action proposed.
   - Obtain concrete current-turn approval where required. Do not reinterpret
     a vague "go back" or "change direction" as permission to discard work.
   - Existing approval suffices only for the exact scope/action accepted and
     only if stricter project/user rules do not require another confirmation.
   - Checkpoint writes outside the project also need permission when project
     rules require it. Stop if safe authorized recovery cannot be prepared.

3. Create a recoverable checkpoint before the risky operation.
   - Use an authorized, non-overwriting location outside the operation's scope.
     Do not call this non-mutating: it writes recovery files.
   - Save status, affected filenames, binary working-tree and staged diffs, and
     copies of relevant untracked files; a diff alone does not save untracked
     content. Keep secrets out of committed notes and shared artifacts.
   - For history changes record original refs; create a local checkpoint branch
     when authorized and useful. A branch alone does not save uncommitted work.
   - For data changes use a verified data backup/recovery procedure; a Git
     checkpoint does not protect database state.
   - Confirm the checkpoint exists and covers the affected work. Do not create
     a WIP commit of unrelated changes without explicit authorization.

4. Write a restore note.
   - If the repo has `docs/`, use `docs/rollback-parking-lot.md`.
   - Otherwise use a short project-local markdown note or the checkpoint folder.
   - Record:
     - timestamp and request
     - checkpoint path/branch
     - features or files being parked
     - what will be removed from live routes
     - what remains as prototype/component/docs
     - restore checklist and verification needed

5. After rollback, verify the intended surface.
   - Run the smallest relevant build/test/smoke.
   - For product UI use `$snapshot` automatically on the actual affected route
     and exercise changed behavior, not only a detached prototype. For an
     explicitly standalone artifact, verify that artifact without inventing a
     live-product integration requirement.
   - Update or close the parking-lot item only when the feature is restored,
     intentionally abandoned, or explicitly accepted as parked.

## Release Guard

Before commit, push, deploy, or handoff after risky rollback-like work:

- Stop if the parking lot has unresolved items that affect the requested
  release surface and the user has not accepted them.
- Stop if live integration is required but a new/prototype UI has no route and
  interaction evidence proving it is wired into the app.
- Stop if the rollback removed tests/smoke coverage for a feature that remains
  expected product behavior.
- Report the checkpoint path and restore note in the release summary.
- Apply `$release-gate` to every active deliverable and required check. A
  checkpoint or accepted parked item does not excuse a failed required check.

For a routine reversible edit, release with its targeted evidence and brief risk
classification; do not demand a nonexistent checkpoint or restore note.

## Impact Statement Template

```text
Rollback guardrail:
- Risk tier / exact action:
- Checkpoint:
- Restore note:
- Will remove from live app:
- Will keep parked as:
- Must restore later:
- Verification after rollback:

Proceed with this rollback?
```
