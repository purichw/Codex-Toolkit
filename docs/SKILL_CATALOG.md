# Skill Catalog

This catalog explains what each skill is for and the context in which it should
be used. The shorter index in [../README.md](../README.md) is for quick scanning;
this file is for choosing the right skill during real work.

## General Workflow

### project-onboarding

- Skill file: [../skills/project-onboarding/SKILL.md](../skills/project-onboarding/SKILL.md)
- Description: Builds a reliable mental map of a repository before implementation.
- Use when: Starting in an unfamiliar or returning codebase, continuing from
  handoff notes, finding commands, locating deploy paths, or preparing a safe
  implementation plan.
- Typical context: `README*`, `AGENTS*`, `CLAUDE*`, `HANDOFF*`, `Memory*`,
  docs, package files, CI config, deployment config, and current `git status`.

### docs-cartographer

- Skill file: [../skills/docs-cartographer/SKILL.md](../skills/docs-cartographer/SKILL.md)
- Description: Creates or updates project maps that explain routes, modules,
  data flow, ownership boundaries, commands, and handoff context.
- Use when: A project needs site maps, architecture docs, interaction maps,
  onboarding docs, memory docs, or better navigation for future sessions.
- Typical context: Existing docs first, then current routes, components, APIs,
  state stores, auth, config, tests, scripts, and deployment files.

### regression-hunter

- Skill file: [../skills/regression-hunter/SKILL.md](../skills/regression-hunter/SKILL.md)
- Description: Searches for a broader class of failures after one bug reveals a
  pattern.
- Use when: Checking for similar hardcoded values, stale placeholders, duplicated
  logic, fragile selectors, or repeated behavior breaks across a codebase.
- Typical context: The concrete bug, violated invariant, related strings,
  selectors, helpers, tests, fixtures, demos, and generated docs.

### release-gate

- Skill file: [../skills/release-gate/SKILL.md](../skills/release-gate/SKILL.md)
- Description: Defines proportional verification before commit, push, deploy,
  merge, release, or handoff.
- Use when: Shipping changes, opening a PR, deploying, checking readiness, or
  confirming a feature is safe enough to publish.
- Typical context: `git status`, staged and unstaged diffs, affected surfaces,
  available test/build commands, browser verification for frontend changes, and
  deployment target.

### efficient-execution

- Skill file: [../skills/efficient-execution/SKILL.md](../skills/efficient-execution/SKILL.md)
- Description: Chooses the fastest quality-preserving path through discovery,
  implementation, verification, commit, push, deploy, and handoff work.
- Use when: Work feels slow, the user asks to move faster, a check plan needs
  batching or trimming, existing evidence might be reused, or a task needs clear
  stop rules without lowering the acceptance bar.
- Typical context: User target, changed risk tier, current diff or source
  state, previously gathered evidence, repo-defined commands, selected domain
  skills, skipped-check rationale, and the next fastest safe step.

### usage-budget-gate

- Skill file: [../skills/usage-budget-gate/SKILL.md](../skills/usage-budget-gate/SKILL.md)
- Description: Chooses and communicates the right work depth before expensive
  discovery, UI/UX audit, Claude parity, regression hunts, release checks, UAT,
  screenshots, test suites, or deploy verification.
- Use when: The user asks to avoid high usage, move faster or cheaper, decide
  fast versus deep mode, set stop rules, define escalation triggers, or prevent
  broad audits from running unnecessarily.
- Typical context: Proposed depth, why that depth fits, evidence needed, stop
  rule, escalation triggers, checks intentionally skipped, user-visible risk,
  and residual risk after the chosen pass.

### uat-environment

- Skill file: [../skills/uat-environment/SKILL.md](../skills/uat-environment/SKILL.md)
- Description: Defines lightweight production-like preview/UAT environments,
  seed/reset data, auth bypass policy, promotion gates, and rollback evidence.
- Use when: Frontend UI, admin/CMS, auth/data/API/config, generated assets,
  Claude parity, mobile QA, or deploy readiness needs realistic verification
  before production.
