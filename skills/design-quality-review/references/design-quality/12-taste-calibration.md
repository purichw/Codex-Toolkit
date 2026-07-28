# 12 · Taste calibration library

Paired specimens: for each product category, one arrangement that works and one that fails, described
in **observable traits** so you can compare against your own screenshot without needing the images.

How to use it: before building a screen in a category, read the pair. After building, put your
screenshot next to the "fails" column and check how many traits you share. Three or more shared
traits means you built the failing specimen.

Each pair ends with **the one difference that matters** — if you fix nothing else, fix that.

## 1. Admin list view

| Works | Fails |
| --- | --- |
| 40px rows, 13.5px text, 14 rows visible at 900px height | 72px rows with avatars, 6 rows visible |
| Sticky header; fixed column widths; columns don't reflow between pages | Header scrolls away; widths recomputed per page |
| One inline primary action per row + `⋯` overflow | 4 buttons in every row, 340px of the width |
| Numbers right-aligned, tabular, uniform precision | Numbers left-aligned, mixed precision |
| Filters visible with active-filter chips and a count ("1,043 matching") | Filters behind a modal; no indication any are active |
| Selection bar appears with count + "select all 1,043 matching" | Header checkbox with ambiguous scope |
| Row click → detail; the row's link is the name, and the whole row is not a link | Whole row clickable *and* contains 3 links; misclicks |
| Empty, zero-results (with "clear filters"), loading, and error states all distinct | One spinner; empty state identical to zero-results |

**The one difference:** rows per viewport. Everything else follows from committing to density.

## 2. SaaS ops / incident console

| Works | Fails |
| --- | --- |
| Severity as the first column: shape + label + color (`▲ Critical`) | Colored dot only |
| "As of 09:14:22 UTC · auto-refresh 30s · Refresh now" in the header | No timestamp; unclear whether data is live |
| Five designed states: healthy / degraded / failing / unknown / muted | Only green and red |
| Counts split by severity, highest first; total secondary | One "47 alerts" number |
| Monospace for IDs, traces, durations | Proportional font for trace IDs |
| Drill-down: summary → affected service → failing instance in 2 clicks | Everything expands inline into a 4,000px page |
| Incident banner persists in the affected scope | Incident announced via a toast that vanished |

**The one difference:** status readable in grayscale, with a data-age stamp.

## 3. Dashboard

| Works | Fails |
| --- | --- |
| Title states the question: "Are we hitting the ingest SLO?" | Title is "Dashboard" |
| One hero metric at 40–48px; supporting metrics at 20–24px | 10 KPI cards, identical size |
| Every number has a baseline: "+448 (+12.0%) vs. previous 30 days" | "+12%" with no period |
| Series direct-labeled at the last point | Legend 300px away, 6 similar colors |
| Axis units and timezone printed | Neither stated |
| Empty state per chart ("no data for this range · widen range") | Empty axes with no message |
| Chart click → the underlying rows | Charts are terminal; no path to records |
| Tabular figures; live values don't change width | Digits reflow every refresh |

**The one difference:** one metric answers one stated question. A dashboard without a question becomes a KPI wall.

## 4. Ledger / statement

| Works | Fails |
| --- | --- |
| Decimal-aligned tabular figures; `1,240.00 USD` in full | `$1.2k`, left-aligned |
| Negative convention consistent: `(1,240.00)` everywhere | Red text only, sometimes `-1240` |
| Running balance column; totals above a hairline rule, repeated at the bottom | No totals; user adds manually |
| Corrections as linked reversing entries | Edit-in-place on posted rows |
| Every row links to its source document | Rows are opaque |
| Date in one fixed format, one timezone, stated | Mixed "3 days ago" and `03/04/26` |
| Export preserves precision and the same column order | Export rounds differently than the screen |

**The one difference:** digits line up between rows. Nothing else in this category recovers from that failure.

## 5. Editorial article

| Works | Fails |
| --- | --- |
| 68ch measure, 19px/1.6, on the page ground | Full-width 16px/1.4 inside a bordered card |
| One `h1` at 40–48px, flush left, `text-wrap: balance` | 28px heading, centered, widow on line 2 |
| Figures with intentional crops and captions naming place/date | Full-bleed strips, `object-fit: cover`, no captions |
| Pull quote as a typographic event: larger, italic, hanging quote | Pull quote in a tinted rounded box |
| Rhythm varies: one wide image per ~1,200 words | Every section identical height and spacing |
| Share/related demoted below the article, small | Sticky share rail heavier than the headline |
| Real typographic characters throughout | Straight quotes, `--` for em dashes |

**The one difference:** the measure. 68 characters and honest leading fix most of the rest.

## 6. Learning lesson screen

| Works | Fails |
| --- | --- |
| "Step 4 of 9" plus a visible map of remaining steps | Percentage bar with no denominator |
| One primary action, bottom-aligned, 48pt tall | Three equal-weight buttons |
| Feedback names the misconception and shows the correct step | "Incorrect. Try again." |
| 17px body, 1.55 leading, ≤60ch | 14px, 1.35, full width |
| Answers persist through refresh; resume where left off | Refresh restarts the lesson |
| Content chunked: one concept, one example, one check | 6 concepts on one scrolling page |
| Continue is always available; skip is explicit and honest | Forced repetition with no exit |

**The one difference:** an honest denominator on progress. It changes how the whole screen is read.

## 7. Landing hero

