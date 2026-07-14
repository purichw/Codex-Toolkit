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
| [`accessible-interaction`](skills/accessible-interaction/SKILL.md) | Verifies keyboard, focus, semantic controls, ARIA state, contrast, touch targets, and modal/drawer accessibility. | Visual or interaction changes could break non-pointer use, focus order, screen-reader-visible state, or mobile keyboard behavior. |
| [`admin-ops`](skills/admin-ops/SKILL.md) | Guides admin portal operations, privileged actions, lifecycle flows, auditability, and CMS/admin UX. | Designing, auditing, implementing, or verifying admin surfaces that change real data, permissions, content, or operational state. |
| [`claude-to-a-tee`](skills/claude-to-a-tee/SKILL.md) | Reproduces an offline Claude Design HTML reference at component level while preserving product behavior. | A UI must match a Claude-generated HTML design, screenshot, or handoff exactly across desktop and mobile. |
| [`coin-quest-admin-ops`](skills/coin-quest-admin-ops/SKILL.md) | Keeps Coin Quest Ledger Admin Portal work aligned with current Firebase-backed admin behavior. | Editing admin auth, boards, users, lifecycle actions, reset/delete flows, publish/restore, revisions, or relationship maps. |
| [`coin-quest-ledger-logic`](skills/coin-quest-ledger-logic/SKILL.md) | Preserves Party Ledger split math, participants, guests, invites, Character IDs, and settlement behavior. | Changing Coin Quest ledger workflows, guest handling, invite links, reminders, payer/participant logic, or settlement tests. |
| [`coin-quest-native-parity`](skills/coin-quest-native-parity/SKILL.md) | Prevents the Coin Quest Expo app from drifting away from web data contracts and native parity requirements. | Working on the native app, iOS/Android build gates, `playerModules`, or native/web backend parity. |
| [`course-image-assets`](skills/course-image-assets/SKILL.md) | Manages educational course image generation, reuse, mapping, crop fixes, audits, and QA. | Working on vocabulary images, lesson card art, visual hints, badges, semantic mappings, or generated educational illustrations. |
| [`data-dense-ux`](skills/data-dense-ux/SKILL.md) | Guides dense dashboards, tables, lists, ledgers, filters, pagination, bulk actions, and operational panels. | Users need to scan, compare, sort, select, or operate large amounts of information without losing clarity. |
| [`design-direction`](skills/design-direction/SKILL.md) | Defines, critiques, or preserves product visual direction across projects. | Creating design briefs, redesign strategy, visual north stars, guardrails, Claude Design prompts, or implementation handoff guidance. |
| [`design-system-guardian`](skills/design-system-guardian/SKILL.md) | Preserves reusable components, tokens, variants, typography, spacing, icons, radius, shadow, and visual consistency. | UI changes risk component drift, one-off CSS, variant sprawl, or breaking existing primitives while adopting a reference design. |
| [`docs-cartographer`](skills/docs-cartographer/SKILL.md) | Creates useful maps of routes, modules, data flow, commands, ownership boundaries, and handoff context. | A project needs architecture docs, site maps, onboarding docs, interaction maps, or better navigation for future sessions. |
| [`efficient-execution`](skills/efficient-execution/SKILL.md) | Chooses the fastest workflow that still preserves the required evidence and quality bar. | Work feels slow, checks need batching, context can be reused, or a task needs a smaller safe path without hiding risk. |
| [`export-html`](skills/export-html/SKILL.md) | Creates live-parity standalone/offline HTML exports and clickable prototypes. | Exporting product screens, design handoffs, Claude/Figma-inspectable HTML, visual audit files, or representative UI states. |
| [`firebase-account-management`](skills/firebase-account-management/SKILL.md) | Separates Firebase billing, Auth, Firestore, Admin SDK, and account-management concerns. | Designing, auditing, or debugging signup/login, user profiles, admin CRUD, custom claims, or Spark vs Blaze assumptions. |
| [`firebase-security-rules`](skills/firebase-security-rules/SKILL.md) | Audits Firebase Auth, Firestore Rules, Admin SDK endpoints, service accounts, and production access guarantees. | Reviewing or changing Firestore rules, privileged backend behavior, auth gates, secrets, or Firebase security posture. |
| [`form-flow-ux`](skills/form-flow-ux/SKILL.md) | Covers complete create/edit form journeys including validation, dirty state, autosave, save/cancel, errors, and mobile keyboard. | A form must work as a real workflow, not only as a visually finished screen. |
| [`image-boundary-iteration`](skills/image-boundary-iteration/SKILL.md) | Guides controlled adult non-explicit image iteration with branch-specific prompt strategy, verdicts, and logging. | Continuing the nudity-reference-prompting workflow, handling Pass/Partial/Reject loops, local edits, or visual baseline tracking. |
| [`interaction-flow-qa`](skills/interaction-flow-qa/SKILL.md) | Exercises real journeys end to end across routing, state, data, permissions, feedback, reload, and back behavior. | Search/detail, onboarding, admin create/edit/publish, modal/drawer, destructive, playback, or completion flows must actually work. |
| [`ledger-logic`](skills/ledger-logic/SKILL.md) | Protects collaborative ledger math, identity, guests/invites, persistence, and settlement outputs. | Implementing, auditing, or debugging expenses, splits, payer/participant logic, reciprocal netting, import/export, or ledger tests. |
| [`mobile-web-qa`](skills/mobile-web-qa/SKILL.md) | Audits responsive web interfaces across phone, tablet, and desktop viewports. | Checking mobile Safari/Chrome behavior, safe areas, keyboard states, tap targets, overflow, modals, or pre-deploy frontend QA. |
| [`native-parity`](skills/native-parity/SKILL.md) | Keeps native iOS/Android apps aligned with web/product source-of-truth behavior. | Working on Expo/React Native builds, native screen parity, shared backend contracts, device gates, or static sample-app drift. |
| [`notenwert-design-direction`](skills/notenwert-design-direction/SKILL.md) | Preserves Notenwert's editorial cultural-network visual direction and reference system. | Designing or critiquing Notenwert public/admin UX, homepage hero motion, NGA-style interactions, typography, color, or imagery. |
| [`notenwert-maintainer`](skills/notenwert-maintainer/SKILL.md) | Provides the safe operating playbook for the Notenwert codebase. | Fixing bugs, editing CMS/admin behavior, changing content models, preparing deploys, updating docs, or making commits in Notenwert. |
| [`placeholder-image`](skills/placeholder-image/SKILL.md) | Sources, selects, replaces, crops, and audits placeholder images as real product content. | Populating missing images, replacing weak stock, finding hero/card/gallery photos, fixing crops, or creating image sourcing playbooks. |
| [`product-ux-contracts`](skills/product-ux-contracts/SKILL.md) | Preserves proven product UX contracts while redesigning, restyling, refactoring, or implementing reference UI. | Routing, persistence, scroll, focus, permissions, destructive safety, media fallbacks, or search click-through could be flattened. |
| [`project-onboarding`](skills/project-onboarding/SKILL.md) | Builds a compact, reliable map of an unfamiliar or returning codebase before edits. | Starting work in a repo, reading handoffs, finding commands, understanding architecture, or preparing a safe implementation plan. |
| [`regression-hunter`](skills/regression-hunter/SKILL.md) | Searches for related bug patterns after one issue reveals a possible class of regressions. | Auditing for similar hardcoded values, duplicated logic, fragile selectors, stale fixtures, or nearby behavior breaks. |
| [`release-gate`](skills/release-gate/SKILL.md) | Collects proportional verification evidence before commit, push, deploy, release, or handoff. | Shipping changes, opening PRs, deploying, merging, or checking whether a feature is ready to publish. |
| [`shane-thai-audio-generator`](skills/shane-thai-audio-generator/SKILL.md) | Generates, regenerates, audits, and QA-checks Google Chirp audio for Shane and His Thai. | Working on lesson audio, Thai TTS text, audio IDs, voice selection, missing/stale audio, or naturalness fixes. |
| [`shane-thai-image-assets`](skills/shane-thai-image-assets/SKILL.md) | Manages vocabulary image generation, reuse, cropping, optimization, and QA for the Shane and His Thai app. | Adding or replacing lesson artwork, mapping assets, fixing crops, generating Unit images, or deciding whether existing art is semantically correct. |
| [`site-maintainer`](skills/site-maintainer/SKILL.md) | Maintains website projects where source, generated artifacts, tests, docs, and hosting outputs must stay aligned. | Working on static/built sites, generated deploy folders, CMS/admin site work, build scripts, deploy prep, or work logs. |
| [`snapshot`](skills/snapshot/SKILL.md) | Captures, crops, inspects, and presents screenshots with enough context for review. | Producing UI screenshots, visual proof, before/after comparisons, viewport captures, or production smoke evidence. |
| [`tts-audio-assets`](skills/tts-audio-assets/SKILL.md) | Manages text-to-speech audio generation, reuse, audit, naturalness QA, and data wiring across projects. | Working on lesson audio, UI playback, dialogues, prompts, voice/pacing policy, stale/missing audio, or audio IDs. |
| [`uat-environment`](skills/uat-environment/SKILL.md) | Defines lightweight preview/UAT environments, seeded test data, auth policy, and promotion evidence. | A frontend, admin, data, auth, asset, or deployment change needs production-like verification before release. |
| [`ui-state-matrix`](skills/ui-state-matrix/SKILL.md) | Defines and verifies UI states beyond the happy path: focus, selected, disabled, loading, empty, error, success, denied, long text, and responsive states. | A component or flow can look finished but still needs state coverage before UI work is complete. |
| [`ui-ux-orchestrator`](skills/ui-ux-orchestrator/SKILL.md) | Routes broad or blurry UI/UX requests to the smallest useful set of design, UX, state, accessibility, flow, and QA skills. | The user asks for UI/UX polish, audits, planning, visual QA, Claude/Figma handoffs, or is unsure which UI/UX skill applies. |

## Installing A Skill

Copy or symlink a skill folder into your Codex skills directory:

```sh
cp -R skills/project-onboarding ~/.codex/skills/project-onboarding
```

## Updating This Repo

The source-of-truth local skills currently live in `~/.codex/skills`. To refresh
the repository copy, sync the personal skill folders into `skills/`, review the
diff, then commit.

Verify the archive with:

```sh
python3 scripts/verify_skills.py --expected-count 36
```
