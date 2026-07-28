# 11 · Reference-vs-implementation critique

A repeatable protocol for comparing what you built to what you were given. The goal is a defect
list with severities, not a feeling.

Applies to any reference: a Figma frame, a screenshot, a live site, a prototype recording.

## What designers notice that developers often miss

- **Ratios survive, values don't.** A designer checks whether the gap between sections is twice the
  gap inside them. Developers check whether the gap is 24px.
- **Repetition is the tell.** A 2px error in one place is nothing. The same 2px error in twelve rows
  is a broken variable and reads as sloppiness immediately.
- **Alignment edges are shared.** Moving one element 2px right breaks a vertical line that six other
  elements were sitting on.
- **Optical size ≠ specified size.** An icon at 20px next to 16px text may need to be 18px to look
  the same weight. Designers judge weight, not dimensions.
- **The reference's odd values are usually intentional.** A 13px label or a 3px offset is a decision
  until proven a mistake.
- **States are half the design.** Most references show one state. The missing states are where
  fidelity is actually lost.
- **Density is the fastest way to lose a design.** Rendering the same components with 20% more
  padding produces a screen that shares no character with the reference.

## Setup (non-negotiable)

Mismatched capture conditions produce phantom defects and hide real ones.

| Variable | Requirement |
| --- | --- |
| Viewport width | Exactly the reference's frame width; note DPR |
| Zoom | 100%; capture at 1× and 2× |
| Content | The reference's own content, not test data |
| Fonts | Real webfonts loaded; check with the network throttled (no FOUT in the capture) |
| Chrome | No devtools, extensions, scrollbars overlaying content, or cursor |
| Theme | Same theme, same OS appearance, same `prefers-*` settings |
| States | Capture rest, hover, focus, active, disabled, loading, empty, error, long content |

**Comparison techniques**
1. **Onion-skin** — implementation over reference at 50% opacity. Best for geometry.
2. **Difference blend** — `mix-blend-mode: difference`; black = identical. Best for finding *where* to look.
3. **Side-by-side at 400%** — for stroke weights, radii, optical centering.
4. **Blur 8px on both** — for hierarchy and weight distribution.
5. **Grayscale both** — for value/contrast fidelity.
6. **Edge/threshold both** — for alignment grids.

## The seven axes

Run in this order. Earlier axes cause later symptoms; fixing geometry often resolves apparent
hierarchy problems.

### 1. Geometry `[FACT]`

Measurable dimensions and shapes.

| Check | Method | Fail condition |
| --- | --- | --- |
| Container width and gutters | Measure the content box's left and right edges | Off by >4px, or gutters unequal |
| Column split | Measure each column's width ratio | Ratio off by >3% (a 60/40 built as 50/50 is S1) |
| Border-radius | 400% crop of each corner | Wrong step, or mixed radii where reference has one |
| Stroke widths | 400% crop; count pixels at 1× | 1px vs 1.5px vs 2px mismatch |
| Icon box vs glyph size | Measure the glyph's ink, not the SVG viewport | Icon optically heavier/lighter than reference |
| Aspect ratios | Measure media boxes | Off by >2% |
| Control heights | Measure buttons, inputs, rows | Off by >2px, or inconsistent among siblings |

### 2. Rhythm `[FACT]`

The spacing system as actually built.

- List six vertical gaps in the reference and six in the build. Are the build's values on a
  consistent scale (4/8-based or the system's), and do the *ratios* match?
- Compute inside-group gap ÷ between-group gap for both. Should match within ~15%.
- Check the first and last child's padding against the container (top/bottom asymmetry is a
  frequent build defect).
- Check baseline rhythm: do text blocks in adjacent columns share baselines?

### 3. Hierarchy `[FACT]`

- Blur both at 8px. Same element dominates? Same reading path (1st, 2nd, 3rd)?
- Grayscale both. Same relative value order for text (title darker than body darker than meta)?
- Count elements competing for primary in each. Should be 1 in both.
- Check the type-size ratio between the two largest text elements. If the reference is 2.4× and the
  build is 1.3×, the hierarchy is flattened even though every size is "close".

### 4. Density `[FACT]`

- Rows or cards visible in one viewport: reference vs build. Off by more than 1 row = S2.
- Characters per line in the main text block.
- Ink coverage: threshold both at 50% and compare the percentage of dark pixels (±20% is fine;
  ±50% means the build is much lighter or heavier).
- Chrome height ÷ viewport height in both.

### 5. Visual weight `[FACT]`

- Grayscale both, then blur 20px. Compare where the "mass" sits — the darkest region should be in
  the same place.
- Identify the single darkest and single lightest elements in each. Same elements?
- Count boundary devices per element in both ([VD-14](01-visual-diagnosis.md)). A build that adds a
  border where the reference used space is heavier even if every color matches.
- Compare shadow presence: reference `shadow-sm` built as `shadow-lg` is the most common weight defect.

### 6. Affordance `[FACT]`

