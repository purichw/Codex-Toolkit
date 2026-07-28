# UI/UX Craft Defaults

Use this reference when `SKILL.md` needs concrete values or a quick calibration
pass. These are fallbacks, not a brand. Local brand, production UI, or user
provided visual direction wins.

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

- warm neutral background and surfaces;
- one accent hue;
- semantic success/danger colors;
- 4/8/12/16/24/32/48/64/96 spacing scale;
- 12/14/16/20/25/31/39/49 type scale;
- restrained radius and neutral elevation.

To restyle without a brand, change only the accent hue and, if necessary, shift
neutral warmth/coolness while keeping chroma very low. Do not invent a new scale
for every project.

## Typography

- Use 1-3 fonts total. Usually: one display/heading face, one body face, optional
  mono for labels/code.
- Use a modular type scale. Avoid arbitrary sizes per component.
- Set body line height around 1.4-1.6 and large heading line height around
  1.0-1.15.
- Constrain body measure to about 60-75 characters.
- Use `text-wrap: pretty` or `balance` where supported.
- Minimums: mobile touch targets 44px; slide text never below 24px at
  1920x1080; print body at least 12pt.
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
- Body text contrast at least 4.5:1; large text/UI at least 3:1.
- Touch targets at least 44px on mobile.
- Respect reduced motion.

## Failure Recovery

If the render looks off:

1. Too busy: remove the three least-necessary elements.
2. Flat: increase size/weight contrast and add whitespace before the primary
   element.
3. Cramped: increase gaps one step on the scale.
4. Misaligned: put related edges on shared axes.
5. Garish: reduce to one accent, desaturate neutrals, remove gradients/shadows.
6. Cheap type: choose a clearer pairing and fix line-height/measure.
7. Still off: compare against `anti-slop-examples.md` and name the specific
   visible problem before editing again.

## Quick Cheat Sheet

```text
FONTS 1-3  |  ACCENTS 0-2  |  BG TONES 1
SPACE 4/8/12/16/24/32/48/64/96
TYPE 12/14/16/20/25/31/39/49
MEASURE 60-75ch  |  TOUCH >=44px  |  BODY CONTRAST >=4.5:1
RADIUS one language  |  SHADOW one philosophy
MOTION 150ms feedback / 250ms transition
STATES ideal/empty/loading/error/edge for every data view
```
