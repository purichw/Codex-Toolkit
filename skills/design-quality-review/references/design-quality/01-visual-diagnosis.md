# 01 · Visual diagnosis vocabulary

Seven words for "it looks wrong." Each has distinct measurable signals and a distinct fix.
Using the wrong word sends the fix in the wrong direction — *cramped* and *scattered* often
appear together, but adding space fixes one and worsens the other.

## Quick differential

| Symptom | Diagnosis | Root cause | Smallest fix |
| --- | --- | --- | --- |
| Everything readable but nothing feels considered | **Cheap** | Value/hue doing the work of size and space; inconsistent primitives | Collapse to one accent, fix the radius/stroke set, re-establish contrast by value |
| Content presses against edges, text hard to scan | **Cramped** | Padding and leading below thresholds | Raise padding/leading to minimums; leave grouping alone |
| Space is plentiful but the eye wanders | **Scattered** | Too many alignment edges and type sizes; no dominant element | Reduce left edges to ≤3, cut type sizes to 4, elect one dominant element |
| Competent but interchangeable with 50 other products | **Generic** | No art direction; template symmetry; default palette | Introduce one deliberate asymmetry + one signature element + real content density |
| Tiring to look at, everything shouts | **Heavy** | Fills where strokes suffice; stacked boundary devices; over-bolding | Reduce to one boundary device per element; cap bold at ~10% of text |
| Looks fine but you wouldn't enter card details | **Low-trust** | Inconsistent data formatting, vague copy, unaccounted states | Normalize number/date formats; write specific error and empty copy |
| Right at a glance, wrong on contact | **Unfinished** | Missing states, untested content extremes | Implement the state matrix; test long/empty/zero content |

## What designers notice that developers often miss

- **Value, not hue.** Designers read a screen in grayscale first. Developers pick colors that
  differ in hue but not in lightness, so hierarchy vanishes for anyone squinting. `[FACT]`
- **Optical vs. geometric centering.** A play triangle or a chevron geometrically centered in a
  circle looks off-center. Designers nudge 1–2px; developers `justify-content: center` and move on.
- **The gap ratio, not the gap.** Whether 12px is right depends entirely on the gaps around it.
  Designers see relationships; developers see values.
- **Stroke consistency.** Icon stroke 1.5px next to a 1px border next to a 2px focus ring reads
  as three different origins. `[FACT]`
- **How many primitives are in play.** 4 radii, 6 shadows, 9 type sizes, 11 spacing values on one
  screen. Each is defensible alone; together they read as assembled rather than designed. `[FACT]`
- **Content extremes.** Designers mock the longest realistic name and the zero state because
  those are the frames that break layouts.
- **Baseline vs. box alignment.** Text and icons in a row align on cap-height/baseline, not on
  bounding-box centers. Flexbox `align-items: center` is often 1px wrong and always looks it at 12px.

## 1. Cheap

**Signals** `[FACT]`
- 3+ accent colors with no dominant one; or the accent used both as fill and as body text color.
- Pure `#000` on pure `#fff`, or a text color and background differing by >95 lightness points.
- Browser-default focus ring or link blue anywhere in a themed UI.
- Mixed radii within a single component (`8px` card, `6px` inner button, `4px` avatar).
- Shadows with zero offset and high opacity: `0 0 20px rgba(0,0,0,.35)` — light has a direction.
- Gradient fills on buttons or headings, gradient mesh backgrounds.
- Display text (>32px) left at default tracking, so it looks loose and unset.
- Icons from two families (outline Lucide beside filled Material) in one toolbar.

**Test:** grayscale the screenshot. If hierarchy collapses, hue was carrying it.

### Before / after

```css
/* ❌ Cheap: hierarchy by hue, light from nowhere, four radii */
.card   { background: #fff; border-radius: 8px; box-shadow: 0 0 20px rgba(0,0,0,.3); }
.title  { color: #2563eb; font-size: 18px; font-weight: 700; }
.body   { color: #7c3aed; font-size: 16px; }
.badge  { border-radius: 12px; background: linear-gradient(#22c55e, #16a34a); }

/* ✅ Hierarchy by value + size, one light direction, one radius, accent as stroke */
.card   { background: var(--color-surface); border: 1px solid var(--color-border-subtle);
          border-radius: var(--radius-md); box-shadow: var(--shadow-sm); }
.title  { color: var(--color-text); font-size: 20px; font-weight: 600; }
.body   { color: var(--color-text-muted); font-size: 15px; }
.badge  { border-radius: var(--radius-md); border: 1px solid var(--color-accent);
          color: var(--color-accent-700); background: transparent; }
```

