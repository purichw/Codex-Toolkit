# 02 · Domain-specific design taste

Good UI is domain-relative. The same screen that is excellent as an ops console is a failure as a
landing page. This file gives, per domain: the value the design optimizes for, hard density
targets, the tell that a screen was built by an engineer without design input, and the
domain-specific defects.

Use it two ways: to calibrate before you start, and to explain in review *why* a pattern is wrong
here even though it's right elsewhere.

## What designers notice that developers often miss

- **The optimization target differs per domain.** Admin optimizes throughput per keystroke;
  editorial optimizes reading; landing optimizes one comprehension moment; ledgers optimize
  verifiability. Applying SaaS-dashboard styling to all four is the most common domain error.
- **Density is a domain constant, not a preference.** A 64px row in an admin table is as wrong as
  a 24px row in a learning app. Developers inherit whatever the component library defaults to.
- **Chrome-to-content ratio.** Designers notice when 40% of an ops screen is toolbar. Engineers
  add affordances additively and never measure the total.
- **Which axis is primary.** Ops screens are organized by status, ledgers by time, CMS by
  hierarchy, dashboards by question. Building the same "list of records" for all of them loses the
  organizing principle.
- **Domain conventions are user muscle memory.** Bulk-select in the top-left, totals at the bottom
  right, `⌘K`, `/` for search, `Esc` to close. Reinventing these costs users more than a nicer widget gains.

## Density reference `[FACT]`

Targets for a 1440px-wide desktop viewport. Measure your build against them.

| Domain | Body size | Row / line height | Container width | Chrome budget |
| --- | --- | --- | --- | --- |
| Admin / CMS | 13–14px | 36–44px rows | full width, min 24px gutters | ≤ 15% of viewport height |
| SaaS ops / monitoring | 13–14px | 28–36px rows | full width | ≤ 20%, must include state + refresh |
| Editorial / cultural | 17–20px | 1.5–1.7 leading, 60–75ch | 640–760px text column | ≤ 8% |
| Learning app | 16–18px | 1.5–1.6 | 560–720px | ≤ 12%, one primary action visible |
| Dashboard | 13–15px labels, 28–48px hero metric | 1.3 | 12-col, full width | ≤ 15% |
| Ledger / finance | 13–14px, tabular | 32–40px rows | full width | ≤ 15%, filters must be visible |
| Landing page | 18–20px body, 48–80px display | 1.5 body | 1120–1280px, 640–720px text | n/a |
| Mobile app | 16–17px | 44–56px rows | single column, 16–20px margins | tab bar + header only |

## 1. Admin / CMS

**Optimizes:** throughput for a repeat user who knows the system. Speed of finding, editing,
and bulk-changing records.

**Good looks like:** dense tables with sticky headers; column-aligned data; one row action set,
overflow behind a `⋯`; filters that persist in the URL; keyboard access to everything; destructive
actions guarded; saved views; inline editing where it's safe.

**Engineer-built tell** `[FACT]`
- Records rendered as cards instead of rows (halves the visible count, destroys column alignment).
- 3–5 buttons repeated in every row.
- Table header not sticky; no column widths set, so columns reflow per page of data.
- Filter state lost on reload or on back-navigation.
- Form fields mirroring the API schema, in schema order, including internal IDs.
- 24px+ padding inherited from a marketing component library.

**Bad patterns → fix**

| Bad | Fix |
| --- | --- |
| Per-row button cluster | Primary inline action + `⋯` overflow menu; bulk bar for multi-select |
| Modal-in-modal for nested edit | Route to a detail page, or a side panel that keeps context |
| "Save" only at page bottom on a long form | Sticky action bar; autosave with status ([IX-7](04-interaction-design.md)) |
| Pagination only | Persistent count, page size, and total; keyboard `j/k` nav is a bonus |
| Delete adjacent to Edit, same weight | Separate destructive by ≥16px and by treatment ([IX-36](04-interaction-design.md)) |

**Rules**
- **DT-1** Rows, not cards, for homogeneous records. Cards only when items carry media or differ structurally. `[CRAFT]`
- **DT-2** Every list view: sticky header, fixed column widths, persistent filter state in the URL, visible total count. `[CRAFT]`
- **DT-3** Group form fields by user task, not by database table. Hide internal identifiers behind a "details" disclosure. `[CRAFT]`

