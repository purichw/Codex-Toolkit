# Skill Catalog

This catalog explains what each skill is for and the context in which it should
be used. The shorter index in [../README.md](../README.md) is for quick scanning;
this file is for choosing the right skill during real work.

Reusable, non-project-specific skills also have `global-*` aliases. See
[GLOBAL_SKILLS.md](GLOBAL_SKILLS.md) for the alias map and the list of skills
that intentionally remain project-specific or specialized.

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
  merge, release, or handoff across all active deliverables. Required failed,
  blocked, pending, or unrun checks block readiness; disclosure is not a pass.
- Use when: Shipping changes, opening a PR, deploying, checking readiness, or
  confirming a feature is safe enough to publish.
- Typical context: `git status`, staged and unstaged diffs, affected surfaces,
  available test/build commands, browser verification for frontend changes, and
  deployment target.
- CI evidence: Record run/attempt, tested SHA, relevant jobs, terminal results,
  and deployment target where applicable. A green workflow with required tests
  skipped, or secrets merely present, does not establish readiness. Route actual
  Actions failure diagnosis to `github-actions-repair`.
- Release waits: Set measured diagnostic checkpoints, inspect failures before
  retrying, and keep push, CI, build readiness, promotion and monitoring evidence
  separate. Docs-only evidence reuse must prove the exact eligible baseline.

### github-actions-repair

- Skill file: [../skills/github-actions-repair/SKILL.md](../skills/github-actions-repair/SKILL.md)
- Global alias: [global-github-actions-repair](../skills/global-github-actions-repair/SKILL.md)
- Description: Diagnoses failed, slow or stalled GitHub Actions runs and verifies the smallest
  evidence-backed repair without weakening checks or exposing credentials.
- Use when: Investigating recurring failure emails, workflow logs, setup timeouts,
  missing/scoped secrets, authentication failures, flaky checks, or a mismatch
  between workflow ref and deployment target, missing triggers/checks or pending
  promotion. Inspect causal errors and progress before another attempt.
- Typical context: Repository/workflow/event, branch/SHA, run ID/attempt,
  first causal error, recent relevant runs, exact secret names and scope,
  authorized workflow side effects, and terminal checks for the fixed revision.
- Boundary: Ordinary release readiness belongs to `release-gate`; authenticated
  live checks use `prod-smoke-harness`. Historical notifications are not proof of
  a current failure. Reruns, publishing, production writes, and cross-chat work
  still require their own applicable authorization; secret values stay out of chat.

### github-actions-usage

- Skill file: [../skills/github-actions-usage/SKILL.md](../skills/github-actions-usage/SKILL.md)
- Global alias: [global-github-actions-usage](../skills/global-github-actions-usage/SKILL.md)
- Description: Measures Actions runner work, repeated runs and artifact/cache
  usage, then chooses evidence-backed optimizations without losing coverage.
- Use when: Auditing CI usage/costs, duplicate work, browser/dependency setup,
  caching, artifacts or conservative docs-only workflow routing.
- Typical context: Bounded run/attempt/job history, current billing evidence,
  comparable workflow modes, runner types, exact baseline SHA, affected consumers
  and required aggregate gates. Elapsed time and billed usage are different.
- Boundary: Failures route to `github-actions-repair`; publishing uses
  `release-gate`. No implicit spending, visibility/credential changes, artifact
  deletion or required-check bypass. Savings need comparable post-change evidence.

### rollback-guardrail

- Skill file: [../skills/rollback-guardrail/SKILL.md](../skills/rollback-guardrail/SKILL.md)
- Description: Classifies rollback risk. Pauses and understood reversible edits
  stay lightweight; risky work loss requires concrete authorization and recovery.
- Use when: Rollback, removal, replacement, history/data changes, or uncertain
  ownership could discard work, or when releasing after a risky rollback.
- Typical context: `git status`, recent diffs, untracked files, checkpoint path,
  staged and unstaged patches, restore note or `docs/rollback-parking-lot.md`,
  live routes affected, parked features, removed verification, and follow-up
  smoke/test evidence.

### efficient-execution

- Skill file: [../skills/efficient-execution/SKILL.md](../skills/efficient-execution/SKILL.md)
- Description: Chooses the smallest quality-preserving path through discovery,
  implementation, verification, commit, push, deploy, handoff work, and
  usage-budget decisions while tracking every active deliverable to completion.
- Use when: Work feels slow, the user asks to move faster or spend less usage, a
  check plan needs batching or trimming, existing evidence might be reused, or a
  task needs protection against missed requirements during interruptions,
  context compaction, or work involving multiple deliverables.
- Typical context: Active requests and acceptance criteria, pending/done/blocked
  status, chosen depth, source and environment state, current evidence,
  asynchronous operation results, affected companion outputs, and blockers.
- Reference depth: Exact fidelity alone does not trigger a deep pass. Use current
  scoped evidence for isolated repairs; escalate for broader claims, affected
  shared/behavioral contracts, or insufficient targeted evidence.
- Completion rule: Stop adding checks once evidence is sufficient, but finish
  every active deliverable before claiming completion. Preserve unfinished work
  when messages arrive, reuse evidence only when all relevant conditions match,
  and distinguish implemented, verified, and blocked outcomes. For skill syncs,
  compare the live source with the archive and update affected catalogs; confirm
  the intended remote commit when publishing is authorized. A clean archive or
  successful local command alone does not prove the requested endpoint.