**Rules**
- **VD-1** One accent role per screen. A second accent needs a semantic reason (danger, success), not variety. `[CRAFT]`
- **VD-2** One radius scale per component tree; a nested element may only be smaller, never larger, than its parent's radius, and only by one step. `[CRAFT]`
- **VD-3** Shadows have a y-offset ≥ their blur ÷ 3 and opacity ≤ 0.12 on light grounds. Never `0 0`. `[CRAFT]`

## 2. Cramped

**Signals** `[FACT]`
- Text within 12px of a container edge at 15–16px body size.
- `line-height` < 1.4 on any element that wraps to 2+ lines; < 1.5 for paragraphs.
- Measure > 90 characters or < 40 characters per line in prose.
- Interactive control shorter than 32px (desktop) / 44px (touch).
- Adjacent tap targets with < 8px between them.
- A divider with unequal space above and below it, or < 16px on either side.
- Descenders/diacritics clipping their line box.

**Test:** find the smallest gap on the screen and the gap between two unrelated groups. If they
are equal, grouping is broken — this is *cramped* causing *scattered*.

### Before / after

```css
/* ❌ Cramped: one gap value for everything, tight leading */
.row { padding: 8px; }
.row > * + * { margin-top: 8px; }
.row p { line-height: 1.3; max-width: none; }

/* ✅ Nested spacing: inside a group ≤ half the gap between groups */
.row { padding: 16px 20px; display: grid; gap: 20px; }
.group { display: grid; gap: 6px; }              /* label → value */
.row p { line-height: 1.55; max-width: 68ch; }
```

**Rules**
- **VD-4** Gap inside a group ≤ ½ the gap between groups. Enforce with nested flex/grid `gap`, never per-child margins. `[CRAFT]`
- **VD-5** Container padding ≥ body font-size, and ≥ 16px on any surface holding prose. `[CRAFT]`
- **VD-6** Prose measure 60–75ch; UI text ≤ 90ch. Set on the text element, not the container. `[CRAFT]`

## 3. Scattered

**Signals** `[FACT]`
- More than 3 distinct left edges within one content column.
- More than 4 font sizes, or more than 3 weights, on one screen.
- Section containers with different max-widths down a single page.
- Cards in a row with unequal heights caused by content, not by design.
- Labels aligned to their own controls instead of a shared grid; mixed label placement (some above, some beside).
- Every element separated by the same amount of space (no grouping signal at all).
- Centered text blocks alternating with left-aligned ones.

**Test:** threshold the screenshot and draw a vertical line at each element's left edge. Count
distinct x positions per column. >3 = scattered.

### Before / after

```html
<!-- ❌ Scattered: three alignment origins, five sizes, centered island -->
<section style="max-width:1200px">
  <h2 style="font-size:28px">Billing</h2>
  <p style="text-align:center;font-size:15px">Manage your plan</p>
  <div style="padding-left:24px"><span style="font-size:13px">Plan</span>
    <span style="font-size:17px">Team</span></div>
</section>

<!-- ✅ One column origin, one label size, grouping by gap -->
<section style="max-width:960px;display:grid;gap:28px">
  <header style="display:grid;gap:6px">
    <h2 style="font-size:28px;margin:0">Billing</h2>
    <p style="font-size:15px;margin:0;color:var(--color-text-muted)">Manage your plan</p>
  </header>
  <dl style="display:grid;gap:6px;margin:0">
    <dt style="font-size:13px;color:var(--color-text-muted)">Plan</dt>
    <dd style="font-size:15px;margin:0">Team</dd>
  </dl>
</section>
```

**Rules**
- **VD-7** ≤3 left edges per content column; ≤4 type sizes and ≤3 weights per screen. Exceptions are for one deliberate display element. `[CRAFT]`
- **VD-8** One container width per page. Full-bleed elements break out of it deliberately, not by having their own width. `[CRAFT]`
- **VD-9** Exactly one element survives the 8px blur test as dominant. If two do, demote one by size or value. `[CRAFT]`

## 4. Generic (the AI-looking screen)

The failure mode is not ugliness; it's absence of decisions. Recognizable pattern set `[FACT]`:

- A row of exactly three cards, each: icon in a rounded square, bold title, two lines of gray text.
- Everything centered, symmetric, evenly weighted; no element larger than 2× any other.
- Indigo/violet accent with slate grays; 8px radius on every corner in the build.
- Hero: large centered headline, gradient or mesh background, two buttons side by side.
- Emoji used as icons; stock 3D/isometric illustration.
- Placeholder-flavored copy: "Powerful features", "Built for teams", "Get started in seconds".
- Uniform density — every section the same height with the same padding.
- No photograph, or one unrelated stock photograph.

**Test:** cover all the copy. If the layout could belong to any product in the category, there is
no art direction. Second test: name the one element a user would remember. If you can't, none exists.

