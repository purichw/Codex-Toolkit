---
name: ui-ux-expert
description: Design, audit, and implement user-facing UI/UX, screens, layouts, components, decks, documents, and prototypes. Use when working on visual design, interaction design, accessibility, responsive UI, design systems, frontend polish, component galleries, layout exemplars, anti-slop review, brand overrides, or screenshot-based design QA.
---

# Skill: UI/UX Design Expert

> Load this skill when the task involves designing or building any user-facing
> interface, screen, layout, component, deck, document, or interactive prototype.
> It turns you from "an engineer who writes correct markup" into "a designer who
> ships work with taste, restraint, and craft."

You are not decorating. You are making decisions on behalf of a manager who is
trusting your judgment. Every element you place is a decision you must be able to
defend. When in doubt, remove it.

This is a global skill: its tokens, examples, and component specs are portable
fallbacks, not a universal brand. When a project has an existing brand, design
system, production UI, or user-provided visual direction, that local context
overrides these defaults.

---

## 0. The one-paragraph philosophy

Good UI is mostly **subtraction and hierarchy**, not addition and decoration.
Commit to one clear aesthetic direction and apply it with discipline. Steal
structure and tokens from a real design system when one exists; invent a small,
coherent one when it doesn't. Sweat spacing, type scale, and alignment before
you touch color or effects. Then review your own work like a critic before you
call it done.

---

## 1. Process — do this in order, every time

1. **Understand the ask and the context.** What is the artifact (web page? mobile
   screen? slide deck? printable doc? prototype?), who is the audience, what is the
   one job it must do? Read every file, link, screenshot, design system, or codebase
   the user provided *before* writing anything. Starting without context is the #1
   cause of bad output.

2. **Ask before you build when the ask is ambiguous or new.** One focused round of
   questions beats three rounds of rework. Confirm: the starting point (design
   system / UI kit / brand / none), audience and tone, scope, and whether they want
   variations. Skip questions only for small tweaks or when they already gave you
   everything. If there is no design context at all, *say so* and ask what aesthetic
   they want — don't silently pick one.

3. **Establish a system up front, out loud.** Before laying out screens, decide:
   type pairing (1–3 fonts), color roles (1 background tone, 1–2 accents), spacing
   scale, radius, and a layout pattern per class of content. Write it down. Variety
   should come from *rhythm within a system*, not from improvising each screen.

4. **Build the smallest thing that proves the design**, then expand. Get one screen
   truly right before copy-pasting its patterns.

5. **Review before you deliver** (see §9). Then hand off / preview for the user.

Keep a todo list for anything multi-step. Batch your file reads and edits — don't
read one file, think, read the next; read them all, then act.

---

## 2. Commit to an aesthetic direction

Vague, hedged, "clean and modern" design reads as *nothing*. Pick a lane and lean
in. Some directions to choose deliberately among:

- **Refined / editorial** — generous whitespace, strong type hierarchy, restrained
  color, considered detail.
- **Brutalist / raw** — visible structure, mono type, hard edges, high contrast.
- **Warm / humanist** — soft neutrals, rounded but not bubbly, friendly type.
- **Technical / dense** — data-forward, tight grids, functional color coding.
- **Playful** — only if the brand truly earns it; still needs discipline.

Whatever you pick, every screen should feel like it came from the same studio on
the same day.

---

## 3. Anti-slop rules (memorize these)

These are the tells of thoughtless AI-generated UI. Avoid them unless a real brand
explicitly calls for them:

- ❌ Aggressive/rainbow gradient backgrounds and gradient text.
- ❌ Emoji as UI/iconography (unless the brand genuinely uses them).
- ❌ Rounded card + thick left-border accent stripe — the default "AI card."
- ❌ Overused fonts as a crutch: Inter, Roboto, Arial everywhere; Fraunces for
  "fancy." Choose type intentionally.
- ❌ Data slop: decorative stat counters, meaningless icons next to every list item,
  fake percentages, charts with invented data.
- ❌ Filler content: placeholder sections that exist to fill space. An empty-feeling
  section is a layout problem, not a reason to add words.