- Typical context: UAT URL, build or commit, isolated env vars/secrets, data
  fixture/reset plan, test accounts and roles, auth mode, external-service
  boundaries, routes/flows checked, logs/screenshots, skips, promotion decision,
  and rollback path.

### prod-smoke-harness

- Skill file: [../skills/prod-smoke-harness/SKILL.md](../skills/prod-smoke-harness/SKILL.md)
- Description: Sets up, documents, runs, or audits safe production and preview
  smoke harnesses for web apps.
- Use when: A deployed app needs HTTP smoke, browser smoke, authenticated smoke
  policy, Playwright automation, production screenshot evidence, test-account
  rules, or a reusable post-deploy harness.
- Typical context: Production/preview URLs, commit or build under test, approved
  smoke account policy, auth providers and roles, allowed live mutations,
  cleanup/reset path, routes to verify, console/network failure policy,
  snapshots, skipped checks, and release decision.

### production-asset-smoke

- Skill file: [../skills/production-asset-smoke/SKILL.md](../skills/production-asset-smoke/SKILL.md)
- Description: Verifies deployed website media and asset rendering after image,
  video, CMS, fallback, service-worker, or deploy changes.
- Use when: Production or preview pages need proof that images, CSS
  backgrounds, videos, posters, lazy-loaded assets, fallbacks, and external
  media domains render without broken requests, stale URLs, ORB/CORS failures,
  or blank boxes.
- Typical context: Deploy URL, commit/build, route list, changed media surfaces,
  stale domains to check, browser network failures, DOM media source inventory,
  screenshots, fallback decisions, rerun result, and residual media risk.

### mobile-web-qa

- Skill file: [../skills/mobile-web-qa/SKILL.md](../skills/mobile-web-qa/SKILL.md)
- Description: Audits responsive web UI across representative mobile, tablet,
  and desktop viewports.
- Use when: Checking iPhone, Android, tablet, Safari, Chrome on iOS, keyboard
  behavior, safe areas, touch targets, overflow, sticky regions, modals, or
  pre-deploy frontend QA.
- Typical context: A local or deployed URL, primary flows, viewport matrix,
  screenshots, console output, failed assets, and dynamic content states.

### snapshot

- Skill file: [../skills/snapshot/SKILL.md](../skills/snapshot/SKILL.md)
- Description: Captures, crops, inspects, and presents UI screenshots with
  enough surrounding context for review.
- Use when: The user asks for screenshots, snapshots, before/after evidence,
  UI comparisons, crops, viewport captures, production smoke evidence, or says a
  screenshot is too tight or missing context.
- Typical context: Target URL or app state, viewport, route, scroll position,
  interaction state, computed geometry when useful, and absolute screenshot
  paths for final presentation.

## Design And Visual Parity

### claude-to-a-tee

- Skill file: [../skills/claude-to-a-tee/SKILL.md](../skills/claude-to-a-tee/SKILL.md)
- Description: Treats offline Claude HTML as executable design documentation and
  matches it at measured component level while preserving product behavior.
- Use when: The user says "to a tee", asks for pixel/component parity, or wants
  a UI implemented from Claude HTML, screenshots, handoff files, or exported
  assets.
- Typical context: Offline Claude HTML/CSS/JS, screenshots, reference assets,
  existing product behavior, responsive states, interactions, measured parity
  audit rows, and verification checklist.

### design-direction

- Skill file: [../skills/design-direction/SKILL.md](../skills/design-direction/SKILL.md)
- Description: Defines, critiques, or preserves product visual direction across
  projects.
- Use when: Creating design briefs, redesign strategy, visual north stars,
  brand/product UX principles, public vs admin UX direction, typography/color/
  imagery guardrails, Claude Design prompts, or implementation handoff guidance.
- Typical context: Product purpose, audience, positioning, existing design
  briefs, screenshots/prototypes, brand assets, current implementation, design
  system primitives, responsive behavior, and release constraints.

### export-html

- Skill file: [../skills/export-html/SKILL.md](../skills/export-html/SKILL.md)
- Description: Creates to-a-tee standalone/offline HTML exports and clickable
  prototypes for design handoff, visual audit, or state review.
