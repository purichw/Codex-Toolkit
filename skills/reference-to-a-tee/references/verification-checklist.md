# Verification Checklist

Select checks by fidelity, effort, reference mode, and requested scope using
[operating-guide.md](operating-guide.md). This is not an always-run checklist:
fast repairs use the requested-property check, current contextual comparison,
and regression evidence for touched risk. No complete ledger/table, all-controls
tour, or full-page/multi-viewport captures are required solely by the skill name.
Broad reconstruction and risk-bearing changes retain the fuller checks below.
Missing source capabilities in image-only mode are evidence limits, not failed
HTML checks. Uninspected relevant evidence and missing requested behavior remain blockers.

## Reference Evidence

- Identify fidelity, allowed adaptations, effort, input mode, source/version,
  and compared region/state. Use hashes for reuse/version tracking or when the
  handoff requires them, not as routine paperwork for a fresh direct comparison.
- HTML: inspect actual rendered states, relevant source/dependencies, computed
  geometry, controls, and source breakpoints. A generated manifest is a seed.
- Image-only: open originals; record pixel dimensions, crop, content region,
  scale/DPR/viewport knowledge, and confidence. Keep unknown metadata explicit.
- Mixed: document which artifact wins for each conflicting surface or state.
  Do not replace image-led visual authority with old source measurements.
- Reject stale versions, wrong routes, unintended login screens, loading shells,
  missing target selectors, and broken reference setup as parity evidence.
- Cover all requested properties/surfaces and relevant supplied states. Include
  lower-page content for page-level claims. A short note is enough for a narrow
  repair; distinguish facts, inferred CSS, and unknown behavior without inventing
  unrelated inventory work.

## Implementation Provenance

- Record source state including uncommitted changes, build/version when relevant,
  requested and final URL, route/state/data/auth, viewport, and hydration state.
- Confirm the tested artifact contains current changed source. Refresh affected
  screenshots after relevant edits, dependency changes, or reference updates.
- Reject captures of deployment protection, unintended login, generic shells,
  404s, stale service-worker builds, or pre-hydration placeholders.
- Keep prior visual baselines separate from current accepted reference evidence.

## Component Parity

For broad work, several measured properties, or a formal audit, maintain a table.
For a one-property repair, record the useful value/tolerance or observation with
its current comparison instead:

```text
component | file/version/state | evidence type | viewport/crop/scale |
reference value + units | implementation value + units | delta/tolerance | status
```

Use `matched`, `behavior exception`, `visual exception`, or `not done` for observed
scope. Note unknown source properties separately from mismatches; a short note
suffices for one fix. A visible mismatch is not an unknown. Set tolerances before judging the result.
Exact and faithful-adaptation claims stay distinct. An authorized adaptation
passes only within its named flexibility; it is not measured exact parity.

Check affected hierarchy, layout, bounds, alignment, wrapping, spacing, density,
count/order, type metrics, line wraps, colors, borders/radii/shadows, icon baseline,
media frames/crops, and visible selected/disabled/overlay states. Verify every
detail the user named. Stable dimensions must survive hover, loading, and content.

HTML uses authoritative source/computed values. Image-only uses calibrated image
measurements and implementation screenshots/geometry. Do not claim exact source
CSS, font identity, or layout algorithms from pixels. Verify OCR-derived text
visually, including numbers and non-Latin labels.

## Page Rhythm And Coverage

For broad pages, inspect beyond the first viewport: major section offsets,
repeated items, media, rails, and footer. Use comparable full-page views or
top/middle/bottom evidence through `$snapshot`. A crop supports only that region.

With runnable source, measure document width/height, section bounds, scroll
milestones, sticky start/end, and nested scroll behavior where relevant. With
images, compare visible order and distances; full-image height may describe a
document rather than a viewport. Do not invent source scrollY or sticky timing.
Verify the implementation's actual scroll behavior separately.

## Interactions And Product Protection

Exercise affected product controls to representative terminal states, not just
their initial appearance. For executable references, compare observable state
transitions. For image-only references, follow product requirements and document
inferred behavior; do not claim the reference interaction was tested.

Cover applicable navigation, tab/filter selection, menus, modal open/close,
save/submit, success/failure, loading/empty/denied, reset/retry, persistence,
keyboard/focus, and touch. Test allow/deny where permissions change. Confirm
stored and reloaded state when an action writes data.

For tours or guided flows, verify all requested steps, live targets after route
changes, skip/back/next/done, and dismissal without a lingering click-blocking
overlay. For deep links or search, verify destination, URL, selected target,
visibility/highlight, back/forward, and reload.

For nested lists/rails, record the selector, visible and total count/page size,
scroll/client heights, first/last reachability, manual versus automatic scroll,
and sticky-action occlusion. Guard preserved/hybrid contracts with focused tests
or equivalent recorded checks; do not rewrite acceptance checks to hide lost UX.

## Responsive Evidence

Use supplied image viewport sizes when known and authoritative source breakpoints
when available. Calibrate image dimensions before treating them as CSS viewports.
Unknown viewports remain assumptions. Multiple images show arrangements, not
necessarily exact breakpoint values.

For requested responsive work, test supplied layouts plus the smallest useful
intermediate or edge widths that could expose wrapping/overflow. Reference-free
mobile is an adaptation, verified as product QA rather than source parity.
Use `$mobile-web-qa` for broader responsive risk. Useful defaults when no project
matrix exists include `390x844` phone, `820x1180` tablet, and `1280x800` desktop;
add narrow `375x667` or wide `430x932` phone coverage when the changed layout needs it.

At required widths, check overflow, clipping, long labels, menus/overlays,
keyboard-sensitive forms, touch targets, safe areas, scrolled content, and
first/last items in internal scroll regions. A desktop match does not establish
mobile parity or Safari support.

## Assets And Runtime

- Verify supplied/product media, fonts, icons, crop, transparency, resolution,
  fallback, and loading state. Label unavailable originals or substitutions.
- Check local and CMS-backed assets, console/page errors, failed network requests,
  and 4xx/5xx media responses after relevant data hydration.
- Confirm selectors hit intended components; an empty result is not a pass.
- Set up auth, fixtures, feature flags, or emulators needed to inspect the actual
  changed screen; a login gate does not verify an authenticated surface.
- Use available browser tooling. Use WebKit/real Safari for Safari-specific
  claims; document untested browsers and environments.
- Apply `$production-asset-smoke` after authorized deployment when media changed.

## Closeout

For fast work briefly report what changed, the reference and compared region,
relevant checks/snapshot, and material uncertainty. For broader work include
fidelity, effort, mode, inspected references, compared surfaces, measured deltas/tolerances,
snapshot evidence, viewport/browser coverage, exercised interactions, tests,
assumptions, accepted differences, missing assets, and outstanding blockers.
Do not conflate visual match with functional correctness or evidence limitations
with completed unobserved parity. Apply [release-gate.md](release-gate.md).
