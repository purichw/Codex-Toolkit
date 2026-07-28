# 08 · Typography refinement

Type is where most of the perceived quality of a UI lives and where the defects are the most
measurable. Every rule here is checkable in a screenshot with a ruler.

## What designers notice that developers often miss

- **Figures have two styles.** Proportional figures make columns ragged; tabular figures make prose
  loose. Developers use whatever the font defaults to, everywhere.
- **Line-height belongs to the block, not the font.** 1.5 is right for a paragraph, wrong for a
  32px heading (1.1–1.2) and wrong for a 12px table cell (1.35).
- **Optical alignment.** A quote mark, a bullet, or an italic capital needs to hang slightly outside
  the measure to look aligned. Box alignment looks indented.
- **Cap-height, not bounding box.** Icons align to cap-height; `align-items: center` puts them
  ~1px low because the box includes descender space.
- **Weight is not the only emphasis.** Size, tone, tracking, italics, and small caps all exist.
  Bold-everything is the sign nobody chose.
- **Non-Latin scripts need more line box.** Devanagari and Thai clip at 1.4; CJK needs no italics
  and no letter-spacing; Arabic needs mirrored layout and a different fallback stack.
- **Widows and orphans.** A heading whose last word drops alone to line 2 is a defect designers
  always catch and developers rarely see, because it depends on the container width.
- **The scale is finite.** Four to six sizes per product. A 17px "because it fit" is drift.

## Bad patterns

| Pattern | Tell `[FACT]` | Fix |
| --- | --- | --- |
| Proportional figures in tables | Digits don't line up between rows; column edge is ragged | `font-variant-numeric: tabular-nums` |
| Tabular figures in prose | Word spaces and punctuation look loose | Keep `normal` in running text |
| One line-height everywhere | Headings look airy, table cells look cramped | Per-role leading (table below) |
| Fixed `px` line-height | Breaks at 200% zoom / user text scaling | Unitless multipliers |
| Uppercase for long labels | 4-word uppercase labels are slow to read | Sentence case; uppercase only ≤2 words with tracking |
| Faux bold / faux italic | Synthesized weights on a single-weight webfont | Load real weights or use a family that has them |
| `letter-spacing` on body | 15px text at `0.02em` reads mushy | Tracking only on display (negative) and small caps (positive) |
| Centered multi-line paragraphs | Ragged both edges, no entry point | Left-align anything over 2 lines |
| Justified with no hyphenation | Rivers of white space in narrow columns | `hyphens: auto` when justifying, or don't justify below 45ch |
| Placeholder as label | Label vanishes on focus; fails a11y | Persistent label above ([MB-19](05-mobile-native-feel.md)) |
| Truncation without recovery | `text-overflow: ellipsis` and no title/tooltip | Tooltip, or wrap to 2 lines with `-webkit-line-clamp` + full value available |
| Heading level chosen for size | `h4` used because it looked right | Semantic level + a size class ([IA-12](03-information-architecture.md)) |

## Line-height reference `[CRAFT]`

| Role | Size | Line-height | Notes |
| --- | --- | --- | --- |
| Display | 40–80px | 1.0–1.1 | Negative tracking −0.01 to −0.02em |
| Heading | 24–36px | 1.15–1.25 | `text-wrap: balance` |
| Subhead | 18–22px | 1.3–1.4 | |
| Body / prose | 16–20px | 1.5–1.65 | `text-wrap: pretty`, 60–75ch |
| UI text | 14–16px | 1.4–1.5 | ≤90ch |
| Table cell | 13–14px | 1.35–1.4 | tabular figures |
| Caption / meta | 12–13px | 1.4 | muted tone, not lighter weight |
| Non-Latin (Devanagari, Thai, Khmer) | any | +0.15–0.2 over the above | prevents diacritic clipping |

## 1. Multilingual text

**Bad patterns** `[FACT]`
- Fixed-width buttons sized to English; German/Finnish labels clip or wrap mid-word.
- `text-transform: uppercase` applied to Turkish (i → I loses the dot; needs `İ`) or to Greek (accents drop).
- Italics applied to CJK (no italic forms; synthesized slant is wrong) or to Arabic.
- `letter-spacing` on CJK/Arabic (breaks connected forms and rhythm).
- `margin-left`/`padding-right` instead of logical properties, so RTL mirrors incorrectly.
- One font stack for all scripts, so CJK falls back to a system font with different metrics and the line height jumps.
- Line-breaking assumptions: CJK breaks anywhere, Thai has no spaces, both need `line-break`/`word-break` care.
- Truncating at N characters rather than by rendered width — meaningless for CJK, breaks grapheme clusters.

