# Skill Index

This folder contains custom Codex skills. Each subfolder is intended to be usable
as a standalone skill directory under `~/.codex/skills`.

Reusable, non-project-specific skills also have `global-*` alias folders. The
aliases route to canonical skills and are listed in
[../docs/GLOBAL_SKILLS.md](../docs/GLOBAL_SKILLS.md).

UI/UX-related skills must call [`snapshot`](snapshot/SKILL.md) automatically
before the final response after visible implementation, redesign, restyle,
visual audit, responsive QA, Claude/Figma/reference handoff, or
screenshot-based design work.

## General Workflow Skills

| Skill | Description | Context |
| --- | --- | --- |
| [`project-onboarding`](project-onboarding/SKILL.md) | Reads project docs, commands, architecture, source layout, and git state before implementation. | Use at the start of work in an unfamiliar or returning repository. |
| [`docs-cartographer`](docs-cartographer/SKILL.md) | Produces living documentation for routes, modules, data flow, interactions, deployment paths, and ownership boundaries. | Use when a codebase needs better maps, handoff notes, or future-maintainer context. |
| [`regression-hunter`](regression-hunter/SKILL.md) | Turns one bug into a targeted search for related patterns and nearby regressions. | Use after finding a suspicious hardcoded value, duplicated behavior, brittle selector, or repeated logic bug. |
| [`release-gate`](release-gate/SKILL.md) | Covers every active deliverable and blocks readiness on failed, pending, or unrun required checks. | Use before commit, push, deploy, merge, release, or handoff with action-specific evidence. |
| [`rollback-guardrail`](rollback-guardrail/SKILL.md) | Routes pauses/reversible edits lightly and requires approved recovery for risky work loss. | Use when rollback, removal, history/data changes, or uncertain ownership could discard work. |
| [`efficient-execution`](efficient-execution/SKILL.md) | Chooses fast/standard/deep/release depth, tracks active deliverables, reuses current evidence, and confirms operation results and dependent outputs. | Use when work needs lower usage, fewer omissions, continuity across interruptions, or a completion gate covering every requested outcome. |
| [`usage-budget-gate`](usage-budget-gate/SKILL.md) | Routes proportional-effort and usage-budget decisions to `efficient-execution`. | Use when existing prompts mention `$usage-budget-gate` or the user asks for lower usage, faster work, stop rules, escalation triggers, or a budget-aware scope. |
| [`uat-environment`](uat-environment/SKILL.md) | Defines isolated UAT with complete acceptance coverage and required-check promotion gates. | Use when runtime changes need production-like verification before authorized promotion. |
| [`prod-smoke-harness`](prod-smoke-harness/SKILL.md) | Defines safe production/preview smoke harness policy, accounts, HTTP/browser checks, and screenshot evidence. | Use when a web app needs post-deploy smoke checks, Playwright smoke setup, authenticated smoke policy, or reusable production verification. |
| [`production-asset-smoke`](production-asset-smoke/SKILL.md) | Verifies deployed media and asset rendering after image, video, CMS, fallback, or deploy changes. | Use when production or preview pages need proof that images, videos, CSS backgrounds, lazy assets, and fallbacks render correctly. |
| [`mobile-web-qa`](mobile-web-qa/SKILL.md) | Verifies responsive UI across representative mobile, tablet, desktop, browser-engine, and platform constraints. | Use for mobile web bugs, pre-deploy QA, keyboard behavior, overflow, safe areas, WebViews, zoom, and touch interaction checks. |
| [`snapshot`](snapshot/SKILL.md) | Captures screenshots with enough visual context for review, including page-level proof for whole-page work. | Use for UI snapshots, before/after evidence, reference/development side-by-side comparisons, viewport captures, full-page/contact-sheet proof, or production smoke proof. |

## Design And Frontend Parity

