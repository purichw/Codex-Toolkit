# Verification Checklist

Use this checklist for every Claude-to-a-tee task. Mark an item not applicable
only after inspecting both the reference and target surface.

## Reference Evidence

- Identify the exact offline HTML and all supporting CSS, JavaScript, fonts,
  icons, images, audio, and handoff files.
- Record the reference filename and a stable hash or modification identity.
- Use `scripts/extract_reference.py` output as a seed for inventory and parity
  tables when available; do not count it as rendered verification by itself.
- Render the reference rather than relying only on source or screenshots.
- From the initial screen, navigate every reachable page/route/screen and click
  every visible control; record static or no-op Claude outcomes explicitly.
- Treat user-supplied screenshots as authoritative evidence for intended
  route/state/viewport, especially when the HTML contains multiple pages,
  states, or responsive branches.
- Exercise tabs, menus, forms, dialogs, loading, empty, disabled, selected,
  hover, focus, error, and success states that exist in the reference.
- Exercise every mapped product interaction to its representative end state,
  including persistence after reload when the interaction writes state.
- Record source breakpoints and capture baseline screenshots.
- Note behavior that the reference mocks but the target implements for real.
- Produce the pre-implementation decision ledger before edits that could replace
  current product UX. For each component, state what follows Claude, what
  preserves product UX, what is hybrid, why, verification, and risk.
- Reject evidence captured from the wrong route, login/account screens, loading
  placeholders, or selector misses; fix setup and recapture.

## Interaction Depth Requirement

Do not treat a visual match of the first screen as sufficient. For every
reachable control in the reference and mapped product surface, click or operate
it until it reaches its terminal or representative states. This includes:

- every tab, route, drawer, dropdown, segmented control, filter, jump list, and
  disabled or locked navigation item;
- every reveal/hide, play/stop/replay audio, mark complete, reset, retry,
  practice-again, got-it, answer, review, shuffle, next/previous, and submit
  action;
- every modal open, cancel, close, confirm, keyboard escape, and outside-click
  behavior;
- every success, failure, completed, empty, locked, disabled, selected,
  persisted-after-reload, and reset-after-completion state;
- every keyboard/touch path that the product claims to support.

When a control affects persisted product state, verify both the immediate UI
state and the stored/reloaded state. When the reference has separate visual
completion and product-earned completion semantics, test both paths rather than
collapsing them into one.

For onboarding tours, coach marks, or spotlight overlays, verify the full step
sequence rather than only the first overlay. Each step must measure the intended
live target after any route/tab/screen switch, keep the target visually
spotlit, avoid fighting manual scroll, support skip/back/next/done and keyboard
escape, and remain usable at every required mobile, tablet, and desktop
breakpoint. Also verify the rest of the product after the tour is dismissed:
the overlay/backdrop must no longer intercept clicks, search results and
navigation targets must be clickable, and first-run onboarding state must not be
mistaken for a broken page during release smoke tests.

For tabbed learning products, verify navigation from every entry point, not just
the top tab strip. This includes overview path rows, next/previous footers,
dropdown/jump menus, locked tabs, deep links, browser back/forward, and reload.
After each navigation, confirm the URL, active tab, scroll position, completion
mark, and persisted progress agree with the product rules.

For search or deep-linkable result cards, verify the full click-through contract:
the visible result metadata must name the real destination section, the click
must route to that section rather than a generic fallback, the URL must include
the target item state when supported, and the target word/phrase/sentence must
be visible or highlighted after navigation.

For embedded scroll regions such as card indexes, sidebars, carousels, and
jump-around lists, test the scroll container itself. Confirm the first and last
items are reachable and visible inside the container, and that automatic
active-item scrolling does not fight the learner's manual scroll.

If automation output shows the wrong page, an empty selector set, missing target
selectors, a login screen, or a route that silently failed to load, discard that
evidence and rerun the audit after fixing the setup. Never count screenshots or
metrics from an unauthenticated shell, placeholder route, or selector miss as
Claude-to-a-tee verification.

When the Claude reference has no animation or no real behavior, do not treat the
absence as permission to skip product behavior verification or to invent motion.
Record the static reference outcome, then verify the closest faithful product
behavior.

## Artifact Provenance