- Use when: The user asks to export HTML, standalone HTML, offline HTML,
  clickable prototypes, design handoff files, or Claude/Figma-inspectable
  reference artifacts.
- Typical context: Source screen or route, live app screenshots/computed
  dimensions, state inventory, product CSS/assets/copy, responsive breakpoints,
  and browser verification of the exported file.

### notenwert-design-direction

- Skill file: [../skills/notenwert-design-direction/SKILL.md](../skills/notenwert-design-direction/SKILL.md)
- Description: Preserves Notenwert's editorial, civic, musical, and cultural
  network visual direction.
- Use when: Designing, critiquing, or briefing Notenwert public site UX, admin
  CMS UX, homepage hero motion, NGA-style sticky/scrub interactions, typography,
  color, imagery, or responsive behavior.
- Typical context: Notenwert design brief, NGA reference notes, codebase map,
  content model, screenshots, and current project rules.

## UI UX Quality

### ui-ux-orchestrator

- Skill file: [../skills/ui-ux-orchestrator/SKILL.md](../skills/ui-ux-orchestrator/SKILL.md)
- Description: Routes broad UI/UX work to the smallest useful set of design,
  UX, visual QA, accessibility, flow, state, form, data-density, and release
  skills.
- Use when: A request is broad or blurry, the user asks for UI/UX polish or
  audit work, a Claude/Figma/reference handoff has multiple risk types, or the
  right combination of UI/UX skills is not obvious.
- Typical context: Goal, primary UI/UX risk, available reference material,
  changed screens and flows, likely evidence needed, and which downstream skill
  files should be read next.

### consistency-audit

- Skill file: [../skills/consistency-audit/SKILL.md](../skills/consistency-audit/SKILL.md)
- Description: Audits whether UI, UX, frontend implementation, shared
  components, pattern weight, and consolidation opportunities form one coherent
  product system.
- Use when: Checking layouts, components, typography, spacing, colors, icons,
  copy tone, interaction patterns, responsive behavior, states, forms,
  data-dense screens, shared primitives, duplicated components, or CSS that may
  need consolidation.
- Typical context: Explicit requirements, design docs or handoffs, comparable
  screens, shared components/tokens/utilities, weighted pattern ledger,
  historical stability, outliers, duplicate implementation traces, screenshots,
  severity, recommended fix phase, and safety checks.

### product-ux-contracts

- Skill file: [../skills/product-ux-contracts/SKILL.md](../skills/product-ux-contracts/SKILL.md)
- Description: Preserves or intentionally changes real product UX contracts
  during redesign, restyling, Claude/Figma implementation, or frontend
  refactors.
- Use when: Routing, deep links, persistence, internal scroll, progressive
  disclosure, focus, permissions, destructive safety, loading/empty/error
  states, media fallbacks, or search click-through could be flattened by a new
  design.
- Typical context: Current product behavior, reference behavior, source/tests
  for routes and state keys, decision ledger entries, implementation rule,
  verification proof, and user acceptance for intentional removals.

### ui-state-matrix

- Skill file: [../skills/ui-state-matrix/SKILL.md](../skills/ui-state-matrix/SKILL.md)
- Description: Defines and verifies UI state coverage beyond the happy path.
- Use when: A component or flow needs default, hover, focus, selected, disabled,
  loading, empty, error, success, validation, permission denied, long text,
  localization, stale/offline, partial failure, or responsive state handling.
- Typical context: Component or flow, reachable state set, triggers, expected
  UI, data/auth condition, reference behavior when any, implementation path,
  screenshots/tests, and skipped-state rationale.

### interaction-flow-qa

- Skill file: [../skills/interaction-flow-qa/SKILL.md](../skills/interaction-flow-qa/SKILL.md)
- Description: Verifies real user/admin journeys by exercising routing, state,
  data, permissions, feedback, reload, and back behavior end to end.
- Use when: Search-to-detail, filter/reload/back, onboarding, navigation,
  modal/drawer, admin create/edit/publish, signup, destructive action, media
  playback, progress, or completion flows must be proven.