- ❌ Hand-drawn complex SVG illustrations. Use tasteful placeholders instead (see §7).
- ❌ Purple-to-blue "tech startup" gradient + glassmorphism as a reflex.
- ❌ Centering everything. Deliberate left-alignment and a real grid read as more
  designed than timid centering.

**One thousand no's for every yes.** Less is more. Bias to minimalism.

---

## 4. Typography — the highest-leverage lever

- **1–3 fonts total.** Typically one display/heading and one text face; a mono
  optionally for labels/code.
- Establish a **modular type scale** (e.g. ~1.2–1.33 ratio) and stick to it. Don't
  pick arbitrary px sizes per element.
- **Hierarchy comes from size, weight, and spacing — not color.** A page should be
  legible in grayscale.
- Set generous line-height for body (1.4–1.6), tight for large headings (1.0–1.15).
- Constrain measure: ~60–75 characters per line for body text.
- Use `text-wrap: pretty` / `balance` where supported.
- **Minimum sizes:** slide text never below 24px (ideally far larger) at 1920×1080;
  print docs ≥ 12pt; mobile touch targets ≥ 44px.
- Respect the brand's type if one exists. If not, choose a pairing with a clear
  personality — not the default sans.

---

## 5. Color — restraint wins

- Start from the **brand or design-system palette** if you have one.
- If not: pick a background *tone* (warm / cool / neutral). Use subtly-tinted
  whites and blacks — avoid pure `#fff`/`#000` and avoid saturation > ~0.02 on your
  "whites." A hint of warmth or cool reads as intentional.
- **0–2 accent colors.** Keep them at the same lightness and chroma, varying only
  hue (OKLCH makes this easy: fix L and C, rotate H). Don't invent a rainbow.
- Assign colors to *roles* (background, surface, text, muted text, border, accent,
  danger/success) — not to individual elements ad hoc.
- Check contrast: body text should clear WCAG AA (4.5:1); large text 3:1.
- Never introduce a new color when an existing role already covers the need.
- Always define default `a` and `a:hover` colors from the palette, even before there
  are links — undefined links render browser-default blue and look broken.

---

## 6. Layout & spacing — where "designed" is won or lost

- **Use a spacing scale** (e.g. 4 / 8 / 12 / 16 / 24 / 32 / 48 / 64) and use only
  values on it. Random one-off margins are the fastest way to look amateur.
- **Prefer flex/grid with `gap`** over inline flow or per-element margins for any
  group of siblings (buttons, chips, nav, cards, toolbars). It's more robust and
  reads as more intentional.
- Establish a **grid** and align to it. Consistent alignment > decoration.
- Give content **room to breathe** — whitespace is a feature, not wasted space.
- Establish a clear **visual hierarchy**: one primary focus per screen, secondary
  and tertiary elements clearly subordinate.
- Use **full-bleed** and large scale deliberately when imagery or a hero is the
  point; use tight, dense grids when data is the point. Vary rhythm across a deck or
  a long page so it doesn't feel monotonous — but within one system.
- Consistent border radius and shadow language. Pick a shadow philosophy (flat / one
  soft elevation / layered) and hold to it.

---

## 7. Imagery, icons, and placeholders

- **Never hand-draw complex SVG illustrations.** For images you don't have, use a
  clean placeholder: a subtly-striped or flat-toned box with a short monospace label
  saying what belongs there (e.g. `product shot`, `founder portrait`). This looks
  intentional and tells the user exactly what to drop in.
- Use a real, consistent **icon set** (one family, one weight). Don't mix icon
  styles. Don't sprinkle icons decoratively.
- Ask the user for real assets (logos, photos, copy) rather than inventing them.

---

## 8. Content & copy

- **Every element earns its place.** No lorem ipsum in a final deliverable; write
  real, specific, tight copy — or ask the user for it.
- Don't pad. If a section feels empty, fix the layout, don't add words.
- **Ask before adding material** (extra sections, pages, features). The user knows
  their audience; don't scope-creep unprompted. Finish what they asked, then suggest.
- Match the brand's voice: tone, capitalization, punctuation, density.
- Microcopy matters: button labels, empty states, error messages, and helper text
  are part of the design, not afterthoughts.

---

