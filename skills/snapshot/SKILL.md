---
name: snapshot
description: Capture, crop, inspect, and present UI screenshots with enough visual context, provenance, and contract evidence for review. Use when the user asks for a snapshot, screenshot, visual proof, Claude Design/reference-vs-development side-by-side comparison, before/after image, UI comparison, crop, viewport capture, production smoke evidence, interaction-state evidence, scroll/container proof, after UI implementation, after UI/UX skill work, or complains that a screenshot is too tight, missing context, hard to judge, or not showing the surrounding layout.
---

# Snapshot

Use this skill whenever visual evidence is part of the answer. A snapshot should
help the user understand the UI, not merely prove that a selector exists.

Use `$mobile-web-qa` for responsive/mobile audit, `$claude-to-a-tee` for
reference-vs-implementation parity, `$reference-implementation-critique` for
measured reference/app comparison, `$design-quality-review` when a formal
capture set, 25-item visual QA pass, severity result, or PR review template is
needed, and `$product-ux-contracts` when screenshots must prove preserved UX
contracts. Use `$release-gate` when screenshots are part of commit/deploy
evidence.

Any UI/UX skill that implements, audits, verifies, redesigns, restyles, or hands
off a visible screen must invoke `$snapshot` automatically before the final
response. Do not wait for the user to ask for screenshots.

Keep the capture depth proportional. For a tiny copy, CSS, selector, spacing,
typography, or one-control visual tweak, one current targeted screenshot is
enough, optionally backed by computed values, unless responsive behavior,
comparison, release, or a shared UI contract is in scope.

After finishing UI development, capture and include a current snapshot before
final response even if the user did not explicitly ask for one. For backend,
data, auth, API, or config work, do this only when the change affects a
user-visible journey, admin flow, state, or screen.

If a screenshot is captured or visual evidence is part of the answer, the final
chat response must embed at least one current, useful image inline using Markdown
image syntax and an absolute filesystem path. Do not finish with only screenshot
paths, prose descriptions, or "saved at ..." references. The only exceptions are
when the user explicitly asks for files/paths only or when the environment cannot
render/capture images; in those cases, state the exception clearly.

## Core Rule

Snapshots must be shown in chat. The saved file is not the deliverable by
itself; the user must be able to see the evidence in the conversation without
opening a path manually.

Do not crop exactly to the target element when the user needs to judge layout,
alignment, spacing, hierarchy, or visual quality. Include surrounding context by
default.

For component, section, panel, modal, table, card, or page-surface screenshots,
show at least a little side context outside the primary container whenever the
viewport allows it. The left and right page gutters, parent background, or
neighboring layout edges should be visible enough for a human to judge alignment.
If a crop lands exactly on the component border, recapture wider or use the full
viewport.

Tight crops are allowed only when inspecting a pixel-level detail such as a
border thickness, icon shape, crop edge, or text overlap. When sending a tight
crop, also send or mention a wider snapshot unless the user explicitly asked
for only the tiny detail.

## Snapshot Intent

Before capturing, name what the image must prove:

- geometry or visual style;
- interaction state such as open drawer, selected tab, disabled reason, error,
  empty, loading, or keyboard-visible mobile state;
- reference/app, before/after, or local/production comparison;
- design-quality QA capture set, 25-item pass, or release-grade review result;
- deployed artifact smoke;
- product UX contract such as internal scroll, sticky behavior, routing,
  persistence, focus, permission state, or media fallback.

If the proof target is behavior, a screenshot is supporting evidence, not the
whole proof. Pair it with click/keyboard steps, computed values, console/network
checks, URL/state checks, storage/reload evidence, or test output as needed.

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
- **Centered page sections or cards:** include visible left and right gutters
  outside the section, normally at least 32-80px per side when available, so the
  crop does not hide the side margins being judged.
- **Small control, line, icon, or label:** crop with breathing room around it,
  normally 80-160px on each relevant side when available.
- **Responsive issue:** capture at the relevant viewport and include enough
  vertical context to see what comes before and after. Include a mobile
  viewport when responsive behavior is in scope, even if the main review is
  desktop.
- **Before/after or reference/app comparison:** use matching viewport sizes and
  comparable framing.
- **Production smoke:** capture the deployed URL with a cache buster when
  relevant, not only the local build.

Avoid screenshots that start or end exactly on the visual border being discussed
unless the point is a microscopic edge inspection.