- Typical context: Flow ledger, entry point, auth/role/data/viewport
  preconditions, step-by-step expected URL/state/data, success and failure
  states, screenshots, console/network results, and residual journey risk.

### design-system-guardian

- Skill file: [../skills/design-system-guardian/SKILL.md](../skills/design-system-guardian/SKILL.md)
- Description: Preserves or extends a product design system while changing UI.
- Use when: Component/token drift, inconsistent buttons/cards/forms/tables,
  typography or spacing mismatch, one-off CSS, variant sprawl, icon/radius/
  shadow inconsistency, cross-page regression, or reference integration risk
  appears.
- Typical context: Existing tokens, primitives, variants, layout rules,
  neighboring surfaces, chosen reuse/extend/local-exception decision, state
  coverage, screenshots, tests, and design-system debt.

### accessible-interaction

- Skill file: [../skills/accessible-interaction/SKILL.md](../skills/accessible-interaction/SKILL.md)
- Description: Designs, audits, or verifies accessible UI interaction behavior.
- Use when: Keyboard navigation, focus order, focus traps, focus restore, ARIA
  names/states, semantic controls, screen-reader-visible state, contrast,
  reduced motion, touch targets, mobile keyboard, modal/drawer accessibility, or
  skip links matter.
- Typical context: Changed controls and containers, keyboard path, focus target,
  accessible name/role/state, dialog/menu behavior, contrast/motion/touch
  coverage, screenshots/tests, and skipped assistive-technology checks.

### data-dense-ux

- Skill file: [../skills/data-dense-ux/SKILL.md](../skills/data-dense-ux/SKILL.md)
- Description: Guides dense operational UI such as admin dashboards, tables,
  lists, ledgers, CMS grids, filters, pagination, bulk actions, virtualized
  lists, relationship maps, and panels.
- Use when: Information density, scanning, sorting, item counts, selection,
  overflow, responsive compression, large-data behavior, or repeated operational
  workflows matter.
- Typical context: Primary data task, fields by priority and risk, sorting/
  filtering/pagination contracts, realistic item counts, long labels, edge
  records, responsive behavior, screenshots/tests, and large-data residual risk.

### form-flow-ux

- Skill file: [../skills/form-flow-ux/SKILL.md](../skills/form-flow-ux/SKILL.md)
- Description: Covers complete create/edit form journeys rather than only form
  appearance.
- Use when: Validation, dirty state, autosave, drafts, save/cancel/reset,
  submit loading, duplicate-submit prevention, server errors, permission denied,
  optimistic UI, mobile keyboard, uploads, crop state, multistep forms, or
  admin/CMS form behavior is touched.
- Typical context: Form mode, data source, field roles, validation timing,
  dirty/autosave/cancel rules, submit/success/error behavior, permission mode,
  mobile keyboard path, screenshots/tests, and unverified backend risk.

## Firebase And Security

### account-recovery-key

- Skill file: [../skills/account-recovery-key/SKILL.md](../skills/account-recovery-key/SKILL.md)
- Description: Defines provider-neutral recovery-key flows for signup, password
  reset, signed-in regeneration, hashing, invalidation, and display policy.
- Use when: A project needs recovery codes/keys, recovery ID, password reset
  without email, account-settings regeneration, recovery hash storage, old-key
  invalidation, or reusable auth guidance across Firebase, Supabase, custom
  auth, or local-first apps.
- Typical context: Auth boundary, account identifier, profile/login records,
  recovery-key format, hash/HMAC rule, signup reveal UI, reset flow,
  regeneration surface, rate limiting, audit logging, mobile UX, and tests for
  wrong-key and old-key invalidation.

### firebase-account-management

- Skill file: [../skills/firebase-account-management/SKILL.md](../skills/firebase-account-management/SKILL.md)
- Description: Separates Firebase account flows, Auth providers, Firestore user
  documents, Admin SDK behavior, custom claims, and billing assumptions.
