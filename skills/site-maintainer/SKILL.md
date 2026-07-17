---
name: site-maintainer
description: Maintain website projects safely when source files, generated deploy artifacts, tests, docs, and hosting outputs must stay aligned. Use when the user asks to work on a website repo, static site, built site, generated deploy folder, service worker/version churn, CMS/admin site work, build scripts, deploy prep, commit hygiene, project work logs, or keeping source and production artifacts in sync.
---

# Site Maintainer

Use this skill for website codebases where edits must respect source/build
boundaries and generated deployment artifacts.

## First Checks

1. Identify project root, source folder, generated output folder, build command,
   dev server command, tests, hosting target, and deploy path.
2. Run `git status --short --branch` and protect unrelated user changes.
3. Read project-local operating docs (`AGENTS*`, `README*`, `PLAYBOOK*`,
   `docs/**`, deploy runbooks, codebase maps) before touching source.
4. Use `rg --files` for source discovery.

Use `$project-onboarding` when the repo is unfamiliar, `$docs-cartographer` when
maps/docs should be updated, `$design-direction` for visual direction,
`$claude-to-a-tee` for exact reference parity, `$mobile-web-qa`/`$snapshot` for
visual evidence, and `$release-gate` before commit/deploy.

Use `$efficient-execution` when site work is slowed by repeated discovery,
unnecessary rebuilds, or unclear commit/push/deploy gates. Reuse a healthy dev
server, current project map, and previous build evidence only when they match
the current source, route, target, and environment.

## Source vs Generated

Define:

- editable source files;
- generated artifacts;
- versioned service workers/manifests/cache files;
- public/static assets;
- docs/work logs;
- hosting config and production deploy directory.

Do not edit generated output as the source of truth unless the project explicitly
works that way. After source changes, run the build command and decide whether
generated artifacts belong in the intended diff.

## Task Routing

- **Content/CMS/admin:** verify draft/preview/publish, autosave, permissions,
  media metadata, and public rendering.
- **Homepage/visual hero:** verify motion/reduced-motion, scroll rhythm,
  responsive layout, and visual evidence.
- **Map/list/detail UX:** verify route state, filters, deep links, empty/error
  states, and responsive behavior.
- **External API/embed:** protect tokens, env vars, server proxy, fallback
  states, and deploy secrets.
- **Docs-only:** inspect diff and run docs/lint checks when defined.

## Compatibility

Respect local browser/runtime constraints. When supporting older browsers or
static deploy targets, prefer explicit fallbacks for newer syntax or CSS that
the project avoids. Do not introduce syntax the project compatibility rules ban.

## Verification

Use project-defined commands first:

- build after source changes;
- focused regression/e2e tests for touched behavior;
- browser check for changed routes and visual work;
- console/network/failed asset inspection;
- production/preview smoke only when deploy is requested.

Update work logs or canonical docs when the change affects future maintenance,
design rules, content model, deploy process, or fragile flows.

## Commit Hygiene

Stage only intended source/docs/generated files. Leave unrelated dirty files and
incidental build churn unstaged. Use concise commit messages and push/deploy
only when asked or authorized by repo policy.

## Closeout

Report source files changed, generated artifacts included or excluded, commands
run, browser evidence, docs/work-log updates, deploy status, and residual risk.