```css
/* ❌ */
.btn { width: 120px; text-transform: uppercase; letter-spacing: .06em; }
.card { margin-left: 16px; padding-right: 24px; text-align: left; }
.body { line-height: 1.4; }

/* ✅ */
.btn { min-width: 120px; padding-inline: 16px; }          /* grows +40% for de/fi */
.card { margin-inline-start: 16px; padding-inline-end: 24px; text-align: start; }
.body { line-height: 1.55; }
:lang(hi), :lang(th), :lang(km) { line-height: 1.75; }
:lang(ja), :lang(zh), :lang(ko) { letter-spacing: normal; font-style: normal;
                                  word-break: normal; line-break: strict; }
:lang(ar), :lang(he) { letter-spacing: normal; }
html[dir="rtl"] .chevron { transform: scaleX(-1); }        /* mirror direction glyphs, not logos */
```

**Rules**
- **TY-1** Every fixed dimension around text becomes a minimum. Assume +40% length for German/Finnish, +30% for Russian, −40% for CJK. `[FACT]`
- **TY-2** Logical properties everywhere (`margin-inline`, `padding-block`, `inset-inline`, `text-align: start`); test the whole UI in RTL. `[FACT]`
- **TY-3** Per-script font stacks and per-script line-height overrides; no `letter-spacing`, `font-style: italic`, or `text-transform: uppercase` on CJK/Arabic/Hebrew. `[FACT]`
- **TY-4** Truncate by rendered width (CSS), never by character count; never split a grapheme cluster or an emoji sequence. `[FACT]`
- **TY-5** Direction-bearing icons mirror in RTL; brand marks, media controls, and clock faces do not. `[CRAFT]`

## 2. Dense data (tables, logs, grids)

**Rules**
- **TY-6** `font-variant-numeric: tabular-nums` on every numeric cell, metric, timestamp, and duration. Never in running prose. `[FACT]`
- **TY-7** Numbers right-aligned (decimal-aligned if precision varies), text left-aligned, dates left-aligned in a fixed format, and the header aligns with its column's content. `[FACT]`
- **TY-8** Uniform precision per column; pad with zeros rather than varying decimals. `[FACT]`
- **TY-9** Monospace for identifiers, hashes, code, and log lines; proportional for names and descriptions. `[CRAFT]`
- **TY-10** Column headers: sentence case, 12–13px, muted; uppercase only for ≤2 words and then with +0.04em tracking. `[CRAFT]`
- **TY-11** Truncation only on non-critical columns, always with the full value available (title attribute, expand row, or detail view). Never truncate money, IDs, or status. `[FACT]`

```css
/* ✅ table type */
.table td, .table th { font-size: 13.5px; line-height: 1.38; }
.table .num { font-variant-numeric: tabular-nums; text-align: right;
              font-feature-settings: "tnum" 1; }
.table .id  { font-family: var(--font-mono); font-size: 12.5px; }
.table th   { font-size: 12.5px; color: var(--color-text-muted); font-weight: 600; }
.table .name { max-width: 28ch; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
```

## 3. Numeric dashboards

**Bad patterns** `[FACT]`
- Hero metric and its unit at the same size and weight, so "4,201 requests" reads as one string.
- Deltas without sign or baseline; `+12%` in green with no period stated.
- Inconsistent abbreviation: `4.2k` beside `1,203`.
- More than 2 significant decimals on a KPI; jittering digit counts on live updates causing width shifts.
- Percentages and absolutes mixed without labels.

```html
<!-- ❌ -->
<div><span style="font-size:32px">4201 requests</span><span style="color:green">+12%</span></div>

<!-- ✅ hierarchy inside the number; tabular so live updates don't shift width -->
<div style="display:grid;gap:4px">
  <span style="font-size:13px;color:var(--color-text-muted)">Requests · last 30 days</span>
  <span style="font-size:40px;line-height:1.05;font-variant-numeric:tabular-nums">
    4,201<span style="font-size:16px;color:var(--color-text-muted);margin-inline-start:6px">req</span>
  </span>
  <span style="font-size:13px;font-variant-numeric:tabular-nums">
    +448 (+12.0%) vs. previous 30 days
  </span>
</div>
```

**Rules**
- **TY-12** Unit and label are typographically subordinate to the figure (≤40% of its size, muted tone). `[CRAFT]`
- **TY-13** One abbreviation policy per surface, and never abbreviate in a record/ledger view ([DT-20](02-domain-taste.md)). Thresholds are `[PD]`. `[PD]`
- **TY-14** Live-updating figures use tabular figures and a reserved width so nothing reflows on change. `[FACT]`
- **TY-15** Deltas carry sign, magnitude, and baseline period; direction is conveyed by sign/arrow as well as color. `[FACT]`