- Publishing recovery: Batch known corrections, collect existing review results,
  and diagnose overdue phases with measured checkpoints. One evidence-supported
  unchanged transient rerun is not permission to retry until green.

### usage-budget-gate

- Skill file: [../skills/usage-budget-gate/SKILL.md](../skills/usage-budget-gate/SKILL.md)
- Description: Thin compatibility router for proportional-effort prompts now
  owned by `efficient-execution`.
- Use when: Existing prompts mention `$usage-budget-gate`, or the user asks to
  avoid high usage, move faster or cheaper, decide fast versus deep mode, set
  stop rules, define escalation triggers, or prevent broad audits from running
  unnecessarily.
- Typical context: Read `$efficient-execution`; then report chosen depth,
  evidence needed, stop rule, escalation triggers, checks intentionally skipped,
  user-visible risk, and residual risk after the chosen pass.

### uat-environment

- Skill file: [../skills/uat-environment/SKILL.md](../skills/uat-environment/SKILL.md)
- Description: Defines lightweight production-like preview/UAT environments,
  seed/reset data, auth policy, complete acceptance coverage, and promotion gates
  that require passed checks and current evidence, plus post-promotion verification.
- Use when: Frontend UI, admin/CMS, auth/data/API/config, generated assets,
  reference parity, mobile QA, or deploy readiness needs realistic verification
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
- Actions integration: Reuse exact workflow secret names, check event/environment
  access, and prove real sign-in on the intended target. An explicitly authorized
  dedicated privileged test account may be appropriate; harness configuration
  alone does not authorize production writes. Setup-only repairs may reuse the
  existing required harness reports without a new full-site visual audit.
- Hosting challenges: Distinguish provider 403/429 challenges from application
  failure. Approved automation credentials need exact-origin and redirect safety,
  sanitized logs and final live monitor evidence, not only fixture success.

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
  desktop, browser-engine, and platform constraints.
- Use when: Checking iPhone, Android, tablet, Safari, Chrome on iOS, keyboard
  behavior, safe areas, touch targets, overflow, sticky regions, modals,
  WebViews, zoom, responsive media, mobile performance, or pre-deploy frontend
  QA.
- Typical context: A local or deployed URL, primary flows, viewport matrix,
  screenshots, console output, failed assets, dynamic content states, and
  `ui-ux-expert/references/responsive-web-design.md` for full-site responsive
  work.

### snapshot

- Skill file: [../skills/snapshot/SKILL.md](../skills/snapshot/SKILL.md)
- Description: Captures, crops, inspects, and presents UI screenshots with
  enough surrounding context for review.
- Use when: The user asks for screenshots, snapshots, before/after evidence,
  reference/development side-by-side evidence, UI comparisons, crops, viewport
  captures, production smoke evidence, or says a screenshot is too tight or
  missing context. Also use page-level evidence for whole-page/dashboard reviews,
  redesign, page-length, information-architecture, or page-level parity claims.
- Typical context: Target URL or app state, viewport, route, scroll position,
  interaction state, computed geometry when useful, full-page or labeled
  top/middle/bottom contact-sheet proof when the whole page matters, and
  absolute screenshot paths for final presentation.

Snapshot gate: UI/UX-related skills must invoke `snapshot` automatically before
the final response after visible implementation, redesign, restyle, visual
audit, responsive QA, Claude/Figma/reference handoff, or screenshot-based design
work. Reference matching requires Reference/Development side-by-side evidence;
add Before when before/after proof is requested or needed to judge the change.
A contextual region pair can prove a tiny repair. A single above-the-fold view
cannot prove whole-page/dashboard, page-length, or page-level reference parity.

## Design And Visual Parity

### claude-design-md-request

- Skill file: [../skills/claude-design-md-request/SKILL.md](../skills/claude-design-md-request/SKILL.md)
- Description: Drafts or refines Claude Design prompts that ask for
  implementation-ready Markdown handoffs/specs.
- Use when: The user wants a Claude MD request, Claude handoff prompt,
  component mapping request, design-to-code spec request, or a prompt that
  separates visual facts from product recommendations while preserving existing
  app contracts.
- Typical context: Target surface, screenshots, standalone HTML, prototypes,
  Figma notes, existing app route/source files, prevail rules, do-not-touch
  areas, required states/viewports, known product decisions, and acceptance
  checks Codex can verify.

### claude-design-reference-bundle

- Skill file: [../skills/claude-design-reference-bundle/SKILL.md](../skills/claude-design-reference-bundle/SKILL.md)
- Description: Creates upload-ready Claude Design handoff/reference bundles
  from live pages, local routes, screenshot sets, or prototypes.
- Use when: Claude Design needs a visual replication package with screenshots,
  measured specs, product context, state coverage, implementation contracts, and
  a paste-ready prompt, especially when a standalone HTML/to-a-tee export would
  be slower than a reference bundle.
- Typical context: Source route/URL or local file, desktop and mobile
  screenshots, relevant states, generated `metrics.json`, manifest, project
  context, design spec, reference states, implementation contract, prompt file,
  and quality-gate exceptions.

### codex-handoff-for-claude

- Skill file: [../skills/codex-handoff-for-claude/SKILL.md](../skills/codex-handoff-for-claude/SKILL.md)
- Description: Packages Codex's context, constraints, evidence, and acceptance
  checks into implementation-ready Markdown handoffs for Claude or Claude
  Design.
- Use when: The user asks to hand off a screen, route, component, prototype,
  screenshot set, design task, or implementation brief to Claude, especially for
  UI/UX work using `ui-ux-expert`.