## Capture Workflow

1. Identify what the screenshot must prove: geometry, style, interaction state,
   responsive behavior, deployed artifact, product UX contract, or visual
   comparison.
   If the task requires formal design QA, follow `$design-quality-review`
   Appendix A for viewport, state, zoom, DPR, theme, network, and motion
   capture conditions.
2. Render the actual state first. Navigate, scroll, click, wait for content, and
   close unrelated overlays before capture.
3. Capture a wide/context snapshot. Add a tighter crop only if it clarifies a
   specific detail.
4. For UI changes, record key computed values when useful: x/y/w/h, font size,
   line height, border width/color, overflow, visible count, or console errors.
5. Record provenance for important evidence: requested URL, final URL,
   route/hash, viewport, browser, device scale/zoom when relevant, auth state,
   data state, scroll position, overlay/state, build/commit, and reference
   file/hash when comparing.
6. Save screenshots with descriptive filenames that include route/component and
   state, for example:
   `/tmp/notenwert-dresden-life-sidebar-after-wide.png`.
7. In the final answer, embed at least one useful image directly in chat with
   an absolute path: `![label](/absolute/path.png)`. Do not only list screenshot
   file paths when visual evidence is the deliverable.

For UI implementation work, run this workflow after the final edit state, not
only during debugging. Use a built or deployed artifact when release/build risk
is in scope. If a snapshot cannot be captured, disclose why and what visual risk
remains.

## Side-By-Side Requirements

When the task depends on comparison inputs, present them side by side as the
primary visual evidence. Do not make the user mentally compare separate,
differently framed screenshots when a paired or contact-sheet image can be
produced.

- **Claude Design or reference available:** show `Reference` plus
  `Development` side by side. A reference can be Claude Design HTML, a Claude
  screenshot, Figma/exported design, static mock, competitor/example page, or
  any user-provided visual target.
- **Enhancing an existing UI with before/after proof in scope:** show `Before`
  plus `After` side by side with matched route, viewport, state, scroll, data,
  and framing whenever possible.
- **Reference plus existing UI plus new implementation:** show all three
  columns side by side, normally labeled `Reference`, `Before`, and
  `After/Development`. Do not collapse the original UI into prose when it is
  available and the new UI is meant to follow the reference.

For responsive work, create matched comparison rows per viewport instead of
mixing desktop, tablet, and mobile panels in one unlabeled row. If a side-by-side
artifact cannot be produced, embed the individual screenshots in comparison
order with clear labels and state why the contact sheet was not possible.

## Comparison Workflow

For before/after, reference/app, or local/production comparison:

1. Use matching viewport size, route, scroll position, auth state, data state,
   and browser when possible.
2. Capture a wide context shot for each side before any tight crops.
3. Apply the side-by-side requirements above before deciding which screenshots
   to capture: `Reference + Development`, `Before + After`, or
   `Reference + Before + After/Development`.
4. When a reference or comparison HTML file is available, always include the
   comparison artifact: capture the HTML reference and the implementation with
   matching framing, then present a side-by-side contact sheet or equivalent
   paired image. If no comparison HTML/artifact is available and there is no
   existing UI to compare, a single implementation snapshot is acceptable.
5. For responsive comparisons, include a mobile viewport as well as the primary
   desktop or tablet viewport. When comparing against HTML, produce matching
   side-by-side evidence for the mobile viewport too.
6. Name files so pairs sort together, such as
   `/tmp/checkout-card-before-390x844.png` and
   `/tmp/checkout-card-after-390x844.png`.
7. For several screenshots, make or present a short contact sheet only when it
   helps comparison; otherwise embed the highest-signal images. When comparing
   against HTML, Claude Design, or before/after states, prefer the side-by-side
   contact sheet as the primary evidence.
8. Label comparison images or the report with source side, route, viewport,
   state, scroll position, build/commit, and reference hash when available.
9. Record mismatched conditions instead of implying the screenshots are directly
   comparable.

## Product UX Contract Evidence

When the snapshot is used to preserve or audit product UX contracts, capture the
actual contract, not only the pretty surface.

- **Internal scroll/sub-container:** record selector, visible item count, total
  item count or page size, `scrollHeight`, `clientHeight`, `scrollTop`, first
  visible item, last reachable item, max-height/overflow style, sticky overlap,
  and page-level overflow.
