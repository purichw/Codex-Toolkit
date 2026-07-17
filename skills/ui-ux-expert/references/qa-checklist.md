# Screenshot-Based Design QA Checklist

> For Codex to run against a rendered artifact. Take screenshots, then verify each
> item **from the image** (and a few from the DOM/computed styles where noted).
> Source of truth: `tokens.css`, `components.md`, `layouts.md`, `anti-slop-examples.md`.
> Legend: **[img]** = judge from screenshot · **[dom]** = check computed style/markup ·
> **REQ** = must pass to ship · **OPT** = polish, note but don't block.

## Capture protocol (do this first)

1. Render the artifact; wait for fonts + async content to settle.
2. Screenshot at **desktop 1280×800** and **mobile 390×844** (**REQ** both).
3. For component work, also screenshot the gallery page showing every state.
4. For interactive elements, capture **hover** and **focus-visible** states
   (`:focus-visible` via keyboard/`.focus()`), not just default.
5. Save a **grayscale** copy of the desktop shot for the hierarchy check.

---

## A. Renders & runs — REQ (blockers)

- [ ] **[dom]** Console is clean: no errors, no failed asset/font requests.
- [ ] **[img]** Nothing overlaps, clips, or overflows its container.
- [ ] **[img]** No horizontal scrollbar at 390px (except intentional `overflow-x` wrappers).
- [ ] **[img]** No visible placeholder tokens leaked as text (`var(--…)`, `undefined`, `NaN`, `{{ }}`).
- [ ] **[img]** No lorem ipsum or filler in a final deliverable.

## B. Hierarchy & type — REQ

- [ ] **[img·grayscale]** Primary element is obvious with color removed; hierarchy survives grayscale.
- [ ] **[dom]** ≤3 font families; ≤ ~2 weights in use.
- [ ] **[dom]** All `font-size` values are on the scale (`--t-xs…--t-4xl`); flag any orphan px.
- [ ] **[img]** Body measure looks ~60–75ch (not full-window-width lines).
- [ ] **[img]** Headings not centered across wide blocks; paragraphs left-aligned.

## C. Color & depth — REQ

- [ ] **[img]** ≤2 accent hues total; one background tone.
- [ ] **[dom]** No `linear-gradient` on large backgrounds or text; no colored (non-neutral) `box-shadow`.
- [ ] **[dom]** Body text contrast ≥4.5:1; large text/UI ≥3:1. Check text-on-accent and accent-on-white specifically.
- [ ] **[img]** Separation uses whitespace → border → single shadow, not all three stacked.
- [ ] **[dom]** One radius value and one shadow philosophy across components (pill only on chips/toggles).

## D. Spacing & alignment — REQ

- [ ] **[dom]** Margins/paddings/gaps resolve to scale values (`--s1…--s9`); flag ad-hoc px.
- [ ] **[img]** Edges share axes — elements align to a grid; no 1px drift.
- [ ] **[img]** Sibling groups use consistent `gap`, not uneven whitespace.
- [ ] **[img]** Content has room to breathe; nothing cramped against edges.

## E. Component states — REQ (gallery/interactive work)

- [ ] **[img]** default · hover · focus-visible · active · disabled all present and distinct for every interactive component.
- [ ] **[img]** Focus ring visible on keyboard focus (never removed).
- [ ] **[img]** Inputs show error state (border + message) and loading/skeleton where they fetch.
- [ ] **[img]** Data views show empty / loading / error, not just populated.
- [ ] **[img]** Disabled elements are dimmed (~.5) and readable, `not-allowed` cursor.

## F. Responsive — REQ

- [ ] **[img]** Multi-column desktop layouts collapse sensibly at 390px.
- [ ] **[img]** Sidebar → drawer/tabs; action rows → full-width stacked on mobile.
- [ ] **[img]** Touch targets ≥44px on the mobile shot.
- [ ] **[img]** No text truncated/clipped; tables wrapped or restacked.

## G. Anti-slop scan — REQ

- [ ] **[img]** No gradient hero, no emoji-as-UI, no left-border accent card.
- [ ] **[img]** No fabricated data/charts/logos/testimonials (unknowns are labeled placeholders).
- [ ] **[img]** No 3+ competing primary buttons; exactly one primary per view.
- [ ] Cross-reference each `anti-slop-examples.md` detection tell — zero hits.

## H. Accessibility floor — REQ

- [ ] **[dom]** Semantic elements (`button`/`nav`/`h1–h3` in order/`label`+`for`/`alt`).
- [ ] **[dom]** No meaning by color alone (status has text/icon too).
- [ ] **[dom]** `prefers-reduced-motion` respected for anything animated.

## I. Motion & polish — OPT (note, don't block)

- [ ] Transitions ≤ ~300ms, `ease-out` on entrances, `transform`/`opacity` only.
- [ ] Hover/active feedback feels tactile, not bouncy.
- [ ] Optical alignment refinements; skeleton shapes match real content boxes.

---

## Verdict format Codex should emit

```
QA RESULT: PASS | FAIL
Blockers (REQ failures): <list with section id + what the screenshot shows, or "none">
Polish notes (OPT): <list or "none">
Unknowns encountered: <placeholders left / questions for the user>
Screens checked: 1280×800, 390×844 [+ gallery/hover/focus/grayscale as applicable]
```
- **REQ** any single REQ failure → overall **FAIL**; fix and re-screenshot.
- **REQ** never claim PASS from imagination — every checked box must trace to a captured image or a DOM read.
- **?** If a check can't be evaluated (missing state, unrendered path), report it as an unknown, not a pass.