- Typical context: Target surface, artifacts Codex has inspected, source-of-
  truth precedence, `DO NOT TOUCH` boundaries, product contracts, visual
  geometry, interaction states, responsive behavior, accessibility notes,
  confidence labels, open questions, and acceptance checks.

### reference-to-a-tee

- Skill file: [../skills/reference-to-a-tee/SKILL.md](../skills/reference-to-a-tee/SKILL.md)
- Description: Implements or audits measured component parity from HTML,
  image-only, or mixed references from any source while preserving real product
  UX and separating fidelity from effort.
- Use when: The user asks for screenshot-to-UI, image-file reconstruction,
  reference-to-code, to-a-tee matching, or precise visual repair from a designer,
  Figma export, Claude output, prototype, or another selected visual reference.
- Fidelity and effort: Exact by default for matching requests, faithful adaptation
  within requested flexibility, and design-skill routing for inspiration only.
  Fast isolated repairs use a short note and current contextual comparison;
  broader work adds affected states, measurements, and coverage/decision records.
  Neither speed nor missing source detail silently lowers acceptance criteria.
- Typical context: Source mode and authority, relevant image dimensions/crop/scale,
  observed facts versus inferred or unknown properties, affected product
  contracts, scoped measurements, and automatic `snapshot`
  Reference/Development evidence. Image-only work does not require
  reference HTML, DOM, or known breakpoints; unobserved behavior is not claimed
  as recovered source behavior.
- Migration and checks: [REFERENCE_PARITY_MIGRATION.md](REFERENCE_PARITY_MIGRATION.md).

### mockup-to-product

- Skill file: [../skills/mockup-to-product/SKILL.md](../skills/mockup-to-product/SKILL.md)
- Description: Translates approved mockups into coherent real-product experiences
  using authorized judgment about layout, assets, content and responsive behavior.
- Use when: The user wants recognizable composition and visual detail without
  literal pixel matching, or repeated visual rework needs a full design review.
- Typical context: Selected image/HTML references, actual rendered product,
  fixed versus flexible constraints, shared owners, truthful data substitutions,
  desktop/mobile image inspection, scoped snapshots and affected behavior checks.
- Updated guidance: Compare the same UI state, derive compactness from the
  selected reference, and preserve real results and controls rather than copying
  an illustrative height. Check alignment within controls, between peers, and
  within groups; inspect actual asset geometry and repeated user corrections.
  [Shared surfaces](../skills/mockup-to-product/references/shared-surfaces.md)
  separates page frames, banners, imagery, and primitives with real consumer
  migration and cross-page proof.
- Authoring and fidelity: Match complete component anatomy, actual glyphs, and
  role-specific typography at comparable content scale. For editable designs,
  exercise real insertion/order/visibility/style controls and save/reopen, then
  inspect live canvas, Preview, and public output. Preserve requested before
  evidence before editing and disclose missing captures. A narrow viewport repair
  checks affected views; a responsive/page-level claim needs desktop and mobile.
- Boundary: Explicit exact matching uses `reference-to-a-tee`; inspiration-only
  work uses design-direction skills. Naming this skill does not override an exact
  request. Flexibility does not authorize lost features or unsupported authoring.

### claude-to-a-tee

- Skill file: [../skills/claude-to-a-tee/SKILL.md](../skills/claude-to-a-tee/SKILL.md)
- Description: Compatibility router to `reference-to-a-tee`.
- Use when: Existing prompts explicitly invoke the old name. New prompts should
  use `reference-to-a-tee` or `global-reference-to-a-tee`.
- Compatibility: Old reference paths redirect to canonical guidance. The old
  extractor CLI forwards to the generic HTML helper, retaining its legacy
  output-directory default and worklog filename. Install the canonical skill
  alongside this router; do not maintain a second copy of the workflow here.

### design-direction

- Skill file: [../skills/design-direction/SKILL.md](../skills/design-direction/SKILL.md)
- Description: Defines, critiques, or preserves product visual direction across
  projects, including valid image-only, HTML/prototype, and mixed handoffs.
- Use when: Creating design briefs, redesign strategy, visual north stars,
  brand/product UX principles, public vs admin UX direction, typography/color/
  imagery guardrails, Claude Design prompts, or implementation handoff guidance.
- Typical context: Product purpose, audience, positioning, existing design
  briefs, screenshots/prototypes, brand assets, current implementation, design
  system primitives, responsive behavior, and release constraints. Handoffs name
  source authority, image calibration limits, missing states, and adaptations;
  they do not require HTML when only images are available.

### export-html

- Skill file: [../skills/export-html/SKILL.md](../skills/export-html/SKILL.md)
- Description: Creates to-a-tee standalone/offline HTML exports and clickable
  prototypes for design handoff, visual audit, or state review.
- Use when: The user asks to export HTML, standalone HTML, offline HTML,
  clickable prototypes, design handoff files, or Claude/Figma-inspectable
  reference artifacts.
- Typical context: Source screen or route, live app screenshots/computed
  dimensions, state inventory, product CSS/assets/copy, responsive breakpoints,
  browser verification of the exported file, existing dependency/tooling state,
  and cleanup rules that avoid deleting useful `node_modules` while still never
  committing it.

### global-full-design-spec

- Skill file: [../skills/global-full-design-spec/SKILL.md](../skills/global-full-design-spec/SKILL.md)
- Description: Exports comprehensive implementation-ready UI design specs from
  screenshots, source files, CSS, routes, prototypes, live app state, or design
  references.