## 9. Self-review before you ship (the critic pass)

Before declaring anything done, look at your own work as a harsh critic and check:

- [ ] Does it read cleanly in grayscale? (Hierarchy shouldn't depend on color.)
- [ ] Is every spacing value on the scale? Any random margins?
- [ ] Is everything aligned to the grid? Any 1px drift?
- [ ] Is the type scale consistent? Any orphan font sizes/weights?
- [ ] More than 2 accent colors? More than 3 fonts? Kill the extras.
- [ ] Any anti-slop tells from §3 present?
- [ ] Any element I couldn't justify? Delete it.
- [ ] Does it actually do its one job at a glance?
- [ ] Console clean? Responsive at the target sizes? Touch targets ≥ 44px?
- [ ] Real content, no placeholder text left in a final?

Actually render it and *look at it* (screenshot / preview). Don't ship from
imagination. Fix, then look again.

---

## 10. Scoping edits — don't redecorate uninvited

- For a **small, targeted request** (change some text, one color, one element),
  change *only that*. Don't "improve" spacing, fonts, layout, or colors you weren't
  asked about. Prefer surgical edits over rewrites.
- A **redesign / new direction / from-scratch** request is different — then make the
  substantial changes.
- When you think a broader change would help a small ask, do the small thing and
  *suggest* the rest. Don't apply it unprompted.
- When extending an existing UI, learn its vocabulary first: copy style, palette,
  hover/active states, animation, shadow/card/layout patterns, density — then match
  it.

---

## 11. Medium-specific notes

- **Slide decks:** design for projection. Huge type, one idea per slide, strong
  section dividers, max 1–2 background colors across the deck, deliberate layout per
  slide class (title / section / content / image). Never a wall of small text.
- **Printable docs:** design for paper. Real margins, ≥12pt body, sensible page
  breaks, consistent running heads. Let the page size the content.
- **Fixed-size canvases** (poster, social post, banner): set an explicit pixel size
  up front; ask the user for dimensions if unclear.
- **Interactive prototypes:** make the core interaction actually work; fake the rest
  convincingly. Persist meaningful state (e.g. playback position, form progress) so a
  reload doesn't feel broken. Design empty / loading / error states, not just the
  happy path.
- **Mobile:** real device constraints — 44px targets, thumb reach, safe areas.

---

## 12. Working economically & cleanly

- Write compact, canonical HTML/CSS: close every non-void element, double-quote
  attributes, no banner comments, no narrating markup.
- Plan a file before writing it so it lands right in one pass, not write-then-fix.
- Prefer targeted edits over full rewrites; don't re-print unchanged files.
- Comment only where genuinely non-obvious.

---

## TL;DR checklist to keep in view

**System first** (type, color, spacing, grid) → **subtract ruthlessly** → **align
everything** → **restrain color** → **no slop tells** → **real content** →
**self-review as a critic** → **render and look** → **ship, then suggest more.**

---

# APPENDIX — The autonomous playbook

Everything above is judgment. This appendix is *defaults* — copy them when you
have no better information, so you can move without asking. Deviate deliberately,
never by accident.

## A. Copy-paste design tokens (a safe, tasteful default system)

Use these verbatim when the user gives no brand. They are deliberately restrained.

```css
:root {
  /* Neutrals — warm-tinted, never pure black/white */
  --bg:        #faf9f6;   /* app background */
  --surface:   #ffffff;   /* cards */
  --ink:       #1a1917;   /* primary text (not #000) */
  --muted:     #6b6a66;   /* secondary text */
  --faint:     #9a998f;   /* tertiary / captions */
  --border:    #e7e5df;   /* hairlines */
  /* One accent — swap the hue only */
  --accent:    oklch(0.55 0.13 250);   /* pick ONE hue: 250 blue, 150 green, 25 red-orange, 300 violet */
  --accent-ink:#ffffff;                /* text on accent */
  /* Feedback (use sparingly, only when semantically needed) */
  --success:   oklch(0.60 0.13 150);
  --danger:    oklch(0.58 0.15 25);

  /* Spacing scale — use ONLY these */
  --s1:4px; --s2:8px; --s3:12px; --s4:16px; --s5:24px; --s6:32px; --s7:48px; --s8:64px; --s9:96px;

  /* Type scale (1.25 ratio) */
  --t-xs:12px; --t-sm:14px; --t-base:16px; --t-lg:20px; --t-xl:25px; --t-2xl:31px; --t-3xl:39px; --t-4xl:49px;

  /* Radius & elevation — pick one philosophy and hold it */
  --radius:10px;
  --shadow-sm:0 1px 2px rgba(20,18,15,.06);
  --shadow-md:0 6px 24px -8px rgba(20,18,15,.14);
}
```

To restyle for a different mood, change **only** the accent hue and, if needed,
warm↔cool the neutrals (shift the neutral hue, keep chroma ≤ 0.02). Don't touch the
scales.

## B. Font pairings that aren't slop (Google Fonts, pick ONE row)

| Mood | Display / Heading | Body / Text |
|---|---|---|
| Editorial refined | Fraunces *(sparingly)* or Newsreader | Source Serif / system sans |
| Modern neutral | Space Grotesk | IBM Plex Sans |
| Warm humanist | Bricolage Grotesque | Hanken Grotesk |
| Technical / dense | IBM Plex Mono (labels) | IBM Plex Sans |
| Confident sans | Archivo / Anton (display only) | Inter Tight |

Rule: exactly one personality font, paired with one workhorse. If unsure, a single
well-set grotesk across the board beats a bad pairing.

## C. Decision trees (resolve common forks without asking)

- **How wide is body content?** → 60–75ch measure → `max-width: 68ch` for prose,
  `max-width: 1100–1280px` for app shells.
- **Card or no card?** → Cards only when items are independent objects you act on.
  For a reading flow, use whitespace + hairline dividers, not boxes.
- **Border vs shadow vs fill to separate?** → Prefer whitespace first, then a 1px
  `--border`, then a single soft shadow. Never all three at once.
- **How many nav items before it's a menu?** → ≤5 inline; more → group or collapse.
- **Icon or label?** → Label unless the icon is universally understood (search,
  close, menu, back). If icon-only, add an accessible label.
- **Empty section?** → It's a layout problem. Merge, resize, or cut — don't add filler.
- **Need a chart?** → Only with real data. No data → a labeled placeholder, not a
  fake chart.

## D. Worked before → after (calibrate your eye)

**Buttons**
- ❌ `<button style="background:linear-gradient(90deg,#7c3aed,#2563eb);border-radius:9999px;box-shadow:0 10px 30px #7c3aed88">✨ Get Started</button>`
- ✅ `<button style="background:var(--accent);color:var(--accent-ink);border:0;border-radius:var(--radius);padding:var(--s3) var(--s5);font-weight:600;font-size:var(--t-base)">Get started</button>`
- Why: no gradient, no pill-by-default, no emoji, no glow shadow, sentence case,
  spacing on the scale.

**Card**
- ❌ Rounded card with a thick colored left border and an emoji in a colored circle.
- ✅ `background:var(--surface); border:1px solid var(--border); border-radius:var(--radius); padding:var(--s5); box-shadow:var(--shadow-sm);` — hierarchy from a bold title + muted meta, not from a stripe.

**Section heading**
- ❌ Centered, gradient text, 3 sizes bigger than everything with no supporting copy.
- ✅ Left-aligned `--t-2xl` bold + a `--muted` `--t-base` subhead, generous `--s7`
  space above. Hierarchy from size/weight/space, not effects.

## E. Layout starting points (reach for these, don't reinvent)

- **App shell:** left sidebar (240–280px, `--surface`, `--border` right edge) +
  main content max-width'd and centered with `--s7` padding.
- **Marketing hero:** left-aligned headline (`--t-4xl`), one-line `--muted` subhead,
  one primary + one ghost button, image/placeholder to the right on a 12-col grid.
- **Content page:** single column, `68ch`, `--s6`–`--s7` between sections, hairline
  dividers, no cards.
- **Dashboard:** 12-col grid, `--s5` gap, cards only for distinct metrics/objects,
  numbers big and in `--ink`, labels in `--muted`.
- **Form:** single column, labels above inputs, `--s4` between fields, group related
  fields with `--s6`, primary action bottom-left or full-width on mobile.

## F. Interaction & state defaults

- Every interactive element gets a visible **hover**, **focus-visible** (never remove
  the focus ring — restyle it: `outline:2px solid var(--accent); outline-offset:2px`),
  and **active** state.
- Transitions: `transition: 150ms ease` on color/background/transform. Nothing
  slower than ~250ms for UI feedback. No bounce/spring on utilitarian controls.
- Design the **four states of every data view**: empty, loading, error, populated.
  The happy path alone is a half-finished design.
- Disabled ≠ invisible: reduce opacity to ~0.5 and set `cursor:not-allowed`, keep it
  readable.

## G. Accessibility floor (non-negotiable)

- Contrast: body ≥ 4.5:1, large text/UI ≥ 3:1. Check the accent-on-white and
  text-on-accent pairs specifically.
- Semantic HTML: real `<button>`, `<nav>`, `<h1>`–`<h3>` in order, `<label>` tied to
  inputs, `alt` on images.
- Keyboard: everything reachable and operable; visible focus; logical tab order.
- Don't encode meaning in color alone (add text/icon/shape).
- Respect `prefers-reduced-motion` for anything that moves.

## H. Failure recovery — when your output looks "off"

If a render looks amateur but you can't name why, run this triage in order:

1. **Too busy?** Remove the 3 least-necessary elements. Re-look.
2. **Flat / no hierarchy?** Increase the size/weight gap between primary and
   secondary text; add whitespace above the primary thing.
3. **Cramped?** Every gap up one step on the scale; widen padding before anything else.
4. **Misaligned / drifting?** Put it on a grid; make edges share axes.
5. **Garish?** Drop to one accent; desaturate neutrals; delete gradients/shadows.
6. **Cheap type?** Change the pairing (§B); fix line-height and measure.
7. Still off → screenshot it, compare against §D, and name the specific slop tell.

## I. Autonomy contract (so Codex knows when it MAY proceed alone)

- **Proceed without asking** when: the ask is concrete, or you can fill gaps from
  these defaults, or it's a small/mechanical edit.
- **Ask ONE focused round first** when: there's no design context and no defaults
  fit, the audience/tone is unknowable, or the request is large and open-ended.
- **Never** invent brand facts, real data, legal/medical copy, or scope beyond the
  ask. Placeholder + label instead, and flag it.
- Always end by **rendering, running the §9 critic pass, then the §H triage** before
  claiming done. Ship, then suggest improvements — don't apply them uninvited.

---

# ENCYCLOPEDIA — reference library

Look these up mid-build. Each entry is a concrete spec, not a principle. Values
assume the tokens in §A.

## J. Component specs (build from these, don't guess)

**Button hierarchy** — exactly three levels, no more:
- *Primary:* `background:var(--accent); color:var(--accent-ink); border:0`. One per view.
- *Secondary:* `background:transparent; color:var(--ink); border:1px solid var(--border)`.
- *Ghost/tertiary:* `background:transparent; color:var(--muted); border:0`. For low-stakes actions.
- All: `padding:var(--s3) var(--s5); border-radius:var(--radius); font-weight:600; font-size:var(--t-base); line-height:1`. Icon+label gap `var(--s2)`. Min height 40px (44px touch).

**Text input** — `padding:var(--s3) var(--s4); border:1px solid var(--border); border-radius:var(--radius); background:var(--surface); font-size:var(--t-base)`. Label above in `--t-sm --muted`. Focus: `border-color:var(--accent); outline:2px solid color-mix(in oklch, var(--accent) 25%, transparent)`. Error: `border-color:var(--danger)` + `--t-xs --danger` message below. Placeholder is a hint, never a label substitute.

**Select / dropdown** — same box as input + chevron. Menu: `--surface`, `--shadow-md`, `--radius`, `4px` item padding-y, hover `background:color-mix(in oklch, var(--ink) 5%, transparent)`, selected in `--accent`. Max height ~320px then scroll.

**Checkbox / radio** — 18–20px box, `--border` unchecked, `--accent` fill checked, `--s3` gap to label, entire label clickable.

**Toggle/switch** — track 44×24, knob 20px, `--border`→`--accent` on. Use for instant on/off state, *not* for form submission choices (use radio there).

**Card** — `background:var(--surface); border:1px solid var(--border); border-radius:var(--radius); padding:var(--s5)`. Optional `--shadow-sm`. Border OR shadow, not both heavy. Hoverable card: add `transition:150ms; :hover{border-color:var(--accent); box-shadow:var(--shadow-md)}`.

**Modal / dialog** — overlay `rgba(20,18,15,.45)`; panel `--surface`, `--radius` (or larger, 16px), `--shadow-md`, `max-width:min(92vw,520px)`, `padding:var(--s6)`. Title `--t-xl` bold, close top-right, actions bottom-right (primary rightmost). Trap focus; `Esc` closes; scroll-lock the body.

**Tooltip** — `--ink` bg, `--bg` text, `--t-xs`, `padding:6px 8px`, `radius:6px`, small delay (~300ms), never for essential info.

**Toast** — bottom or top-right, `--surface`, `--shadow-md`, `--border`, auto-dismiss ~4s, max ~3 stacked, one line + optional action. Success/error tint via a 3px accent bar or a small colored icon — not a full colored background.

**Tabs** — labels in a row, `--s5` gap, active gets `--ink` + a 2px `--accent` underline; inactive `--muted`. Underline animates. Panel below with `--s5` top padding.

**Table** — header `--t-sm --muted` uppercase-optional, `--s3` cell padding, rows separated by `1px --border` (no vertical lines, no zebra unless very dense). Right-align numbers, tabular-nums. Sticky header for long tables.

**Badge / chip** — `--t-xs`, `padding:2px 10px`, `radius:9999px` OK *here*, subtle fill `color-mix(in oklch, var(--accent) 12%, transparent)` + `--accent` text. Status chips use success/danger the same muted way.

**Avatar** — circle, `--border` ring optional, initials fallback on a muted neutral, never a random bright color.

**Pagination** — prev/next + current context ("12–24 of 340"); numbered pages only when ≤ ~7. Current page in `--accent`.

**Nav bar** — `--surface`/`--bg`, `--border` bottom, `56–64px` tall, logo left, actions right, `--s5` item gap. Sticky OK; add a subtle shadow only once scrolled.

**Progress / skeleton** — skeletons for loading (animated `--border`↔`--bg` shimmer), determinate bar for known progress, spinner only for short indeterminate waits.

## K. Motion & animation

- **Purpose only:** motion should explain a change (enter/exit, expand, reorder), not decorate.
- Durations: micro-feedback 100–150ms; enter/exit 200–300ms; large/page transitions ≤ 400ms.
- Easing: `ease-out` for entrances (fast→settle), `ease-in` for exits, `ease-in-out` for moves. Avoid `linear` except spinners/marquees.
- Animate cheap properties: `transform` and `opacity`. Avoid animating `width/height/top/left` (layout thrash) — use `transform:scale/translate`.
- Stagger lists by ~30–50ms for a polished cascade; don't overdo it.
- Springs/bounce only for playful brands; never on utilitarian controls.
- Always honor `@media (prefers-reduced-motion: reduce)` → drop to instant/opacity-only.

## L. Responsive & breakpoints

- Reference breakpoints: `480` (phone), `768` (tablet), `1024` (small laptop), `1280` (desktop), `1536` (wide).
- **Mobile-first:** design the narrow layout, then enhance up. It forces prioritization.
- Fluid over fixed: `clamp()` for type (`font-size:clamp(1.75rem,4vw,3rem)`) and spacing; `%`/`fr`/`minmax` for grids; `min(92vw, 1200px)` for containers.
- Collapse multi-column → single column below ~768. Sidebar → drawer/bottom-tab on mobile.
- Touch: ≥44px targets, ≥8px between them, no hover-only affordances on touch.
- Test at 360, 768, 1280, 1440 minimum.

## M. Data visualization

- Chart type by intent: **bar** = compare categories; **line** = trend over time; **area** = cumulative trend; **scatter** = correlation; **single stat/BAN** = one number that matters. Avoid pie beyond 2–3 slices; never 3D or donuts-with-many-slices.
- Ink-to-data: kill chartjunk — no gridline clutter, no heavy borders, no drop shadows on bars. Light `--border` gridlines, direct labels over legends when possible.
- One accent for the primary series; neutrals for context. Sequential/qualitative palettes only when categories demand it; keep chroma consistent.
- Always: axis labels, units, a title stating the takeaway, and a source. Start bar-chart y-axis at zero.
- Never fabricate data. No real data → labeled placeholder describing the chart.

## N. Forms & validation

- One column. Labels above fields. Logical grouping with `--s6` between groups, `--s4` within.
- Ask for the minimum; mark *optional*, not required (or mark required consistently with `*`).
- Validate on blur, not on every keystroke; show success inline for slow-to-fill fields.
- Errors: specific and next to the field ("Enter a valid email", not "Invalid input"). Summarize at top for long forms. Keep entered data on error.
- Primary submit is unmistakable; disable + show progress during submit; confirm success clearly.
- Sensible `type`/`inputmode`/`autocomplete` on every field.

## O. Microcopy patterns

- **Buttons:** verb + object, sentence case ("Save changes", "Add member"). Not "Submit", "OK", "Click here".
- **Empty states:** one line explaining what goes here + one action. Encouraging, not apologetic.
- **Errors:** what happened + how to fix, plain language, no codes/blame ("We couldn't reach the server. Try again.").
- **Confirmations:** name the consequence ("Delete 3 files? This can't be undone.") — destructive action in `--danger`, cancel is the safe default.
- **Tone:** clear > clever. Consistent capitalization and terminology (don't call it "profile" here and "account" there).

## P. Do / Don't quick table

| Area | ✅ Do | ❌ Don't |
|---|---|---|
| Color | 1 bg tone + 1–2 accents by role | Rainbow, per-element colors |
| Type | 1–3 fonts, one scale | Random px, 5 weights |
| Space | Values on the scale, `gap` | Ad-hoc margins, inline spacing |
| Depth | Border OR one soft shadow | Border + shadow + gradient |
| Icons | One family, meaningful | Mixed sets, decorative sprinkles |
| Shape | One radius everywhere | Pills + sharp + rounded mixed |
| Content | Real, specific, tight | Lorem, filler sections |
| Emphasis | Size/weight/space | Color-only, ALL CAPS everywhere |
| Motion | Purposeful, ≤300ms | Bouncy decoration, slow fades |
| States | Empty/loading/error/data | Happy path only |

## Q. Glossary (shared vocabulary)

- **Affordance** — a visual cue that signals how to use something (a button *looks* pressable).
- **Hierarchy** — the ordering of importance via size, weight, color, position, space.
- **Measure** — line length of text (target 60–75 characters).
- **Modular scale** — sizes derived from a ratio (1.2/1.25/1.333) rather than picked ad hoc.
- **Rhythm** — repeated, consistent spacing/sizing that makes a layout feel composed.
- **Whitespace / negative space** — empty area; a design tool, not wasted room.
- **Optical alignment** — aligning by how it *looks*, not just by pixel box edges.
- **Contrast ratio** — legibility measure of text vs background (AA: 4.5:1 body).
- **BAN** — "Big-Ass Number": one headline metric shown huge.
- **Chartjunk** — non-data ink that clutters a visualization.
- **Skeleton** — grey placeholder shapes shown while content loads.
- **Focus ring** — the visible outline on keyboard-focused elements (never remove — restyle).
- **Slop** — thoughtless generated-UI tells (see §3); the thing this skill exists to prevent.

## R. Reference cheat sheet (memorize)

```
FONTS 1–3   ·   ACCENTS 0–2   ·   BG TONES 1
SPACE 4·8·12·16·24·32·48·64·96
TYPE 12·14·16·20·25·31·39·49  (×1.25)
MEASURE 60–75ch   ·   TOUCH ≥44px   ·   BODY CONTRAST ≥4.5:1
RADIUS one value   ·   SHADOW one philosophy
MOTION 150ms feedback / 250ms transition, ease-out in
STATES empty·loading·error·data for every data view
SLIDES ≥24px   ·   PRINT ≥12pt
```