- Cover all text. Can you still tell which things are clickable in both?
- Is every interactive element identifiable without hovering (border, underline, icon, tint)?
- Are affordance treatments consistent across like elements (all rows clickable, or only some)?
- Cursor states: pointer on interactive, text on selectable, `not-allowed` on disabled.
- Does the build add affordances the reference didn't have (a whole card clickable when only the
  title was a link)? That's a behavioral change, not a visual one — flag it.

### 7. States `[FACT]`

Build the state matrix and compare each cell. Missing cells are the most common S2 finding.

| | rest | hover | focus-visible | active | disabled | loading | empty | error | long content |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Primary button | | | | | | | — | — | ✓ |
| Row | | | | | — | | — | — | ✓ |
| Input | | | | — | | | | | ✓ |
| List/table | — | — | — | — | — | ✓ | ✓ | ✓ | ✓ |

If the reference doesn't specify a state, the derivation rule is: hover = 8% accent tint or one
ramp step; active = one step past hover + 0.5px translate; focus-visible = the system's ring;
disabled = muted text + subtle border, reason attached. Log every derived state so the designer can
correct it.

## Defect record format

One line per defect. This is what you paste into the PR.

```
[axis] element — observed vs. reference — severity — proposed fix

geometry   Card corner radius — built 12px, ref 4px (measured at 400%) — S2 — use --radius-md
rhythm     Section gap 16px inside and between groups; ref 8/20 — S1 — nest gaps, 8 inner / 20 outer
hierarchy  Title 18px vs body 16px; ref 28/16 — S1 — title to 28px, weight 600
density    9 rows per viewport, ref 14 — S2 — row height 56→40px, cell padding 16→10px
weight     Card uses border + tint + shadow-lg; ref border only — S2 — drop tint and shadow
affordance Whole card clickable; ref links the title only — S1 (behavior change) — confirm with design [PD]
states     No focus-visible on row links — S1 — add the system focus ring
```

## Rules

- **RC-1** Capture conditions match the reference exactly before any comparison. A defect found under mismatched conditions is not a defect. `[FACT]`
- **RC-2** Run the axes in order: geometry → rhythm → hierarchy → density → weight → affordance → states. `[CRAFT]`
- **RC-3** Report ratios, not just values: "gap ratio 1:1, reference 1:2.5" beats "gap is 16px". `[CRAFT]`
- **RC-4** ≤2px differences are S3 unless repeated, on a shared alignment edge, or crossing a minimum — then S2. `[FACT]`
- **RC-5** Treat unusual reference values as intentional; implement them and ask, rather than normalizing silently. `[CRAFT]`
- **RC-6** Any state not shown in the reference is derived by the documented rule and logged as derived. `[CRAFT]`
- **RC-7** Behavioral divergence (what's clickable, what's optional, what's destructive) is escalated as `[PD]`, never resolved by matching pixels. `[PD]`
- **RC-8** Never "improve" the reference during implementation. Build it, log the objection, and raise it separately — except for accessibility failures ([AX](10-accessibility.md)), which you fix and report. `[CRAFT]`
- **RC-9** Every defect gets a severity. A list without severities can't be triaged and will be ignored. `[CRAFT]`
- **RC-10** Re-capture after fixes and re-diff. Fixes routinely introduce new alignment defects. `[CRAFT]`

## Screenshot QA — the 12-minute pass

1. Capture build and reference under identical conditions. (RC-1)
2. Difference-blend them. Note the three brightest regions — start there.
3. Onion-skin at 50%: check container edges, column split, control heights.
4. Crop three corners and two strokes at 400%: radii and stroke widths.
5. Measure six gaps in each; compute the inside/between ratio.
6. Blur both to 8px: same dominant element, same reading path?
7. Grayscale both: same value order, same darkest/lightest elements?
8. Count rows/cards per viewport and characters per line in both.
9. Count boundary devices on the busiest element in both.
10. Cover all text in both: is clickability equally evident?
11. Capture the state matrix for the build; fill the table; list missing cells.
12. Write the defect record. Assign severities. Re-capture after fixing. (RC-9, RC-10)

## Adapt or override

- **Screenshot-only references** can't be measured precisely (unknown DPR, unknown font rendering).
  Derive the scale from a known quantity (a 16px body line, a 44px control) and then measure in
  ratios. Report tolerances rather than exact px.
- **Responsive references** show one width. Everything between the given breakpoints is `[PD]` —
  don't invent breakpoint behavior silently; propose it explicitly.
- **Living references (a competitor's site)** change under you. Archive the capture with a date, and
  compare only against the archive.
- **When the reference is a prototype recording**, motion fidelity uses [09](09-motion.md)'s frame
  captures; static axes still apply to each frame.
- **Platform-native builds** legitimately deviate: system fonts, native controls, platform metrics.
  Match intent and hierarchy, not pixels, and record which deviations are platform-mandated.
- **Reference vs. system conflict** — when the reference contradicts the design system, the system
  usually wins for shared components (or the system is out of date and needs updating). Either way
  it's a `[PD]`, resolved once and applied to all instances, not per screen.