- Use when: The user asks for a full or detailed design spec, exhaustive design
  handoff, complete page contract, source-mapped spec, accessibility/state
  matrix, or Markdown artifact that future Codex/Claude/dev work can implement
  from without rediscovery.
- Typical context: Screenshot/design reference, runtime route or surface,
  implementation files, styling/design-system files, components, states,
  responsive behavior, accessibility contract, guardrails, and QA checklist.

### global-quick-design-spec

- Skill file: [../skills/global-quick-design-spec/SKILL.md](../skills/global-quick-design-spec/SKILL.md)
- Description: Exports concise implementation-ready UI design specs quickly from
  screenshots, source files, CSS, routes, prototypes, or live app state.
- Use when: The user asks for a quick or fast design spec, lightweight design
  handoff, concise page spec, screenshot-to-spec export, or reusable Markdown
  artifact without redesigning or modifying app code.
- Typical context: Provided screenshot or visual artifact, likely route/source
  files, relevant component and style ranges, existing handoff examples,
  layout, visible components, tokens/styles, responsive behavior, accessibility,
  guardrails, and short QA checklist.

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

### ui-ux-expert

- Skill file: [../skills/ui-ux-expert/SKILL.md](../skills/ui-ux-expert/SKILL.md)
- Description: Designs, audits, and implements UI with cause-directed diagnosis,
  explicit tradeoffs, contextual defaults, selective alternatives, existing
  design systems, state coverage, and current visual/behavior evidence. Routes
  repeated UI and shared-contract changes to `design-system-guardian` for reuse,
  extraction, and consumer verification without forcing abstractions on tiny edits.
- Use when: Working on visual design, interaction design, accessibility,
  responsive UI, design systems, frontend polish, component galleries, layout
  exemplars, UX flow/state coverage, cross-browser/platform responsive QA,
  decks, documents, prototypes, brand overrides, or screenshot-based design QA.
- Typical context: User goal, audience, artifact type, existing brand or design
  system, screenshots or source files, tokens, component references, layout
  patterns, UX behavior and state requirements, anti-slop checks, responsive
  targets, `references/responsive-web-design.md` for full-site responsive work,
  accessibility expectations, rendered preview/screenshot evidence, and QA
  checklist. See [design judgment](../skills/ui-ux-expert/references/design-judgment.md)
  for consequential decisions and
  [evaluation protocol](../skills/ui-ux-expert/references/evaluation-protocol.md)
  for eight synthetic scenarios, three runnable domain fixtures, authored
  same-content demonstrations, negative evidence-integrity tests, and a matched
  human-review protocol. Core instructions are routed by task; tokens contain
  no global reset. Structural/rendered/behavior/comparative results stay separate.
  No agent A/B improvement or real user outcome is established by those tools.
  See the [2026-10-12 update report](UI_UX_EXPERT_UPDATE_2026-10-12.md).
- Redesign contracts: Read
  [product redesign contracts](../skills/ui-ux-expert/references/product-redesign-contracts.md)
  when restyling data-backed products. Preserve existing actions, navigation,
  CMS ownership/publication, deliberate empty values, asynchronous editor state,
  session boundaries, and realistic API fixtures. Shared appearance does not
  imply shared authentication or permissions.
- Visual authoring: The live canvas must display authored design while editing,
  not only in Preview. Trace model, controls, serialization, persistence, and
  all rendered consumers. Test UI-authored save/reopen, ordering/placement,
  deliberate hide/remove states, and supported typography overrides. Seeded
  fixtures alone do not prove those editing capabilities.
- Visual verification: Inspect reference density and real imagery, carry explicit
  user corrections into acceptance criteria, and verify control/peer/group
  alignment. Center stat/KPI content, dropdown selections/options, and table/grid
  headings per the user's preferences; preserve content-appropriate body-cell,
  prose, and input alignment. Measure painted controls and layered hit areas
  separately; inspect icon geometry and surrounding parent space. Requested
  before/after comparisons use real preserved captures, not reconstructed history.
  The QA checklist uses bounded font/image/data readiness, lazy-media activation,
  scoped viewport coverage, and failure triage instead of fixed sleeps or
  retry-until-green evidence.

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

### accessibility-beyond-basics

- Skill file: [../skills/accessibility-beyond-basics/SKILL.md](../skills/accessibility-beyond-basics/SKILL.md)
- Description: Extends accessibility review past basic keyboard and axe checks.
- Use when: screen-reader flow, cognitive load, low vision, zoom reflow, forced colors, complex widgets, charts/data visualization, touch, or reduced motion need advanced review.
- Typical context: Heading/landmark/label map, live region/error announcement behavior, zoom and forced-colors captures, chart alternatives, touch spacing, skipped assistive-tech checks, and residual risk.

### art-direction-imagery

- Skill file: [../skills/art-direction-imagery/SKILL.md](../skills/art-direction-imagery/SKILL.md)
- Description: Directs image and media treatment as part of UI quality.
- Use when: hero images, thumbnails, generated assets, crops, captions, focal points, placeholder behavior, lazy loading, media failure states, or text-over-image contrast matter.
- Typical context: Image job, source/provenance, aspect ratios, focal points per breakpoint, alt/caption policy, placeholder/loading/failure states, production asset checks, and screenshots.

### design-quality-review