- Record target commit SHA and generated build/version identifier.
- Set the test base URL explicitly; label each run local, preview, or production.
- Record requested URL, final URL after redirects, route/hash, title, viewport,
  and the hydration marker used.
- Confirm the generated deploy artifact contains the changed source before
  testing or deployment.
- Reject captures from deployment-protection/login pages, a different host,
  generic shells, 404s, stale service-worker builds, or pre-hydration content.
- Keep legacy visual baselines separate from current Claude parity evidence;
  refresh stale baselines only after the new parity is approved.

## Screenshot State Frames

- When screenshots accompany offline HTML, build a screenshot ledger before
  implementation: file, route/screen, viewport if known, scroll position
  (top/full-page/mid-page/bottom), active state, visible overlays, and whether
  the screenshot supersedes older references.
- Use full-page screenshots to identify intended content order, missing
  route-specific components, sidebar/footer composition, list item counts, and
  where the page is expected to end.
- Use the HTML/CSS for exact values whenever available; use screenshots to
  choose the correct state to measure and to catch rendered intent that source
  inspection may hide.
- If a screenshot shows a component or state that the implementation lacks,
  classify it as `matched`, `behavior exception`, `visual exception`, or `not
  done` in the route component manifest. Do not silently ignore it because the
  first viewport or default route already matches.
- If screenshots and HTML disagree, inspect whether the screenshot is from a
  newer export, a different route, a scrolled state, an interaction state, or a
  stale baseline before choosing the source of truth.

## Component Geometry

- Build a measured parity table before release:
  `component | viewport | reference | implementation | delta | status`.
- Mark each row `matched`, `behavior exception`, `visual exception`, or
  `not done`; `not done` blocks completion.
- DOM/component hierarchy and layout mode
- width, height, min/max constraints, and aspect ratio
- padding, margin, row gap, column gap, and section rhythm
- alignment, wrapping, ordering, overflow, sticky/fixed positioning
- border width/style/color, radius, shadow, and background treatment
- icon dimensions, optical centering, baseline, and label spacing
- stable dimensions across hover, loading, labels, and dynamic content
- source value recorded before editing when the offline HTML/CSS exposes it
- implementation computed value checked after editing for every user-mentioned
  or high-risk geometry value
- Product behavior may differ only as a behavior exception. If the visual box,
  item count, order, spacing, copy set, or component state changes, record it as
  a visual exception and report it before release.

## Page Rhythm And Scroll Choreography

- Do not treat a matching first viewport as page parity. Measure the whole
  rendered experience.
- Record `documentElement.scrollHeight` and page-level `scrollWidth` for the
  reference and implementation at every required viewport.
- Measure the document-space `top` and `height` of major sections: masthead,
  nav, hero/chapter panels, sticky runways, first repeated grid/list, map or
  modal trigger, and footer.
- Record the scrollY where each major chapter/component first becomes visible
  and where it leaves the viewport. For sticky/scrub/peel systems, record the
  sticky start, sticky end, pinned duration, and first scrollY that reveals the
  next chapter.
- Capture at least three comparable scrolled states for long pages: top,
  mid-hero or mid-flow, and the first repeated grid/list. Add footer/bottom when
  the footer is part of the reference.
- If the implementation reaches a later chapter, register, feed, or footer
  hundreds of pixels earlier/later than Claude, mark it as `visual exception` or
  `not done` even when individual components look correct.
- Treat real product media, live data, cookie banners, or loading states as
  behavior only when they preserve Claude's rhythm. If they shorten/lengthen
  sections, change scroll milestones, or alter sticky timing, record a visual
  exception.

## Typography And Content

- exact available font asset and fallback order
- font size, weight, line height, letter spacing, casing, and alignment
- professional placeholder and helper copy
- localization and long-label wrapping
- no text clipping, overlap, or unexplained truncation
- computed font size/weight/line-height verified against Claude for affected
  headings, labels, buttons, stats, chips, and compact cards

## Controls And States

- button, input, pill, segmented control, tab, and close-button dimensions
- selected, unselected, disabled, pressed, focus, validation, and loading states
- touch targets without visually inflating Claude-compact components
- pointer, keyboard, touch, and screen-reader semantics
- modal focus, close behavior, confirmation flows, and scroll locking
- animation size, timing, easing, direction, and reduced-motion behavior

## Assets

