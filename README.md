# Codex Toolkit

A private collection of custom Codex skills for project onboarding, release
checks, Firebase work, visual parity, QA, and project-specific operating
playbooks.

Each skill lives under `skills/<skill-name>/` and contains a `SKILL.md` file.
Some skills also include reference notes, helper scripts, or agent metadata.

Reusable, non-project-specific skills also have explicit `global-*` aliases such
as [`global-release-gate`](skills/global-release-gate/SKILL.md) and
[`global-ui-ux-expert`](skills/global-ui-ux-expert/SKILL.md). See
[Global skills](docs/GLOBAL_SKILLS.md) for the full alias map.

UI/UX-related skills have a mandatory snapshot gate: after implementation,
redesign, restyle, visual audit, responsive QA, Claude/Figma/reference handoff,
or screenshot-based design work, use [`snapshot`](skills/snapshot/SKILL.md)
before the final response without waiting for the user to ask.

## Documentation

- [Codex context](docs/CODEX_CONTEXT.md): future-agent orientation, source of
  truth, and safe update workflow.
- [Skill catalog](docs/SKILL_CATALOG.md): fuller descriptions and usage context
  for each skill.
- [Global skills](docs/GLOBAL_SKILLS.md): reusable non-project-specific skills
  and their `global-*` aliases.
- [Installation and usage](docs/INSTALLATION.md): how to install skills locally
  and use the toolkit from another machine.
- [Maintenance guide](docs/MAINTENANCE.md): how to refresh, add, review, and
  publish changes to this repository.
- [Docs index](docs/README.md): quick map of the documentation set.
- [Reference parity migration](docs/REFERENCE_PARITY_MIGRATION.md): generic
  reference-to-a-tee modes, fidelity versus effort, image evidence, and legacy compatibility.
- [Design judgment and gates](docs/SKILL_JUDGMENT_AND_GATES.md): five UI/UX
  improvements, evaluation limits, complete-deliverable gates, and risk routing.

## Skills