- Skill file: [../skills/design-quality-review/SKILL.md](../skills/design-quality-review/SKILL.md)
- Description: Applies the shared design-quality guide as a reusable review protocol.
- Use when: a UI needs rule IDs, `[FACT]` / `[CRAFT]` / `[PD]` labels, S1/S2/S3 severity, capture protocol, 25-item QA, PR review notes, definition of done, or a router to the design-quality specialist suite.
- Typical context: Claude Design guide files under `references/design-quality/`, target screenshots or rendered route, desired review depth, capture conditions, defect table, product-decision list, and snapshot evidence.

### visual-diagnosis

- Skill file: [../skills/visual-diagnosis/SKILL.md](../skills/visual-diagnosis/SKILL.md)
- Description: Diagnoses why a rendered UI looks visually wrong before fixing it.
- Use when: a screen feels cheap, cramped, scattered, generic, heavy, low-trust, unfinished, or hard to critique in precise language.
- Typical context: Rendered screenshots, grayscale/blur/invert/edge checks, measured spacing/alignment/type/color defects, VD rule IDs, severity, and smallest proposed fix.

### domain-taste

- Skill file: [../skills/domain-taste/SKILL.md](../skills/domain-taste/SKILL.md)
- Description: Applies category-specific taste, density, hierarchy, and evidence conventions.
- Use when: designing or reviewing admin lists, SaaS ops consoles, dashboards, ledgers/statements, editorial pages, learning screens, landing heroes, or mobile settings-style screens.
- Typical context: Screen category, primary question, density tier, real data length, state obligations, category-specific conventions, and any `[PD]` choices that product must own.

### information-architecture-ux

- Skill file: [../skills/information-architecture-ux/SKILL.md](../skills/information-architecture-ux/SKILL.md)
- Description: Structures screen purpose, navigation, grouping, hierarchy, sequencing, and progressive disclosure.
- Use when: users cannot tell where they are, what matters, which action is primary, what comes next, or whether empty/loading/error/permission states are distinct.
- Typical context: Screen purpose written as a question, nav/landmark/heading map, grouping rationale, progressive disclosure choices, state taxonomy, and snapshot proof that the hierarchy reads.

### interaction-design

- Skill file: [../skills/interaction-design/SKILL.md](../skills/interaction-design/SKILL.md)
- Description: Designs real interaction behavior and recovery paths.
- Use when: autosave, save/cancel, undo, retry, bulk selection, optimistic updates, permissions, interruption recovery, or destructive safety must be specified or audited.
- Typical context: Action inventory, state transitions, feedback timing, partial failure behavior, permission outcomes, destructive friction rung, flow proof, and visible state evidence.

### mobile-native-feel

- Skill file: [../skills/mobile-native-feel/SKILL.md](../skills/mobile-native-feel/SKILL.md)
- Description: Makes mobile UI feel platform-native instead of desktop-compressed.
- Use when: safe areas, dvh, touch targets, thumb reach, mobile keyboard, sheets/dialogs, gestures, platform controls, or mobile settings/list conventions matter.
- Typical context: 390x844 and 360x800 captures, safe-area checks, keyboard and sticky-action behavior, platform conventions, target sizes, scroll ownership, and mobile snapshot evidence.

### design-system-architect

- Skill file: [../skills/design-system-architect/SKILL.md](../skills/design-system-architect/SKILL.md)
- Description: Architects design-system structure beyond local drift fixes.
- Use when: token layers, semantic roles, component taxonomy, variants, state matrices, gallery coverage, drift metrics, naming, and governance need definition or repair.
- Typical context: Token inventory, primitive/component map, variant matrix, gallery/test surface, drift checks, token-exception ledger, adjacent surface screenshots, and governance notes.

### typography-refinement

- Skill file: [../skills/typography-refinement/SKILL.md](../skills/typography-refinement/SKILL.md)
- Description: Refines the typographic system for UI, prose, multilingual text, and data.
- Use when: type scale, measure, line-height, heading rhythm, tabular numbers, date/unit formats, truncation, localization, or RTL behavior affects quality.
- Typical context: Type role inventory, font sizes/weights/leading, measure, number/date precision, multilingual expansion, logical properties, realistic text lengths, and snapshot/measurement evidence.

### motion-choreography

- Skill file: [../skills/motion-choreography/SKILL.md](../skills/motion-choreography/SKILL.md)
- Description: Specifies purposeful UI motion and reduced-motion alternatives.
- Use when: overlays, route transitions, loading feedback, hover/press states, drag, scroll, choreography, timing, easing, or reduced-motion behavior needs design or QA.
- Typical context: State-change map, duration/easing tiers, enter/exit relationship, performance constraints, reduced-motion behavior, interaction proof, and snapshots or short visual evidence.

### reference-implementation-critique

- Skill file: [../skills/reference-implementation-critique/SKILL.md](../skills/reference-implementation-critique/SKILL.md)
- Description: Turns reference-vs-implementation comparison into measured defect axes.
- Use when: Claude, Figma, screenshot, static mock, or live reference must be compared with implementation across geometry, rhythm, hierarchy, density, weight, affordance, states, and product decisions.
- Typical context: Matched reference and implementation captures, viewport/state/provenance, measured deltas, RC axes, derived values, accessibility overrides, product decisions, and defect table.

### taste-calibration