| Skill | Description | Context |
| --- | --- | --- |
| [`mockup-to-product`](mockup-to-product/SKILL.md) | Adapts approved mockups into real product UI while preserving composition, details and behavior. | Use when layout/assets/content/mobile judgment is authorized; use reference-to-a-tee for explicit exact matching. |
| [`claude-design-md-request`](claude-design-md-request/SKILL.md) | Drafts Claude Design prompts for implementation-ready Markdown handoffs/specs. | Use when Claude should produce component maps, visual geometry, state matrices, product-decision reviews, and acceptance checks from screenshots, HTML, or design references. |
| [`claude-design-reference-bundle`](claude-design-reference-bundle/SKILL.md) | Creates Claude Design reference bundles with screenshots, measured specs, state notes, product contracts, and a paste-ready prompt. | Use when Claude Design needs a visual replication package from a live page, route, screenshot set, or prototype without requiring standalone HTML. |
| [`reference-to-a-tee`](reference-to-a-tee/SKILL.md) | Matches HTML, image-only, or mixed references with risk-proportional effort and preserved product behavior. | Use for exact repairs/reconstruction or explicitly requested adaptation; a tiny exact fix needs scoped evidence, not a full-page audit. |
| [`claude-to-a-tee`](claude-to-a-tee/SKILL.md) | Compatibility router to `reference-to-a-tee`, including old extractor commands. | Use when an existing prompt still invokes the former name. |
| [`codex-handoff-for-claude`](codex-handoff-for-claude/SKILL.md) | Packages Codex context into implementation-ready Markdown handoffs for Claude or Claude Design. | Use when handing off a screen, route, component, prototype, screenshot set, design task, or implementation brief with contracts and acceptance checks. |
| [`design-direction`](design-direction/SKILL.md) | Defines product direction and image-only, HTML, or mixed handoffs. | Use for design briefs, redesign strategy, visual guardrails, and explicit reference authority/unknowns. |
| [`export-html`](export-html/SKILL.md) | Creates live-parity standalone HTML exports and clickable prototypes. | Use for offline HTML, design handoff, Claude/Figma inspection, or representative UI state review. |
| [`global-full-design-spec`](global-full-design-spec/SKILL.md) | Exports comprehensive implementation-ready UI design specs. | Use for full page contracts, source-mapped specs, accessibility/state matrices, guardrails, and future Codex/Claude/dev handoffs. |
| [`global-quick-design-spec`](global-quick-design-spec/SKILL.md) | Exports concise implementation-ready UI design specs quickly. | Use for lightweight screenshot-to-spec exports or fast design handoffs without redesigning or modifying app code. |
| [`notenwert-design-direction`](notenwert-design-direction/SKILL.md) | Captures Notenwert's editorial, civic, cultural-network design intent. | Use for Notenwert design direction, homepage hero behavior, NGA-style references, typography, imagery, and public/admin UX critique. |

## UI UX Quality Skills

