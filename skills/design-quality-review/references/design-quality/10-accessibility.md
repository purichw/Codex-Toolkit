# 10 · Accessibility beyond basics

Assumes you already do alt text, labels, and 4.5:1 contrast. This file covers what breaks after
that: reading order, cognitive load, low-vision reflow, composite widgets, and data visualization.

Framing: accessibility defects here are **S1** — they change whether a user can complete the task.

## What designers notice that developers often miss

- **The heading outline is the site map.** Screen-reader users navigate by headings first. A page
  with one `h1` and eleven `div`s styled as headings has no structure at all.
- **Reading order is a design decision.** Visual order, DOM order, and focus order must agree. CSS
  grid/flex reordering silently breaks this.
- **Focus has to land somewhere after every change.** Route change, dialog close, row deletion, step
  advance — each needs an explicit focus target, or the user is dropped at the top of the document.
- **Announcements need restraint.** A live region that fires on every keystroke is worse than silence.
- **Low vision is mostly reflow, not contrast.** 400% zoom in a 1280px viewport ≈ a 320px viewport.
  Fixed heights, `white-space: nowrap`, and horizontal scroll are what actually break.
- **Cognitive load is an accessibility axis.** Timeouts, memory demands across steps, and vague
  errors exclude people, not just annoy them.
- **Colour-only encoding fails four ways** — CVD, grayscale printing, low-contrast screens, and
  bright sunlight.
- **Custom widgets need a documented keyboard model.** If the team can't state it, users can't discover it.

## 1. Screen reader flow

**Bad patterns** `[FACT]`
- Headings chosen by size; skipped levels; visual headings marked up as `div`/`p`.
- No landmarks (`header`/`nav`/`main`/`aside`/`footer`), so there's no way to skip to content.
- DOM order ≠ visual order because of `order`, `grid-area`, or `position`.
- SPA route change with no focus move and no announcement — the page changed silently.
- Dialog without `aria-modal`, without a focus trap, or that returns focus to `<body>` on close.
- `aria-live="assertive"` for routine updates; two live regions announcing the same thing.
- Icon-only buttons with no accessible name, or a name that's the icon's file name.
- `aria-label` overriding visible text with different wording (voice-control users say the visible text).
- Decorative SVGs exposed as `graphics-document` with no `aria-hidden`.
- Toasts that disappear before a screen reader finishes them, with no persistent record.

```html
<!-- ❌ -->
<div class="h2">Invoices</div>
<div class="row" onclick="open()">…</div>
<button><svg/></button>
<div aria-live="assertive"><!-- fires on every keystroke --></div>

<!-- ✅ -->
<main id="main">
  <h1>Invoices</h1>
  <h2>Overdue</h2>
  <a class="row" href="/invoices/1043">INV-1043 · 1,240.00 USD · 12 days overdue</a>
  <button type="button" aria-label="Filter invoices"><svg aria-hidden="true" focusable="false"/></button>
  <p aria-live="polite" aria-atomic="true">18 invoices match your filters.</p>
</main>
```

```js
// ✅ SPA route change: name the page, then move focus to the region (not to the whole document)
function onRouteChange(title) {
  document.title = `${title} · Acme`;
  liveRegion.textContent = `${title} loaded`;      // polite, once
  const h1 = document.querySelector('main h1');
  h1.setAttribute('tabindex', '-1');
  h1.focus({ preventScroll: false });
}
```