| Skill | Short description | Use when |
| --- | --- | --- |
| [`dootaa-new-chat`](skills/dootaa-new-chat/SKILL.md) | Onboards DOOTAA with current app, camera, benchmark, dataset and website contracts. | Continuing DOOTAA or preparing a starter prompt without confusing source/build evidence with real-device or clinical validation. |
| [`ios-app-development`](skills/ios-app-development/SKILL.md) | Provides reusable iOS setup, build, install, launch and troubleshooting workflows. | Checking Mac/Xcode readiness, Expo/native ownership, Simulator/iPhone runs, signing or Metro while preserving the project's stack. |
| [`korat-tan-phai-new-chat`](skills/korat-tan-phai-new-chat/SKILL.md) | Onboards Korat web and iOS work with forecast-only routing and shared brand/data contracts. | Preparing a continuation prompt or finding current docs, rev03 semantics, Supabase boundaries, native setup and verification evidence. |
| [`mockup-to-product`](skills/mockup-to-product/SKILL.md) | Adapts approved mockups while preserving behavior, component anatomy, typography, and real editing capabilities. | Same-state visual review, cross-page components, live-editor parity, scoped before/after evidence, and responsive adaptation; exact reproduction remains owned by reference-to-a-tee. |
| [`accessible-interaction`](skills/accessible-interaction/SKILL.md) | Verifies keyboard, focus, semantic controls, ARIA state, contrast, touch targets, and modal/drawer accessibility. | Visual or interaction changes could break non-pointer use, focus order, screen-reader-visible state, or mobile keyboard behavior. |
| [`account-recovery-key`](skills/account-recovery-key/SKILL.md) | Defines provider-neutral recovery-key flows for signup, reset, regeneration, hashing, and display policy. | A project needs recovery codes/keys, password reset without email, signed-in key regeneration, or reusable auth recovery guidance. |
| [`admin-ops`](skills/admin-ops/SKILL.md) | Guides admin portal operations, privileged actions, lifecycle flows, auditability, and CMS/admin UX. | Designing, auditing, implementing, or verifying admin surfaces that change real data, permissions, content, or operational state. |
| [`admin-prototype-reconciliation`](skills/admin-prototype-reconciliation/SKILL.md) | Reconciles admin/CMS/dashboard prototypes against live production admin contracts before implementation. | A Claude/Figma/offline prototype must be compared with live fields, workflows, auth, APIs, drafts, publish, revisions, or data shape. |
| [`claude-design-md-request`](skills/claude-design-md-request/SKILL.md) | Drafts Claude Design requests for implementation-ready Markdown handoffs/specs from visual artifacts. | A Claude prompt should separate visual facts from product decisions, map components, preserve product contracts, and produce implementable acceptance checks. |
| [`claude-design-reference-bundle`](skills/claude-design-reference-bundle/SKILL.md) | Creates upload-ready Claude Design reference bundles from live pages, screenshots, routes, or prototypes. | Claude Design needs screenshots, measured specs, state notes, product constraints, and a paste-ready prompt without building a standalone HTML export. |
| [`reference-to-a-tee`](skills/reference-to-a-tee/SKILL.md) | Matches HTML, image-only, or mixed references with fidelity separate from verification effort. | Exact repairs or reconstruction, explicitly requested adaptation, and scoped comparison evidence while preserving product behavior; inspiration-only requests route to design skills. |
| [`claude-to-a-tee`](skills/claude-to-a-tee/SKILL.md) | Compatibility name routing to `reference-to-a-tee`. | Existing prompts or extractor commands still use the old Claude-specific name. |
| [`codex-handoff-for-claude`](skills/codex-handoff-for-claude/SKILL.md) | Prepares implementation-ready Markdown handoffs from Codex to Claude or Claude Design. | Codex needs to package source-of-truth rules, product contracts, visual geometry, states, responsive behavior, accessibility notes, and acceptance checks for Claude. |
| [`coin-quest-admin-ops`](skills/coin-quest-admin-ops/SKILL.md) | Keeps Coin Quest Ledger Admin Portal work aligned with current Firebase-backed admin behavior. | Editing admin auth, boards, users, lifecycle actions, reset/delete flows, publish/restore, revisions, or relationship maps. |
| [`coin-quest-ledger-logic`](skills/coin-quest-ledger-logic/SKILL.md) | Preserves Party Ledger split math, participants, guests, invites, Character IDs, and settlement behavior. | Changing Coin Quest ledger workflows, guest handling, invite links, reminders, payer/participant logic, or settlement tests. |
| [`coin-quest-native-parity`](skills/coin-quest-native-parity/SKILL.md) | Prevents the Coin Quest Expo app from drifting away from web data contracts and native parity requirements. | Working on the native app, iOS/Android build gates, `playerModules`, or native/web backend parity. |
| [`consistency-audit`](skills/consistency-audit/SKILL.md) | Audits UI, UX, implementation, shared components, pattern weight, and consolidation opportunities for product consistency. | Checking whether layouts, components, typography, spacing, copy, states, responsive behavior, or shared primitives feel coherent. |
| [`course-image-assets`](skills/course-image-assets/SKILL.md) | Manages educational course image generation, reuse, mapping, crop fixes, audits, and QA. | Working on vocabulary images, lesson card art, visual hints, badges, semantic mappings, or generated educational illustrations. |
| [`covermate-design-spec`](skills/covermate-design-spec/SKILL.md) | Preserves CoverMate public/admin design contracts using current checkout docs and a dated fallback spec. | Compact Home, Articles, Cases v2, CMS ownership/history, media, copy voice, handoffs, and scoped snapshots; bundled context is not proof of deployment. |
| [`covermate-new-chat`](skills/covermate-new-chat/SKILL.md) | Onboards CoverMate work with active-checkout authority, current docs, product rules, and starter prompts. | Picking up visitor/admin/CMS work, publication and session boundaries, media, or release tasks with proportional UAT and explicit production evidence. |
| [`data-dense-ux`](skills/data-dense-ux/SKILL.md) | Guides dense dashboards, tables, lists, ledgers, filters, pagination, bulk actions, and operational panels. | Users need to scan, compare, sort, select, or operate large amounts of information without losing clarity. |
| [`design-direction`](skills/design-direction/SKILL.md) | Defines product visual direction and image-only, HTML, or mixed handoffs. | Creating briefs, redesign strategy, visual guardrails, or handoffs with explicit source authority and unknown states. |
| [`design-system-guardian`](skills/design-system-guardian/SKILL.md) | Guides shared-component reuse/extraction, minimal contracts, consumer migration, and drift prevention. | Repeated UI, duplicate fixes, shared API/default changes, or consolidation need decisions about what to share and how to preserve behavior. |
| [`accessibility-beyond-basics`](skills/accessibility-beyond-basics/SKILL.md) | Advanced accessibility beyond axe checks for screen-reader flow, cognitive load, low vision, complex widgets, charts, zoom, and forced colors. | Basic keyboard/focus checks are not enough and the UI needs advanced accessibility coverage. |
| [`art-direction-imagery`](skills/art-direction-imagery/SKILL.md) | Directs imagery, crops, focal points, hero media, thumbnails, placeholders, captions, loading states, and asset failure states. | Images, generated media, thumbnails, hero visuals, or placeholders determine whether the screen feels intentional. |
| [`design-quality-review`](skills/design-quality-review/SKILL.md) | Applies the shared design-quality rule language, severity model, screenshot QA protocol, calibration library, and definition of done. | A UI needs rigorous rule-tagged design QA, severity, capture protocol, calibration, PR notes, or future-readable critique. |
| [`visual-diagnosis`](skills/visual-diagnosis/SKILL.md) | Names visible UI defects such as cheap, cramped, scattered, generic, heavy, low-trust, or unfinished using observable rules. | A rendered UI looks off and the first job is to diagnose why before editing. |
| [`domain-taste`](skills/domain-taste/SKILL.md) | Chooses category-appropriate density, hierarchy, controls, and evidence for admin, SaaS ops, dashboards, ledgers, editorial, learning, landing, and mobile screens. | A screen should feel native to its product category rather than generically polished. |
| [`information-architecture-ux`](skills/information-architecture-ux/SKILL.md) | Structures navigation, grouping, hierarchy, progressive disclosure, screen purpose, and sequencing. | Users cannot tell where they are, what matters, what comes next, or how content/actions are grouped. |
| [`interaction-design`](skills/interaction-design/SKILL.md) | Designs real UI interactions including autosave, undo, bulk actions, optimistic updates, permissions, interruption recovery, and destructive flows. | A control implies real behavior that needs feedback, recovery, safety, or permission handling. |
| [`mobile-native-feel`](skills/mobile-native-feel/SKILL.md) | Audits mobile UI for safe areas, native controls, touch targets, keyboard behavior, thumb reach, sheets, gestures, and platform feel. | Mobile web or app UI feels like squeezed desktop or misses platform-native ergonomics. |
| [`design-system-architect`](skills/design-system-architect/SKILL.md) | Architects tokens, component taxonomies, variants, galleries, drift metrics, and token-layer governance. | The design system itself needs structure, not just one-off component consistency. |
| [`typography-refinement`](skills/typography-refinement/SKILL.md) | Refines type scale, measure, line-height, multilingual behavior, numeric data, dates, units, truncation, and typographic rhythm. | Text, numbers, headings, prose, tables, dashboards, or multilingual content carry the experience. |
| [`motion-choreography`](skills/motion-choreography/SKILL.md) | Specifies UI motion timing, easing, choreography, loading feedback, overlay transitions, scroll motion, and reduced-motion alternatives. | Motion exists or should exist and needs to communicate state without feeling decorative or inaccessible. |
| [`reference-implementation-critique`](skills/reference-implementation-critique/SKILL.md) | Compares reference design and implementation across geometry, rhythm, hierarchy, density, visual weight, affordance, states, and product decisions. | Claude, Figma, screenshot, or other reference artifacts need measured comparison against the real app. |
| [`taste-calibration`](skills/taste-calibration/SKILL.md) | Uses paired works/fails specimens and calibration drills to improve UI taste with measurable smallest-change loops. | The goal is to sharpen design judgment or compare a screen against category specimens. |
| [`docs-cartographer`](skills/docs-cartographer/SKILL.md) | Creates useful maps of routes, modules, data flow, commands, ownership boundaries, and handoff context. | A project needs architecture docs, site maps, onboarding docs, interaction maps, or better navigation for future sessions. |
| [`efficient-execution`](skills/efficient-execution/SKILL.md) | Chooses proportionate depth and tracks every deliverable through verification and completion. | Work needs lower usage, fewer missed requirements, continuity across interruptions, valid evidence reuse, or confirmed sync and publishing outcomes. |
| [`export-html`](skills/export-html/SKILL.md) | Creates live-parity standalone/offline HTML exports and clickable prototypes. | Exporting product screens, design handoffs, Claude/Figma-inspectable HTML, visual audit files, or representative UI states. |
| [`firebase-account-management`](skills/firebase-account-management/SKILL.md) | Separates Firebase billing, Auth, Firestore, Admin SDK, and account-management concerns. | Designing, auditing, or debugging signup/login, user profiles, admin CRUD, custom claims, or Spark vs Blaze assumptions. |
| [`firebase-security-rules`](skills/firebase-security-rules/SKILL.md) | Audits Firebase Auth, Firestore Rules, Admin SDK endpoints, service accounts, and production access guarantees. | Reviewing or changing Firestore rules, privileged backend behavior, auth gates, secrets, or Firebase security posture. |
| [`form-flow-ux`](skills/form-flow-ux/SKILL.md) | Covers complete create/edit form journeys including validation, dirty state, autosave, save/cancel, errors, and mobile keyboard. | A form must work as a real workflow, not only as a visually finished screen. |
| [`github-actions-repair`](skills/github-actions-repair/SKILL.md) | Diagnoses failed Actions runs and verifies focused repairs on the intended revision and target. | Failure emails, setup timeouts, missing secrets, auth failures, flaky checks, or wrong-ref deployment smoke; ordinary readiness stays with release-gate. |
| [`global-full-design-spec`](skills/global-full-design-spec/SKILL.md) | Exports comprehensive implementation-ready UI design specs from screenshots, source, CSS, routes, prototypes, or live app state. | A future Codex/Claude/dev handoff needs a full page contract, source-mapped design spec, accessibility matrix, state matrix, and guardrails. |
| [`global-quick-design-spec`](skills/global-quick-design-spec/SKILL.md) | Exports concise implementation-ready UI design specs quickly from screenshots, source, CSS, routes, prototypes, or live app state. | A user needs a fast lightweight design handoff or screenshot-to-spec export without redesigning or modifying app code. |
| [`image-boundary`](skills/image-boundary/SKILL.md) | Routes boundary-forward adult non-explicit image work to the right boundary, polish, safety, or recovery skill. | The user invokes image-boundary work, is unsure which boundary skill applies, or needs coordinated PASS/PARTIAL/REJECT iteration. |
| [`image-boundary-efficient`](skills/image-boundary-efficient/SKILL.md) | Adds a removable speed layer for image-boundary loops without lowering quality, safety, or verdict discipline. | The user wants faster, cheaper, less blocked image-boundary iteration, or wants to toggle efficient mode. |
| [`image-boundary-iteration`](skills/image-boundary-iteration/SKILL.md) | Guides controlled adult non-explicit image iteration with branch-specific prompt strategy, verdicts, and logging. | Continuing the nudity-reference-prompting workflow, handling Pass/Partial/Reject loops, local edits, or visual baseline tracking. |
| [`image-boundary-nonexplicit-max`](skills/image-boundary-nonexplicit-max/SKILL.md) | Pushes sensual, intimate, boundary-forward image prompts to the strongest safe non-explicit result. | The user wants the hardest allowed adult fantasy/editorial push without explicit nudity detail, sexual acts, or safety evasion. |
| [`image-boundary-polish`](skills/image-boundary-polish/SKILL.md) | Restores quality in accepted boundary-forward non-explicit image iterations without changing the boundary level. | Faces, hands, linework, water, anatomy, or rendering quality need cleanup before continuing image-boundary iteration. |
| [`image-boundary-rejection-recovery`](skills/image-boundary-rejection-recovery/SKILL.md) | Recovers after generation blocks, user rejects, underdelivery, identity drift, or quality collapse. | A boundary prompt family blocked, failed, got rejected, or needs a safe change-of-strategy/backtrack. |
| [`image-boundary-safety-map`](skills/image-boundary-safety-map/SKILL.md) | Maps risk zones and chooses safe routes before prompting near the non-explicit boundary. | Stronger sensuality, fewer garments, transparent water, bedroom/bathhouse scenes, or other near-limit image requests need routing. |
| [`interaction-flow-qa`](skills/interaction-flow-qa/SKILL.md) | Exercises real journeys end to end across routing, state, data, permissions, feedback, reload, and back behavior. | Search/detail, onboarding, admin create/edit/publish, modal/drawer, destructive, playback, or completion flows must actually work. |
| [`kaset-tan-phai-new-chat`](skills/kaset-tan-phai-new-chat/SKILL.md) | Onboards fresh Codex chats for the Kaset Tan Phai / เกษตรทันภัย water-risk alert project, including Nakhon Ratchasima dashboard decisions. | A future chat needs Kaset read order, durable Thai-first public-safety constraints, Nakhon Ratchasima route/data/map contracts, source areas, setup commands, or a copy-ready pickup prompt before UI, data, map, alerts, operations, QA, release, or deploy work. |
| [`ledger-logic`](skills/ledger-logic/SKILL.md) | Protects collaborative ledger math, identity, guests/invites, persistence, and settlement outputs. | Implementing, auditing, or debugging expenses, splits, payer/participant logic, reciprocal netting, import/export, or ledger tests. |
| [`mobile-web-qa`](skills/mobile-web-qa/SKILL.md) | Audits responsive web interfaces across phone, tablet, desktop, browser engines, and platform quirks. | Checking mobile Safari/Chrome behavior, safe areas, keyboard states, tap targets, overflow, modals, WebViews, zoom, or pre-deploy frontend QA. |
| [`mongkol-new-chat`](skills/mongkol-new-chat/SKILL.md) | Onboards a fresh Codex chat for the Mongkol Wela / hora-astro project. | A future chat needs read order, durable project constraints, task-specific source maps, commands, or a copy-ready starter prompt for Mongkol Wela. |
| [`native-parity`](skills/native-parity/SKILL.md) | Keeps native iOS/Android apps aligned with web/product source-of-truth behavior. | Working on Expo/React Native builds, native screen parity, shared backend contracts, device gates, or static sample-app drift. |
| [`notenwert-design-direction`](skills/notenwert-design-direction/SKILL.md) | Preserves Notenwert's editorial cultural-network visual direction and reference system. | Designing or critiquing Notenwert public/admin UX, homepage hero motion, NGA-style interactions, typography, color, or imagery. |
| [`notenwert-maintainer`](skills/notenwert-maintainer/SKILL.md) | Provides the safe operating playbook for the Notenwert codebase. | Fixing bugs, editing CMS/admin behavior, changing content models, preparing deploys, updating docs, or making commits in Notenwert. |
| [`placeholder-image`](skills/placeholder-image/SKILL.md) | Sources, selects, replaces, crops, and audits placeholder images as real product content. | Populating missing images, replacing weak stock, finding hero/card/gallery photos, fixing crops, or creating image sourcing playbooks. |
| [`prod-smoke-harness`](skills/prod-smoke-harness/SKILL.md) | Defines safe deployed smoke checks with approved accounts, secret scope, and real authentication evidence. | Production/preview HTTP or browser checks, Actions credentials, intended build/URL verification, and visual evidence when relevant. |
| [`product-ux-contracts`](skills/product-ux-contracts/SKILL.md) | Preserves proven product UX contracts while redesigning, restyling, refactoring, or implementing reference UI. | Routing, persistence, scroll, focus, permissions, destructive safety, media fallbacks, or search click-through could be flattened. |
| [`production-asset-smoke`](skills/production-asset-smoke/SKILL.md) | Verifies deployed media and asset rendering across images, videos, CSS backgrounds, lazy loading, and fallbacks. | Production or preview pages need proof that media loads without broken assets, stale domains, CORS/ORB failures, or blank fallbacks. |
| [`project-onboarding`](skills/project-onboarding/SKILL.md) | Builds a compact, reliable map of an unfamiliar or returning codebase before edits. | Starting work in a repo, reading handoffs, finding commands, understanding architecture, or preparing a safe implementation plan. |
| [`regression-hunter`](skills/regression-hunter/SKILL.md) | Searches for related bug patterns after one issue reveals a possible class of regressions. | Auditing for similar hardcoded values, duplicated logic, fragile selectors, stale fixtures, or nearby behavior breaks. |
| [`release-gate`](skills/release-gate/SKILL.md) | Verifies every active deliverable and blocks readiness on failed, pending, or skipped required coverage. | Commit, push, deploy, merge, or handoff with action-specific gates, terminal CI evidence, tested revision/target, and confirmed endpoints. |
| [`rollback-guardrail`](skills/rollback-guardrail/SKILL.md) | Separates pauses and reversible edits from risky work-loss operations requiring approval and recovery. | Rollback-like work could discard implementation, alter history/data, remove behavior, or leave parked scope. |
| [`shane-thai-audio-generator`](skills/shane-thai-audio-generator/SKILL.md) | Generates, regenerates, audits, and QA-checks Google Chirp audio for Shane Thai. | Working on lesson audio, Thai TTS text, audio IDs, voice selection, missing/stale audio, or naturalness fixes. |
| [`shane-thai-export-chatgpt`](skills/shane-thai-export-chatgpt/SKILL.md) | Exports Shane Thai learner lesson content into ChatGPT-ready patch packets. | The user needs lesson patch packets, all-lesson ChatGPT exports, or future learner tab/module proposal packets. |
| [`shane-thai-image-assets`](skills/shane-thai-image-assets/SKILL.md) | Manages vocabulary image generation, reuse, cropping, optimization, and QA for the Shane Thai app. | Adding or replacing lesson artwork, mapping assets, fixing crops, generating Unit images, or deciding whether existing art is semantically correct. |
| [`shane-thai-new-chat`](skills/shane-thai-new-chat/SKILL.md) | Onboards a fresh Codex chat for Shane Thai with current docs, skills, rules, and starter prompts. | A future chat needs a copy-ready pickup prompt, required read order, project constraints, or task-specific Shane Thai context before work begins. |
| [`shane-thai-prod-smoke`](skills/shane-thai-prod-smoke/SKILL.md) | Runs Shane Thai production smoke checks with the dedicated dummy learner account and safe learner-flow policy. | Verifying the Shane production Vercel app, topbar/Learning hub, login surface, learner smoke account, or post-deploy screenshot evidence. |
| [`site-maintainer`](skills/site-maintainer/SKILL.md) | Maintains website projects where source, generated artifacts, tests, docs, and hosting outputs must stay aligned. | Working on static/built sites, generated deploy folders, CMS/admin site work, build scripts, deploy prep, or work logs. |
| [`snapshot`](skills/snapshot/SKILL.md) | Captures, crops, inspects, and presents screenshots with enough context for review, including page-level evidence for whole-page work. | Producing UI screenshots, visual proof, before/after comparisons, reference/development side-by-side evidence, viewport captures, full-page/contact-sheet proof, or production smoke evidence. |
| [`tts-audio-assets`](skills/tts-audio-assets/SKILL.md) | Manages text-to-speech audio generation, reuse, audit, naturalness QA, and data wiring across projects. | Working on lesson audio, UI playback, dialogues, prompts, voice/pacing policy, stale/missing audio, or audio IDs. |
| [`uat-environment`](skills/uat-environment/SKILL.md) | Defines isolated UAT and promotion gates covering acceptance criteria and all required checks. | Runtime changes need current production-like evidence, appropriate auth, and verified promotion outcomes. |
| [`ui-state-matrix`](skills/ui-state-matrix/SKILL.md) | Defines and verifies UI states beyond the happy path: focus, selected, disabled, loading, empty, error, success, denied, long text, and responsive states. | A component or flow can look finished but still needs state coverage before UI work is complete. |
| [`ui-ux-expert`](skills/ui-ux-expert/SKILL.md) | Diagnoses UI problems and verifies product-preserving redesign, including live authoring and rendered output. | Design tradeoffs, shared components, CMS/data/session boundaries, typography, alignment, editor save/reopen parity, and scoped visual comparisons. |
| [`korat-tan-phai-shared-components`](skills/korat-tan-phai-shared-components/SKILL.md) | Preserves Korat Tan Phai shared components and domain semantics with automatic visual evidence. | Changing or auditing Korat stats, selects, provenance, map previews, or shared responsive/interaction behavior. |
| [`ui-ux-orchestrator`](skills/ui-ux-orchestrator/SKILL.md) | Routes broad or blurry UI/UX requests to the smallest useful set of design, UX, state, accessibility, flow, and QA skills. | The user asks for UI/UX polish, audits, planning, visual QA, Claude/Figma handoffs, or is unsure which UI/UX skill applies. |
| [`usage-budget-gate`](skills/usage-budget-gate/SKILL.md) | Compatibility router for proportional-effort decisions now owned by `efficient-execution`. | Existing prompts mention `$usage-budget-gate`, or the user asks for lower usage, faster work, stop rules, or fast/standard/deep/release depth. |

## Installing A Skill

Copy or symlink a skill folder into your Codex skills directory:

```sh
cp -R skills/project-onboarding ~/.codex/skills/project-onboarding
```

## Updating This Repo

The source-of-truth local skills currently live in `~/.codex/skills`. To refresh
the repository copy, sync the personal skill folders into `skills/`, review the
diff, then commit.

Do not let a broad `--delete` sync remove repo-only `global-*` aliases. If the
live local tree lacks those aliases, sync changed canonical skill folders
selectively and preserve the archive's global layer.

Verify the archive with:

```sh
python3 scripts/verify_skills.py --expected-count 138
```