- Skill file: [../skills/taste-calibration/SKILL.md](../skills/taste-calibration/SKILL.md)
- Description: Uses paired specimens to calibrate design judgment over time.
- Use when: improving taste, comparing a shipped screen to works/fails examples, running a weekly 15-minute drill, or identifying the smallest change that improves a category-specific screen.
- Typical context: Fair screenshot capture, screen category, fail-trait count, visual diagnosis word, smallest change, score log, and `[PD]` items that need product confirmation.

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
- Description: Preserves or extends a design system and guides safe shared UI
  reuse/extraction, minimal API/state contracts, and actual consumer migration.
- Use when: Repeated UI, copy-forked components, duplicate fixes, consolidation,
  shared API/default changes, component/token drift, variant sprawl, or reference
  integration risk requires a reuse-versus-local decision.
- Typical context: Existing tokens, primitives, variants, layout rules,
  neighboring surfaces, chosen reuse/extend/local-exception decision, state
  coverage, screenshots, tests, and design-system debt. Read
  [shared component workflow](../skills/design-system-guardian/references/shared-components.md)
  for when not to merge, tokens/styles versus helper/hook versus UI reuse,
  props/events/state ownership, scoped migration, and representative regression
  checks. The eight review scenarios are guidance, not executed runtime tests.

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

### ios-app-development

- Skill file: [../skills/ios-app-development/SKILL.md](../skills/ios-app-development/SKILL.md)
- Description: Reusable Mac/iOS setup, build, install, launch and troubleshooting
  guidance, especially Expo/React Native, without forcing a stack migration.
- Use when: Starting an app, checking Xcode/SDK readiness, selecting Simulator
  versus iPhone, rebuilding native modules, diagnosing Metro or handling signing.
- Typical context: Repo/app roots, package and runtime pins, generated versus
  hand-maintained native ownership, current tool/device observations and build notes.
- Helper: `scripts/check-environment.py` is read-only inventory, not a readiness
  certificate. Android checks are optional; source/export/build/launch/feature
  verification are separate outcomes. No installs or builds are implied by inventory.

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

### coin-quest-new-chat

- Skill file: [../skills/coin-quest-new-chat/SKILL.md](../skills/coin-quest-new-chat/SKILL.md)
- Description: Onboards Coin Quest Ledger from current checkout docs rather
  than conversation memory or stale release claims.
- Use when: Preparing a starter prompt, finding required reading/setup, or
  picking up web, native, Firebase, ledger, Admin, QA or release work.
- Typical context: The selected Coin Quest checkout (primary `/Users/point/toolbox`),
  `Memory.md`, `PLAYBOOK.md`, `PROJECT_STRUCTURE_GUIDE.md` and the bundled
  [task map](../skills/coin-quest-new-chat/references/new-chat-context.md).
  Preserve identity, finance, cloud conflicts and player/Admin boundaries.
- Boundary: A handoff does not authorize another chat or publishing. Source,
  emulators, own-binary Simulator, exact-SHA CI and production are separate proof.

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
- Updated contracts: UID-preserving Admin SDK recovery, reset leases and session
  revocation, transactional lifecycle/publish conflicts and financial-record
  preservation during deletion. Per-board ACL/public-hash migrations remain
  separate work; backend emulator checks are not production mutations.

### coin-quest-ledger-logic

- Skill file: [../skills/coin-quest-ledger-logic/SKILL.md](../skills/coin-quest-ledger-logic/SKILL.md)
- Description: Protects Party Ledger behavior for split math, participants,
  guests, invites, Character IDs, reminders, and settlement.
- Use when: Editing payer/participant logic, Add by Character ID, Add Guest,
  Reminders invites, direct invite links, settlement calculations, or ledger
  regressions.
- Typical context: Current memory and invite docs, site map, data contracts,
  shared ledger logic, trip UI wiring, unit tests, and relevant Playwright tests.
- Updated contracts: Satang precision, unique invitation attempts, transactional
  reply/membership, no resurrection of deleted nested records, and guest
  detachment that retains financial obligations.

### coin-quest-native-parity

- Skill file: [../skills/coin-quest-native-parity/SKILL.md](../skills/coin-quest-native-parity/SKILL.md)
- Description: Keeps the Coin Quest Expo app aligned with web data contracts,
  native build gates, and real backend state.
- Use when: Working on the native app, iOS/Android builds, native screen parity,
  `playerModules`, or web/native backend contract questions.
- Typical context: Native parity docs, mobile README, iOS build notes,
  architecture docs, data contracts, site map, and relevant `mobile/src/` files.
- Evidence: Use the app's own Simulator binary for affected native flows and
  authorized Firebase/web round trips for shared writes. Expo Go, JS exports,
  browser fixtures and web/API deployment do not establish native acceptance
  or distribution. Preserve explicit local/cloud conflict choices.

## CoverMate

### covermate-design-spec

- Skill file: [../skills/covermate-design-spec/SKILL.md](../skills/covermate-design-spec/SKILL.md)
- Description: Maintains, audits, snapshots, and hands off CoverMate public/admin
  design contracts using current checkout docs and a dated bundled fallback.
- Use when: Working on compact Home, Articles publishing, Cases v2, admin
  login/launcher/edit/arrange/analytics, CMS content/media, design handoffs,
  copy voice, responsive polish, or product decisions that must not drift.
- Typical context: The active task checkout (default `/Users/point/CoverMate`),
  the recorded production domain `https://covermateinsurance.com`, current
  `docs/HANDOFF.md` and task-specific product docs, the bundled
  `references/current-design-spec.md`, and scoped `references/snapshot-suite.md`.
  Current project evidence overrides dated candidate or historical inventories;
  the bundled spec does not establish which revision is deployed.
