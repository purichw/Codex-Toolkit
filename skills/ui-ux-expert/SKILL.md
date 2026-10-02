---
name: ui-ux-expert
description: Practical UI/UX design and QA guidance for visible user-facing screens, components, flows, decks, documents, and prototypes. Use when the user asks to design, redesign, polish, audit, implement, or visually verify an interface; when layout, hierarchy, responsiveness, accessibility, interaction states, design-system fit, or screenshot evidence matters. Do not use for purely backend, data, CLI, or non-visual code tasks.
---

# Skill: UI/UX Design Expert

Use this skill to make Codex behave like a disciplined product designer who can
also implement. Keep the work grounded in the user's goal, the existing product,
and rendered evidence. Do not treat these defaults as a brand.

## Core Workflow

1. Read the request, existing UI, screenshots, brand/design-system rules, and
   target audience before changing visuals.
2. Choose the source of truth in this order:
   - user-provided direction, screenshot, Figma, Claude artifact, or brand guide;
   - existing production UI and local design system;
   - project-specific skill or maintainer instructions;
   - this skill's fallback defaults and `tokens.css`.
3. Name the user's task, relevant constraints, and what would count as success.
   For an unclear defect, separate observed symptoms from candidate causes;
   choose a small check that can distinguish them before prescribing a fix.
4. Resolve material tradeoffs, then define the small system needed: type,
   spacing, color roles, layout, controls, states, and responsive behavior.
   Compare 2-3 lightweight alternatives only for consequential new design or
   structural choices; skip this for clear references and tiny edits.
5. Build or review the smallest useful surface first; keep edits scoped unless
   the user asked for broader redesign. Preserve product contracts and user work.
6. Render in the real medium when possible. Use browser/app/deck/PDF previews
   instead of judging from source alone.
7. Test the expected improvement and possible regressions, not just whether a
   checklist passed. Run a critic pass and close out with evidence and risk.

## Judgment And Scope

Use [design-judgment.md](references/design-judgment.md) when the cause is unclear,
principles conflict, or a consequential design choice needs alternatives. Keep
the diagnosis, chosen tradeoff, and test compact; do not require a document for
every edit. A source-of-truth order chooses visual direction, not permission to
break accessibility, data integrity, product behavior, or higher-priority rules.

Treat numerical craft defaults and category specimens as contextual starting
points, not universal pass/fail thresholds. Use
[contextual-rules.md](references/contextual-rules.md) when adapting them for the
task, script/language, input method, content, or platform. Never present a craft
preference or a screenshot inference as a measured fact or user-research result.

`$ui-ux-orchestrator` owns broad skill selection; specialists own detailed rules.
Use `$visual-diagnosis`, `$domain-taste`, `$interaction-design`, or another
relevant specialist only for the present risk, not all specialists by default.
Use `$reference-to-a-tee` for image/HTML/mixed fidelity rather than inventing
alternative art directions for a faithful-copy request.

## Reference-Led Redesigns

Match the reference's density, grouping, surface contrast, illustration style,
icon weight and complete page rhythm, not just its section order. Rebuild legacy
geometry when authorized. Derive compactness targets from the current reference
and real content; never generalize one project's palette or viewport count.
Preserve CMS/Admin ownership while changing presentation. Check optical image
size, equal collapsed peers, disclosure insets and tablet touch behavior as well
as desktop/mobile composition. Personally open and inspect captured images before
claiming fidelity; a screenshot path or green functional tests are not that review.
Use `$mockup-to-product` for flexible translation and `$reference-to-a-tee` for
explicit faithful/exact targets.

For a whole-surface fidelity request, the user's marked examples are a minimum
defect list, not the boundary of inspection. Compare the complete component
anatomy: icon and badge, heading, body/list markers, artwork, attribution, and
their spacing inside the parent. A generic colored box or a roughly related
icon does not reproduce that composition. Check actual glyph shape, optical
size, stroke/fill, and alignment, including branded share controls.

Derive typography by role at the reference's content scale: heading levels,
body, captions, and controls. Match the loaded font, weight, line height, text
measure, wrapping, and margins; do not inflate all text to make it readable in
a reduced screenshot. A requested font is project direction (for example,
Google Sans for CoverMate), not a new default for unrelated brands.

Treat a mockup as presentation evidence, not a complete feature or data schema.
Reconcile existing capabilities with the reference before replacing a screen.
Keep supported fields/actions accessible even when absent from the mockup. Do
not invent persistence, permissions, metrics, or service availability to make a
reference-only control appear functional; resolve that dependency and record
user-approved deferrals with their reintroduction condition in project docs.