## 2. SaaS ops / monitoring / queues

**Optimizes:** answering "is anything wrong, and what do I do about it" in under 5 seconds.

**Good looks like:** status as the primary visual axis; severity legible in grayscale (shape +
text, not hue alone); absolute + relative timestamps; explicit "last updated" and manual refresh;
degraded and partial states designed; drill-down from summary to the exact failing object in ≤2 clicks.

**Engineer-built tell** `[FACT]`
- Colored dot with no adjacent text label.
- No "as of" time on live data; no indication that polling stopped.
- Charts on library default palettes with legends far from the data.
- Only success and total-failure states; nothing for "partial", "degraded", "stale", "no data yet".
- Log/trace text in a proportional font.
- Every metric equally sized — no primary signal.

**Bad patterns → fix**

| Bad | Fix |
| --- | --- |
| Red/green dots only | Dot + label + shape (●▲■), so it survives grayscale and CVD |
| Infinite spinner while polling | Show last-success time + "retrying (3rd attempt)" + manual retry |
| Toast for an incident | Persistent banner tied to the affected scope; toasts are for actions the user took |
| Alert count with no severity split | Split by severity with the highest first; total is secondary |

**Rules**
- **DT-4** Status is never encoded by color alone; label + shape are mandatory. `[CRAFT]` (see [AX-19](10-accessibility.md))
- **DT-5** Every live surface shows data age and how to refresh. Auto-refresh cadence is `[PD]`. `[PD]`
- **DT-6** Design the five states of a monitored thing: healthy, degraded, failing, unknown/no-data, disabled-by-user. `[CRAFT]`
- **DT-7** Monospace for identifiers, logs, traces, hashes, durations in ms. `[CRAFT]`

## 3. Editorial / cultural

**Optimizes:** sustained reading and atmosphere. The interface should mostly disappear.

**Good looks like:** a single measured text column (60–75ch); generous leading; typographic
hierarchy instead of UI chrome; real photography, cropped and captioned; asymmetric layouts;
hairline rules; no cards around prose; footnotes/marginalia as considered elements.

**Engineer-built tell** `[FACT]`
- Article body inside a card, full container width, 16px/1.4.
- Images stretched to full-bleed at a fixed height with `object-fit: cover` cutting the subject; no captions.
- Share buttons and related-content modules with more visual weight than the headline.
- Uniform section spacing; no rhythm change between passages.
- Pull quotes styled as tinted boxes rather than typographic events.
- Sans-serif used for emphasis inside a serif column.

**Bad patterns → fix**

| Bad | Fix |
| --- | --- |
| Prose in a bordered card | Prose on the ground, rules for structure ([VD-12](01-visual-diagnosis.md)) |
| Full-width body text | `max-width: 68ch` on the paragraph element |
| Uncaptioned images | Caption + credit as part of the figure; `<figcaption>` sized 13–14px |
| Sidebar competing with body | Demote by value/size, or move below on narrow viewports |

**Rules**
- **DT-8** One text column, 60–75ch, leading 1.5–1.7, paragraph spacing = one line or an indent, never both. `[CRAFT]`
- **DT-9** Every image is a `figure` with a crop chosen for the subject and a caption ([AD-2](07-art-direction-imagery.md)). `[CRAFT]`
- **DT-10** Vary rhythm across the piece: at least one full-bleed or wide element per ~1,200 words. `[CRAFT]`

## 4. Learning apps

**Optimizes:** momentum. The learner should always know where they are, what's next, and that
progress is real.

**Good looks like:** one task per screen; honest progress (steps completed / total, not a fake
percentage); immediate, specific feedback; gentle error recovery with retry; chunked content;
resumability; low chrome.

**Engineer-built tell** `[FACT]`
- A dashboard of eight cards as the learner's home instead of "continue where you left off".
- Progress bar with no denominator, or one that includes items the learner can't see.
- "Incorrect" with no explanation and no path back.
- Two or three equally-weighted CTAs on a lesson screen.
- Timer pressure added without a product reason.
- Body text at 14px for an audience that may be 11 years old or on a phone.

**Bad patterns → fix**

| Bad | Fix |
| --- | --- |
| "Wrong. Try again." | Name the misconception, show the correct step, offer retry and "explain" |
| Progress by percentage only | "Step 4 of 9" + the map of remaining steps |
| Losing answers on refresh | Persist per-item answers; restore scroll and step ([IX-30](04-interaction-design.md)) |
| Streaks/points added by default | Gamification is `[PD]` — it changes learner behavior and can harm it |