- exact supplied image, icon, font, sound, and animation source
- crop, object position, transparency, scale, and resolution
- no accidental substitution with emoji, generic icons, or stale assets
- no custom approximation of a Claude icon/component when the reference
  primitive can be reused directly
- product-owned required assets are preserved even if the Claude reference uses
  placeholders, unless the user explicitly asks to remove or replace them
- no broken paths or assets that work only from the offline file location
- validate remote CMS/data-backed assets, not only repository files
- prefer repairing a broken remote asset at its source; if permissions block
  that, quarantine only the confirmed public asset, preserve admin visibility,
  add regression coverage, and disclose the remaining source record

## Behavior Protection

- Verify every `product UX preserved` and `hybrid` decision against its stated
  evidence. A current-product behavior cannot beat Claude unless the task,
  state, container, safety, accessibility, mobile, performance, test,
  documentation, or production evidence was actually checked.
- For existing sub-containers or nested scroll regions, verify the scroll
  container itself after implementation: first item reachable, last item
  reachable, manual scroll works, active-item auto-scroll does not fight manual
  scroll, keyboard/touch behavior works, sticky actions do not cover content,
  and page-level horizontal overflow remains absent.
- inventory event listeners, delegated selectors, IDs, data attributes, and tests
  before changing markup
- preserve auth, persistence, APIs, calculations, i18n, and accessibility
- test both success and failure paths for changed controls
- distinguish reference-only demo behavior from production behavior
- add focused regression coverage when the failure could recur silently

## Default Responsive Matrix

Use source-defined widths first. For mobile work, add these defaults when they
are not already covered:

| Target | Viewport |
| --- | --- |
| iPhone SE class | `375 x 667` |
| common iPhone | `390 x 844` or `393 x 852` |
| iPhone Pro class | `402 x 874` or `414 x 896` |
| iPhone Pro Max class | `430 x 932` |
| Android secondary | `412 x 915` |
| tablet | `820 x 1180` |
| desktop | `1280 x 800` or source-defined desktop size |

At each required width, check first viewport, scrolled content, menus/dialogs,
keyboard-sensitive forms, safe-area spacing, and horizontal overflow.
When a reference uses horizontally scrollable controls, confirm the control
itself scrolls while the page-level document width remains within the viewport.
If full-page screenshots of long mobile pages are slow or unstable, capture
viewport screenshots for key states and collect computed layout metrics across
all sizes; do not skip the size coverage.
Responsive verification must include interaction states at those sizes, not just
static screenshots. At minimum, open menus/dropdowns, switch tabs, press audio
buttons, complete/reset one activity where relevant, and inspect a scrolled
mid-page and bottom-page state on long screens.
For slide-overs, drawers, modals with internal scroll, sticky footers, and
right/left rails, verify the scroll container itself at top, middle, and bottom.
Record the first visible and last visible section names, whether lower sections
such as badges/streak/history are reachable, and whether sticky actions cover
content.

## Browser Evidence

- Use the in-app browser to inspect the rendered offline source.
- Use agent-browser to verify the implementation and capture screenshots.
- Use browser computed styles, not only screenshots, for values that are present
  in Claude source or that the user specifically called out.
- Check runtime console/page errors, failed requests, and 4xx/5xx asset responses
  after live data hydration.
- Confirm selector queries in automation are hitting the intended product
  components; empty selector results are a failed audit, not a pass.
- When authentication, emulators, seeded data, feature flags, or remote state are
  needed to see the real product screen, set them up before visual verification.
- Use WebKit or real Safari for Safari-specific claims when available.
- Treat Chrome on iOS as WebKit behavior, not desktop Chromium behavior.
- Report any browser or device that could not be tested.
- If a named browser skill is unavailable, use the closest browser automation
  and inspection capability, preserve the same evidence standard, and report the
  substitution.
- After deploy, run the same small parity smoke against the production URL; do
  not count a generic HTTP/functionality smoke as Claude-to-a-tee verification.

## Completion Report

Include:

- reference files inspected;
- measured parity table summary, including any `visual exception` rows;
- component-contract values extracted and verified, especially any
  user-mentioned sizes, spacing, layout modes, or asset treatments;
- routes and components changed;
- viewport and browser matrix verified;
- interactions and states exercised;
- tests run and results;
- intentional differences from Claude;
- remaining unverified coverage or known risk.