**Rules**
- **AX-1** Heading levels form a correct outline that matches the visual hierarchy; every visual heading is a real heading; no skipped levels. `[FACT]`
- **AX-2** One `main`, plus `nav`/`header`/`footer`/`aside` landmarks, plus a skip link that is visible on focus. `[FACT]`
- **AX-3** DOM order equals visual order equals focus order. Never use CSS reordering to fix a layout whose source order is wrong. `[FACT]`
- **AX-4** Every route change moves focus deliberately (to the `h1` or the main region) and announces the new page name once. `[FACT]`
- **AX-5** Dialogs: `role="dialog"` + `aria-modal="true"` + accessible name + focus trapped inside + `Esc` closes + focus returns to the trigger. `[FACT]`
- **AX-6** Live regions: `polite` by default, `assertive` only for errors that interrupt; one region per concern; `aria-atomic` where the whole message matters. `[FACT]`
- **AX-7** Accessible names include the visible label verbatim; icons are `aria-hidden="true" focusable="false"`. `[FACT]`
- **AX-8** Any transient message (toast) also exists somewhere persistent — inline near the object or in a notification list. `[CRAFT]`

## 2. Cognitive load

**Bad patterns** `[FACT]`
- Session timeout with no warning and no extension; work lost.
- A step that requires remembering a value from a previous step.
- Errors describing the system's state rather than the user's next action.
- Instructions only in a tooltip or a video.
- Nav or actions moving position between similar screens.
- Multiple simultaneous demands: a modal over a form over an unread banner.
- Required input with an undisclosed format ("enter a valid ID").

**Rules**
- **AX-9** One primary task per screen; one primary action ([IA-10](03-information-architecture.md)). `[CRAFT]`
- **AX-10** Errors state what happened, why, and the next action, in plain language, at the field or object. No codes as the only content. `[FACT]`
- **AX-11** No unavoidable timeout: warn at 2 minutes remaining, allow extension, and preserve entered data on expiry. Duration is `[PD]`. `[PD]`
- **AX-12** Never require the user to remember data across steps: carry values forward, show a running summary, allow review before submit. `[CRAFT]`
- **AX-13** Input requirements (format, range, allowed characters) are stated before the error, adjacent to the field. `[FACT]`
- **AX-14** Consistent placement and labels for the same function across screens. `[CRAFT]`

## 3. Low vision

**Bad patterns** `[FACT]`
- Fixed-height containers with `overflow: hidden`, so zoomed text is clipped.
- Two-dimensional scrolling at 400% zoom.
- `user-scalable=no` / `maximum-scale=1` in the viewport meta.
- Contrast measured on the "average" background under text over an image.
- Focus indicator that is a 1px light-gray outline, or one clipped by `overflow: hidden`.
- Text-spacing user overrides breaking layout (because heights were fixed).
- `prefers-contrast: more` ignored; disabled controls at 30% opacity, unreadable.

```css
/* ❌ */
.card { height: 140px; overflow: hidden; }
.btn:focus { outline: 1px solid #ccc; }

/* ✅ */
.card { min-height: 140px; }                            /* grows with text */
:focus-visible { outline: 2px solid var(--color-accent); outline-offset: 2px; }
/* the ring needs 3:1 against BOTH the component and the background it sits on */
@media (prefers-contrast: more) {
  :root { --color-border: var(--color-text); --color-text-muted: var(--color-text); }
}
@media (forced-colors: active) {
  .btn { border: 1px solid ButtonText; }                 /* keep shape when colors are replaced */
  .icon { forced-color-adjust: auto; }
}
```

**Rules**
- **AX-15** 200% browser zoom and 400% zoom at 1280px wide both reflow to a single column with no horizontal scroll and no clipped text. `[FACT]`
- **AX-16** No fixed heights on text containers; `min-height` only. Survives the WCAG text-spacing overrides (line-height 1.5×, letter-spacing 0.12em, word-spacing 0.16em, paragraph spacing 2×). `[FACT]`
- **AX-17** Pinch-zoom never disabled. `[FACT]`
- **AX-18** Focus indicator: ≥2px, ≥3:1 against adjacent colors, never clipped, visible on every focusable element including custom widgets and elements inside scroll containers. `[FACT]`
- **AX-19** No information by color alone: add text, shape, icon, position, or pattern. Verify in grayscale. `[FACT]`
- **AX-20** Support `prefers-contrast: more` and `forced-colors: active`; disabled states remain legible (≥3:1). `[FACT]`
- **AX-21** Text over images has verified contrast against the lightest/darkest pixel actually under the text, not the average ([AD](07-art-direction-imagery.md)). `[FACT]`