## Data-Backed Redesigns

When a redesign touches CMS editing, publication, live content, or an Admin
workflow, read [product-redesign-contracts.md](references/product-redesign-contracts.md).
It covers shell reachability, shared UI versus session boundaries, field ownership,
import/editor/export parity, explicit clearing, async form stability, and evidence
that distinguishes a working UI from a richer test fixture.
For visual authoring, also apply its live-editor contract: the editable canvas
must show the authored typography, blocks, and composition while editing.
Preview checks the complete page layout; it must not be the first place the
design appears. Verify that the requested design can be created through real
editor controls and survives save/reopen, not just rendered from seeded data.
Use `$admin-ops` or `$product-ux-contracts` for deeper workflow work
only when the touched risk warrants it. A visual cleanup is not authorization to
migrate content, enable a service, or write to production.

For nontechnical operators, make the supported workflow usable without code:
use task-based labels in the audience's language, explain unfamiliar fields,
and supply realistic sample values where users must enter or map data. Keep
internal paths, schema keys and raw JSON out of the primary task. Verify a
registry, option or action has a real purpose before exposing it; scaffolding
and dead stubs are not useful navigation. When their removal is requested,
remove unsupported entry points while preserving needed backend permissions
and future role extensibility. Distinguish a dead feature from a working control
temporarily disabled by permissions, loading, or validation. Removing UI clutter
does not itself authorize deleting stored data or supported capabilities.

## Shared Component Decisions

When the task exposes repeated UI, copy-forked components, the same fix in
several places, or a change to an existing shared API/default, load
`$design-system-guardian` before extracting or changing the shared contract.
It owns the reuse/extraction workflow; use `$design-system-architect` only when
the wider token system, taxonomy, or governance needs redesign.

Look for existing components and actual consumers first. Share a component when
its semantics, behavior, and reasons to change belong together, not merely
because screenshots or CSS look similar. Choose the smallest useful shared
unit: tokens/styles, helper/hook, UI primitive, or feature/domain pattern. Keep
different workflows separate and prefer composition over page-specific flags.

Consistency includes behavior: comparable controls should preserve keyboard,
focus/dismissal, scrolling, reset, loading, and recovery conventions across public
and Admin surfaces, even when separate implementations are justified. Reuse the
existing primitives instead of copying their appearance. Shared branding or a
shared login form does not decide session, permission, or business-state ownership.

Before extraction, define props/events, state ownership, styling/layout
boundaries, and preserved behavior. Migrate the in-scope consumers to the real
shared implementation, then verify its states and affected usages with targeted
tests and automatic `$snapshot` evidence. A new component file with the old
copies still active is not a completed consolidation.

Do not turn a tiny unique edit into a component-library project. Recurrence is
evidence, not a mandatory count; correctness-sensitive logic may warrant sharing
early, while repeated but independently evolving workflows may stay separate.

## When To Ask

Ask one focused question only when the audience, tone, required brand direction,
or primary task is unknowable and a default would materially change the result.
For concrete or small UI work, proceed with a reasonable assumption.

## Reference Routing

Load extra files only when needed:

- `tokens.css`: fallback tokens only when no local brand/design system exists.
- `references/token-map.md`: token roles and hard token-use rules.
- `references/craft-defaults.md`: detailed defaults for type, color, spacing,
  forms, motion, microcopy, data visualization, accessibility, and recovery.
- `references/components.md`: reusable controls, variants, and state coverage.
- `references/layouts.md`: app shell, dashboard, form, content, and hero layout
  patterns.
- `references/responsive-web-design.md`: mobile/tablet/desktop QA, browser
  engines, safe areas, keyboard, zoom, media, and performance.
- `references/anti-slop-examples.md`: diagnose generic, AI-made, decorative, or
  visually weak output.
- `references/qa-checklist.md`: state-specific capture readiness, failed-check
  triage, and final visual QA when screenshots or DOM reads can verify the result.
- `$design-quality-review`: rigorous severity-tagged review, rule IDs, or
  definition-of-done work.
- [evaluation-protocol.md](references/evaluation-protocol.md): benchmark this
  skill or investigate repeated design failures. Includes a runnable scenario
  pack, matched before/after protocol, human review, and evidence limits. Do not
  run the benchmark suite for ordinary UI edits.
