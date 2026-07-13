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

## Firebase And Security

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