### Before / after

```
❌ Generic feature section
[icon] Fast          [icon] Secure        [icon] Scalable
Bold 18px            Bold 18px            Bold 18px
Two lines of gray.   Two lines of gray.   Two lines of gray.

✅ Directed feature section
Fast                                          ← 34px, flush left, one column of 3
  Median query 40 ms across 2.1 B rows.        ← real number, real unit
  ────────────────────────────────────────     ← hairline rule carries the structure
Secure
  SOC 2 Type II, audited quarterly. Read the report →
Scalable
  One customer runs 4,000 concurrent jobs on a single project.
```

Differences that matter: asymmetry (one column, not three equal cards), real specifics instead of
adjectives, structure from rules instead of boxes, one type size doing the heading job.

**Rules**
- **VD-10** Every screen carries one deliberate asymmetry — an off-center focal point, an uneven column split, a full-bleed element against a narrow one. `[CRAFT]`
- **VD-11** Replace adjectives with figures. If copy has no number, unit, name, or date in it, treat it as unfinished. Actual claims are `[PD]`. `[PD]`
- **VD-12** Prefer rules, borders and type scale over cards. A card is for a thing you can act on as a unit, not for grouping paragraphs. `[CRAFT]`
- **VD-13** Vary section density on purpose: a page should have at least one high-density and one low-density region. `[CRAFT]`

## 5. Heavy

**Signals** `[FACT]`
- Three boundary devices on one element (background tint **and** border **and** shadow).
- Solid accent fills larger than ~15% of the viewport.
- Bold applied to more than ~10% of visible text; body text at 600+.
- Every surface elevated — no flat baseline to elevate *from*.
- Icons filled at 20px+ where outline would read; icon size ≥ adjacent text cap-height × 2.
- Uppercase + bold + letter-spaced + colored on the same label (four emphases for one job).

**Test:** count boundary devices per element. 1 = normal, 2 = deliberate, 3 = defect. Then invert
the screenshot: heavy UIs become unreadable slabs.

### Before / after

```css
/* ❌ Heavy: three boundaries, filled accent, bold body */
.panel { background: #eef2ff; border: 1px solid #6366f1; box-shadow: 0 4px 12px rgba(0,0,0,.2); }
.panel h3 { text-transform: uppercase; letter-spacing: .08em; font-weight: 800; color: #4338ca; }
.panel p  { font-weight: 600; }

/* ✅ One boundary, accent as stroke, emphasis by one channel */
.panel { background: transparent; border: 1px solid var(--color-border); }
.panel h3 { font-weight: 600; color: var(--color-text); }        /* size does the work */
.panel p  { font-weight: 400; color: var(--color-text-muted); }
.panel::before { content: ""; display: block; height: 2px; background: var(--color-accent); width: 32px; }
```

**Rules**
- **VD-14** One boundary device per element: tint, border, or shadow. `[CRAFT]`
- **VD-15** One emphasis channel per label: size, weight, color, case, or tracking. Pick one. `[CRAFT]`
- **VD-16** Elevation is relative — keep a flat ground so raised surfaces mean something. `[CRAFT]`

## 6. Low-trust

Trust is destroyed by inconsistency in the parts users check, not by aesthetics.

**Signals** `[FACT]`
- Same quantity formatted two ways on one screen: `1,234` and `1234.00`, `$1.2k` and `$1,200.00`.
- Numbers rendered with proportional figures, so columns don't line up (see [TY-6](08-typography.md)).
- Dates in mixed formats, or relative-only ("3 days ago") with no absolute value on hover.
- Truncated money, IDs, or names with no way to see the full value.
- Generic errors: "Something went wrong", "Error 400", "Invalid input" with no field named.
- A timestamp with no "as of" or refresh affordance on data that changes.
- Rounding that doesn't sum: rows showing 33.3% × 3 with a 100.1% total.
- Empty state indistinguishable from loading or from error.
- Icon and label disagreeing (a trash icon on "Archive").
- Test/placeholder content shipped: "asdf", `user@example.com`, "Lorem".

### Before / after

```
❌  Balance   1234.5     Updated 3 days ago
    Pending   $1.2k
    [Something went wrong]

✅  Balance   1,234.50 USD    As of 12 Mar 2026, 09:14 UTC · Refresh
    Pending   1,200.00 USD
    [Card declined by your bank (code 51). Try another card or contact your bank.]
```

**Rules**
- **VD-17** One formatter per data type per product: money, date, percentage, count, ID. Format at the boundary, never ad hoc in a component. `[CRAFT]`
- **VD-18** Every error names the object and the next action. No bare status codes in user-facing copy. `[CRAFT]`
- **VD-19** Any value that can be stale shows its as-of time. Refresh cadence and whether stale data may be shown at all are `[PD]`. `[PD]`
- **VD-20** Empty, loading, error and partial states must be visually distinguishable from each other at a glance. `[CRAFT]`