## 4. Complex widgets

Use a native element if one exists. If not, implement an established ARIA pattern exactly — and
write the keyboard model into the component's docs.

| Widget | Keyboard model (minimum) | Common failure `[FACT]` |
| --- | --- | --- |
| Combobox / autocomplete | `↓`/`↑` move active option, `Enter` select, `Esc` close-then-clear, `Home`/`End`; `aria-expanded`, `aria-activedescendant`, `aria-controls` | Focus moved into the listbox; typed text lost on close; result count never announced |
| Menu button | `Enter`/`Space`/`↓` open, arrows move, `Esc` close and return focus, typeahead | Implemented as links; no focus return; `role="menu"` on a nav |
| Tabs | `←`/`→` move (with roving tabindex), `Tab` leaves the tablist, `Home`/`End` | Every tab in the tab order; panel not `aria-labelledby` its tab |
| Data grid | Arrows move cell, `Tab` exits the grid, `Enter` edits, `Esc` cancels; sort state via `aria-sort` | Arrows scroll the page; sort announced only visually |
| Tree | `→` expand, `←` collapse/parent, arrows move, `*` expand siblings | Expand only via mouse; state not in `aria-expanded` |
| Slider | Arrows ±step, `PageUp/Down` ±large, `Home`/`End`; `aria-valuenow/min/max/valuetext` | Drag-only; `valuetext` missing so "72" is announced without its unit |
| Date picker | Arrows move day, `PageUp/Down` month, `Esc` close; text entry always available | Calendar-only, no typed date; month change not announced |
| Drag and drop | Keyboard alternative: select + move with arrows, or explicit "move to…" | Mouse-only reordering |
| Toast/snackbar with action | Reachable by keyboard before it disappears, or persists while focused | Action unreachable |

**Rules**
- **AX-22** Native element first. A custom widget requires a written justification and a documented keyboard model in its docs/gallery entry. `[CRAFT]`
- **AX-23** Composite widgets use roving `tabindex` (one tab stop) — never put every child in the tab order. `[FACT]`
- **AX-24** State lives in ARIA attributes (`aria-expanded`, `aria-selected`, `aria-checked`, `aria-sort`, `aria-current`), not only in classes. `[FACT]`
- **AX-25** Every mouse-only interaction (drag, hover-reveal, long-press) has a keyboard path that is discoverable, not just present. `[FACT]`
- **AX-26** Dynamic result counts and filter changes are announced politely and once ("18 results"). `[FACT]`
- **AX-27** `role="button"` on a non-button requires `tabindex="0"` plus `Enter` *and* `Space` handlers — or just use `<button>`. `[FACT]`

## 5. Accessible data visualization

**Bad patterns** `[FACT]`
- Series distinguished only by hue; default palettes with two indistinguishable greens.
- Legend far from the data, requiring color matching across 300px.
- SVG chart with no accessible name, or `alt="chart"`.
- No table equivalent and no data download.
- Tooltip-only values: nothing readable without a mouse.
- Red/green for negative/positive with no sign or arrow.
- Sub-3:1 contrast for thin lines and small marks.
- Axis without units; truncated y-axis unlabeled.

```html
<!-- ✅ chart with a name, a stated finding, and a table equivalent -->
<figure>
  <figcaption id="c1-cap">Monthly active users, Jan–Jun 2026</figcaption>
  <svg role="img" aria-labelledby="c1-cap c1-desc" viewBox="0 0 640 240"><!-- … --></svg>
  <p id="c1-desc" class="sr-only">
    Line chart. Users rose from 12,400 in January to 21,800 in June,
    with a dip to 11,900 in March. Growth concentrated in April and May.
  </p>
  <details>
    <summary>View data as a table</summary>
    <table><caption>Monthly active users</caption>
      <thead><tr><th scope="col">Month</th><th scope="col">Users</th></tr></thead>
      <tbody><!-- one row per point, tabular-nums --></tbody>
    </table>
  </details>
</figure>
```