## 4. Editorial rhythm

**Rules**
- **TY-16** Measure 60–75ch for prose; set on the text element. `[FACT]`
- **TY-17** Paragraph separation is *either* a blank line (0.75–1× leading) *or* a first-line indent — never both. `[CRAFT]`
- **TY-18** `text-wrap: balance` on headings and pull quotes; `text-wrap: pretty` on body. No single-word last lines in headings. `[FACT]`
- **TY-19** Justify only with `hyphens: auto` and only above ~45ch; otherwise left-align. `[CRAFT]`
- **TY-20** Optical alignment for hanging punctuation: opening quotes, bullets, and em-dashes hang outside the measure. `[CRAFT]`
- **TY-21** Vertical rhythm on a 4px grid: every block's margin and line-height resolve to multiples of 4px so blocks align across columns. `[CRAFT]`
- **TY-22** Real typographic characters: `—` `–` `’` `“ ”` `×` `→` `−` (minus, not hyphen) `′″`. No straight quotes in prose, no `->`. `[FACT]`
- **TY-23** Ligatures and contextual alternates on for prose (`liga`, `calt`); off for code and identifiers. `[CRAFT]`
- **TY-24** Icons align to cap-height, not box-center: with `align-items: center`, nudge the icon by `translateY(-0.5px)` or align on a shared baseline grid. `[FACT]`

```css
/* ✅ editorial defaults */
.prose p { max-width: 68ch; line-height: 1.6; text-wrap: pretty; margin-block: 0 1em; }
.prose h2 { font-size: 30px; line-height: 1.2; text-wrap: balance; margin-block: 2em .5em; }
.prose blockquote { margin-inline-start: -0.5em; text-indent: -0.36em; }  /* hanging quote */
.prose { hanging-punctuation: first last; }                              /* where supported */
.prose code { font-variant-ligatures: none; font-feature-settings: "calt" 0; }
```

## Screenshot QA

Zoom the screenshot to 400% for the alignment checks.

1. Screenshot a numeric column. Do digit stems line up vertically row to row? (TY-6, TY-7)
2. Is every value in a column at the same precision? (TY-8)
3. Count characters in the longest prose line. 60–75? (TY-16)
4. Measure heading line-height ÷ font-size. ≤1.25 for headings, ≥1.5 for body? (line-height table)
5. Look at every heading's last line: any single-word widow? (TY-18)
6. Search the screenshot for `"`, `'`, `--`, `->`. Any straight quotes or hyphen-dashes in prose? (TY-22)
7. Count distinct font sizes and weights on the screen. ≤6 sizes, ≤3 weights? (Drift, [DS-17](06-design-systems.md))
8. Zoom to 400% on an icon+label row: is the icon's cap aligned with the text's cap? (TY-24)
9. Switch the UI to German and Japanese; screenshot the same screens. Any clipping, mid-word breaks, clipped diacritics, or wrong line-height? (TY-1, TY-3)
10. Switch to RTL; screenshot. Is the layout mirrored, are chevrons flipped, is the logo *not* flipped? (TY-2, TY-5)
11. Set browser font-size to 200% (and user text-scaling on mobile): does text reflow without clipping or fixed-height overflow? (TY-1, [AX-15](10-accessibility.md))
12. Watch a live-updating figure for 30s: does its width change? (TY-14)
13. Screenshot a truncated cell: is the full value available anywhere? Is any money/ID truncated? (TY-11)

## Adapt or override

- **TY-19 (justification)** — some editorial systems justify as a signature (the Classical direction
  in this project does). Then hyphenation is mandatory and the measure must stay ≥45ch; check for
  rivers at 400% zoom rather than abandoning the style.
- **TY-6 (tabular figures)** does not apply to display typography in marketing settings, where
  proportional figures usually look better in a headline. It always applies in tables and dashboards.
- **TY-16 (measure)** yields for deliberately narrow captions/marginalia (35–45ch) and for
  single-line UI text of any length.
- **TY-10 (sentence-case headers)** is overridden by dense financial and scientific tables where
  short uppercase abbreviations are the domain's convention (`YTD`, `EPS`, `Δ`).
- **Legal copy** may be mandated at a specific size or in a specific case. Follow the mandate;
  don't fix its typography. `[PD]`
- **When a font lacks a feature** (no tabular figures, no small caps, missing script coverage), that
  is a font-selection problem, not a CSS problem. Escalate rather than synthesizing. `[PD]`