- **Sticky/anchor/scroll choreography:** capture top and scrolled states, record
  scrollY milestones, sticky start/end, anchor target position, and whether
  manual scroll is preserved.
- **Routing/deep link/persistence:** record requested/final URL, route/hash/query,
  selected state, reload/back-forward result, and the screenshot after state
  restoration.
- **Modal/drawer/focus:** capture open state plus focus target, close/escape
  result, scroll lock, backdrop, and focus restoration.
- **Permission/destructive states:** capture allowed, denied, disabled-with-reason,
  confirmation, success/failure, and audit/rollback state when relevant.

Use `$claude-to-a-tee` when the contract is being balanced against a Claude
reference, and include the snapshot evidence in the decision ledger.

## Behavior Evidence

Do not present a screenshot alone as proof that a control works. For buttons,
filters, search, forms, routing, persistence, media, auth, or destructive
actions, pair the image with the exercised steps and at least one confirming
signal: URL/state change, DOM/computed value, storage/reload result,
console/network status, API/test result, or visible success/failure state.

## Crop Construction

When building a crop from an element rectangle:

- Expand the clip beyond the element bounds before taking the screenshot.
- Prefer including parent edges and adjacent content over perfectly centered
  framing.
- Preserve side gutters for layout evidence. For non-tight crops, make sure the
  crop includes background outside both horizontal edges of the primary surface
  when the page provides it. If either side gutter is unavailable because the
  element touches the viewport, fall back to a wider viewport or full-viewport
  screenshot.
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

- Always embed at least one current snapshot directly in chat when any snapshot
  exists for the task. Listing paths alone is not acceptable visual evidence.
- State what was captured and from where: local app, reference HTML, or
  production URL.
- State what the screenshot proves and any conditions needed to interpret it.
- Include the screenshot inline in the chat using Markdown image syntax with an
  absolute filesystem path, for example `![label](/absolute/path.png)`.
- For multiple relevant screenshots, embed the highest-signal images directly
  in the chat; include additional paths only as supporting references.
- Include measured values only when they answer the user's question.
- For comparison/contact sheets, label reference/app, before/after, viewport,
  route/state, and scroll position.
- When Claude Design/reference, before UI, and after UI all exist, use a
  labeled three-column side-by-side image as the primary comparison evidence.
- If a screenshot is intentionally tight, say that and provide a wider context
  image when useful.

## Quality Gate

Before claiming a visual change is done, check:

- The screenshot shows enough context for a human to understand the issue.
- The screenshot intent is clear: what it proves and what it does not prove.
- The state in the screenshot matches the route/device/reference being discussed.
- Provenance is recorded for release/comparison evidence: URL, viewport,
  browser, auth/data state, build or reference identity, and scroll/state.
- No crop hides the very edge, neighbor, label, or parent needed for judgment.
- Non-tight layout screenshots show side context outside the main container;
  crops that hug the left/right border of the component are rejected unless the
  screenshot is explicitly a microscopic edge inspection.
- The file path is absolute and renderable in the Codex app.
- The visual evidence is shown in chat, not merely saved to disk or described by
  path. Reject a closeout that lists screenshot paths without embedding at least
  one image, unless the user explicitly asks for files only or capture/rendering
  is impossible.
- For UI changes, at least one current snapshot is included in the closeout.
- After UI development, a current post-implementation snapshot is included even
  when the user did not explicitly request one.
- If Claude Design or another visual reference is in scope, the closeout
  includes a side-by-side `Reference` and `Development` comparison.
- If the task asks for before/after proof or the comparison is needed to judge
  the change, the closeout includes a matched side-by-side `Before` and `After`
  comparison.
- If Claude Design/reference, the old UI, and the new implementation all exist,
  the closeout includes all three side by side with clear labels.
- For backend/data/auth/API/config changes that alter a user-visible journey,
  at least one snapshot or equivalent visual proof covers the affected journey.
- For responsive work, a mobile snapshot or mobile side-by-side comparison is
  included unless the user explicitly scoped the review away from mobile.
- For behavior claims, interaction or state evidence accompanies the image.
- For product UX contracts, relevant metrics or before/after state evidence are
  recorded, not only a static screenshot.

A screenshot is invalid evidence when it shows the wrong route, stale build,
loading shell, hidden overlay, wrong viewport, unauthenticated gate, pre-hydrated
state, unlabeled comparison side, omits an available reference/before/after panel
required for the comparison, or uses a crop that hides the layout relationship
being judged.