| Works | Fails |
| --- | --- |
| One claim in ≤12 words naming job + outcome | "The modern platform for modern teams" |
| Real product surface at legible scale (its text readable at 100% zoom) | 40%-scale screenshot behind a gradient, unreadable |
| Asymmetric: display type left, product bleeding off the right edge | Centered stack: headline, subhead, two buttons, hero image |
| One primary CTA; secondary is a text link | 4 buttons of equal weight |
| One accent, applied as a rule/underline/border | 3 gradients, glow, mesh background |
| Evidence within one screen: a number, a name, or an artifact | Adjective list |
| Type scale jumps hard: 64px display over 19px body | Nothing above 32px |

**The one difference:** showing the real product at readable scale instead of describing it.

## 8. Mobile settings screen

| Works | Fails |
| --- | --- |
| Grouped list with section headers; 48pt rows | One long ungrouped list, 36pt rows |
| Current value on the right of each row, truncating from the middle | Value hidden until you enter the sub-screen |
| Switches for instant, reversible settings; rows for sub-screens | Everything a row; user drills in to flip a toggle |
| Destructive item last, in its own group, outlined-danger | Delete Account third from top, next to "Notifications" |
| Bottom inset respected; last row fully scrollable above the indicator | Last row under the home indicator |
| Native platform controls for pickers | Custom wheel with wrong momentum |
| Labels above fields on any edit screen; correct keyboards | Placeholders as labels; one keyboard type |

**The one difference:** showing current values in the list, so the screen answers questions without navigation.

## 9. Empty state

| Works | Fails |
| --- | --- |
| Names what goes here and why it's empty ("No invoices yet — they appear after your first sale") | "Nothing here" |
| One action that creates the first item, plus one link to learn how | No action |
| Visually distinct from zero-results and from loading | Identical to both |
| Sized to the content area, not a 400px illustration | Large centered illustration dominating the page |
| Zero-results variant names the filters and offers "clear filters" | Zero-results says "No invoices yet" (wrong and confusing) |

**The one difference:** distinguishing "never had any" from "none match your filters".

## 10. Error state

| Works | Fails |
| --- | --- |
| Names the object, the cause, and the next action | "Something went wrong" |
| Placed at the thing that failed; global banners only for global failures | Toast for a field-level error |
| Retry that retries only what failed | Retry that reloads the page |
| Preserves the user's input | Clears the form |
| Technical detail available but collapsed (request ID, code) | Raw stack trace, or nothing at all |
| Partial failure enumerated: "23 of 25 saved · 2 failed (locked)" | All-or-nothing message |

**The one difference:** the error is attached to the failing object and names the next action.

## 11. Form

| Works | Fails |
| --- | --- |
| Labels above fields; help text before the error, not after | Placeholder-as-label; requirements revealed only by failing |
| Single column; related fields grouped with 8/20 nesting | Two columns of unrelated fields |
| Validation on blur; cross-field on submit | Validation on every keystroke |
| Submit always enabled; errors named, listed, and focused | Submit disabled, no reason |
| Autosave status in one persistent place, or one explicit Save | Both autosave and a Save button |
| Optional fields marked; required is the default assumption | Every field marked "required" |
| Field width hints at expected length (postcode short, address long) | All fields 100% width |

**The one difference:** the user can always tell what is wrong and what is expected, before submitting.

## 12. Pricing table

| Works | Fails |
| --- | --- |
| Rows are features, columns are plans; one column emphasized by a rule, not a fill | 3 filled cards, the middle one scaled up 8% |
| Prices tabular, same precision, billing period stated per price | `$19` vs `$1,200/yr` mixed |
| Differences highlighted; identical rows collapsed into "all plans include…" | Every row repeated with checkmarks in all columns |
| The limit that matters is a number ("50 GB", "10 seats") | "Generous limits" |
| Enterprise column states what changes, not just "Contact us" | "Custom" in every cell |

**The one difference:** a reader can find the one row that decides their plan.

## Calibration drill (15 minutes, weekly)

1. Pick a screen you shipped this week and capture it under [Appendix A](appendix-a-screenshot-qa-protocol.md) conditions.
2. Find its category above. Read the "fails" column and count matching traits. Record the number.
3. Run the four transforms ([00](00-conventions.md)): grayscale, blur 8px, invert, threshold.
4. Name the defect with one word from [01](01-visual-diagnosis.md). One word, not three.
5. Write the single smallest change that would move the screen one column left. Ship it.
6. Log the score. Falling scores across a quarter is the only reliable evidence that taste is improving.

**Team version:** two people score the same screenshot independently, then compare. Disagreement
about a `[FACT]` means someone measured wrong. Disagreement about a `[PD]` means it needs a decision,
not a debate.

## Adapt or override

- These specimens describe **conventional excellence** in each category. A product with a genuine
  art direction may deliberately take traits from the "fails" column — centered layouts, big
  illustration, low density. That is legitimate when it is *systematic* and *stated*. It is not
  legitimate as a default.
- Category boundaries blur. When a screen sits between two categories, apply the stricter one for
  correctness traits (numbers, status, states) and the more expressive one for layout.
- Everything in the "works" column that concerns *what to show* (which limit matters, whether to
  offer skip, retention periods) is `[PD]`. The library shows the shape of a good answer, not the answer.
- Regional and regulatory conventions override specimens: pricing display rules, mandatory
  disclosures, date and number formats. `[PD]`