## 7. Unfinished

**Signals** `[FACT]`
- A control with a hover state but no `:focus-visible`, or vice versa.
- Disabled state that is just `opacity: .5` on a filled button (unreadable) or with no reason given.
- Long content untested: no truncation, or truncation without a tooltip/title.
- Layout shift on load; content jumping when data arrives; no reserved aspect ratio for media.
- Scrollbar overlapping content or appearing/disappearing and shifting layout.
- Focus ring clipped by an ancestor `overflow: hidden`.
- Icon optically off-center in a round button; text 1px off the baseline in a row.
- The last item in a list having a bottom border that meets the container border (double line).
- Hover state on a touch-only surface (sticky hover after tap).

### Before / after

```css
/* ❌ Unfinished: one state, clipped ring, unreadable disabled */
.btn:hover { background: #eee; }
.btn:disabled { opacity: .5; }
.list { overflow: hidden; }

/* ✅ Full state matrix, ring survives, disabled stays legible */
.btn:hover { background: color-mix(in oklch, var(--color-accent) 8%, transparent); }
.btn:active { border-color: var(--color-accent-600); transform: translateY(.5px); }
.btn:focus-visible { outline: 2px solid var(--color-accent); outline-offset: 2px; }
.btn[aria-disabled="true"] { color: var(--color-text-muted); border-color: var(--color-border-subtle);
                             cursor: not-allowed; }                 /* + a title/tooltip with the reason */
.list { overflow: clip visible; }        /* or padding to keep the 2px ring inside */
.list > *:last-child { border-bottom: 0; }
```

**Rules**
- **VD-21** Every interactive element implements: rest, hover, active, focus-visible, disabled (with reason), loading if async. Missing one is S2. `[CRAFT]`
- **VD-22** Every data surface implements: empty, loading, error, partial/permission-limited, and max-content. `[CRAFT]`
- **VD-23** Reserve space for anything that arrives late (`aspect-ratio`, min-height, skeleton of the real shape). Zero layout shift after first paint. `[FACT]`
- **VD-24** Test every string at 3× its expected length and at 0 length before calling a screen done. `[CRAFT]`

## Screenshot QA

Run on a static capture at 100% zoom. Each check is pass/fail, no judgement.

1. Grayscale copy: is the reading order identical? (fails → cheap)
2. Count distinct: accent hues, radii, shadow definitions, font sizes, weights. Record the numbers. (VD-1, VD-2, VD-7)
3. Measure smallest gap and the gap between two unrelated groups. Ratio ≥ 2? (VD-4)
4. Measure container padding vs body size. Padding ≥ font-size? (VD-5)
5. Count characters in the longest prose line. 60–75? (VD-6)
6. Draw left edges. ≤3 per column? (VD-7)
7. Blur 8px: exactly one dominant element? (VD-9)
8. Count boundary devices on the busiest element. ≤2? (VD-14)
9. Estimate % of bolded text. ≤10%? (VD-15)
10. Cover the copy: is this screen identifiable as *this* product? (VD-10)
11. Scan every number: one format per type? Right-aligned where columnar? (VD-17)
12. Screenshot the hover, focus-visible, active, disabled, empty, loading, error, long-content states. All present? (VD-21, VD-22)
13. Reload with throttled network: does anything move after first paint? (VD-23)

## Adapt or override

- **Data-dense tools legitimately violate VD-4/VD-5.** A trading grid or log viewer runs 24–28px
  rows and 4–8px padding on purpose; density *is* the feature. Judge against comparable tools,
  not against a marketing page. Which density tier the product targets is `[PD]`.
- **Brutalist, editorial, and expressive directions violate VD-7 deliberately** — many alignment
  edges and type sizes can be the point. The test becomes: is the variation systematic (a
  repeated logic) or incidental? Systematic is direction; incidental is scattered.
- **VD-14 (one boundary device)** is suspended for the single highest-priority surface on a screen
  (an active row, a selected card): border + tint is a legitimate selection signal.
- **VD-10 (asymmetry)** doesn't apply to a grid of like objects — a table, a photo grid, a
  keyboard. Uniformity is correct when the objects are genuinely peer-level.
- **VD-11 (numbers over adjectives)**: claims must be true and often need legal review. If real
  figures aren't available, use fewer words rather than inventing specifics. `[PD]`
- **When the reference violates one of these rules, the reference wins** — but log it in the
  implementation note as an intentional deviation so it doesn't get "fixed" later.
