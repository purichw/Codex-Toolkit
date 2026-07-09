# Verification Checklist

Use this checklist for every Claude-to-a-tee task. Mark an item not applicable
only after inspecting both the reference and target surface.

## Reference Evidence

- Identify the exact offline HTML and all supporting CSS, JavaScript, fonts,
  icons, images, audio, and handoff files.
- Render the reference rather than relying only on source or screenshots.
- Exercise tabs, menus, forms, dialogs, loading, empty, disabled, selected,
  hover, focus, error, and success states that exist in the reference.
- Exercise every mapped product interaction to its representative end state,
  including persistence after reload when the interaction writes state.
- Record source breakpoints and capture baseline screenshots.
- Note behavior that the reference mocks but the target implements for real.
- Reject evidence captured from the wrong route, login/account screens, loading
  placeholders, or selector misses; fix setup and recapture.

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

## Behavior Protection

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

## Browser Evidence

- Use the in-app browser to inspect the rendered offline source.
- Use agent-browser to verify the implementation and capture screenshots.
- Use browser computed styles, not only screenshots, for values that are present
  in Claude source or that the user specifically called out.
- Check runtime console errors and failed network/asset requests.
- Confirm selector queries in automation are hitting the intended product
  components; empty selector results are a failed audit, not a pass.
- Use WebKit or real Safari for Safari-specific claims when available.
- Treat Chrome on iOS as WebKit behavior, not desktop Chromium behavior.
- Report any browser or device that could not be tested.
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
