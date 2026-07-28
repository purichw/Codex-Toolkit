# Layout Exemplars

> Source of truth: `tokens.css`. Five layouts, each with desktop + mobile behavior.
> Legend: **FACT** = fixed by tokens/spec · **REC** = recommended default ·
> **REQ** = must implement · **OPT** = polish · **?** = unknown → placeholder/ask.
> Breakpoints (**FACT**): 480 / 768 / 1024 / 1280 / 1536. Mobile-first: author the
> narrow layout, enhance up. All spacing on the scale; grids use `fr`/`minmax`/`clamp`.

Shared container (**REC**): `.wrap{max-width:min(92vw,1200px);margin-inline:auto;padding-inline:var(--s5)}`.

---

## 1. App shell

**Desktop (≥1024)** — fixed left sidebar + fluid main.
```
┌────────┬───────────────────────────┐
│ sidebar│ topbar                     │
│ 260px  ├───────────────────────────┤
│        │ main (max-width, padded)   │
└────────┴───────────────────────────┘
```
- **FACT/REQ** grid: `display:grid; grid-template-columns:260px 1fr; min-height:100dvh`.
- Sidebar: `background:var(--surface); border-right:1px solid var(--border); padding:var(--s5); display:flex; flex-direction:column; gap:var(--s2)`. Nav items = ghost buttons; active item `background:var(--accent-soft); color:var(--accent)`.
- Topbar: `height:64px; border-bottom:1px solid var(--border); display:flex; align-items:center; justify-content:space-between; padding-inline:var(--s6)`.
- Main: `padding:var(--s7)`; inner content `max-width:1100px`.

**Mobile (<768)** — **REQ** sidebar collapses to an off-canvas drawer.
- Grid becomes single column; sidebar `position:fixed; inset:0 auto 0 0; transform:translateX(-100%)`, slides in on menu tap, with overlay `rgba(20,18,15,.45)`.
- Topbar gains a hamburger (left). **REQ** drawer traps focus, Esc/overlay closes. **OPT** bottom tab bar instead of drawer for ≤4 primary destinations (`height:56px`, safe-area padding).

## 2. Dashboard

**Desktop** — metric row + content grid.
- **FACT/REQ** `display:grid; grid-template-columns:repeat(12,1fr); gap:var(--s5)`.
- Stat cards span 3 cols each (4 across); charts span 6–8; tables span 12.
- Stat card (**REC**): label `var(--t-sm) var(--muted)`, number `var(--t-3xl)` bold `var(--ink)` (a "BAN"), optional delta chip. Border card, no shadow.
- **REQ** every data widget has empty/loading/error states (skeletons on load). **?** No real data → labeled placeholder, never invented numbers/charts.

**Mobile** — **REQ** columns collapse: `grid-template-columns:repeat(2,1fr)` at 480–768 for stats, single column below 480; charts full-width and horizontally scrollable if dense; tables → stacked key/value cards or an `overflow-x:auto` wrapper (**REQ** never let a table clip silently).

## 3. Form

**Desktop** — single column, centered, `max-width:560px`.
- **FACT/REQ** `display:flex; flex-direction:column; gap:var(--s4)`; groups separated by `var(--s6)` with a group heading `var(--t-lg)` bold.
- Labels above inputs; helper text below in `var(--t-xs) var(--muted)`; errors inline (§components error state).
- Actions row at bottom: primary + ghost cancel, `gap:var(--s3)`, right-aligned on desktop.
- **REQ** validate on blur, keep entered data on error, summarize errors at top for long forms, correct `type`/`inputmode`/`autocomplete` per field.

**Mobile** — same single column full-width; **REQ** action row becomes full-width stacked buttons (primary top or bottom-fixed), `min-height:44px`; avoid multi-column field rows (they cramp).

## 4. Content page

**Desktop** — single reading column.
- **FACT/REQ** body `max-width:68ch; margin-inline:auto`; section spacing `var(--s7)`; headings on the type scale; hairline dividers `1px solid var(--border)` between major sections (not cards).
- **OPT** sticky in-page TOC in a left/right margin at ≥1280 (`position:sticky; top:var(--s6)`), hidden below.
- Images/figures full column width with `var(--t-xs) var(--muted)` captions.

**Mobile** — column already fluid; `padding-inline:var(--s5)`; drop the TOC; keep measure via `max-width:68ch` (naturally full-width on phones). **REQ** tap targets in body links ≥44px line height.

## 5. Marketing hero

**Desktop** — asymmetric, left-aligned (**REC** not centered).
```
┌───────────────────────────┬───────────────┐
│ headline (t-4xl)          │  image /      │
│ subhead (t-lg, muted)     │  placeholder  │
│ [Primary] [Ghost]         │               │
└───────────────────────────┴───────────────┘
```
- **FACT/REQ** `display:grid; grid-template-columns:1.1fr .9fr; gap:var(--s8); align-items:center; padding-block:var(--s9)`.
- Headline `font-size:clamp(2.5rem,5vw,var(--t-4xl)); line-height:var(--lh-tight); text-wrap:balance; max-width:16ch`. Subhead `var(--t-lg) var(--muted); max-width:48ch`.
- One primary + one ghost button. **?** Hero image unknown → striped placeholder
  box with a mono label (`SKILL.md` "Craft Rules"); never a stock gradient.

**Mobile (<768)** — **REQ** stack to single column, text first then image; headline `clamp(2rem,8vw,2.75rem)`; buttons full-width stacked; reduce `padding-block` to `var(--s7)`.

---

## Cross-cutting requirements (all layouts)

- **REQ** test at 360 / 768 / 1280 / 1440. No horizontal scroll at any width (except intentional `overflow-x` wrappers).
- **REQ** hierarchy legible in grayscale; spacing only on the scale; one radius + one shadow philosophy throughout.
- **REQ** keyboard reachable, visible focus, logical tab order
  (`references/craft-defaults.md` accessibility floor).
- **REC** deliver each exemplar as its own `*.html` linking `tokens.css` so the QA checklist can screenshot desktop + mobile widths.
- **?/assumption boundary:** these are structural exemplars. Any brand, copy, imagery, icon set, or data is **unknown** — insert labeled placeholders; do **not** invent.
