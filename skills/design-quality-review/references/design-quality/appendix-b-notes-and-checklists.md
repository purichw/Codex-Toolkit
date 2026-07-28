# Appendix B · Implementation notes & checklists

Templates for the writing around the code: how to record design intent, how to ask a designer a
question that gets answered, and what "done" means for a UI change.

Copy these into your issue tracker as templates. They are deliberately short — a note nobody
fills in is worse than no template.

## 1. Design intent note

Write this **before** implementing, while reading the reference. It takes ~10 minutes and prevents
most rework. Attach it to the ticket; link it from the PR.

```markdown
## Design intent — <screen / component>

**Reference:** <Figma frame / capture + date / live URL>
**Category:** admin list · ops console · dashboard · ledger · editorial · learning · landing · mobile
**Density tier:** compact · default · comfortable        (see 02 · Domain taste)

### What this screen is for
One sentence, as a question the screen answers.
> "Which invoices need chasing today?"

### Hierarchy (in order)
1. <dominant element> — why it's first
2. <second>
3. <third>
Everything else is subordinate.

### The system I'm following
- Type: sizes __ / __ / __ / __ · weights __ / __ · leading per role
- Space: scale __ · inside-group __ · between-group __ · container padding __
- Color: accent role __ · how the accent is applied (stroke / underline / fill)
- Radii: __ · Shadows: __ · Boundary device per surface: __
- Image treatment: <hero / figure / thumb>, ratio sequence __

### States I will build
rest · hover · focus-visible · active · disabled(+reason) · loading · empty · zero-results · error ·
permission-limited · long-content · RTL (if applicable)

### Values in the reference I am treating as intentional
- 13px meta label (not 14) — RC-5
- 3px offset on the status dot — RC-5

### States/values not in the reference (derived — please confirm)
- Row hover: 8% accent tint
- Zero-results copy: "No invoices match these filters"

### Requires product decision
- [PD] <question> — blocking? yes/no — asked in <thread>
```

## 2. Asking a designer a question that gets answered

Bad questions get "looks good, use your judgement". Good questions are closed, show the options, and
state the cost of each.

```markdown
**Screen:** Orders list · **Element:** row overflow menu
**Context:** 6 row actions; only 2 fit inline at 1280px.
**Options**
A. 2 inline (Edit, Refund) + `⋯` for 4 — matches the reference's row height, 1 extra click for the rest
B. All 6 inline, row height 40→56px — 9 rows per viewport instead of 14 (density drops 35%)
C. Hover-reveal all 6 — fails keyboard/touch (MB-7, AX-25); not recommended
**My recommendation:** A
**Decision needed by:** Thu · **Default if no answer:** A (logged as derived, RC-6)
```

Three properties that make this work: numbered options, a stated consequence per option, and a
default that ships if nobody replies.

## 3. QA checklist generator

Don't write a bespoke checklist. Build it from the screen's category and the elements present.

**Always** (from [Appendix A](appendix-a-screenshot-qa-protocol.md), items 1–8, 14–21, 24–25).

**Then add, per element present:**

