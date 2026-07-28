# Component Gallery Spec

> Source of truth: `tokens.css` (all values below reference its custom properties).
> Every component lists all interactive states. Build to the **REQUIRED** lines;
> **OPTIONAL** lines are polish. `assets` = markup you can copy verbatim.
>
> Legend — **FACT** = defined in tokens.css / fixed by spec · **REC** = recommended
> default, may adapt · **REQ** = must implement · **OPT** = polish · **?** = unknown,
> ask or leave a labeled placeholder.

State coverage required for every interactive component: **default · hover · focus-visible · active · disabled**, plus **error** and **loading** where the component accepts input or fetches.

Global focus rule (**FACT**, from tokens.css): `:focus-visible { outline:2px solid var(--accent); outline-offset:2px }`. Never remove it; components below only override when a tighter ring is needed.

---

## 1. Button

**FACT** shared box: `padding:var(--s3) var(--s5); border-radius:var(--radius); font:600 var(--t-base)/1 inherit; min-height:40px; display:inline-flex; align-items:center; gap:var(--s2); cursor:pointer; transition:background var(--dur-fast) var(--ease-out), border-color var(--dur-fast) var(--ease-out)`.

| Variant | default | hover | active | disabled |
|---|---|---|---|---|
| Primary | `background:var(--accent); color:var(--accent-ink); border:0` | `background:color-mix(in oklch, var(--accent) 88%, black)` | `background:color-mix(in oklch, var(--accent) 78%, black)` | `opacity:.5; cursor:not-allowed` |
| Secondary | `background:transparent; color:var(--ink); border:1px solid var(--border)` | `border-color:var(--ink); background:color-mix(in oklch, var(--ink) 4%, transparent)` | `background:color-mix(in oklch, var(--ink) 8%, transparent)` | `opacity:.5; cursor:not-allowed` |
| Ghost | `background:transparent; color:var(--muted); border:0` | `color:var(--ink); background:color-mix(in oklch, var(--ink) 5%, transparent)` | `background:color-mix(in oklch, var(--ink) 9%, transparent)` | `opacity:.5; cursor:not-allowed` |

- **REQ** exactly one primary per view. Touch target ≥44px → set `min-height:44px` on touch layouts.
- **loading** (**REQ** when the click triggers async): swap label for a spinner, keep width, set `aria-busy="true"`, disable pointer. Do not collapse the button.
- **OPT** `:active { transform:translateY(1px) }` for tactile feedback.

```html
<button class="btn btn--primary">Save changes</button>
<button class="btn btn--secondary">Cancel</button>
<button class="btn btn--primary" aria-busy="true" disabled><span class="spinner"></span>Saving…</button>
```
```css
.btn{padding:var(--s3) var(--s5);border-radius:var(--radius);font:600 var(--t-base)/1 inherit;min-height:40px;display:inline-flex;align-items:center;gap:var(--s2);cursor:pointer;border:0;transition:background var(--dur-fast) var(--ease-out),border-color var(--dur-fast) var(--ease-out)}
.btn--primary{background:var(--accent);color:var(--accent-ink)}
.btn--primary:hover{background:color-mix(in oklch,var(--accent) 88%,black)}
.btn--primary:active{background:color-mix(in oklch,var(--accent) 78%,black)}
.btn--secondary{background:transparent;color:var(--ink);border:1px solid var(--border)}
.btn--secondary:hover{border-color:var(--ink);background:color-mix(in oklch,var(--ink) 4%,transparent)}
.btn--ghost{background:transparent;color:var(--muted)}
.btn--ghost:hover{color:var(--ink);background:color-mix(in oklch,var(--ink) 5%,transparent)}
.btn:disabled{opacity:.5;cursor:not-allowed}
```

## 2. Text input

**FACT** box: `padding:var(--s3) var(--s4); border:1px solid var(--border); border-radius:var(--radius); background:var(--surface); color:var(--ink); font-size:var(--t-base); width:100%`.

| State | style |
|---|---|
| default | box above; label above in `var(--t-sm)` `var(--muted)` |
| hover | `border-color:var(--faint)` |
| focus | `border-color:var(--accent); outline:2px solid var(--accent-soft); outline-offset:0` |
| disabled | `background:color-mix(in oklch,var(--ink) 3%,var(--surface)); color:var(--faint); cursor:not-allowed` |
| error | `border-color:var(--danger)` + message below in `var(--t-xs)` `var(--danger)`; set `aria-invalid="true"` (**REQ**) |
| loading/readonly | `readonly` + `var(--faint)` text; **REQ** don't fake as disabled if value is real |

- **REQ** placeholder is a hint (`var(--faint)`), never a label replacement. **REQ** associate `<label for>`.
- **OPT** leading/trailing icon inside the box with `var(--s2)` gap.

```html
<label class="field">
  <span class="field__label">Email</span>
  <input class="input" type="email" inputmode="email" autocomplete="email" placeholder="you@example.com">
  <span class="field__error" hidden>Enter a valid email address</span>
</label>
```

## 3. Select / dropdown menu

**FACT** trigger = input box + trailing chevron. Menu: `background:var(--surface); border:1px solid var(--border); border-radius:var(--radius); box-shadow:var(--shadow-md); padding:var(--s1); max-height:320px; overflow:auto`.

| Item state | style |
|---|---|
| default | `padding:var(--s2) var(--s3); border-radius:calc(var(--radius) - 4px); color:var(--ink)` |
| hover/highlighted | `background:color-mix(in oklch,var(--ink) 5%,transparent)` |
| selected | `color:var(--accent); font-weight:600` (+ **OPT** check icon) |
| disabled item | `color:var(--faint); cursor:not-allowed` |