- `references/brand-override.template.md`: copy into a branded project only when
  the user provides brand assets or a brand source of truth.
- `assets/component-gallery.html`: optional local test bench; do not copy into
  user projects unless explicitly asked.

## Design Rules

- Make one primary task obvious, reversible, and trustworthy.
- Prefer project vocabulary over new decoration: density, tokens, copy tone,
  icons, radius, shadows, controls, and responsive behavior should fit.
- Pick a clear aesthetic lane only when designing from scratch: editorial,
  raw/brutalist, warm/humanist, technical/dense, or genuinely playful.
- Public and editorial surfaces may be expressive; admin, CMS, CRM, ledger,
  dashboard, and operator surfaces should be quiet, dense, and predictable.
- Use hierarchy from size, weight, position, and spacing, not color alone.
- Stat/KPI cards always center their content horizontally and vertically:
  center the icon, value, label, and supporting text as a balanced group, with
  centered text on desktop and mobile. Prefer a centered vertical stack; keep
  wrapping and equal peer sizing stable. This is the user's explicit design
  preference, not a rule for tables, forms, prose, or every card. Only depart
  from it when the user explicitly requests a different stat-card alignment.
- Dropdown/select text is centered by default, both the selected value and
  option labels, on desktop and mobile unless the user explicitly requests
  otherwise. This is the user's design preference. Reserve balanced space for
  chevrons/checkmarks so they do not shift the text off-center; preserve readable
  wrapping, keyboard behavior, and native platform limitations. Do not center
  unrelated form labels or text inputs as a side effect.
- Table/grid column headings are centered by default as the user's stated
  preference, including headings with sorting or filtering controls. Balance
  indicator space so the label remains visually centered. Keep body cells
  aligned for their content; this does not center every cell or form label.
  When the user requests this across the site, update the relevant shared
  owners and in-scope consumers, including Admin and public variants, rather
  than applying an Articles-only override or a blanket centering selector.
- Use a coherent role-based type, color, and spacing system. As fallbacks use
  1-3 fonts, 0-2 accents, and grid/flex `gap`; context and script coverage matter
  more than meeting these example counts.
- Use real assets when possible. Use labeled placeholders for unknown assets,
  data, logos, metrics, testimonials, legal, or medical copy.

### Alignment And Action Affordance

- For icon-only controls, center the glyph in both axes of the actual painted
  button and hit area, then check the button within its toolbar or surrounding
  frame. Inspect computed border-box sizes, padding, grid tracks and minimum
  sizes: a centered SVG can still sit off-center in a mismatched parent. Keep
  intrinsic SVG proportions and balanced insets; do not compensate for a broken
  layout with an arbitrary glyph translation. Verify disabled/loading variants
  and narrow viewports as relevant.
- For layered controls such as enhanced native selects, measure the painted
  field and overlaid hit area separately: their bounds must agree before
  centering labels or chevrons. A taller transparent button can look centered
  internally while its icon sinks below the visible field. Check closed/open
  indicators, text clearance, adjacent controls and mobile touch sizing; use
  the existing icon library and fix the sizing owner rather than adding offsets.
- When alignment is requested across a product, inspect the shared owners and
  representative public/Admin consumers, including open menus and dialogs.
  Fix proven shared causes at their owner rather than adding page-by-page
  offsets. Preserve intentional leading/trailing icons and left-aligned prose;
  report which surfaces were actually rendered instead of claiming exhaustive
  coverage from a source search alone.
- Size noninteractive legends and captions around their content, not inherited
  button hit-target heights. Remove excess reserved space without shrinking the
  primary visualization. Recheck wrapping, filters and alternate layers so a
  compact default does not cause clipping or unexpected layout shifts.
- Check three distinct relationships: content inside a control, peer controls
  beside one another, and the whole group inside its parent. When the user says
  "center" on a pictured action group, check the group's position in the card
  or section as well as its labels/icons. Centered text does not center a group.
  Use balanced surrounding space and a suitable group width; preserve readable
  alignment of nearby prose, labels and tables.
- Align the actual interactive boxes in a row. A select's label/helper wrapper
  is taller than the select itself; centering a neighboring upload button against
  that wrapper can visibly lift it. Use compatible control heights and align
  their edges within the existing design system. Check wrapping and responsive
  stacking; equal peer widths are appropriate when the design calls for them,
  not for every action. Do not generalize one screen's pixel dimensions.
