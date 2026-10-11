# UI/UX Craft Defaults

Use this reference when `SKILL.md` needs concrete values or a quick calibration
pass. These are fallbacks, not a brand. Local brand, production UI, or user
provided visual direction wins.

Read [contextual-rules.md](contextual-rules.md) when a default does not fit. The
values below are starting points, not mandatory dimensions or a compliance
certificate. Inspect actual content, scripts, input method, and platform. For
ambiguous defects use [design-judgment.md](design-judgment.md) before selecting a
repair. Preserve applicable accessibility and product requirements.

## Table of Contents

- [Default Tokens](#default-tokens)
- [Typography](#typography)
- [Color](#color)
- [Layout And Spacing](#layout-and-spacing)
- [Imagery And Icons](#imagery-and-icons)
- [Motion](#motion)
- [Data Visualization](#data-visualization)
- [Forms And Validation](#forms-and-validation)
- [Microcopy](#microcopy)
- [Accessibility Floor](#accessibility-floor)
- [Failure Recovery](#failure-recovery)
- [Quick Cheat Sheet](#quick-cheat-sheet)

## Default Tokens

Use `tokens.css` instead of retyping the full token block. Its default system is:

- neutral light background and surfaces;
- one accent hue;
- semantic success/danger colors;
- 4/8/12/16/24/32/48/64/96 spacing scale;
- 12/14/16/20/25/31/39/49 type scale;
- restrained radius and neutral elevation.

Reuse an existing scale where possible. For a truly unbranded surface, choose
color and density roles that serve the task; accent-only restyling is an option,
not the definition of a design system. The fallback palette is not a universal
visual direction.

## Typography

- Use 1-3 fonts total. Usually: one display/heading face, one body face, optional
  mono for labels/code.
- Use a modular type scale. Avoid arbitrary sizes per component.
- Set body line height around 1.4-1.6 and large heading line height around
  1.0-1.15.
- Constrain body measure to about 60-75 characters.
- Use `text-wrap: pretty` or `balance` where supported.
- Starting comfort targets: mobile controls around 44 CSS px, slide body around
  24px at 1920x1080, print body around 12pt. Actual device, viewing distance,
  script, font metrics, and applicable accessibility requirements govern; these
  examples are not universal minimums for every medium.
- Respect brand type when available. If not, a single well-set grotesk beats a
  bad pairing.

Fallback font pairings:

| Mood | Display / Heading | Body / Text |
| --- | --- | --- |
| Editorial refined | Newsreader or Fraunces sparingly | Source Serif / system sans |
| Modern neutral | Space Grotesk | IBM Plex Sans |
| Warm humanist | Bricolage Grotesque | Hanken Grotesk |
| Technical / dense | IBM Plex Mono for labels | IBM Plex Sans |
| Confident sans | Archivo / Anton display only | Inter Tight |

## Color

- Start from brand or design-system colors.
- If absent, choose one background tone and 0-2 accents.
- Assign color by role: background, surface, text, muted text, border, accent,
  danger, success.
- Body contrast must meet WCAG AA, and text on accent must be checked.
- Links need default and hover colors from the palette; do not leave browser
  default blue by accident.
- State cannot be color-only. Pair color with text, icon, shape, or position.

## Layout And Spacing

- Use a spacing scale for all margin, padding, and `gap`.
- Prefer flex/grid with `gap` over sibling margins.
- Group with proximity before dividers.
- Use dividers before shadows; use shadows sparingly.
- Establish shared axes. Alignment beats decoration.
- Cards are for independent objects. Reading flows usually need whitespace and
  hairlines, not boxes around everything.
- Use full-bleed scale only when image/video/hero experience is the point. Use
  dense grids when repeated scanning or comparison is the point.

Common defaults:

- Prose width: `max-width: 68ch`.
- App shell width: `max-width: 1100-1280px`.
- Desktop page gutters: 24-48px depending on density.
- Section rhythm: 48-96px.
- Card padding: 24px.

## Imagery And Icons

- Use real assets whenever they matter to understanding the product.
- Missing imagery gets a labeled placeholder such as `product screenshot` or
  `venue image`, not a fake screenshot or generic gradient.
- Use one icon set and one icon weight.
- Icon-only controls need accessible names and visible affordance.
- Do not hand-draw complex SVG illustrations unless the user explicitly asks for
  illustrative SVG work or the project is a game/tool where vector construction
  is the correct medium.

## Motion

- Motion explains a change; it does not decorate.
- Micro-feedback: 100-150ms.
- UI transitions: 120-240ms.
- Enter/exit: 200-300ms.
- Avoid transitions beyond 400ms for ordinary UI.
- Animate `transform` and `opacity`, not layout properties.
- Honor `prefers-reduced-motion`.
- Springs/bounce only fit playful products, not admin or utilitarian tools.

## Data Visualization

- Bar charts compare categories.
- Line charts show trends over time.
- Area charts show cumulative trend.
- Scatter charts show correlation.
- A single headline number works when one metric matters.
- Avoid pie charts beyond 2-3 slices; avoid 3D charts.
- Start bar-chart y axes at zero.
- Use direct labels when possible; keep gridlines quiet.
- Never fabricate data. No real data means a labeled placeholder.

## Forms And Validation

- Use one column unless the existing product strongly supports another pattern.
- Put labels above fields.
- Mark optional fields, or mark required fields consistently.
- Validate on blur for ordinary fields; do not shout on every keystroke.
- Keep entered data on error.
- Errors live next to the field and say how to fix the problem.
- Long forms need an error summary.
- Submit shows progress and prevents duplicate actions.
- Use correct `type`, `inputmode`, and `autocomplete`.

## Microcopy

- Buttons use verb + object: `Save changes`, `Add member`, `Delete unit`.
- Avoid `Submit`, `OK`, `Yes`, and `Click here`.
- Empty states explain what belongs there and offer the next action.
- Errors explain what happened and the way out.
- Confirmations name the consequence and keep cancel as the safe default.
- Clear beats clever. Keep terminology consistent.

## Accessibility Floor

- Use semantic HTML: `button`, `nav`, ordered headings, labels tied to inputs,
  useful `alt` where images carry meaning.
- Everything interactive must be keyboard reachable and operable.
- Keep focus visible.
- Do not use color as the only signal.
- Distinguish text, large text and necessary non-text UI contrast; measure
  actual foreground/background pairs, including alpha-composited fills.
- Around 44px is a touch-comfort default; use the applicable size/spacing
  criteria and exceptions, not a blanket rule for inline prose links.
- Respect reduced motion.

See [accessibility-checks.md](accessibility-checks.md) for current primary
sources and exact distinctions. These few checks do not certify accessibility.

## Failure Recovery

If the render looks off, use these as hypotheses, not automatic fixes:

1. Busy: inspect competing actions, grouping, and redundant chrome before
   demoting decoration. Do not remove required content or product functions.
2. Flat: check whether the task lacks hierarchy before increasing type weight
   or spacing; a deliberately quiet surface may already be appropriate.
3. Cramped: distinguish actual collisions from poor grouping or visual weight.
   Increase gaps only if usable spacing is the cause.
4. Misaligned: inspect intended shared axes and content width; preserve deliberate
   brand offsets and alignment appropriate to the script/data.
5. Garish: inspect color roles and competing emphasis before reducing accents;
   preserve meaningful states and coherent brand choices.
6. Weak type: inspect loading/fallback, script coverage, line-height, wrapping,
   and hierarchy before replacing the project's font.
7. Make one cause-directed adjustment and compare the same state/viewport.
   If it does not help, revisit the cause instead of stacking cosmetic changes.

## Quick Cheat Sheet

Fallback reminders only; use the contextual checks above before treating any
number as a target. A matching checklist does not establish good design.

```text
FONTS 1-3  |  ACCENTS 0-2  |  BG TONES 1
SPACE 4/8/12/16/24/32/48/64/96
TYPE 12/14/16/20/25/31/39/49
MEASURE 60-75ch  |  TOUCH >=44px  |  BODY CONTRAST >=4.5:1
RADIUS one language  |  SHADOW one philosophy
MOTION 150ms feedback / 250ms transition
STATES ideal/empty/loading/error/edge for every data view
```