- Use when: Designing, auditing, debugging, or explaining signup/login, Google
  or email-password providers, Firestore profiles, admin CRUD, Firebase Admin
  SDK, service accounts, custom claims, or Spark vs Blaze requirements.
- Typical context: Firebase app config, Auth providers, Firestore collections,
  security rules, backend routes, Admin SDK usage, service-account handling, and
  billing state when relevant.

### firebase-security-rules

- Skill file: [../skills/firebase-security-rules/SKILL.md](../skills/firebase-security-rules/SKILL.md)
- Description: Focuses on Firebase Auth, Firestore Rules, Admin SDK bypasses,
  service-account environment variables, and production access guarantees.
- Use when: Auditing or changing Firestore rules, privileged backend endpoints,
  auth gates, secrets, Firebase security posture, or billing-sensitive claims.
- Typical context: `firestore.rules`, `firebase.json`, Firebase config, backend
  Admin SDK entrypoints, deployment secrets, CI workflows, and security docs.

## Reusable Product Domains

### admin-ops

- Skill file: [../skills/admin-ops/SKILL.md](../skills/admin-ops/SKILL.md)
- Description: Guides admin portal operations where UI can change real data,
  permissions, content, accounts, or operational state.
- Use when: Designing, auditing, implementing, or verifying admin auth/roles,
  dashboards, lifecycle actions, revisions, audit logs, destructive actions,
  relationship maps, privileged backend actions, or CMS/admin UX.
- Typical context: Admin routes, auth/role source, data contracts, privileged
  routes, Admin SDK/service accounts, audit logs, destructive confirmations,
  fixtures, deploy/runbooks, and rollback notes.

### admin-prototype-reconciliation

- Skill file: [../skills/admin-prototype-reconciliation/SKILL.md](../skills/admin-prototype-reconciliation/SKILL.md)
- Description: Reconciles new admin/CMS/dashboard prototypes, Claude/Figma
  references, offline HTML, and design-side data models against live production
  admin systems before implementation.
- Use when: Prototype fields, components, workflows, draft/publish states,
  revisions, auth/roles, navigation/settings, store APIs, or fixture models
  must be classified as already live, net-new, conflicting, or mock-only before
  merging.
- Typical context: Prototype files and fixtures, live admin routes and APIs,
  validators, auth checks, live read/write data source, public consumption
  paths, field map, component classification, gating decisions, mock/unbuilt
  list, and do-not-implement-yet blockers.

### ledger-logic

- Skill file: [../skills/ledger-logic/SKILL.md](../skills/ledger-logic/SKILL.md)
- Description: Protects collaborative ledger behavior where actors, entries,
  shares, payments, obligations, and settlement outputs must stay correct.
- Use when: Implementing, auditing, or debugging expenses, splits, payer/
  participant logic, settlement math, reciprocal netting, guests vs real
  accounts, invites, imports/exports, persistence contracts, or ledger tests.
- Typical context: Actor identity model, entry shape, split modes, settlement
  algorithm, rounding examples, persistence shape, invite/guest lifecycle, and
  regression tests.

### native-parity

- Skill file: [../skills/native-parity/SKILL.md](../skills/native-parity/SKILL.md)
- Description: Keeps native iOS/Android apps aligned with web/product source of
  truth behavior.
- Use when: Working on Expo, React Native, native builds, web/native data
  parity, shared backend contracts, native screen parity, mobile design
  handoffs, device build gates, or preventing static sample-app drift.
- Typical context: Native root, build docs, environment files, shared data
  contracts, backend routes, navigation map, design references, platform config,
  and typecheck/build/simulator commands.

### site-maintainer

- Skill file: [../skills/site-maintainer/SKILL.md](../skills/site-maintainer/SKILL.md)
- Description: Maintains website projects where source files, generated deploy
  artifacts, tests, docs, and hosting outputs must stay aligned.
- Use when: Working on static or built sites, generated deploy folders, service
  worker/version churn, CMS/admin site work, build scripts, deploy prep, commit
  hygiene, or project work logs.
- Typical context: Project root, source folder, generated output, build/dev
  commands, tests, hosting target, docs/runbooks, generated assets, and deploy
  path.