- Updated contracts: Preserve CMS-owned section visibility/order and intentional
  empty values, bilingual FAQ editing, Articles publication rules, Cases v2 draft
  conflicts, separate draft history versus live-publish rollback, selected
  Cloudinary media handling, and source/default changes versus CMS publication.
- Portability and reconciliation: Bundled links into `/Users/point/CoverMate/docs`
  require that project checkout and are not included in this toolkit. The skill
  entrypoint retains older `#insurers`/`#motor` wording than the bundled spec;
  resolve anchor behavior from current project docs/runtime before changing it.

### covermate-new-chat

- Skill file: [../skills/covermate-new-chat/SKILL.md](../skills/covermate-new-chat/SKILL.md)
- Description: Onboards a fresh Codex chat for CoverMate using current on-disk
  docs, skills, durable product rules, proportional UAT policy, setup commands,
  source areas, and a copy-ready starter prompt.
- Use when: The user asks for a new-chat prompt, handoff prompt, context pickup
  checklist, required docs/skills/setup for CoverMate, or wants a future chat to
  know what to read before visitor, admin, CMS, Firebase, analytics, Claude
  Design, QA, snapshot, UAT/regression, push, deploy, or consistency work.
- Typical context: The active task checkout (default `/Users/point/CoverMate`),
  git status, `README.md`,
  `PROJECT_MAP.md`, `docs/ADMIN_CMS_REBUILD_DECISIONS.md`, `docs/HANDOFF.md`,
  `docs/RELEASE_RUNBOOK.md`, task-specific CoverMate docs/source areas, current
  on-disk skills, durable route/admin/CMS rules, proportional UAT triggers, and
  `references/new-chat-context.md`.
- Updated context includes compact Home and Articles, Cases v2, CMS publication
  and editor-history boundaries, Thai admin copy, Cloudinary media, customer-facing
  copy voice, and one-time legacy insurer migration that preserves later CMS
  edits. Refactor/release work records the UAT baseline and exact production
  revision; do not switch checkouts or infer deployed state from fallback notes.

## DOOTAA

### dootaa-new-chat

- Skill file: [../skills/dootaa-new-chat/SKILL.md](../skills/dootaa-new-chat/SKILL.md)
- Description: Onboards DOOTAA / VisionX app, close-eye camera, gaze benchmark,
  dataset and website work from current repo evidence rather than old chat memory.
- Use when: Preparing a new-chat prompt, locating task-specific owner docs or
  continuing DOOTAA with its product, data and device-verification constraints.
- Typical context: `/Users/point/Projects/DOOTAA`, current AGENTS/PROJECT_MAP/
  PLAYBOOK, versioned specifications, acquisition policy, consent/account isolation,
  evidence provenance and separate native/website checkpoints. No clinical
  accuracy, dataset-use approval or cross-chat permission follows from onboarding.

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

## Korat Tan Phai

### korat-tan-phai-new-chat

- Skill file: [../skills/korat-tan-phai-new-chat/SKILL.md](../skills/korat-tan-phai-new-chat/SKILL.md)
- Description: Onboards the Korat forecast dashboard and isolated iOS app with
  current docs, rev03 origin/horizon semantics, Supabase boundaries and shared CI.
- Use when: Preparing starter prompts or continuing web/mobile, map/data,
  shared-component, brand, setup or release work in `/Users/point/korattanphai`.
- Typical context: Current HANDOFF, DATA_CONTRACT, FORECAST_ONLY_RESTORATION,
  SHARED_COMPONENTS, DESIGN_SYSTEM and mobile README; parked Actual code is not
  active navigation, and a branded native shell is not connected product parity.

### korat-tan-phai-shared-components

- Skill file: [../skills/korat-tan-phai-shared-components/SKILL.md](../skills/korat-tan-phai-shared-components/SKILL.md)
- Description: Preserves shared React components and domain semantics across
  Korat province, district, and subdistrict surfaces; requires automatic snapshot
  evidence for visible work and browser checks for changed interactions.
- Use when: Auditing or changing stats, selects, provenance chips, map previews,
  dashboard sections, local maps, or shared responsive behavior.
- Typical context: `/Users/point/korattanphai`, `docs/SHARED_COMPONENTS.md`,
  owner source/CSS, current usages, data-readiness vs hazard semantics, and the
  smallest relevant route/state/breakpoint evidence.
- Version caveat: Its retained Actual/legacy-link guidance predates the forecast-only
  restoration described by `korat-tan-phai-new-chat`. Read the current project's
  restoration contract before using those temporal examples as active routing rules.

## Kaset Tan Phai

### kaset-tan-phai-new-chat

- Skill file: [../skills/kaset-tan-phai-new-chat/SKILL.md](../skills/kaset-tan-phai-new-chat/SKILL.md)
- Description: Onboards a fresh Codex chat for the Kaset Tan Phai /
  เกษตรทันภัย public flood, drought, and water-risk alert project using current
  on-disk docs, durable public-safety rules, Nakhon Ratchasima dashboard
  decisions, source maps, commands, and a copy-ready starter prompt.
- Use when: The user asks for a new-chat prompt, handoff prompt, context pickup
  checklist, required docs/skills/setup for Kaset Tan Phai, or wants a future
  chat to know what to read before UI, data, Nakhon Ratchasima
  routes/geodata/dashboard work, map behavior, alerts, notifications,
  operations, QA, push, or deploy work.