**Rules**
- **AX-28** Series are distinguished by ≥2 channels: hue plus dash pattern, marker shape, direct label, or fill pattern. Verify in grayscale and with a CVD simulator. `[FACT]`
- **AX-29** Direct-label series at their last data point; a legend is a fallback, never the only key. `[CRAFT]`
- **AX-30** Every chart has an accessible name and a text description stating the finding, not the chart type. `[FACT]`
- **AX-31** Every chart offers a table equivalent (inline `details` or a linked view) with the same numbers. `[FACT]`
- **AX-32** No value is available only on hover: show values, or make data points keyboard-focusable with announced values. `[FACT]`
- **AX-33** Chart strokes, marks, and text meet contrast minimums (3:1 non-text, 4.5:1 text) against the plot background. `[FACT]`
- **AX-34** Axes carry units; a non-zero baseline is labeled as such. `[FACT]`
- **AX-35** Which palette (and whether a CVD-safe palette is mandatory) is `[PD]` — but the ≥2-channel rule applies regardless. `[PD]`

## Screenshot QA

Some checks need the a11y tree or a keyboard, which is still "static review" — no product knowledge needed.

1. Screenshot the a11y tree / heading outline. Does it read as a sensible table of contents? Any skips? (AX-1)
2. Tab through the page, screenshotting every focus stop. Is the ring visible in all of them? Any stop invisible or off-screen? Does the order match the visual order? (AX-3, AX-18)
3. Open a dialog, `Tab` past the last element, screenshot. Did focus leave the dialog? Close with `Esc` and screenshot — did focus return to the trigger? (AX-5)
4. Navigate between routes; check the live region content and where focus landed. (AX-4)
5. Zoom to 200% and to 400% at 1280px. Screenshot both. Horizontal scroll? Clipped text? (AX-15)
6. Apply the WCAG text-spacing overrides via devtools; screenshot. Any overlap or clipping? (AX-16)
7. Grayscale every screenshot. Is any status, series, or state now ambiguous? (AX-19, AX-28)
8. Run a CVD simulation (deuteranopia, protanopia) on charts and status indicators. (AX-28)
9. Screenshot with `prefers-contrast: more` and with forced colors on. Any element vanishing? (AX-20)
10. Screenshot every disabled control; measure its contrast. ≥3:1? Is the reason available? (AX-20, [IX-21](04-interaction-design.md))
11. For every custom widget: operate it with keyboard only, screenshot each state, and confirm the documented keyboard model matches. (AX-22, AX-23)
12. For every chart: is there a table equivalent, a stated finding, direct labels, and units? (AX-29..AX-34)
13. Sample the lightest pixel under text-over-image; compute contrast. (AX-21)

## Adapt or override

- **Deliberately compact expert tools** may fail AX-15 at 400% for a data grid; the accepted
  mitigation is a documented alternative view (list mode, export) rather than abandoning the grid.
  This is a `[PD]` with a legal dimension — get it decided, don't decide it in a PR.
- **AX-31 (table equivalent)** can be satisfied by a single "download data" affordance for a
  dashboard with many charts, rather than per-chart tables.
- **AX-22 (native first)** yields when the native control genuinely cannot express the requirement
  (multi-select with search, range with availability). Then follow the ARIA pattern exactly and test
  with two screen readers.
- **Games, creative canvases, and maps** can't meet all of these literally; provide an equivalent
  path to the same outcome and document what is and isn't reachable.
- **Regulatory context sets the floor, not the ceiling** — WCAG 2.2 AA is a common minimum, and
  which level applies is `[PD]`. Everything marked `[FACT]` here is worth doing regardless.
- **When the reference design fails accessibility** (low-contrast placeholder gray, color-only
  status, 1px focus ring), accessibility wins. Fix it, log the deviation, and tell the designer —
  this is the one category where you override the reference by default.