## Coin Quest

### coin-quest-admin-ops

- Skill file: [../skills/coin-quest-admin-ops/SKILL.md](../skills/coin-quest-admin-ops/SKILL.md)
- Description: Keeps Coin Quest Ledger Admin Portal work aligned with the live
  Firebase-backed implementation.
- Use when: Working on Super Admin auth, boards, users, account lifecycle,
  reset/delete flows, publish/restore, revisions, relationship maps, or admin
  Firebase behavior.
- Typical context: Admin implementation docs, security docs, data contracts,
  `/admin/` source files, privileged API routes, and Firestore rules when
  permissions are involved.

### coin-quest-ledger-logic

- Skill file: [../skills/coin-quest-ledger-logic/SKILL.md](../skills/coin-quest-ledger-logic/SKILL.md)
- Description: Protects Party Ledger behavior for split math, participants,
  guests, invites, Character IDs, reminders, and settlement.
- Use when: Editing payer/participant logic, Add by Character ID, Add Guest,
  Reminders invites, direct invite links, settlement calculations, or ledger
  regressions.
- Typical context: Current memory and invite docs, site map, data contracts,
  shared ledger logic, trip UI wiring, unit tests, and relevant Playwright tests.

### coin-quest-native-parity

- Skill file: [../skills/coin-quest-native-parity/SKILL.md](../skills/coin-quest-native-parity/SKILL.md)
- Description: Keeps the Coin Quest Expo app aligned with web data contracts,
  native build gates, and real backend state.
- Use when: Working on the native app, iOS/Android builds, native screen parity,
  `playerModules`, or web/native backend contract questions.
- Typical context: Native parity docs, mobile README, iOS build notes,
  architecture docs, data contracts, site map, and relevant `mobile/src/` files.

## Notenwert

### notenwert-maintainer

- Skill file: [../skills/notenwert-maintainer/SKILL.md](../skills/notenwert-maintainer/SKILL.md)
- Description: Provides the safe operating playbook for implementation work in
  the Notenwert project.
- Use when: Fixing Notenwert bugs, editing CMS/admin behavior, changing homepage
  hero behavior, updating content models, adding tests, preparing deploys,
  updating docs, or making commits.
- Typical context: `AGENTS.md`, codebase map, content model, NGA reference for
  hero/banner work, source under `src/`, build script, regression tests, and
  work log.

## Shane And His Thai

### shane-thai-prod-smoke

- Skill file: [../skills/shane-thai-prod-smoke/SKILL.md](../skills/shane-thai-prod-smoke/SKILL.md)
- Description: Runs or sets up safe authenticated production smoke checks for
  the Shane and His Thai app using the dedicated dummy learner account.
- Use when: Verifying Shane production after Vercel deploys, checking the
  production login surface, topbar, Learning hub, learner-flow smoke policy, or
  collecting screenshot evidence for `https://shane-and-his-thai.vercel.app`.
- Typical context: Project root, current commit/deploy URL, production alias,
  dummy learner account policy, HTTP status/header smoke, unauthenticated title
  and login surface, authenticated `codex` learner flow, console/network
  failures, snapshot path, skipped live mutations, and failure classification.

### shane-thai-export

- Skill file: [../skills/shane-thai-export/SKILL.md](../skills/shane-thai-export/SKILL.md)
- Description: Exports Shane and His Thai learner content, scene/dialogue
  rewrite packets, unit text dumps, Claude/offline HTML handoffs, clickable
  learner prototypes, and ChatGPT-ready restructuring briefs.
- Use when: The user asks for Shane Thai exports, ChatGPT content packets,
  unit exports, learner journey handoffs, dialogue/scene restructure material,
  Claude design/offline HTML files, or which files to give ChatGPT or Claude.
- Typical context: Thai flashcards project root, export type, target reader,
  output folder, unit count, README instructions, unit content files, project
  export command, spot-check unit, and files the next tool should or should not
  receive.

## Image And Asset Work

### course-image-assets

