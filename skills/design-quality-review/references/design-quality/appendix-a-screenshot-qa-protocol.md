# Appendix A · Screenshot QA protocol

The mechanical procedure. If a team adopts only one file from this guide, adopt this one — it turns
"looks fine to me" into a repeatable pass with a written result.

## Capture conditions

Wrong conditions manufacture defects and hide real ones. Fix these before capturing anything.

| Variable | Setting |
| --- | --- |
| Viewport | 1440×900 desktop · 1280×800 (for 400% zoom checks) · 768×1024 tablet · 390×844 and 360×800 mobile |
| Zoom | 100% for the main pass; 200% and 400% for the low-vision pass |
| DPR | Capture at 1× and 2×; note which |
| Content | Real content at realistic length; include one longest-realistic and one shortest value |
| Fonts | Webfonts loaded; no FOUT/FOIT in the frame |
| Chrome | No devtools, no extensions, no cursor; overlay scrollbars off or accounted for |
| Network | One pass on fast, one throttled to slow 3G for loading states |
| Theme | Each supported theme; plus `prefers-contrast: more` and forced-colors |
| Motion | One pass with `prefers-reduced-motion: reduce` |

## What to capture

Per screen, the minimum capture set. Name files so a reviewer can find them:
`<screen>--<state>--<viewport>@<dpr>.png`, e.g. `orders-list--zero-results--390x844@2x.png`.

**Always**
1. rest (default)
2. empty (never had data)
3. zero-results (filters exclude everything)
4. loading (throttled, captured mid-load)
5. error
6. long content (3× expected string lengths, longest realistic name)
7. permission-limited, if roles exist

**Per interactive element** (a single capture with all controls in the state, or one per control)
8. hover 9. focus-visible 10. active 11. disabled 12. pending/loading

**Per overlay** 13. open, plus 14. the frame ~50% through its enter transition

**Per breakpoint** 15. the rest state at each viewport in the table above

## The 25-item pass

Each item is pass/fail with a measurement. Rule references point at the file that explains the fix.

### Structure and hierarchy
1. Blur 8px: exactly one element dominates, and the reading path is the intended one. `[VD-9]`
2. Cover the nav: the page's purpose is still identifiable. `[IA-9, IA-11]`
3. Exactly one primary action. `[IA-10]`
4. Heading outline matches visual hierarchy, no skipped levels. `[IA-12, AX-1]`

### Space and alignment
5. ≤3 distinct left edges per content column (threshold the image to check). `[VD-7]`
6. Inside-group gap ≤ ½ between-group gap. `[VD-4]`
7. Container padding ≥ body font-size, ≥16px around prose. `[VD-5]`
8. One container width per page. `[VD-8]`

### Type
9. ≤6 font sizes, ≤3 weights on the screen. `[VD-7, DS-17]`
10. Prose measure 60–75ch; UI text ≤90ch. `[TY-16, VD-6]`
11. Heading line-height ≤1.25; body ≥1.5. `[TY table]`
12. No heading widows; real typographic characters (no straight quotes, no `--`). `[TY-18, TY-22]`
13. Numeric columns: tabular figures, right/decimal aligned, uniform precision. `[TY-6..8]`

### Color and weight
14. Grayscale: reading order unchanged; no information lost. `[VD-1, AX-19]`
15. ≤2 boundary devices on the busiest element. `[VD-14]`
16. Shadows have direction (y-offset ≥ blur ÷ 3) and are consistent. `[VD-3]`
17. Bold ≤~10% of visible text. `[VD-15]`

### States and affordance
18. Every interactive element has rest/hover/active/focus-visible/disabled captures, and disabled shows a reason. `[VD-21, IX-21]`
19. Focus ring ≥2px, ≥3:1, never clipped, present on every focus stop (tab through and capture). `[AX-18]`
20. Empty ≠ zero-results ≠ loading ≠ error, visually and in copy. `[VD-20, IA-25]`
21. Cover all text: clickable things are still identifiable. `[RC axis 6]`

### Data integrity
22. One format per data type; nothing truncated that must be exact (money, IDs, status). `[VD-17, TY-11]`
23. Anything stale shows its as-of time. `[VD-19, DT-5]`

### Resilience
24. Nothing shifts after first paint (capture at 300ms, 1s, 3s throttled); images reserve space. `[VD-23, AD-10]`
25. 200% zoom and 400% at 1280px reflow with no clipping and no horizontal scroll; reduced-motion pass shows no translation but all state changes. `[AX-15, MO-23]`

**Result format:** `passed 21/25 · S1: 1 (item 19) · S2: 3 (items 6, 13, 18) · S3: 0`

An S1 blocks. S2s block unless deferred with a ticket ID in the PR.

## PR review template

```markdown
## Design QA — <screen name>

**Reference:** <link or archived capture + date>
**Captures:** <link to the capture set>
**Conditions:** 1440×900 @2x · light theme · real content · webfonts loaded

### Result
passed __/25 · S1: __ · S2: __ · S3: __

### Defects
| # | Axis | Element | Observed | Expected | Sev | Rule | Fix |
|---|------|---------|----------|----------|-----|------|-----|
| 1 | rhythm | Card stack | 16px inside and between groups | 8 inner / 20 outer | S1 | VD-4 | nest gaps |
| 2 | states | Row link | no focus-visible | 2px accent ring, offset 2 | S1 | AX-18 | add ring |

### Derived decisions
States/values not in the reference that I derived (please confirm):
- Row hover: 8% accent tint (reference shows rest only) — RC-6
- Zero-results copy: "No invoices match these filters" — RC-6

### Requires product decision
- [PD] Whether deleting a posted invoice is allowed at all, or only reversible — IX-38
- [PD] Retention period for soft-deleted invoices — IX-38

### Deliberate deviations from the reference
- Placeholder gray raised from #c9c9c9 to #6f6f6f: reference fails 4.5:1 — AX-21 (accessibility overrides the reference, RC-8)
```

## Automatable subset

Put these in CI so the human pass covers only what needs eyes.

| Check | Tool approach |
| --- | --- |
| Items 9, 15, 16 (primitive counts) | Parse the built CSS; count distinct radii/shadows/sizes/weights (`DS-17`) |
| Item 13 (tabular figures) | Lint: numeric cell classes must include the tnum utility |
| Item 19 (focus ring) | Automated tab-walk; assert a computed outline ≥2px on every focus stop |
| Item 24 (layout shift) | CLS budget in Lighthouse CI; assert 0 after first paint |
| Item 25 (zoom reflow) | Playwright at 1280px with 400% zoom; assert `scrollWidth <= clientWidth` |
| Items 14, 20 (grayscale/state diffs) | Visual regression on the component gallery + state fixtures (`DS-16`) |
| Contrast, names, landmarks, roles | axe/pa11y on every route and every gallery cell |
| Off-scale spacing, hex literals | The greps in [06 · Design systems](06-design-systems.md) |

## Cadence

| When | Pass |
| --- | --- |
| Every PR touching UI | Items 1–8, 18–21 on the changed screens |
| Before merging a new screen | Full 25-item pass + the capture set |
| Before a release | Full pass on the 5 highest-traffic screens + the gallery diff |
| Weekly, per engineer | The 15-minute calibration drill ([12](12-taste-calibration.md)) |
| Quarterly | Drift metrics ([06](06-design-systems.md)) + multilingual and RTL pass ([08](08-typography.md)) |