**Rules**
- **DT-11** One primary action per learning screen; everything else is a link or a secondary control. `[CRAFT]`
- **DT-12** Progress is expressed with a denominator the learner can verify. `[CRAFT]`
- **DT-13** Every incorrect state includes cause + correction + retry. Whether to reveal the answer is `[PD]`. `[PD]`

## 5. Dashboards

**Optimizes:** answering a specific question. A dashboard without a question is a data dump.

**Good looks like:** one hero metric answering the screen's question; every number with a
comparison baseline (vs. previous period, vs. target); axes labeled with units; direct labels on
series instead of legends; sparklines for trend at small size; drill-down to the underlying rows;
explicit time range and timezone.

**Engineer-built tell** `[FACT]`
- 8–12 equally sized KPI cards, no hierarchy, no baselines.
- Deltas without a comparison window ("+12%" — since when?).
- Donut charts with 6+ segments; 3D effects; gradient-filled areas.
- Y-axis not starting at zero on a bar chart, or unlabeled units.
- Legend in a corner, 300px from the lines it describes.
- No empty state — an axis-only chart with no "no data for this range" message.
- Time zone unstated.

**Bad patterns → fix**

| Bad | Fix |
| --- | --- |
| KPI grid with no primary | One metric at 2–3× the others; the rest at equal, smaller size |
| "+12%" | "+12% vs. previous 30 days" with the absolute delta beside it |
| Legend-based charts | Direct-label the last data point of each series |
| Donut with 7 slices | Ranked horizontal bars; group the tail as "Other" with a count |
| Truncated axis | Zero-baselined bars; use a line chart if zero-baselining hides the signal |

**Rules**
- **DT-14** Each dashboard screen states its question in the title, and one metric answers it. `[CRAFT]`
- **DT-15** Every number carries a baseline and a period. Which baseline is `[PD]`. `[PD]`
- **DT-16** Units and timezone are always visible, never implied. `[FACT]`
- **DT-17** Every chart has an empty state, a loading skeleton with the correct footprint, and a table equivalent ([AX-31](10-accessibility.md)). `[CRAFT]`

## 6. Ledgers / finance

**Optimizes:** verifiability. The user is checking arithmetic and will trust nothing that looks approximate.

**Good looks like:** tabular figures, decimal-aligned; explicit currency; a consistent negative
convention; totals separated by a rule and repeated at the bottom; running balance; immutable
records with amendments shown as new lines; exportable; every row traceable to a source document.

**Engineer-built tell** `[FACT]`
- Numbers left-aligned or centered.
- Proportional figures, so digits don't line up between rows.
- Abbreviations in a ledger context: `$1.2k`, `3.4M`.
- Mixed precision down a column (`10`, `10.5`, `10.50`).
- Currency implied by locale rather than printed.
- Negative numbers shown only by a red color (invisible in grayscale, print, and CVD).
- Rounded rows that don't sum to the displayed total.
- A "delete" on a posted transaction rather than a reversing entry.

**Bad patterns → fix**

| Bad | Fix |
| --- | --- |
| `font-variant-numeric: normal` | `tabular-nums` on every numeric cell ([TY-6](08-typography.md)) |
| Red text for negatives | `(1,234.50)` or a leading `−` **plus** color; convention is `[PD]` |
| `$1.2k` in a statement | Full precision in ledgers; abbreviate only in charts and summary tiles |
| Client-side float math | Integer minor units or decimal library; format once at the boundary |
| Totals computed from rounded row values | Compute on raw values, then round; show a reconciliation note if they differ |

**Rules**
- **DT-18** All figures tabular, right- or decimal-aligned, uniform precision per column. `[FACT]`
- **DT-19** Currency and precision printed, never inferred. Negative convention chosen once, product-wide `[PD]`. `[PD]`
- **DT-20** Never truncate or abbreviate a monetary value in a record view. `[CRAFT]`
- **DT-21** Financial records are append-only in the UI: corrections appear as new, linked entries. Actual policy is `[PD]`. `[PD]`

## 7. Landing pages

**Optimizes:** one comprehension moment. A visitor should be able to say what this is and who
it's for after 5 seconds.