- Make task actions such as upload, download and save visibly recognizable as
  controls, with the intended surface/border, padding, shape and focus treatment.
  A button class on an anchor does not prove it renders as a button: tag-specific
  CSS may supply only part of the appearance. Keep correct semantics, including
  real links for downloads/navigation and buttons for in-page actions; ordinary
  prose links need not become buttons. Inspect the rendered result and verify
  the relevant action still works after changing its element or styling.

## Interaction And State Rules

- Use the right control: toggle for immediate on/off, radio/segmented for one
  choice among a few, checkbox for multi-select, menu/select for many choices.
- Show current location, visible modes, clear labels, feedback, and back paths.
- Cover relevant default, hover, focus-visible, active, disabled, loading,
  empty, error, success, and edge states.
- Keep user-entered data on errors. Disable impossible actions with a reason.
- Make destructive actions confirmed, undoable, reversible, or clearly
  recoverable.
- Meet the accessibility floor: semantic controls, labels, visible focus,
  keyboard path, contrast, touch targets, no color-only meaning, and reduced
  motion support.

## Anti-Slop Rules

Avoid these unless a real brand explicitly requires them:

- aggressive rainbow gradients, gradient text, or purple/blue glassmorphism;
- emoji as primary UI/iconography;
- rounded card plus thick left accent stripe as a default pattern;
- decorative stat counters, fake percentages, or invented chart data;
- filler sections, lorem ipsum, generic claims, or fake screenshots;
- centering everything instead of using a real grid (stat/KPI card contents and
  dropdown text and table headings follow the centered alignment rules above);
- complex hand-drawn SVG illustrations where real images or labeled
  placeholders would be clearer.

## Snapshot Policy

For visible UI/UX work, use `$snapshot` before the final response without
waiting for the user to ask when a preview or rendered artifact is available.
This includes implementation, redesign, restyle, visual audit, responsive QA,
Claude/Figma/reference handoff, screenshot-based design work, new screens,
reference/parity work, formal audits, and final visual QA. Add mobile or
side-by-side evidence when viewport behavior or comparison is in scope.
For micro visual edits, keep this to the smallest useful current visual proof
instead of expanding into a full visual QA run by default.

When before/after comparison is requested, preserve the before state before
editing. For repeated fidelity corrections, inspect reference, available before,
and current after evidence at comparable viewport, content scale, and state;
include desktop/mobile only as scoped. Show enough parent context to assess
composition. If before evidence is unavailable, say so; do not reconstruct it
and present it as a captured earlier state.

If capture is genuinely blocked, state why, what was not visually verified, and
the remaining risk. Do not silently skip snapshot evidence for UI/UX work.

## Critic Pass

Before final response on UI work, check:

- the proposed fix addresses the diagnosed cause and preserves the user's task;
- primary task appears clear on a brief scan (a heuristic, not a timed user test);
- hierarchy works in grayscale;
- type, spacing, radius, shadow, and accents are consistent;
- controls match the choice model;
- action affordance and all three alignment relationships hold in the rendered
  UI; evidence includes the parent edges and surrounding space needed to judge;
- data views include relevant loading/empty/error/edge states;
- destructive behavior is safe;
- mobile has no overflow, clipping, tiny targets, or hover-only affordances when
  mobile/responsive behavior is touched or in scope;
- console/network errors are absent when a browser check is practical;
- visible content is real or clearly labeled placeholder;
- for visual-authoring changes, the live editable canvas, saved/reopened content,
  and preview/public renderer agree on the touched design and operations;
- anti-slop tells are absent or intentionally justified.

If a visible issue remains and is practical to fix now, fix and re-render before
closing. Compare the same viewport/state/content; vary only the intended design
change where possible. If evidence contradicts the diagnosis, revise it instead
of accumulating cosmetic fixes. One improvement does not establish general taste.

Treat explicit user corrections as acceptance criteria for the current scope.
Before closing a repeated correction, recheck that criterion and the affected
neighboring pattern against the latest chosen reference. A small fix needs a
current contextual render and targeted checks, not a new whole-site audit or
tests that merely assert the CSS you just wrote. Use geometry measurements when
they resolve uncertainty; they supplement personal visual inspection.

## Closeout

Report the design decision or change, source of truth used, material tradeoff,
visual evidence captured or why blocked, checks run, and remaining risk. Separate
observed improvement, reasoned expectation, and untested user outcomes. Keep the
closeout proportional and do not expose a lengthy internal reasoning transcript.
