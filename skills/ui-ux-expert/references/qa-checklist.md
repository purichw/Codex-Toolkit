# Screenshot-Based Design QA Checklist

> For Codex to run against a rendered artifact. Take screenshots, then verify each
> item **from the image** (and a few from the DOM/computed styles where noted).
> Source of truth: latest user-approved reference/brand first, existing product
> second, skill defaults last. `tokens.css` is fallback only. Scope REQ checks
> to the touched surface and applicable product contract, not every possible state.
> Legend: **[img]** = judge from screenshot · **[dom]** = check computed style/markup ·
> **REQ** = must pass to ship · **OPT** = polish, note but don't block.

## Capture protocol (do this first)

1. Render the intended state using bounded, state-specific readiness checks.
   For browser ready-state captures, await `document.fonts.ready`, relevant visible
   images/logo decode with nonzero natural dimensions, and expected data/controls.
   Use equivalent asset/data readiness signals in other rendering environments.
   A visible shell or vanished spinner alone does not prove readiness. Arbitrary
   sleeps or global network-idle are not substitutes for those conditions.
2. Screenshot affected viewports; 1280×800 and 390×844 are examples, not mandatory
   dimensions. Full-page fidelity needs desktop and mobile plus tablet when in scope.
3. Use a gallery only when it exists and relevant shared states changed.
4. For data-bearing views, capture or inspect ideal, empty, loading, error, and
   partial/edge states when the app exposes them.
5. For interactive elements, capture **hover** and **focus-visible** states
   (`:focus-visible` via keyboard/`.focus()`), not just default.
6. Inspect hierarchy independently of color; create a grayscale copy only when
   it adds useful evidence, not by habit for every small edit.
7. For full-site responsive QA, also follow `responsive-web-design.md`: resize
   continuously from about 320px, test short landscape/tall mobile constraints,
   and cover relevant browser engines/platforms.
8. For deferred media, scroll or activate the relevant state before classifying
   a missing source as broken. Exercise the controls visible at that viewport;
   do not force-click hidden desktop controls to claim a mobile journey passed.
9. Set and verify the intended scroll position after interaction; browser automation
   can scroll a control into view and crop the heading. Record route/artifact,
   viewport, build/data state, and scroll context as relevant. Open the image and
   inspect it; label intentional loading/error captures instead of presenting
   unfinished content as the ready-state result.

## Failed-Check Triage

When a check fails, distinguish test readiness/selector failure from a real
request, rendering, or product-state failure before changing the harness. Keep
the failed-state screenshot and relevant bounded console/network diagnostics;
exclude credentials, tokens, and private payloads from shared evidence.

Correct an early assertion by waiting for the actual contract without weakening
the expected result. A visible error after the readiness deadline is application
evidence, not permission to extend timeouts or retry until green. Use bounded
reproduction or an isolated/read-only failure-and-retry check when recovery is the
touched risk; never induce failures in live writes. Record the failed run and
subsequent recovery separately. Later success does not establish a root cause or
prove the original defect fixed. Stop once the touched risk is covered, disclose
unresolved failures and skipped checks, and expand only when evidence warrants it.

---

## A. Renders & runs — REQ (blockers)

- [ ] **[dom]** Console is clean: no errors, no failed asset/font requests.
- [ ] **[img]** Nothing overlaps, clips, or overflows its container.
- [ ] **[img]** No horizontal scrollbar at 390px (except intentional `overflow-x` wrappers).
- [ ] **[img]** No visible placeholder tokens leaked as text (`var(--…)`, `undefined`, `NaN`, `{{ }}`).
- [ ] **[img]** No lorem ipsum or filler in a final deliverable.
- [ ] **[img]** The primary task on each screen is obvious within ~3 seconds.

## B. Hierarchy & type — REQ

- [ ] **[img·grayscale]** Primary element is obvious with color removed; hierarchy survives grayscale.
- [ ] **[dom]** Fonts/weights match the product's type roles and required scripts.
- [ ] **[dom]** Font sizes follow the local type system, not a forced generic scale.
- [ ] **[img]** Reading measure suits the script and component; 60-75ch is a
  prose starting point, not a target for compact cards or Thai UI labels.
- [ ] **[img]** Alignment follows the reference and reading task: centered
  tile/icon groups when called for, readable prose rather than blanket centering.

## C. Color & depth — REQ

- [ ] **[img]** Palette and contrasting section bands follow the approved reference;
  generic accent-count/background defaults must not erase its visual language.