- **REQ** keyboard: ↑/↓ move highlight, Enter selects, Esc closes, focus returns to trigger.
- **?** async option loading → show a skeleton row set; do not show an empty menu.

## 4. Checkbox & radio

**FACT** control 18px (20px touch), `border:1.5px solid var(--faint)`, `border-radius:4px` (checkbox) / `50%` (radio); `gap:var(--s3)` to label; entire label clickable.

| State | style |
|---|---|
| checked | `background:var(--accent); border-color:var(--accent)` + `var(--accent-ink)` glyph |
| hover | `border-color:var(--accent)` |
| focus | global ring on the control |
| disabled | `opacity:.5; cursor:not-allowed` |
| error (group) | group label + helper in `var(--danger)` |

- **REQ** radio for mutually exclusive choices, checkbox for independent ones. Toggle (below) is not a form-choice control.

## 5. Toggle / switch

**FACT** track 44×24, knob 20px, `2px` inset. off → `background:var(--border)`; on → `background:var(--accent)`; knob `background:var(--surface)`, `transition:transform var(--dur-fast) var(--ease-out)`.

- States: hover `+2%` track darkening; focus global ring on track; disabled `opacity:.5`.
- **REQ** use only for instant on/off state, not deferred form submission.

## 6. Card

**FACT** `background:var(--surface); border:1px solid var(--border); border-radius:var(--radius); padding:var(--s5)`.

| State | style |
|---|---|
| default | box above; **OPT** `box-shadow:var(--shadow-sm)` |
| hover (interactive only) | `border-color:var(--accent); box-shadow:var(--shadow-md); transition:var(--dur) var(--ease-out)` |
| focus (if link/button card) | global ring on the card |
| loading | skeleton (see "Progress & skeleton" below) inside the same box |

- **REQ** border **or** heavy shadow, not both. Cards only for independent,
  actionable objects (`SKILL.md` "Craft Rules"). Reading flows use dividers, not
  cards.

## 7. Modal / dialog

**FACT** overlay `background:rgba(20,18,15,.45)`; panel `background:var(--surface); border-radius:var(--radius-lg); box-shadow:var(--shadow-md); padding:var(--s6); max-width:min(92vw,520px)`.

- **REQ** trap focus; Esc closes; overlay click closes (non-destructive only); scroll-lock body; return focus to trigger on close; `role="dialog" aria-modal="true"` + labelled title.
- Layout: title `var(--t-xl)` bold; close button top-right (ghost); actions bottom-right, primary rightmost.
- **OPT** enter: overlay fade `var(--dur)`, panel `translateY(8px)→0` + fade.

## 8. Tabs

**FACT** row of labels, `gap:var(--s5)`; active `color:var(--ink)` + `2px solid var(--accent)` underline; inactive `color:var(--muted)`.

| State | style |
|---|---|
| hover | inactive → `color:var(--ink)` |
| focus | global ring on the tab |
| active | underline + bold; `aria-selected="true"` |
| disabled | `opacity:.5` |

- **REQ** roving tabindex, ←/→ move, `role="tab"/"tablist"/"tabpanel"`. **OPT** animate underline position.

## 9. Table

**FACT** header `var(--t-sm)` `var(--muted)`; cell `padding:var(--s3)`; rows separated by `1px solid var(--border)`; numbers right-aligned, `font-variant-numeric:tabular-nums`.

- States: row hover `background:color-mix(in oklch,var(--ink) 3%,transparent)`; sortable header hover shows arrow; selected row `background:var(--accent-soft)`.
- **REQ** no vertical rules; zebra only for very dense tables. Sticky header
  (`position:sticky;top:0`) for long tables. **REQ** empty state row using
  `references/craft-defaults.md` microcopy rules when no data — never a blank
  table.

## 10. Badge / chip

**FACT** `font-size:var(--t-xs); padding:2px 10px; border-radius:var(--radius-pill); background:var(--accent-soft); color:var(--accent)`. Radius pill is allowed **only here** and toggles.
- Status: success/danger variants swap the two colors to `--success`/`--danger` at the same soft tint. Removable chip: trailing × button (ghost, focusable).

## 11. Toast / notification

**FACT** `background:var(--surface); border:1px solid var(--border); border-radius:var(--radius); box-shadow:var(--shadow-md); padding:var(--s3) var(--s4)`; container top/bottom-right; max 3 stacked; auto-dismiss ~4s.
- **REQ** `role="status"` (info) / `role="alert"` (error); pause dismiss on hover/focus; dismiss button.
- Type signalled by a 3px left accent bar or small colored icon — **REQ** not a full colored background.

## 12. Progress & skeleton

- **Skeleton** (**REQ** for content loads): shapes filled `background:var(--border)` with a shimmer `@keyframes` between `--border`↔`--bg`, `border-radius:var(--radius)`. Match the real content's box sizes.
- **Determinate bar** (known progress): track `var(--border)`, fill `var(--accent)`, `role="progressbar"` with aria values.
- **Spinner** (short indeterminate only): 2px ring, `var(--border)` track + `var(--accent)` head, `@keyframes spin`.
- **REQ** honor `prefers-reduced-motion` → freeze shimmer/spin to a static state.

---

## Gallery page (build this to verify all states at once)

**REQ** produce `component-gallery.html` linking `tokens.css`, rendering every component above in a grid, each showing its states side by side (default / hover-simulated / focus / disabled / error / loading) with a label under each. This is the artifact the QA checklist screenshots.

**?** Unknowns to leave as labeled placeholders, not inventions: real icon set, brand fonts, product copy, and any data shown in the table/cards.
