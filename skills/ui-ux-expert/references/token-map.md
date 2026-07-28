# Token Usage Map

> For every custom property in `tokens.css`: what it's for, where to use it, and
> where NOT to. Source of truth: `tokens.css`. Legend: **FACT** = the token's
> defined role · **REQ** = must follow · **REC** = default, may adapt · **DON'T** =
> anti-pattern. Rule of thumb: **use tokens by ROLE, never by appearance.** If you'd
> pick a token because "it looks right," you're using it wrong — pick by meaning.

---

## Neutrals

### `--bg` (app background)
- **USE:** the page/app canvas behind everything; large empty areas.
- **DON'T:** card surfaces (use `--surface`); text; borders.

### `--surface` (raised surfaces)
- **USE:** cards, panels, modals, menus, table headers, toasts, inputs — anything sitting *above* `--bg`.
- **DON'T:** the page background; text color.
- **FACT:** `--surface` on `--bg` is the primary depth cue; keep them distinct.

### `--ink` (primary text)
- **USE:** headings, body, primary numbers, high-emphasis labels.
- **DON'T:** as a fill for large areas (too heavy); as pure black — it's intentionally off-black.
- **REC:** overlays use `rgba(20,18,15,.45)` (the ink color at low alpha), not `--ink` solid.

### `--muted` (secondary text)
- **USE:** subheads, captions, metadata, helper text, inactive nav/tab labels, table headers.
- **DON'T:** primary body copy (fails emphasis); small text on colored fills (recheck contrast).

### `--faint` (tertiary)
- **USE:** placeholders, disabled text, timestamps, watermark/placeholder mono labels.
- **DON'T:** any text that must be reliably read (often below AA on `--bg`) — **REQ** don't use for essential content.

### `--border` (hairlines & dividers)
- **USE:** 1px borders, dividers, table row rules, skeleton fills, unfilled toggle/progress tracks.
- **DON'T:** text; large fills; as a shadow substitute where elevation is meant.

---

## Accent

### `--accent` (single brand/action hue)
- **USE:** the one primary button, active/selected state, focus ring, links, primary chart series, tab underline, progress fill.
- **DON'T:** large background areas; body text (contrast/overuse); more than one hue — **REQ** keep to a single accent. Multiple accents = slop.
- **RETHEME:** change only this hue to reskin (`tokens.css` and
  `references/craft-defaults.md`).

### `--accent-ink` (text/icons on accent)
- **USE:** label on a filled `--accent` button/badge/bar.
- **DON'T:** on `--surface`/`--bg` (it's near-white); **REQ** verify ≥4.5:1 on the actual accent.

### `--accent-soft` (tinted accent wash)
- **USE:** selected-row background, active nav item background, badge/chip fills, subtle highlight.
- **DON'T:** as a border or text color; stacked with a solid accent fill on the same element.

---

## Feedback

### `--success` / `--danger`
- **USE:** semantic status only — success/error messages, destructive actions, validation, status chips (as a soft tint + text label).
- **DON'T:** decoration, general accents, or the only signal of meaning — **REQ** always pair with text/icon (color-blind safety).
- **?** `--warning` is not defined; if needed, add it to a brand override, don't improvise inline.

---

## Spacing scale — `--s1 … --s9` (4→96px)

- **USE:** every margin, padding, and `gap`. Pick the nearest step.
- **REC mapping:** `--s1/--s2` icon gaps & tight pairs · `--s3/--s4` control padding & field gaps · `--s5` card padding & grid gaps · `--s6` group separation · `--s7` section spacing · `--s8/--s9` hero/section rhythm.
- **DON'T:** ad-hoc px values; **REQ** if nothing fits, the design is off — don't invent `--s4.5`.

## Type scale — `--t-xs … --t-4xl` (12→49px, ×1.25)

- **USE:** every `font-size`. `--t-xs` captions/badges · `--t-sm` labels/meta · `--t-base` body · `--t-lg` sub-headings/lead · `--t-xl` card/section titles · `--t-2xl` page titles · `--t-3xl` dashboard BANs · `--t-4xl` hero.
- **DON'T:** orphan sizes; **REQ** slides ≥`--t-lg` region, print body ≥12pt regardless.

## Line heights — `--lh-tight / --lh-snug / --lh-body`

- **USE:** `--lh-tight` (1.1) large headings · `--lh-snug` (1.3) sub-heads/short blocks · `--lh-body` (1.55) paragraphs.
- **DON'T:** body text at `--lh-tight` (cramped); huge headings at `--lh-body` (loose).

## Radius — `--radius / --radius-lg / --radius-pill`

- **USE:** `--radius` default (buttons, inputs, cards) · `--radius-lg` modals/large panels · `--radius-pill` **only** chips/badges/toggles.
- **DON'T:** mix pill and sharp arbitrarily — **REQ** one radius language; pill is the documented exception.

## Elevation — `--shadow-sm / --shadow-md`

- **USE:** `--shadow-sm` resting cards (optional) · `--shadow-md` overlays (modals, menus, toasts, hover-lifted cards).
- **DON'T:** border + heavy shadow on the same element; colored shadows; shadows on flat/inline elements. **REQ** pick border **or** shadow per surface.

## Motion — `--ease-out / --dur-fast / --dur`

- **USE:** `--dur-fast` (150ms) hover/press feedback · `--dur` (250ms) enter/exit, expand, reorder · `--ease-out` for entrances/most UI.
- **DON'T:** animate `width/height/top/left` (use `transform`); exceed `--dur` for routine UI; ignore `prefers-reduced-motion` (**REQ** honor it).

---

## Quick lookup (role → token)

| Need | Token |
|---|---|
| Page background | `--bg` |
| Card / panel / menu | `--surface` |
| Heading & body text | `--ink` |
| Secondary / caption | `--muted` |
| Placeholder / disabled text | `--faint` |
| Divider / 1px border / track | `--border` |
| Primary action / selected / link / focus | `--accent` |
| Text on accent fill | `--accent-ink` |
| Selected-row / chip / active-nav wash | `--accent-soft` |
| Success / error status | `--success` / `--danger` |
| Any gap/padding/margin | `--s1…--s9` |
| Any font-size | `--t-xs…--t-4xl` |
| Corner radius | `--radius` (pill only on chips/toggles) |
| Elevation | `--shadow-sm` rest / `--shadow-md` overlay |
| Transition | `--dur-fast` feedback / `--dur` transition |

## Hard rules (REQ)

- Use tokens by **role**, not by how they look.
- Never hard-code a hex/px that a token already covers.
- Never introduce a color outside these tokens (add to a brand override instead).
- If no token fits, the design likely needs rethinking — don't invent one inline.