**Good looks like:** one idea above the fold, stated in specific language; a real view of the
product (screenshot, not an illustration of a screenshot); evidence (numbers, names, artifacts);
asymmetric composition; a big type-scale jump; one accent; one primary CTA with a genuinely
secondary alternative.

**Engineer-built tell** `[FACT]`
- Three-card feature grid, gradient hero, generic illustration (see [01 · Generic](01-visual-diagnosis.md#4-generic-the-ai-looking-screen)).
- Five CTAs of equal visual weight.
- Product screenshot at 40% size, inside a fake browser frame, behind a gradient overlay, unreadable.
- Section rhythm identical top to bottom.
- Logo wall with no context and no permission-checked logos.
- Type scale that never exceeds 32px.

**Bad patterns → fix**

| Bad | Fix |
| --- | --- |
| Adjective headline ("The modern way to work") | Name the job and the outcome; keep it under 12 words. Copy is `[PD]` |
| Equal-weight CTAs | One filled/outlined primary, one text link; never two primaries |
| Decorative hero image | The real interface at readable scale, cropped to the part that proves the claim |
| Uniform sections | Alternate density and width; put the single widest element next to the narrowest |

**Rules**
- **DT-22** Above the fold: what it is, who it's for, one action. Nothing else competes. `[CRAFT]`
- **DT-23** Show the product surface at legible scale (real text readable at 100% zoom) within the first two screens. `[CRAFT]`
- **DT-24** One primary CTA per page; repeats of it are allowed, competitors are not. `[CRAFT]`

## 8. Mobile apps

**Optimizes:** one-handed operation and platform familiarity. Covered in depth in
[05 · Mobile-native feel](05-mobile-native-feel.md); the domain-taste summary:

**Engineer-built tell** `[FACT]`
- Desktop layout scaled down: multi-column, 13px text, 32px controls.
- Hover states on touch; sticky hover after tap.
- Primary action at the top of the screen, out of thumb reach.
- Custom back button that diverges from the platform gesture.
- Bottom bar sitting under the home indicator / gesture area.
- Modal dialogs where the platform uses sheets.
- Web-style dropdown `<select>` menus instead of native pickers/sheets.

**Rules**
- **DT-25** Match the platform's navigation model before adding a custom one; ≤5 top-level destinations. `[CRAFT]`
- **DT-26** Primary action in the bottom third; 44×44pt (iOS) / 48×48dp (Android) minimum targets. `[FACT]`
- **DT-27** Sheets for choices and quick tasks; dialogs only for blocking, consequential decisions. `[CRAFT]`

## Screenshot QA (cross-domain)

1. Name the domain from the screenshot alone. If it reads as the wrong domain, density or chrome is wrong.
2. Measure body size, row height, container width; compare to the table above. Off by >25%? Record it.
3. Measure chrome: header + toolbar + footer height ÷ viewport height. Within the domain's budget?
4. Count elements competing for primary. Should be 1.
5. Identify the organizing axis (status / time / hierarchy / question). Is it visually first?
6. Domain-specific single check:
   - Admin: is the filter state in the URL?
   - Ops: is there an "as of" timestamp?
   - Editorial: characters per line in 60–75?
   - Learning: is there a denominator on progress?
   - Dashboard: does every number have a baseline?
   - Ledger: are digits vertically aligned between rows?
   - Landing: is any real product text readable at 100% zoom?
   - Mobile: is the primary action reachable by a right thumb at 390×844?

## Adapt or override

- **Hybrid products inherit the stricter domain.** A finance dashboard follows ledger rules for
  every number and dashboard rules for layout. When domains conflict, verifiability beats density,
  density beats decoration.
- **Consumer-facing admin** (a seller console, a creator studio) sits between admin and SaaS: keep
  admin density in tables, but raise body size to 14–15px and add more onboarding affordance.
- **Internal-only tools** may drop DT-22..24 entirely and can trade polish for throughput —
  but never trade away DT-4 (status not by color alone) or DT-18 (aligned figures), which are
  correctness issues, not polish.
- **Density tier is a product decision.** Some teams deliberately ship a comfortable-density admin
  for infrequent users. Decide once, write it down, apply everywhere. `[PD]`
- **Regulated domains override everything here** — required disclosures, retention notices,
  mandated wording and placement take precedence over any layout rule. `[PD]`