- Skill file: [../skills/course-image-assets/SKILL.md](../skills/course-image-assets/SKILL.md)
- Description: Manages educational course image generation, reuse, cropping,
  mapping, audits, and QA across projects.
- Use when: Working on vocabulary images, lesson card art, visual hints, badges,
  semantic image mapping, inclusive learning imagery, crop/centering fixes, or
  generated educational illustrations.
- Typical context: Learning item, meaning, lesson context, target component,
  existing mappings/files/manifests, image audit reports, canonical helper/
  manifest, crop constraints, alt text, and card/thumbnail rendering.

### placeholder-image

- Skill file: [../skills/placeholder-image/SKILL.md](../skills/placeholder-image/SKILL.md)
- Description: Sources, selects, replaces, crops, and audits placeholder images
  as product content rather than decoration.
- Use when: Populating missing images, replacing placeholders, finding stronger
  hero/card/gallery photos, matching images to a brand mood or content type,
  fixing bad crops/object-position, auditing responsive image reuse, removing
  low-quality stock or watermarked images, or creating a sourcing playbook.
- Typical context: Image slot brief, surrounding copy, desired mood, subject,
  crop/container dimensions, responsive reuse, licensing/source notes, alt text,
  and rendered page screenshots when the image affects a real product surface.

### shane-thai-audio-generator

- Skill file: [../skills/shane-thai-audio-generator/SKILL.md](../skills/shane-thai-audio-generator/SKILL.md)
- Description: Generates, regenerates, audits, and QA-checks Google Chirp audio
  files for the Shane and His Thai learning app.
- Use when: Working on lesson audio, main-course Chirp generation, audio ID
  wiring, Thai TTS text, voice selection, full-phrase regeneration, stale or
  missing audio audits, or naturalness fixes.
- Typical context: Unit ID, audio ID, output path, displayed Thai text, spoken
  Thai text, English meaning, speaker role, politeness particle, voice policy,
  generation commands, audit reports, and whether the item is a word, phrase,
  sentence, dialogue line, grammar example, quiz prompt, or UI prompt.

### tts-audio-assets

- Skill file: [../skills/tts-audio-assets/SKILL.md](../skills/tts-audio-assets/SKILL.md)
- Description: Generates, regenerates, reuses, audits, and QA-checks text-to-
  speech audio assets across projects.
- Use when: Working on lesson audio, prompts, UI playback, dialogues, story
  lines, voice/pacing policy, stale or missing audio audits, naturalness fixes,
  or audio ID/data wiring.
- Typical context: Audio ID, source entry, target path, displayed vs spoken
  text, language/script, pronunciation overrides, meaning, lesson/component,
  voice policy, provider credentials/project, and audit/naturalness reports.

### shane-thai-image-assets

- Skill file: [../skills/shane-thai-image-assets/SKILL.md](../skills/shane-thai-image-assets/SKILL.md)
- Description: Guides image generation, reuse, crop fixes, optimization, and QA
  for the Shane and His Thai learning app.
- Use when: Adding or replacing vocabulary images, mapping lesson card artwork,
  generating Unit images, fixing crops, making badge assets, or deciding whether
  an existing image is semantically correct.
- Typical context: Exact Thai item, English meaning, lesson context, existing
  asset mappings, image files, flashcard rendering size, and app visual style.

### image-boundary-iteration

- Skill file: [../skills/image-boundary-iteration/SKILL.md](../skills/image-boundary-iteration/SKILL.md)
- Description: Controls adult non-explicit image iteration with prompt hygiene,
  branch routing, verdict loops, visual baselines, and logging.
- Use when: Continuing the nudity-reference-prompting project, handling
  Pass/Partial/Reject loops, making local edits, reducing visual clutter,
  strengthening poses within non-explicit boundaries, or maintaining branch
  baselines.
- Typical context: Branch notes, visual baseline files, workbook/JSON/Markdown
  logs, prompt strategy notes, rejection-handling notes, and the user's current
  verdict shorthand.

### image-boundary

- Skill file: [../skills/image-boundary/SKILL.md](../skills/image-boundary/SKILL.md)
- Description: Routes all adult non-explicit image-boundary work to the
  smallest useful set of boundary iteration, polish, max-push, recovery, and
  safety-map skills.