| Skill | Description | Context |
| --- | --- | --- |
| [`ui-ux-expert`](ui-ux-expert/SKILL.md) | Adds diagnosis, tradeoffs, contextual rules, shared-component routing, alternatives, and evidence-based evaluation to UI work. | Use for visible design, implementation, or review; benchmark only when improving the skill or investigating repeated failures. |
| [`ui-ux-orchestrator`](ui-ux-orchestrator/SKILL.md) | Routes broad UI/UX work to the smallest useful set of design, UX, state, accessibility, flow, and QA skills. | Use when the request is broad, blurry, or needs help choosing which UI/UX skills should run together. |
| [`accessibility-beyond-basics`](accessibility-beyond-basics/SKILL.md) | Advanced accessibility beyond axe checks for screen-reader flow, cognitive load, low vision, complex widgets, charts, zoom, and forced colors. | Basic keyboard/focus checks are not enough and the UI needs advanced accessibility coverage. |
| [`art-direction-imagery`](art-direction-imagery/SKILL.md) | Directs imagery, crops, focal points, hero media, thumbnails, placeholders, captions, loading states, and asset failure states. | Images, generated media, thumbnails, hero visuals, or placeholders determine whether the screen feels intentional. |
| [`design-quality-review`](design-quality-review/SKILL.md) | Applies the shared design-quality rule language, severity model, screenshot QA protocol, calibration library, and definition of done. | A UI needs rigorous rule-tagged design QA, severity, capture protocol, calibration, PR notes, or future-readable critique. |
| [`visual-diagnosis`](visual-diagnosis/SKILL.md) | Names visible UI defects such as cheap, cramped, scattered, generic, heavy, low-trust, or unfinished using observable rules. | A rendered UI looks off and the first job is to diagnose why before editing. |
| [`domain-taste`](domain-taste/SKILL.md) | Chooses category-appropriate density, hierarchy, controls, and evidence for admin, SaaS ops, dashboards, ledgers, editorial, learning, landing, and mobile screens. | A screen should feel native to its product category rather than generically polished. |
| [`information-architecture-ux`](information-architecture-ux/SKILL.md) | Structures navigation, grouping, hierarchy, progressive disclosure, screen purpose, and sequencing. | Users cannot tell where they are, what matters, what comes next, or how content/actions are grouped. |
| [`interaction-design`](interaction-design/SKILL.md) | Designs real UI interactions including autosave, undo, bulk actions, optimistic updates, permissions, interruption recovery, and destructive flows. | A control implies real behavior that needs feedback, recovery, safety, or permission handling. |
| [`mobile-native-feel`](mobile-native-feel/SKILL.md) | Audits mobile UI for safe areas, native controls, touch targets, keyboard behavior, thumb reach, sheets, gestures, and platform feel. | Mobile web or app UI feels like squeezed desktop or misses platform-native ergonomics. |
| [`design-system-architect`](design-system-architect/SKILL.md) | Architects tokens, component taxonomies, variants, galleries, drift metrics, and token-layer governance. | The design system itself needs structure, not just one-off component consistency. |
| [`typography-refinement`](typography-refinement/SKILL.md) | Refines type scale, measure, line-height, multilingual behavior, numeric data, dates, units, truncation, and typographic rhythm. | Text, numbers, headings, prose, tables, dashboards, or multilingual content carry the experience. |
| [`motion-choreography`](motion-choreography/SKILL.md) | Specifies UI motion timing, easing, choreography, loading feedback, overlay transitions, scroll motion, and reduced-motion alternatives. | Motion exists or should exist and needs to communicate state without feeling decorative or inaccessible. |
| [`reference-implementation-critique`](reference-implementation-critique/SKILL.md) | Compares reference design and implementation across geometry, rhythm, hierarchy, density, visual weight, affordance, states, and product decisions. | Claude, Figma, screenshot, or other reference artifacts need measured comparison against the real app. |
| [`taste-calibration`](taste-calibration/SKILL.md) | Uses paired works/fails specimens and calibration drills to improve UI taste with measurable smallest-change loops. | The goal is to sharpen design judgment or compare a screen against category specimens. |
| [`consistency-audit`](consistency-audit/SKILL.md) | Audits whether UI, UX, implementation, shared components, and pattern weight form one coherent product system. | Use when checking layouts, components, typography, spacing, colors, icons, copy tone, interactions, responsive behavior, states, or duplicate primitives. |
| [`product-ux-contracts`](product-ux-contracts/SKILL.md) | Preserves real product UX contracts while redesigning, restyling, refactoring, or matching a reference. | Use when routing, persistence, scroll, focus, permissions, destructive safety, media, or search click-through could be lost. |
| [`ui-state-matrix`](ui-state-matrix/SKILL.md) | Covers UI states beyond the happy path. | Use for focus, selected, disabled, loading, empty, error, success, denied, long text, localization, and responsive states. |
| [`interaction-flow-qa`](interaction-flow-qa/SKILL.md) | Exercises complete user/admin journeys end to end. | Use for search-to-detail, filter/reload/back, onboarding, modal/drawer, admin create/edit/publish, destructive, playback, or completion flows. |
| [`design-system-guardian`](design-system-guardian/SKILL.md) | Chooses reuse/extraction boundaries, defines shared contracts, migrates consumers, and prevents drift. | Use for repeated UI, duplicate fixes, component consolidation, shared API/default changes, or inconsistent neighboring surfaces. |
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
| [`ios-app-development`](ios-app-development/SKILL.md) | Guides Mac toolchain inventory, native ownership, build/install/launch and runtime diagnosis. | Use for iOS setup, Simulator/iPhone, Metro, signing or native rebuild issues; preserve existing stacks and keep Android checks optional. |
| [`dootaa-new-chat`](dootaa-new-chat/SKILL.md) | Routes DOOTAA onboarding to current product, camera, dataset, build and website docs. | Use for starter prompts or continuation context; keep real-device evidence, simulated fixtures and clinical readiness distinct. |
| [`korat-tan-phai-new-chat`](korat-tan-phai-new-chat/SKILL.md) | Routes Korat web/iOS onboarding to current forecast, Supabase, brand and native setup contracts. | Use for starter prompts or continuation context; distinguish parked Actual code from the active forecast product. |
| [`coin-quest-native-parity`](coin-quest-native-parity/SKILL.md) | Keeps the Coin Quest native Expo app aligned with the web data model and native build requirements. | Use for native app changes, iOS/Android gates, `playerModules`, and web/native parity checks. |
| [`site-maintainer`](site-maintainer/SKILL.md) | Maintains website projects where source, generated deploy artifacts, docs, tests, and hosting output must stay aligned. | Use for static/built sites, CMS/admin site work, generated deploy folders, build scripts, deploy prep, and work logs. |
| [`covermate-design-spec`](covermate-design-spec/SKILL.md) | Keeps CoverMate public/admin designs aligned with the current production product spec. | Use for CoverMate visitor pages, admin login/launcher/edit/arrange/analytics, Claude Design handoffs, snapshot suites, Firestore CMS behavior, SEO/analytics design guardrails, or product-decision reconciliation. |
| [`covermate-new-chat`](covermate-new-chat/SKILL.md) | Onboards fresh Codex chats for CoverMate with current docs, durable rules, proportional UAT policy, skills, commands, and starter prompt. | Use when creating a new-chat prompt, handoff prompt, context checklist, UAT trigger map, or task-specific pickup map for CoverMate visitor, admin, CMS, Firebase, analytics, QA, release, or consistency work. |
| [`kaset-tan-phai-new-chat`](kaset-tan-phai-new-chat/SKILL.md) | Onboards fresh Codex chats for the Kaset Tan Phai / เกษตรทันภัย public water-risk alert project, including Nakhon Ratchasima dashboard decisions. | Use when creating a new-chat prompt, handoff prompt, context checklist, or task-specific pickup map for Kaset UI, data, Nakhon Ratchasima routes/geodata, map behavior, alerts, notifications, operations, QA, release, or deploy work. |
| [`korat-tan-phai-shared-components`](korat-tan-phai-shared-components/SKILL.md) | Preserves Korat shared React components, data semantics, and automatic snapshot evidence. | Use for Korat stats, selects, provenance chips, map previews, shared layout, or interaction changes. |
| [`mongkol-new-chat`](mongkol-new-chat/SKILL.md) | Onboards a fresh Codex chat for the Mongkol Wela / hora-astro project with read order, durable rules, source areas, and starter prompt. | Use when creating a new-chat prompt, handoff prompt, context checklist, or task-specific pickup map for Mongkol Wela work. |
| [`notenwert-maintainer`](notenwert-maintainer/SKILL.md) | Defines the operating playbook for the Notenwert project. | Use for Notenwert implementation, CMS/admin work, tests, docs, deploy prep, and commits. |
| [`tts-audio-assets`](tts-audio-assets/SKILL.md) | Manages TTS audio generation, reuse, audits, naturalness QA, voice policy, and data wiring across projects. | Use for lesson audio, UI playback, dialogues, prompts, stale/missing audio, or audio ID wiring. |
| [`shane-thai-audio-generator`](shane-thai-audio-generator/SKILL.md) | Manages Google Chirp audio generation, regeneration, audit, and QA for Thai lessons. | Use for Shane Thai lesson audio, Thai TTS text, audio IDs, voice selection, stale/missing audio, or naturalness fixes. |
| [`shane-thai-export-chatgpt`](shane-thai-export-chatgpt/SKILL.md) | Exports Shane Thai learner lesson content into ChatGPT-ready patch packets. | Use for all-lesson ChatGPT exports, lesson patch packets, or future learner tab/module proposal packets. |
| [`shane-thai-image-assets`](shane-thai-image-assets/SKILL.md) | Manages image selection, generation, reuse, cropping, and QA for Thai vocabulary lessons. | Use for Shane Thai lesson art, badge imagery, Unit image generation, or semantic asset mapping. |
| [`shane-thai-new-chat`](shane-thai-new-chat/SKILL.md) | Onboards a fresh Codex chat with Shane Thai read order, durable rules, skills, commands, and starter prompt. | Use when creating a new-chat prompt, handoff prompt, context checklist, or task-specific pickup map for Shane Thai. |
| [`shane-thai-prod-smoke`](shane-thai-prod-smoke/SKILL.md) | Runs safe authenticated production smoke checks for Shane Thai using the dedicated dummy learner account. | Use after Shane production deploys or when verifying login, topbar, Learning hub, learner-flow smoke, or production screenshot evidence. |
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
