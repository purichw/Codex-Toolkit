# Codex Toolkit

A private collection of custom Codex skills for project onboarding, release
checks, Firebase work, visual parity, QA, and project-specific operating
playbooks.

Each skill lives under `skills/<skill-name>/` and contains a `SKILL.md` file.
Some skills also include reference notes, helper scripts, or agent metadata.

## Documentation

- [Codex context](docs/CODEX_CONTEXT.md): future-agent orientation, source of
  truth, and safe update workflow.
- [Skill catalog](docs/SKILL_CATALOG.md): fuller descriptions and usage context
  for each skill.
- [Installation and usage](docs/INSTALLATION.md): how to install skills locally
  and use the toolkit from another machine.
- [Maintenance guide](docs/MAINTENANCE.md): how to refresh, add, review, and
  publish changes to this repository.
- [Docs index](docs/README.md): quick map of the documentation set.

## Skills

| Skill | Short description | Use when |
| --- | --- | --- |
| [`claude-to-a-tee`](skills/claude-to-a-tee/SKILL.md) | Reproduces an offline Claude Design HTML reference at component level while preserving product behavior. | A UI must match a Claude-generated HTML design, screenshot, or handoff exactly across desktop and mobile. |
| [`coin-quest-admin-ops`](skills/coin-quest-admin-ops/SKILL.md) | Keeps Coin Quest Ledger Admin Portal work aligned with current Firebase-backed admin behavior. | Editing admin auth, boards, users, lifecycle actions, reset/delete flows, publish/restore, revisions, or relationship maps. |
| [`coin-quest-ledger-logic`](skills/coin-quest-ledger-logic/SKILL.md) | Preserves Party Ledger split math, participants, guests, invites, Character IDs, and settlement behavior. | Changing Coin Quest ledger workflows, guest handling, invite links, reminders, payer/participant logic, or settlement tests. |
| [`coin-quest-native-parity`](skills/coin-quest-native-parity/SKILL.md) | Prevents the Coin Quest Expo app from drifting away from web data contracts and native parity requirements. | Working on the native app, iOS/Android build gates, `playerModules`, or native/web backend parity. |
| [`docs-cartographer`](skills/docs-cartographer/SKILL.md) | Creates useful maps of routes, modules, data flow, commands, ownership boundaries, and handoff context. | A project needs architecture docs, site maps, onboarding docs, interaction maps, or better navigation for future sessions. |
| [`firebase-account-management`](skills/firebase-account-management/SKILL.md) | Separates Firebase billing, Auth, Firestore, Admin SDK, and account-management concerns. | Designing, auditing, or debugging signup/login, user profiles, admin CRUD, custom claims, or Spark vs Blaze assumptions. |
| [`firebase-security-rules`](skills/firebase-security-rules/SKILL.md) | Audits Firebase Auth, Firestore Rules, Admin SDK endpoints, service accounts, and production access guarantees. | Reviewing or changing Firestore rules, privileged backend behavior, auth gates, secrets, or Firebase security posture. |
| [`image-boundary-iteration`](skills/image-boundary-iteration/SKILL.md) | Guides controlled adult non-explicit image iteration with branch-specific prompt strategy, verdicts, and logging. | Continuing the nudity-reference-prompting workflow, handling Pass/Partial/Reject loops, local edits, or visual baseline tracking. |
| [`mobile-web-qa`](skills/mobile-web-qa/SKILL.md) | Audits responsive web interfaces across phone, tablet, and desktop viewports. | Checking mobile Safari/Chrome behavior, safe areas, keyboard states, tap targets, overflow, modals, or pre-deploy frontend QA. |
| [`notenwert-design-direction`](skills/notenwert-design-direction/SKILL.md) | Preserves Notenwert's editorial cultural-network visual direction and reference system. | Designing or critiquing Notenwert public/admin UX, homepage hero motion, NGA-style interactions, typography, color, or imagery. |
| [`notenwert-maintainer`](skills/notenwert-maintainer/SKILL.md) | Provides the safe operating playbook for the Notenwert codebase. | Fixing bugs, editing CMS/admin behavior, changing content models, preparing deploys, updating docs, or making commits in Notenwert. |
| [`project-onboarding`](skills/project-onboarding/SKILL.md) | Builds a compact, reliable map of an unfamiliar or returning codebase before edits. | Starting work in a repo, reading handoffs, finding commands, understanding architecture, or preparing a safe implementation plan. |
| [`regression-hunter`](skills/regression-hunter/SKILL.md) | Searches for related bug patterns after one issue reveals a possible class of regressions. | Auditing for similar hardcoded values, duplicated logic, fragile selectors, stale fixtures, or nearby behavior breaks. |
| [`release-gate`](skills/release-gate/SKILL.md) | Collects proportional verification evidence before commit, push, deploy, release, or handoff. | Shipping changes, opening PRs, deploying, merging, or checking whether a feature is ready to publish. |
| [`shane-thai-image-assets`](skills/shane-thai-image-assets/SKILL.md) | Manages vocabulary image generation, reuse, cropping, optimization, and QA for the Shane and His Thai app. | Adding or replacing lesson artwork, mapping assets, fixing crops, generating Unit images, or deciding whether existing art is semantically correct. |

## Installing A Skill

Copy or symlink a skill folder into your Codex skills directory:

```sh
cp -R skills/project-onboarding ~/.codex/skills/project-onboarding
```

## Updating This Repo

The source-of-truth local skills currently live in `~/.codex/skills`. To refresh
the repository copy, sync the personal skill folders into `skills/`, review the
diff, then commit.
