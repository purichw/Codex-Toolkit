# Codex Toolkit Agent Notes

This repository stores the user's personal Codex skills. Treat it as a personal
toolkit and backup, not as a generic package. The repository is public; the user
confirmed publication of the reviewed skill updates on 2026-10-13.

## First Read

When a future Codex session lands here, read these files before making changes:

1. `README.md` for the public-facing overview.
2. `docs/CODEX_CONTEXT.md` for source-of-truth rules and update workflow.
3. `docs/MAINTENANCE.md` before syncing, committing, or pushing.
4. `docs/SKILL_CATALOG.md` when choosing or documenting skills.

## Source Of Truth

The live personal skills usually live in:

```text
~/.codex/skills
```

This repository is the GitHub copy. Before changing skill content, determine
whether the user wants to edit the live local skill, the repository copy, or
both. If syncing from local skills, exclude `.system` and bundled plugin skills.
If the live local tree does not contain repo-only `global-*` aliases, do not run
a broad delete sync that removes them. Sync changed canonical folders
selectively unless the user explicitly asks to rebuild the global layer.

## UI/UX Design

For any user-facing UI, screen, layout, component, deck, doc, or prototype,
load `/Users/point/.codex/skills/ui-ux-expert/SKILL.md` and follow it. Copy
`/Users/point/.codex/skills/ui-ux-expert/tokens.css` as the default design
system only when the project has no brand, design system, production UI, or
user-provided visual direction.

After UI/UX implementation, redesign, restyle, visual audit, responsive QA,
Claude/Figma/reference handoff, or screenshot-based design work, load and use
`/Users/point/.codex/skills/snapshot/SKILL.md` before the final response. Do
not wait for the user to ask for visual evidence.

## Proportional Effort And Usage Budget

Default to the smallest safe pass for the user's current request. Do not carry
deep-audit, release, or whole-site verification momentum from a previous turn
into a tiny follow-up unless the new request has a fresh escalation trigger.

- Fast pass: for tiny copy, CSS, selector, spacing, typography, or one-off visual
  tweaks. Read only owner files and nearby selectors, make the focused edit, run
  `git diff --check`, and use one targeted browser/computed-style/snapshot check
  only when the change is visible.
- Standard pass: for one component, one route, one flow, or narrow runtime logic.
  Read the relevant source and run targeted checks for the touched risk.
- Deep or release pass: only for architecture, auth, data/admin/CMS contracts,
  cache/fallback behavior, routing, broad shared logic, migrations, destructive
  actions, production, or when the user asks to commit, push, deploy, merge, or
  release.
- Escalate only when targeted evidence requires it: a check fails, ownership is
  unclear, the bug appears across routes or breakpoints, a shared contract is
  changing, or the user explicitly broadens the scope.
- Stop adding checks once each active deliverable has proportionate evidence.
  Report skipped broader checks instead of running them by habit.

Stopping additional checks does not finish the task. Follow `efficient-execution`
to track all active deliverables through interruptions, confirm required
operation results, and align affected companion outputs. Before closing, verify
each requested outcome with proportionate evidence or report its actual blocker;
do not silently drop remaining work after the highest-risk item passes.

## Repository Shape

- `skills/<skill-name>/SKILL.md` is the required skill entrypoint.
- `skills/<skill-name>/references/` holds required supporting notes.
- `skills/<skill-name>/scripts/` holds reusable helpers.
- `skills/<skill-name>/agents/` holds agent metadata.
- `docs/` explains how to use, install, maintain, and understand the toolkit.
- `scripts/verify_skills.py` verifies the archived skill set.

## Safety Rules

- Preserve the user-approved public visibility; do not change visibility without
  explicit authorization. Public publishing still requires the privacy review.
- Review for secrets, service-account files, tokens, passwords, private keys,
  private URLs, personal data, and sensitive project details before pushing.
- Do not add generated caches, system skills, plugin cache contents, or unrelated
  local project files.
- Do not delete, move, overwrite, chmod, chown, or bulk-edit files outside this
  project without explicit approval in the current turn.
- Do not run destructive commands unless the user explicitly requests that exact
  operation. Destructive commands include `rm`, `rm -rf`, `unlink`,
  `git reset --hard`, `git clean`, `git checkout --`, `find -delete`, `trash`,
  and `mv` over existing files.
- Preserve unrelated user changes. Never revert or overwrite changes you did not
  make unless the user explicitly asks.
- Preserve executable bits on helper scripts.
- Use concise commits and push only the intended scope.

## Push And Deploy Authorization

- Before every push or deploy, require an explicit user request or confirmation
  covering that action, the current changes, and the target. If absent or
  unclear, ask and wait for the user's answer before proceeding.
- Instructions to edit, fix, test, prepare a release, or commit do not authorize
  push or deploy. Push and deploy are separate permissions; neither implies the
  other. A clear request for both authorizes both within its stated scope.
- Earlier completed tasks, standing repo policies, handoffs, available tools,
  and passing checks are not authorization for a new push or deploy.
- Before an authorized push, check whether its branch triggers an automatic
  preview or production deployment. If that deployment is not also authorized,
  explain the target and ask before pushing. Apply the same rule to workflow
  dispatches, reruns, and other commands that trigger deployment indirectly.
- Do not ask again for the exact action and scope already explicitly requested.
  When only local work is requested, finish it and report that no push/deploy
  occurred; do not publish merely to complete the workflow.

## Verification

For most changes, run:

```sh
git diff --check
python3 scripts/verify_skills.py --expected-count 141
```

The verifier checks skill frontmatter, folder/name consistency, Markdown links,
helper script syntax, accidental bundled/system paths, and high-confidence
secret patterns.

For skill syncs, also inspect the actual skill list when names may have changed:

```sh
find skills -name SKILL.md | sort
```
