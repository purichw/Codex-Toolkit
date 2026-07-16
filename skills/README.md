# Skill Index

This folder contains custom Codex skills. Each subfolder is intended to be usable
as a standalone skill directory under `~/.codex/skills`.

## General Workflow Skills

| Skill | Description | Context |
| --- | --- | --- |
| [`project-onboarding`](project-onboarding/SKILL.md) | Reads project docs, commands, architecture, source layout, and git state before implementation. | Use at the start of work in an unfamiliar or returning repository. |
| [`docs-cartographer`](docs-cartographer/SKILL.md) | Produces living documentation for routes, modules, data flow, interactions, deployment paths, and ownership boundaries. | Use when a codebase needs better maps, handoff notes, or future-maintainer context. |
| [`regression-hunter`](regression-hunter/SKILL.md) | Turns one bug into a targeted search for related patterns and nearby regressions. | Use after finding a suspicious hardcoded value, duplicated behavior, brittle selector, or repeated logic bug. |
| [`release-gate`](release-gate/SKILL.md) | Defines the verification checklist before publishing, committing, pushing, deploying, or handing off work. | Use when changes are about to leave the local working state. |
| [`efficient-execution`](efficient-execution/SKILL.md) | Finds the fastest quality-preserving path by reusing valid context, batching checks, and keeping stop rules explicit. | Use when work needs to move faster without lowering verification, release, or product-quality standards. |
| [`usage-budget-gate`](usage-budget-gate/SKILL.md) | Chooses fast, standard, deep, or release depth before expensive discovery, audit, QA, or deploy verification. | Use when the user wants lower usage, faster work, stop rules, escalation triggers, or a budget-aware scope. |
| [`uat-environment`](uat-environment/SKILL.md) | Defines lightweight production-like preview/UAT targets, seeded data, auth modes, and promotion evidence. | Use when UI, admin, auth/data, asset, or deployment changes need realistic pre-production verification. |
| [`prod-smoke-harness`](prod-smoke-harness/SKILL.md) | Defines safe production/preview smoke harness policy, accounts, HTTP/browser checks, and screenshot evidence. | Use when a web app needs post-deploy smoke checks, Playwright smoke setup, authenticated smoke policy, or reusable production verification. |
| [`production-asset-smoke`](production-asset-smoke/SKILL.md) | Verifies deployed media and asset rendering after image, video, CMS, fallback, or deploy changes. | Use when production or preview pages need proof that images, videos, CSS backgrounds, lazy assets, and fallbacks render correctly. |
| [`mobile-web-qa`](mobile-web-qa/SKILL.md) | Verifies responsive UI across representative mobile, tablet, and desktop viewports. | Use for mobile web bugs, pre-deploy QA, keyboard behavior, overflow, safe areas, and touch interaction checks. |
| [`snapshot`](snapshot/SKILL.md) | Captures screenshots with enough visual context for review. | Use for UI snapshots, before/after evidence, viewport captures, or production smoke proof. |

## Design And Frontend Parity

| Skill | Description | Context |
| --- | --- | --- |
| [`claude-to-a-tee`](claude-to-a-tee/SKILL.md) | Treats offline Claude HTML as executable design documentation and verifies measured component parity. | Use for exact visual implementation from Claude Design exports, screenshots, or handoff files. |
| [`design-direction`](design-direction/SKILL.md) | Defines and preserves product visual direction across projects. | Use for visual north stars, design briefs, redesign strategy, guardrails, Claude prompts, and handoff guidance. |
| [`export-html`](export-html/SKILL.md) | Creates live-parity standalone HTML exports and clickable prototypes. | Use for offline HTML, design handoff, Claude/Figma inspection, or representative UI state review. |
| [`notenwert-design-direction`](notenwert-design-direction/SKILL.md) | Captures Notenwert's editorial, civic, cultural-network design intent. | Use for Notenwert design direction, homepage hero behavior, NGA-style references, typography, imagery, and public/admin UX critique. |

## UI UX Quality Skills