- [ ] **[dom]** No `linear-gradient` on large backgrounds or text; no colored (non-neutral) `box-shadow`.
- [ ] **[dom]** Body text contrast ≥4.5:1; large text/UI ≥3:1. Check text-on-accent and accent-on-white specifically.
- [ ] **[img]** Separation uses whitespace → border → single shadow, not all three stacked.
- [ ] **[dom]** Radius and depth follow coherent component roles in the local system.

## D. Spacing & alignment — REQ

- [ ] **[dom]** Margins/paddings/gaps resolve to scale values (`--s1…--s9`); flag ad-hoc px.
- [ ] **[img]** Edges share axes — elements align to a grid; no 1px drift.
- [ ] **[img]** Sibling groups use consistent `gap`, not uneven whitespace.
- [ ] **[img]** Content has room to breathe; nothing cramped against edges.

## E. Component states & UX behavior — REQ (gallery/interactive work)

- [ ] **[img]** default · hover · focus-visible · active · disabled all present and distinct for every interactive component.
- [ ] **[img]** Focus ring visible on keyboard focus (never removed).
- [ ] **[img]** Inputs show error state (border + message) and loading/skeleton where they fetch.
- [ ] **[img]** Data views cover ideal / empty / loading / error / partial-edge, not just populated.
- [ ] **[img]** Empty states explain what belongs there and offer a next step.
- [ ] **[img]** Error states explain what happened and provide a way out; no dead ends.
- [ ] **[img|dom]** Feedback appears immediately after input (press/selected/loading/inline response).
- [ ] **[img|dom]** Control type matches the choice: radio/segmented for one-of-few, toggle for instant on/off, checkbox for multi-select, menu/select for many.
- [ ] **[img]** Advanced or rare options are progressively disclosed, not dumped into the primary path.
- [ ] **[dom]** When async form data is touched, late responses preserve unsaved
  edits, focus, and open controls; verify with a deliberately delayed response.
- [ ] **[dom]** When CMS fields are touched, editor/save/public rendering evidence
  comes from the actual supported contract, not a richer mock payload. See
  [product-redesign-contracts.md](product-redesign-contracts.md) for the scoped matrix.
- [ ] **[img|dom]** Dangerous actions are confirmed, undoable, or visually separated from safe actions.
- [ ] **[img]** Disabled elements are dimmed (~.5) and readable, `not-allowed` cursor.

## F. Responsive — REQ

- [ ] **[img]** Multi-column desktop layouts collapse sensibly at 390px.
- [ ] **[img]** Mobile grouping follows the reference and real tasks; compact
  multi-column cards/actions remain grouped when readable and operable. Do not
  turn every item into a tall full-width stack by default.
- [ ] **[img|dom]** Tablet layout and touch interaction are verified separately;
  desktop-like columns must not imply hover-only controls.
- [ ] **[img]** Touch targets ≥44px on the mobile shot.
- [ ] **[img]** No text truncated/clipped; tables wrapped or restacked.
- [ ] **[dom]** Correct viewport meta; no `maximum-scale=1` or `user-scalable=no`.
- [ ] **[img|dom]** No page-level horizontal overflow at any width checked.
- [ ] **[dom]** Full-height mobile sections avoid raw `100vh` when `svh`/`dvh` is needed.
- [ ] **[img|dom]** iOS safe areas, mobile keyboard behavior, and hover alternatives are handled when relevant.
- [ ] **[img|dom]** When shell navigation is touched, collapsed active/focus states
  stay inside the rail and the final menu item remains reachable at short heights;
  sticky actions do not cover it.
- [ ] **[dom]** Responsive images reserve space and use suitable `srcset`/`sizes`/fallbacks when image-heavy.

## G. Anti-slop scan — REQ

- [ ] **[img]** No gradient hero, no emoji-as-UI, no left-border accent card.
- [ ] **[img]** No fabricated data/charts/logos/testimonials (unknowns are labeled placeholders).
- [ ] **[img]** No 3+ competing primary buttons; exactly one primary per view.
- [ ] Cross-reference each `anti-slop-examples.md` detection tell — zero hits.

## H. Accessibility floor — REQ

- [ ] **[dom]** Semantic elements (`button`/`nav`/`h1–h3` in order/`label`+`for`/`alt`).
- [ ] **[dom]** No meaning by color alone (status has text/icon too).
- [ ] **[dom]** `prefers-reduced-motion` respected for anything animated.
- [ ] **[dom]** Icon-only controls have both accessible names and visible hover/focus affordance.

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
