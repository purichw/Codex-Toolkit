---
name: snapshot
description: Capture, crop, inspect, and present UI screenshots with enough visual context for review. Use when the user asks for a snapshot, screenshot, visual proof, before/after image, UI comparison, crop, viewport capture, production smoke evidence, or complains that a screenshot is too tight, missing context, hard to judge, or not showing the surrounding layout.
---

# Snapshot

Use this skill whenever visual evidence is part of the answer. A snapshot should
help the user understand the UI, not merely prove that a selector exists.

Use `$mobile-web-qa` for responsive/mobile audit and `$claude-to-a-tee` for
reference-vs-implementation parity. Use `$release-gate` when screenshots are
part of commit/deploy evidence.

## Core Rule

Do not crop exactly to the target element when the user needs to judge layout,
alignment, spacing, hierarchy, or visual quality. Include surrounding context by
default.

Tight crops are allowed only when inspecting a pixel-level detail such as a
border thickness, icon shape, crop edge, or text overlap. When sending a tight
crop, also send or mention a wider snapshot unless the user explicitly asked
for only the tiny detail.

## Efficient Capture

Use `$efficient-execution` when a visual task starts producing too many images.
For a narrow change, capture one wide/context shot for the relevant state and
add one tight crop only if it clarifies the decision. For before/after work,
capture matched pairs after the fix stabilizes instead of taking a full set on
every edit.

Reuse a screenshot only when URL or local route, build/source, viewport, auth
state, data state, scroll position, and overlay state still match.

## Framing Defaults

Choose the smallest frame that still explains the issue:

- **Layout or alignment:** capture the full viewport or a wide section that
  includes the parent container, neighboring columns, and nearby headings.
- **Sidebar, card, panel, or table row:** include the whole component plus at
  least one neighboring area or parent edge.
- **Small control, line, icon, or label:** crop with breathing room around it,
  normally 80-160px on each relevant side when available.
- **Responsive issue:** capture at the relevant viewport and include enough
  vertical context to see what comes before and after.
- **Before/after or reference/app comparison:** use matching viewport sizes and
  comparable framing.
- **Production smoke:** capture the deployed URL with a cache buster when
  relevant, not only the local build.

Avoid screenshots that start or end exactly on the visual border being discussed
unless the point is a microscopic edge inspection.

## Capture Workflow

1. Identify what the screenshot must prove: geometry, style, interaction state,
   responsive behavior, deployed artifact, or visual comparison.
2. Render the actual state first. Navigate, scroll, click, wait for content, and
   close unrelated overlays before capture.
3. Capture a wide/context snapshot. Add a tighter crop only if it clarifies a
   specific detail.
4. For UI changes, record key computed values when useful: x/y/w/h, font size,
   line height, border width/color, overflow, visible count, or console errors.
5. Save screenshots with descriptive filenames that include route/component and
   state, for example:
   `/tmp/notenwert-dresden-life-sidebar-after-wide.png`.
6. In the final answer, embed at least one useful image with an absolute path:
   `![label](/absolute/path.png)`.

## Comparison Workflow

For before/after, reference/app, or local/production comparison:

1. Use matching viewport size, route, scroll position, auth state, data state,
   and browser when possible.
2. Capture a wide context shot for each side before any tight crops.
3. Name files so pairs sort together, such as
   `/tmp/checkout-card-before-390x844.png` and
   `/tmp/checkout-card-after-390x844.png`.
4. For several screenshots, make or present a short contact sheet only when it
   helps comparison; otherwise embed the highest-signal images.
5. Record mismatched conditions instead of implying the screenshots are directly
   comparable.

## Crop Construction

When building a crop from an element rectangle:

- Expand the clip beyond the element bounds before taking the screenshot.
- Prefer including parent edges and adjacent content over perfectly centered
  framing.
- Clamp the crop to the viewport/page bounds.
- If the element is near an edge and padding cannot be added, use a wider
  viewport or full-page screenshot instead.
- If the issue concerns a vertical sidebar or long list, include enough height
  to show multiple repeated items and section breaks.

Example Playwright clip pattern:

```js
const box = await locator.boundingBox();
const padX = 120;
const padY = 80;
await page.screenshot({
  path: '/tmp/example-wide-context.png',
  clip: {
    x: Math.max(0, box.x - padX),
    y: Math.max(0, box.y - padY),
    width: Math.min(viewport.width - Math.max(0, box.x - padX), box.width + padX * 2),
    height: box.height + padY * 2
  }
});
```

Adjust the padding to the UI scale; 80-160px is a starting point, not a law.

## Presentation

Keep the final visual report compact:

- State what was captured and from where: local app, reference HTML, or
  production URL.
- Include the screenshot inline.
- Include measured values only when they answer the user's question.
- If a screenshot is intentionally tight, say that and provide a wider context
  image when useful.

## Quality Gate

Before claiming a visual change is done, check:

- The screenshot shows enough context for a human to understand the issue.
- The state in the screenshot matches the route/device/reference being discussed.
- No crop hides the very edge, neighbor, label, or parent needed for judgment.
- The file path is absolute and renderable in the Codex app.
- For UI changes, at least one current snapshot is included in the closeout.

A screenshot is invalid evidence when it shows the wrong route, stale build,
loading shell, hidden overlay, wrong viewport, unauthenticated gate, pre-hydrated
state, or a crop that hides the layout relationship being judged.