| Skill | Description | Context |
| --- | --- | --- |
| [`ui-ux-orchestrator`](ui-ux-orchestrator/SKILL.md) | Routes broad UI/UX work to the smallest useful set of design, UX, state, accessibility, flow, and QA skills. | Use when the request is broad, blurry, or needs help choosing which UI/UX skills should run together. |
| [`consistency-audit`](consistency-audit/SKILL.md) | Audits whether UI, UX, implementation, shared components, and pattern weight form one coherent product system. | Use when checking layouts, components, typography, spacing, colors, icons, copy tone, interactions, responsive behavior, states, or duplicate primitives. |
| [`product-ux-contracts`](product-ux-contracts/SKILL.md) | Preserves real product UX contracts while redesigning, restyling, refactoring, or matching a reference. | Use when routing, persistence, scroll, focus, permissions, destructive safety, media, or search click-through could be lost. |
| [`ui-state-matrix`](ui-state-matrix/SKILL.md) | Covers UI states beyond the happy path. | Use for focus, selected, disabled, loading, empty, error, success, denied, long text, localization, and responsive states. |
| [`interaction-flow-qa`](interaction-flow-qa/SKILL.md) | Exercises complete user/admin journeys end to end. | Use for search-to-detail, filter/reload/back, onboarding, modal/drawer, admin create/edit/publish, destructive, playback, or completion flows. |
| [`design-system-guardian`](design-system-guardian/SKILL.md) | Protects component primitives, tokens, variants, typography, spacing, icons, radius, shadow, and consistency. | Use when UI work risks design-system drift, one-off CSS, duplicate variants, or inconsistent neighboring surfaces. |
| [`accessible-interaction`](accessible-interaction/SKILL.md) | Verifies keyboard, focus, ARIA, semantic controls, contrast, touch targets, reduced motion, and modal/drawer accessibility. | Use when visual or interaction changes could break non-pointer access or screen-reader-visible behavior. |
| [`data-dense-ux`](data-dense-ux/SKILL.md) | Guides dense dashboards, tables, lists, ledgers, filters, pagination, bulk actions, and operational panels. | Use when scanning, sorting, selecting, item counts, overflow, responsive compression, or large-data behavior matters. |
| [`form-flow-ux`](form-flow-ux/SKILL.md) | Covers complete create/edit form journeys. | Use for validation, dirty state, autosave, save/cancel/reset, submit loading, duplicate prevention, server errors, permission denied, uploads, and mobile keyboard behavior. |

## Firebase And Security

| Skill | Description | Context |
| --- | --- | --- |
| [`account-recovery-key`](account-recovery-key/SKILL.md) | Defines generic recovery-key flows, hashing, reset, and regeneration policy. | Use for signup recovery codes, password reset without email, signed-in regeneration, and reusable auth recovery guidance. |
| [`firebase-account-management`](firebase-account-management/SKILL.md) | Clarifies Firebase Auth, Firestore user profiles, Admin SDK, custom claims, and billing-sensitive assumptions. | Use for account creation, signup/login, admin user operations, or Spark vs Blaze questions. |
| [`firebase-security-rules`](firebase-security-rules/SKILL.md) | Focuses on Firestore Rules, Admin SDK bypass behavior, service-account setup, and production access guarantees. | Use for security audits, rules changes, privileged endpoints, and Firebase deployment risk. |

## Project-Specific Skills