| If the screen has… | Add checks |
| --- | --- |
| A table or list | Rows per viewport vs. category target · sticky header · fixed column widths · filter state in URL · selection scope wording · empty/zero-results distinction — `DT-1..3, IX-16..18, IA-25` |
| Numbers | Tabular figures · alignment · uniform precision · one format per type · baseline+period on deltas — `TY-6..8, TY-15, DT-18` |
| Money | Full precision, never abbreviated · currency printed · negative convention · totals from raw values — `DT-18..20` |
| A chart | Units · timezone · baseline · direct labels · ≥2 encoding channels · table equivalent · empty state — `DT-14..17, AX-28..34` |
| A form | Labels above · blur validation · submit never silently disabled · error names+focuses the blocker · autosave state · draft recovery — `IX-1..3, IX-7..9, IX-30` |
| Bulk actions | Selection count visible · page-vs-matching wording · filter change behavior · per-item results · friction scaled — `IX-16..20` |
| A destructive action | Correct friction rung · object named · cascade listed · cancel focused · separation ≥16px — `IX-34..38` |
| An overlay | Sheet-vs-dialog choice · focus trap · Esc · focus return · scrim · enter/exit direction and timing — `AX-5, MB-12..13, MO-9` |
| Images | Focal point per breakpoint · face/edge margins · reserved ratio · alt correctness · placeholder labelled · contrast under text — `AD-1..3, AD-10..13, AD-17, AX-21` |
| Motion | Duration tier · exit ≈0.7× enter · transform-only · spinner delay · reduced-motion equivalent — `MO-3..8, MO-19, MO-23` |
| Mobile viewport | Safe-area insets · dvh · 44/48pt targets · thumb reach · keyboard type · 16px inputs · field above keyboard · system back — `MB-1..8, MB-16..18` |
| Multiple languages | +40% length · logical properties · RTL mirroring · per-script leading · width-based truncation — `TY-1..5` |
| Roles/permissions | Hide-vs-disable decided · reason on hover and focus · no silent 403 · partial access counts — `IX-21..24` |
| A shared component change | Gallery updated · all variants × states · drift metrics unchanged · themes checked — `DS-16..18` |

## 4. Definition of done for a UI change

```markdown
- [ ] Design intent note attached to the ticket
- [ ] Capture set produced (states × viewports, named per Appendix A)
- [ ] 25-item pass run; result recorded in the PR; no open S1
- [ ] S2 defects fixed or deferred with a ticket ID
- [ ] Reference diff run (11 · seven axes) with a defect table
- [ ] Derived states/values listed for designer confirmation
- [ ] [PD] items listed, with the default that shipped
- [ ] Deliberate deviations from the reference documented in code comments
- [ ] Keyboard-only walkthrough completed; focus stops captured
- [ ] axe/pa11y clean on the route; custom widgets' keyboard model documented
- [ ] Gallery updated if a shared component changed; drift metrics unchanged
- [ ] Throttled-network capture shows no layout shift after first paint
- [ ] Longest and empty content tested for every string
- [ ] Reduced-motion pass shows no translation and no lost feedback
```

## 5. Writing a critique comment

Four parts, in order. Anything missing makes the comment ignorable.

```
<tag> <severity> — <observed measurement> vs <expected> — <rule id> — <proposed fix>
```

```
✅ [FACT] S2 — row height 56px, 9 rows visible; category target 40px / 14 rows — DT-1 — reduce cell padding 16→10px
✅ [CRAFT] S1 — title 18px vs body 16px; reference ratio 1.75 — RC axis 3 — title to 28px/600
✅ [PD] — should a posted invoice be deletable, or only reversible? Default shipped: reversible only — IX-38
❌ "spacing feels off here"
❌ "can we make this more polished?"
❌ "I'd probably center this"
```

**Reviewer discipline**
- One comment per defect; don't bundle.
- Measure before you comment. "Looks like ~30px" is not a measurement.
- Never post a `[PD]` as a change request.
- If you can't cite a rule, either it's a `[PD]` or the guide is missing a rule — propose it.

## 6. Adding to this guide

The guide only stays useful if it grows from real defects.

1. A defect appears twice in review → propose a rule.
2. New rules take the next number in their file's sequence. Never renumber.
3. Every rule needs: a tag (`[FACT]`/`[CRAFT]`/`[PD]`), a screenshot-observable check, and an
   "adapt or override" note. A rule with no override condition is usually too broad to follow.
4. Retire rather than delete: `~~TY-7~~ (retired 2026-03 — superseded by TY-19)`.
5. Anything that can be automated moves to the CI table in [Appendix A](appendix-a-screenshot-qa-protocol.md)
   and out of the human pass. The human pass should shrink over time.
