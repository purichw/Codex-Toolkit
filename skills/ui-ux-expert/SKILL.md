---
name: ui-ux-expert
description: Canonical UI/UX Expert skill for designing, auditing, and implementing user-facing screens, layouts, components, decks, documents, and prototypes. Use when working on visual design, interaction design, accessibility, responsive UI, cross-browser/platform responsiveness, design systems, frontend polish, component galleries, layout exemplars, UX flow/state coverage, anti-slop review, brand overrides, or screenshot-based design QA.
---

# Skill: UI/UX Design Expert

Load this skill for any user-facing interface, screen, layout, component, deck,
document, or interactive prototype. Its job is not to decorate output; its job is
to make Codex act like a disciplined product designer who can implement.

This is the canonical UI/UX Expert skill. It is portable across projects, but it
is not a universal brand. `global-ui-ux-expert` is only an alias that routes
back here. If a project has an existing brand, design system, production UI, or
user-provided visual direction, that local context overrides these defaults.

## Operating Principle

Good UI is mostly subtraction, hierarchy, behavior, and verification. The user's
goal is the spec: every screen should make one primary task obvious, reversible,
and trustworthy. Establish a small system, build the smallest surface that proves
it, render the result, critique it from screenshots, and fix what still feels
off before calling it done.

## Process

1. **Read context first.** Inspect the ask, existing files, screenshots, design
   system, brand rules, production UI, and target audience before writing UI.
2. **Ask once only when needed.** Ask a focused question when the task is broad,
   has no design context, no defaults fit, or the audience/tone is unknowable.
   For small or concrete work, proceed.
3. **Choose the source of truth.** Prefer project brand/design system/production
   UI. If absent, use `tokens.css` and the references listed below.
4. **Establish the system.** Decide type, color roles, spacing scale, radius,
   layout pattern, control vocabulary, state coverage, and responsive behavior
   before laying out screens.
5. **Build one surface well.** Make the smallest screen/component/flow correct
   before duplicating patterns.
6. **Design behavior with visuals.** Cover feedback, loading, errors, disabled
   states, focus, destructive safety, persistence, and responsive compression.
7. **Render and inspect.** Use a real browser/app/deck/doc preview whenever
   possible. Do not ship from imagination.
8. **Capture `$snapshot` evidence automatically.** Before the final response,
   capture wide/current visual evidence. Add mobile or side-by-side reference /
   before / after evidence when responsive, parity, or comparison work is in
   scope. If capture is blocked, disclose why and what visual risk remains.

## Reference Routing

Read these only when the task needs them:

- `tokens.css`: default fallback design system. Copy it only when no local brand,
  design system, production UI, or user-provided visual direction exists.
- `references/token-map.md`: token roles and hard token-use rules.
- `references/craft-defaults.md`: typography, color, spacing, motion, forms,
  microcopy, data-viz, accessibility, failure recovery, and cheat-sheet defaults.
- `references/components.md`: component specs and state requirements; read before
  building reusable controls or a component gallery.
- `references/layouts.md`: app shell, dashboard, form, content page, and hero
  exemplars; read before building a new screen layout.
- `references/responsive-web-design.md`: read before full-site responsive work,
  mobile QA, platform/browser engine checks, viewport meta, safe areas, keyboard,
  responsive media, zoom, or performance work.
- `references/anti-slop-examples.md`: read when a render looks generic, AI-made,
  too decorative, or hard to diagnose.
- `references/qa-checklist.md`: read before claiming visual work is complete when
  screenshots or DOM reads can verify the result.
- `$design-quality-review`: read when the user asks for a rigorous design review,
  severity-tagged visual QA, screenshot protocol, rule IDs, or definition of
  done. It routes to specialist skills for visual diagnosis, domain taste,
  information architecture, interaction design, mobile-native feel, design-system
  architecture, art direction, typography, motion, advanced accessibility,
  reference critique, and taste calibration.
- `references/brand-override.template.md`: copy into a branded project when the
  user provides brand assets or a brand source of truth.
- `references/claude-design-learning-brief.md`: gaps this skill still has and a
  prompt outline for asking Claude Design to teach or improve those areas.
- `assets/component-gallery.html`: optional local test bench for default tokens
  and components. Do not copy it into user projects unless explicitly asked.

## Design System Precedence

Use this order:

1. User-provided visual direction, screenshot, Figma, Claude Design artifact, or
   brand guide.
2. Existing production UI and local project design system.
3. Project-specific skill or maintainer instructions.
4. `ui-ux-expert` defaults: `tokens.css` plus references.

Never invent brand facts, real data, logos, testimonials, legal/medical copy, or
metrics. Use labeled placeholders and mark unknowns instead.

## Aesthetic Direction

Pick a lane deliberately. Vague "clean and modern" usually reads as nothing.
Choose one direction, then apply it consistently:

- refined/editorial;
- brutalist/raw;
- warm/humanist;
- technical/dense;
- playful, only when the product earns it.

Public/marketing/editorial surfaces can be more expressive. Admin, CMS, CRM,
ledger, dashboard, and operator surfaces should be quiet, dense, predictable,
and optimized for repeated work.

## UX Behavior Rules

- Show choices, labels, current state, and visible modes.
- Use the correct control: toggle for instant on/off, radio/segmented for one of
  a few, checkbox for multi-select, select/menu for many.
- Provide feedback within 100ms through press, selected, loading, optimistic, or
  inline response.
- Make destructive actions confirmed, undoable, reversible, or clearly
  recoverable.
- Constrain impossible input, disable impossible actions with a reason, and keep
  user-entered data on errors.
- Orient the user with current location, clear back paths, and progressive
  disclosure for rare options.

## Anti-Slop Rules

Avoid these unless a real brand explicitly requires them:

- aggressive rainbow gradients or gradient text;
- emoji as UI/iconography;
- rounded card plus thick left-border accent stripe;
- default font reflexes without intent;
- decorative stat counters, fake percentages, or invented chart data;
- filler sections or placeholder prose in final output;
- complex hand-drawn SVG illustrations where real images or labeled
  placeholders would be better;
- purple/blue glassmorphism as a reflex;
- centering everything instead of using a real grid.

When a render looks off and you cannot name why, read
`references/anti-slop-examples.md`, use `$visual-diagnosis` when available, and
run the failure recovery section in `references/craft-defaults.md`.

## Craft Rules

Use `references/craft-defaults.md` for detailed values. Keep these core rules in
working memory:

- 1-3 fonts total; one display/personality face plus one workhorse is usually
  enough.
- 0-2 accent colors; assign colors by role, not by decoration.
- Hierarchy comes from size, weight, position, and spacing, not color alone.
- Use spacing and type scales; avoid arbitrary one-off px values.
- Prefer grid/flex with `gap` for sibling groups.
- Cards are for independent objects users can inspect or act on; reading flows
  usually need whitespace and dividers instead.
- Use real assets where possible. Missing assets get labeled placeholders, not
  invented logos, stock-gradient panels, or fake screenshots.
- Every interactive element needs default, hover, focus-visible, active, and
  disabled states; inputs/data views also need loading/error/empty/edge states.
- Accessibility floor: semantic controls, labels, visible focus, keyboard path,
  contrast, touch target size, no color-only meaning, reduced-motion support.

## Medium Notes

- **Web/app screens:** verify in browser, check console/network, responsive
  layout, state coverage, and snapshot evidence.
- **Slide decks:** design for projection; one idea per slide, large type, strong
  section rhythm, no walls of small text.
- **Documents/PDFs:** design for reading/printing; real margins, hierarchy,
  page breaks, and at least 12pt body text.
- **Fixed canvases:** confirm dimensions before designing if they are missing.
- **Interactive prototypes:** make the core interaction work and persist state
  where the user would expect continuity.
- **Mobile:** design for 44px touch targets, thumb reach, keyboard, safe areas,
  and no hover-only affordances.

## Scoping Rules

- For a small request, change only the requested surface. Do not redecorate.
- For redesign/from-scratch work, make a clear system decision and apply it
  consistently.
- When a broader improvement would help, finish the requested change first, then
  suggest the rest instead of applying it uninvited.
- When extending an existing UI, learn its vocabulary first: density, tokens,
  copy tone, interaction states, radius, shadows, icons, and responsive behavior.

## Critic Pass

Before final response, check:

- Does the primary task read within about 3 seconds?
- Does hierarchy still work in grayscale?
- Are type, spacing, radius, and shadow values consistent?
- Are there more than 2 accents or more than 3 fonts?
- Are any anti-slop tells visible?
- Does every visible element earn its place?
- Are ideal, empty, loading, error, and edge states handled for data-bearing
  views?
- Do controls match the user's choice model?
- Is destructive behavior safe?
- Are console/network errors absent?
- Does mobile avoid overflow, clipping, unreachable controls, and tiny targets?
- Is there real content or a labeled placeholder, not lorem/filler?
- When formal design QA is in scope, can defects be tagged with `[FACT]`,
  `[CRAFT]`, or `[PD]`, severity, rule ID, observed measurement, and fix?
- Does `$snapshot` evidence exist for the final visible state?

If any answer is no, fix and re-render before final response.

## Closeout

Report:

- what changed or what design decision was made;
- source of truth used: brand, production UI, reference artifact, or fallback
  defaults;
- visual evidence captured with `$snapshot`, including mobile/side-by-side when
  applicable;
- checks run and any visual risk that remains;
- focused follow-up suggestions only after the requested work is complete.