| Skill | Description | Context |
| --- | --- | --- |
| [`admin-ops`](admin-ops/SKILL.md) | Defines reusable admin-operation rules for privileged actions, lifecycle flows, audit logs, and CMS/admin UX. | Use for admin portals across projects before applying a project-specific admin skill. |
| [`admin-prototype-reconciliation`](admin-prototype-reconciliation/SKILL.md) | Compares admin/CMS/dashboard prototypes against live production admin contracts. | Use before implementing a prototype into a real admin system with existing fields, workflows, auth, APIs, drafts, publish, or revisions. |
| [`coin-quest-admin-ops`](coin-quest-admin-ops/SKILL.md) | Defines safe behavior for the Coin Quest Ledger Admin Portal. | Use for Super Admin auth, users, boards, lifecycle actions, delete/reset flows, revisions, and Firebase-backed admin operations. |
| [`ledger-logic`](ledger-logic/SKILL.md) | Protects collaborative ledger identity, split math, settlement, guests, invites, and persistence. | Use for shared expense/ledger behavior across projects before applying a project-specific ledger skill. |
| [`coin-quest-ledger-logic`](coin-quest-ledger-logic/SKILL.md) | Protects Party Ledger rules for split math, invites, guests, Character IDs, and settlement. | Use for Coin Quest participant entry, payer/participant logic, reminders, direct invite links, or ledger regressions. |
| [`native-parity`](native-parity/SKILL.md) | Keeps native apps aligned with product contracts, backend data, and design parity. | Use for Expo/React Native/iOS/Android work before applying a project-specific native skill. |
| [`coin-quest-native-parity`](coin-quest-native-parity/SKILL.md) | Keeps the Coin Quest native Expo app aligned with the web data model and native build requirements. | Use for native app changes, iOS/Android gates, `playerModules`, and web/native parity checks. |
| [`site-maintainer`](site-maintainer/SKILL.md) | Maintains website projects where source, generated deploy artifacts, docs, tests, and hosting output must stay aligned. | Use for static/built sites, CMS/admin site work, generated deploy folders, build scripts, deploy prep, and work logs. |
| [`notenwert-maintainer`](notenwert-maintainer/SKILL.md) | Defines the operating playbook for the Notenwert project. | Use for Notenwert implementation, CMS/admin work, tests, docs, deploy prep, and commits. |
| [`tts-audio-assets`](tts-audio-assets/SKILL.md) | Manages TTS audio generation, reuse, audits, naturalness QA, voice policy, and data wiring across projects. | Use for lesson audio, UI playback, dialogues, prompts, stale/missing audio, or audio ID wiring. |
| [`shane-thai-audio-generator`](shane-thai-audio-generator/SKILL.md) | Manages Google Chirp audio generation, regeneration, audit, and QA for Thai lessons. | Use for Shane and His Thai lesson audio, Thai TTS text, audio IDs, voice selection, stale/missing audio, or naturalness fixes. |
| [`shane-thai-export-chatgpt`](shane-thai-export-chatgpt/SKILL.md) | Exports Shane and His Thai learner lesson content into ChatGPT-ready patch packets. | Use for all-lesson ChatGPT exports, lesson patch packets, or future learner tab/module proposal packets. |
| [`shane-thai-image-assets`](shane-thai-image-assets/SKILL.md) | Manages image selection, generation, reuse, cropping, and QA for Thai vocabulary lessons. | Use for Shane and His Thai lesson art, badge imagery, Unit image generation, or semantic asset mapping. |
| [`shane-thai-prod-smoke`](shane-thai-prod-smoke/SKILL.md) | Runs safe authenticated production smoke checks for Shane and His Thai using the dedicated dummy learner account. | Use after Shane production deploys or when verifying login, topbar, Learning hub, learner-flow smoke, or production screenshot evidence. |
| [`image-boundary`](image-boundary/SKILL.md) | Routes image-boundary work to iteration, polish, max non-explicit, recovery, or safety-map skills. | Use when the user invokes image-boundary work broadly or is unsure which boundary skill applies. |
| [`image-boundary-efficient`](image-boundary-efficient/SKILL.md) | Speeds image-boundary loops by reducing wasted generations while preserving quality and safety. | Use when the user wants faster/cheaper image-boundary work, fewer retries, less blocking, or wants efficient mode toggled. |
| [`image-boundary-iteration`](image-boundary-iteration/SKILL.md) | Controls adult non-explicit image iteration with prompt hygiene, verdict loops, branch notes, and logging. | Use for the nudity-reference-prompting project when continuing boundary-forward visual iterations or maintaining baselines. |
| [`image-boundary-nonexplicit-max`](image-boundary-nonexplicit-max/SKILL.md) | Pushes adult fantasy/editorial image prompts to the strongest safe non-explicit result. | Use when the user wants maximum sensual intensity without explicit nudity detail, sexual acts, or safety evasion. |
| [`image-boundary-polish`](image-boundary-polish/SKILL.md) | Restores image quality without increasing an accepted boundary level. | Use when boundary-forward non-explicit images need face, hand, linework, water, anatomy, or artifact cleanup before another iteration. |
| [`image-boundary-rejection-recovery`](image-boundary-rejection-recovery/SKILL.md) | Recovers safely after generation blocks, user rejects, underdelivery, identity drift, or quality collapse. | Use when a prompt family fails and needs backtracking, change-of-HOW, polish, or redraw strategy. |
| [`image-boundary-safety-map`](image-boundary-safety-map/SKILL.md) | Maps risk zones and safe routes for near-boundary adult non-explicit image prompts. | Use before stronger sensuality, fewer garments, transparent water, bedroom/bathhouse, or other near-limit image requests. |

## Image And Media Sourcing

| Skill | Description | Context |
| --- | --- | --- |
| [`course-image-assets`](course-image-assets/SKILL.md) | Manages educational course image generation, reuse, mapping, crop fixes, and QA. | Use for vocabulary images, lesson card art, visual hints, badges, and semantic educational image mapping. |
| [`placeholder-image`](placeholder-image/SKILL.md) | Sources, selects, replaces, crops, and audits placeholder images as real product content. | Use when populating missing images, replacing weak stock, finding hero/card/gallery photos, fixing crops, or making an image sourcing playbook. |