- Use when: The user invokes `/image-boundary`, is unsure which image-boundary
  skill applies, asks to continue PASS/PARTIAL/REJECT loops, push sensual
  non-explicit boundaries, recover from safety blocks, polish quality, map risk,
  update docs, or coordinate several image-boundary skills.
- Typical context: User request, current branch/base/verdict, whether the task
  is normal iteration, quality repair, max non-explicit push, rejection
  recovery, safety mapping, or docs/logging, plus the exact downstream skill
  files to read.

### image-boundary-efficient

- Skill file: [../skills/image-boundary-efficient/SKILL.md](../skills/image-boundary-efficient/SKILL.md)
- Description: Adds a removable speed-preserving operating layer over
  image-boundary workflows without replacing the boundary, polish, recovery, or
  safety skills.
- Use when: The user wants Imagen/image-boundary iterations faster, cheaper,
  less blocked, less retry-heavy, or asks to add, remove, pause, or toggle
  efficient mode without lowering quality.
- Typical context: Current base/verdict, active downstream boundary skill,
  whether efficient mode should be active, one selected push axis, quality bar,
  blocked prompt families to avoid, prompt shape, generated result, and reason
  to turn the layer off.

### image-boundary-nonexplicit-max

- Skill file: [../skills/image-boundary-nonexplicit-max/SKILL.md](../skills/image-boundary-nonexplicit-max/SKILL.md)
- Description: Pushes sensual, intimate, boundary-forward adult image prompts to
  the strongest safe non-explicit result.
- Use when: The user wants stronger sensuality, intimacy, reduced costume bulk,
  visible skin-read, or maximum fantasy/editorial intensity without explicit
  nudity detail, sexual acts, or safety-system evasion.
- Typical context: Accepted base and branch, translated non-explicit visual
  goal, selected push axis, coverage structure, quality requirements, generated
  prompt, tool result, and PASS/PARTIAL/REJECT verdict.

### image-boundary-polish

- Skill file: [../skills/image-boundary-polish/SKILL.md](../skills/image-boundary-polish/SKILL.md)
- Description: Restores quality in accepted boundary-forward non-explicit image
  iterations without changing the boundary level.
- Use when: An accepted image is muddy, artifacted, breaking, or needs face,
  hand, anatomy, water/reflection, linework, lighting, or rendering cleanup
  before the `image-boundary-iteration` workflow continues.
- Typical context: Strongest accepted base, branch identity and medium,
  accepted boundary level, pose/crop/waterline/lower-frame structure to
  preserve, defects to repair, forbidden boundary changes, verdict, and logging
  decision.

### image-boundary-rejection-recovery

- Skill file: [../skills/image-boundary-rejection-recovery/SKILL.md](../skills/image-boundary-rejection-recovery/SKILL.md)
- Description: Recovers after image generation safety blocks, moderation
  rejections, user REJECT verdicts, underdelivery, identity drift, local-edit
  saturation, or quality collapse.
- Use when: A boundary-forward prompt family blocks, repeats a failure, misses
  the user's goal, damages quality, drifts identity, or needs a safe
  change-of-HOW rather than another retry.
- Typical context: Failure class, blocked or rejected prompt family, last
  accepted base, branch identity, what worked, what failed, new visual
  mechanism, stop rule, recovery prompt, and next verdict.

### image-boundary-safety-map

- Skill file: [../skills/image-boundary-safety-map/SKILL.md](../skills/image-boundary-safety-map/SKILL.md)
- Description: Maps risk zones and safe routes for boundary-forward adult
  non-explicit image prompting before generation.
- Use when: The user asks for stronger sensuality, nudity-adjacent styling,
  intimate poses, fewer garments, transparent water, bedroom/bathhouse scenes,
  or anything near the non-explicit safety limit.
- Typical context: Request translation, selected risk zone, route/skill choice,
  current base type, allowed non-explicit mechanism, disallowed explicit detail
  or repeated blocked family, exact prompt, and post-generation verdict.