- Typical context: `/Users/point/Kaset-Tan-Phai`, production
  `https://kasettanphai.vercel.app`, `README.md`, `PROJECT_MAP.md`,
  `docs/PROJECT_PLAYBOOK.md`, `docs/HANDOFF.md`, git status, task-specific docs/source areas, Thai-first
  public-safety constraints, canonical JSON, Nakhon Ratchasima `TH-P29`
  district/subdistrict hierarchy, code-based joins, 77-province GeoJSON joins,
  map interaction contracts, localStorage key behavior, setup/verification
  commands, and `references/new-chat-context.md`.

The Kaset context also maps normalized Excel reconciliation, separate ThaiWater
forecast inputs and inherited map controls; do not confuse it with Korat's newer
forecast-only restoration contract.

## Mongkol Wela

### mongkol-new-chat

- Skill file: [../skills/mongkol-new-chat/SKILL.md](../skills/mongkol-new-chat/SKILL.md)
- Description: Onboards a fresh Codex chat for the Mongkol Wela / hora-astro
  project using current on-disk docs, durable product rules, source maps,
  commands, and a copy-ready starter prompt.
- Use when: The user asks for a new-chat prompt, handoff prompt, context pickup
  checklist, required docs/skills/setup for Mongkol Wela, or wants a future chat
  to know what to read before temple, homepage, admin/CMS, data, anti-bot, QA,
  export/prototype, commit, push, or deploy work.
- Typical context: `/Users/point/Website Projects/hora-astro`, `AGENTS.md`,
  `Architecture.md`, `Roadmap.md`, `README.md`, git status, task-specific
  Mongkol docs/source areas, durable Thai-first temple-product constraints,
  commands, and `references/new-chat-context.md`.

The Mongkol pickup map now covers authoritative live CMS, immutable place keys
and URL aliases, current bundled source owners, and Tarot research/import
boundaries. Prepared research is not completed content or supported CMS schema;
dated release evidence is not a new production check.

## Shane Thai

### shane-thai-prod-smoke

- Skill file: [../skills/shane-thai-prod-smoke/SKILL.md](../skills/shane-thai-prod-smoke/SKILL.md)
- Description: Runs or sets up safe authenticated production smoke checks for
  the Shane Thai app using the dedicated dummy learner account.
- Use when: Verifying Shane production after Vercel deploys, checking the
  production login surface, topbar, Learning hub, learner-flow smoke policy, or
  collecting screenshot evidence for `https://shanethai.vercel.app`.
- Typical context: Project root, current commit/deploy URL, production alias,
  dummy learner account policy, HTTP status/header smoke, unauthenticated title
  and login surface, authenticated `codex` learner flow, console/network
  failures, snapshot path, skipped live mutations, and failure classification.

### shane-thai-export-chatgpt

- Skill file: [../skills/shane-thai-export-chatgpt/SKILL.md](../skills/shane-thai-export-chatgpt/SKILL.md)
- Description: Exports Shane Thai learner lesson content into
  ChatGPT-ready patch packets.
- Use when: The user invokes `/shane-thai-export-ChatGPT`, asks to export all
  lessons for ChatGPT, wants lesson patch packets, or needs packet structure
  flexible enough for future learner tabs/modules such as Passage Reading.
- Typical context: Thai flashcards project root, output folder, bundled
  generator command, 17 unit packet files, folder-level protocol files, spot
  check unit, source map, and exact files the user should give ChatGPT for
  normal lesson edits, cross-unit work, or tab/module proposals.
- Content contract: Shane/course romanization is the learner-facing default;
  reference Paiboon/IPA is aligned only when the touched objects contain it.

### shane-thai-new-chat

- Skill file: [../skills/shane-thai-new-chat/SKILL.md](../skills/shane-thai-new-chat/SKILL.md)
- Description: Onboards a fresh Codex chat for Shane Thai using current
  on-disk docs, skills, durable product rules, commands, and a copy-ready starter
  prompt.
- Use when: The user asks for a new-chat prompt, handoff prompt, context pickup
  checklist, required docs/skills/setup for Shane Thai, or wants a future chat
  to know what to read before learner, admin, content, audio, image, Firebase,
  QA, deploy, or consistency work.
- Typical context: Thai flashcards repo status, `README.md`,
  `docs/project-intent.md`, `docs/memory.md`, `docs/course-status.md`,
  task-specific docs, current on-disk Shane Thai skills, durable product rules,
  commands, source areas, and `references/new-chat-context.md`.

Current Shane pickup notes include bounded account startup, background learning-
event sync, unlocked Quiz/Fill/Listen, optional Typing order/checking, and the
Romanized Thai / Thai Word Bank surfaces. Recheck project evidence during pickup.

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
  files for the Shane Thai learning app.
- Use when: Working on lesson audio, main-course Chirp generation, audio ID
  wiring, Thai TTS text, voice selection, full-phrase regeneration, stale or
  missing audio audits, or naturalness fixes.
- Typical context: Unit ID, audio ID, output path, displayed Thai text, spoken
  Thai text, English meaning, speaker role, politeness particle, voice policy,
  generation commands, audit reports, and whether the item is a word, phrase,
  sentence, dialogue line, grammar example, quiz prompt, or UI prompt.
- Romanized Thai / Word Bank batches also use packed audio and the committed
  TypeScript readiness manifest; its generated worker JSON is not hand-edited.

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
  for the Shane Thai learning app.
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
