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
- `references/qa-checklist.md`: final visual QA when screenshots or DOM reads
  can verify the result.
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
- Use a coherent role-based type, color, and spacing system. As fallbacks use
  1-3 fonts, 0-2 accents, and grid/flex `gap`; context and script coverage matter
  more than meeting these example counts.
- Use real assets when possible. Use labeled placeholders for unknown assets,
  data, logos, metrics, testimonials, legal, or medical copy.

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
- centering everything instead of using a real grid;
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

If capture is genuinely blocked, state why, what was not visually verified, and
the remaining risk. Do not silently skip snapshot evidence for UI/UX work.

## Critic Pass

Before final response on UI work, check:

- the proposed fix addresses the diagnosed cause and preserves the user's task;
- primary task appears clear on a brief scan (a heuristic, not a timed user test);
- hierarchy works in grayscale;
- type, spacing, radius, shadow, and accents are consistent;
- controls match the choice model;
- data views include relevant loading/empty/error/edge states;
- destructive behavior is safe;
- mobile has no overflow, clipping, tiny targets, or hover-only affordances when
  mobile/responsive behavior is touched or in scope;
- console/network errors are absent when a browser check is practical;
- visible content is real or clearly labeled placeholder;
- anti-slop tells are absent or intentionally justified.

If a visible issue remains and is practical to fix now, fix and re-render before
closing. Compare the same viewport/state/content; vary only the intended design
change where possible. If evidence contradicts the diagnosis, revise it instead
of accumulating cosmetic fixes. One improvement does not establish general taste.

## Closeout

Report the design decision or change, source of truth used, material tradeoff,
visual evidence captured or why blocked, checks run, and remaining risk. Separate
observed improvement, reasoned expectation, and untested user outcomes. Keep the
closeout proportional and do not expose a lengthy internal reasoning transcript.
