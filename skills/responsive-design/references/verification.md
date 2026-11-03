# Responsive Verification

## Scope Before Matrix Size

| Change | Minimum useful evidence | Expand when |
| --- | --- | --- |
| One-control/spacing repair | Failing width/state, changed boundary if any, previously good source sanity check | Shared owner, new defect, or another range affected |
| Component or route | Changed ranges and B-1/B/B+1, representative consumers/content states, focused interactions | Shared layout or data/state contract changes |
| Full responsive page/system | Reference viewport, narrow/medium/wide, 320 CSS px, intermediate widths, short landscape, wide-screen cap; target engines and key flows | Required product support or observed failure demands more |

390 / 820 / 1440 CSS px are useful starting anchors, not fixed design breakpoints
or universal device coverage. A 1920px view can expose unbounded wide composition.
Use the product's actual requirements and layout pressure. A fix at one width is
not a full-site claim. Stop only after all current deliverables have proportionate
evidence; name checks intentionally skipped instead of running them by habit.

For each observed defect record route/state/viewport, evidence, likely cause,
owner fix and matched after evidence. Separate functionality failures from
composition issues. Test with actual fonts, images and representative Thai/English
content. Wait for known app-ready/data conditions using the project harness;
generic page load or a timed sleep does not establish readiness.

## Visual And Interaction Evidence

Use `$snapshot` automatically and inspect its actual output. Match route, data,
state, CSS viewport and source/build for comparisons. Source/reference plus
before/after is useful when available; never invent a missing before. Whole-page
claims need whole-page evidence plus readable viewport crops where necessary.

Review hierarchy, line length, tablet grouping, card proportions, negative space,
primary action, image focal point, glyph clipping and overlaps. Then exercise
real controls in the same page: open navigation, enter form data, select filters,
open a dialog, resize across the changed threshold, and close it. Assert data,
explicit view choice and logical focus survive. Use only states that exist in
scope; do not invent features to satisfy a generic checklist.

Also inspect relevant loading/empty/error states, long content, local scroll
access, short-height layouts, sticky/fixed controls, keyboard and reduced motion.
Screenshots alone cannot establish these behaviors. Native keyboard/safe-area
claims need appropriate device/platform evidence; a desktop resize cannot prove
them. Playwright WebKit is not identical to physical-device Safari.

## Optional Initial-State Collector

Use [responsive-audit.mjs](../scripts/responsive-audit.mjs) when repeated width
measurements add value. Prefer an existing project harness if it already handles
authentication, fixtures, readiness and assertions. Do not install or alter
project dependencies merely to use this optional helper; use an available runtime
or obtain any required authorization first.

Run from the target project so its installed `playwright` or `@playwright/test`
can resolve. `SKILL_DIR` below means the absolute installed skill directory.
Always use a new output directory; the helper refuses an existing path so prior
reports and screenshots cannot be overwritten.

```sh
node "$SKILL_DIR/scripts/responsive-audit.mjs" \
  --url http://127.0.0.1:3000/example \
  --out ./artifacts/responsive/run-01 \
  --widths 390,820,1440 --screenshots 390,820,1440 \
  --breakpoints 640,960
```

Replace sample breakpoints with actual CSS-pixel thresholds, or omit them when
there are none. `--screenshots` adds its widths to the audit, so explicitly use
`--screenshots none` for measurement-only runs. `--height` covers short heights.
Optional `--sweep`, `--text-stress`, `--reduced-motion` and a separate
`--browser chromium|firefox|webkit` run should follow touched risk, not habit.
`--text-stress` adds four fixed widths and `--reduced-motion` adds three; they do
not capture screenshots automatically. Inspect required variants separately.

Existing tool runtimes may be selected without installing:

```sh
RESP_AUDIT_PLAYWRIGHT_MODULE=/absolute/path/to/playwright/index.mjs \
RESP_AUDIT_BROWSER_EXECUTABLE=/absolute/path/to/compatible-browser \
node "$SKILL_DIR/scripts/responsive-audit.mjs" --help
```

Use an executable compatible with the selected engine. Help itself checks only
CLI availability, not browser startup. For routine use, omit either environment
override when normal resolution works.

The collector opens fresh, unauthenticated desktop contexts at DPR 1 and captures
initial page states only. It does not reuse a personal browser profile, click
controls, or assert application-specific readiness. Use authorized URLs/fixtures
without secrets in query strings. Reports include URLs, console/network messages
and page content screenshots: keep private evidence local and review before any
sharing. Running this collector does not authorize production data mutations.

| Result | Meaning |
| --- | --- |
| Exit 0 | Its measured assertions passed; visual/manual and app-specific checks still required. |
| Exit 1 | Document overflow (>1px tolerance), page JavaScript error, navigation failure or requested capture failed. |
| Exit 2 | Invalid options, setup/browser startup or output-writing problem; not a UI pass. |

`report.json` records engine/version, viewport, options, metrics and runtime
events; `report.md` summarizes them. Small targets, clipping, edge candidates,
local scrollers, failed images/fonts and console/network events need review;
they are not all automatic failures. Candidate lists are capped at 30/category.
An essential local table scroller is not a document-overflow failure. Conversely,
global overflow hiding can conceal defects despite a successful exit code.
Full-page captures disable animations only during capture, not during measurement.

## Accessibility And Claim Boundaries

- For vertically scrolling content, WCAG reflow considers an equivalent width
  of 320 CSS px; essential two-dimensional content has exceptions. A 1280 CSS-px
  content viewport at 400% zoom is a common equivalent, not a required device
  model. Inspect loss of information/function as well as document width.
  [W3C: Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)
- Text must be resizable up to 200% without loss of content/function, with the
  criterion's stated exceptions. Test supported browser/text scaling. Authoring
  `html { font-size: 200% }` is a stress probe, not browser zoom and not a doubling
  of every text size. DPR changes pixel density, not zoom.
  [W3C: Resize Text](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html)
- WCAG 2.2 AA target-size minimum is 24 by 24 CSS px or an applicable exception,
  including spacing. A 44-48px touch-comfort target is a design preference, not
  a blanket AA minimum. The collector's below-44px candidates are advisory.
  [W3C: Target Size (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)

Check semantics, focus order/occlusion, contrast and assistive technology where
required; this helper cannot certify WCAG. For component-query mechanics see
[MDN: Container Queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries).

## Maintaining The Helper

Run syntax and behavioral fixture tests when changing the collector. Browser
tests need the same Playwright/browser prerequisites and respect the runtime
environment overrides above. They serve loopback fixtures, never a production app.

```sh
node --check "$SKILL_DIR/scripts/responsive-audit.mjs"
node --test "$SKILL_DIR/scripts/responsive-audit.test.mjs"
```

Tests cover CLI rejection, initial-state metrics/screenshots and boundaries,
local-scroll classification, runtime/HTTP failures, hidden-overflow warnings,
stress labels and output preservation. They retain their own temporary evidence
directory and print its location. Passing them proves helper behavior on those
fixtures, not that the skill makes every implementation beautiful.
