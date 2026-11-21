---
name: mockup-fidelity-repair
description: Course-correct an existing website or app that misses an approved mockup, including rework that matches at only one viewport. Use when the user says an implementation looks unlike the reference, requests a second pass after a failed mockup-to-product attempt, or identifies desktop, tablet, mobile, or language-specific fidelity gaps.
---

# Mockup Fidelity Repair

Recover the reference composition in the real product. A view that already
matches is evidence to protect. Each failing view needs its own diagnosis and
verification.

For first implementation, use `$mockup-to-product`. In a repair, use that skill
for reference interpretation when needed and `$responsive-design` for tricky
reflow. Use `$snapshot` for matched visual proof. See
[lessons from prior repairs](references/repair-lessons.md) for examples involving
public pages, separate brand identities, CMS editors, and loading states.

## 1. Re-establish the target

- Find the latest user-selected reference for each affected view. Map each to the
  actual route, component, viewport, language, and state. On an annotated
  board, identify the actual screen inside device frames, arrows, notes, and
  comparison images. Treat those surrounding elements as evidence about the
  design. Resolve genuine conflicts using the user's latest direction and
  established product decisions.
- Confirm the rendered source before editing. Match the URL and renderer,
  source/build, CSS viewport or container width, language, scroll position,
  and representative content. For editors and previews, confirm the selected
  design, workspace, draft/published state, and preview width separately.
  Stale content, a different renderer, or a misreported viewport can look
  exactly like a failed CSS correction.
- Capture a genuine Before with enough surrounding context to see alignment
  and density. Compare the reference and real UI at equivalent scale. Keep
  aspect ratios when cropping or scaling a reference. Distinguish values read
  from source, proportions measured from an image, and inferred behavior.
  Mark any missing Before or missing viewport reference explicitly.

## 2. Turn the mismatch into a repair plan

Start with the differences that most change what the user sees or does. A
marked defect is the minimum; also inspect its surrounding layout and other
in-scope instances of the same pattern. Record the intended relationship,
the observed difference, and the code or content that controls it. One line
per significant defect is enough.

| Symptom | Check first | Likely place to repair |
| --- | --- | --- |
| Whole page feels too long, sparse, or crowded | Section order, occupied height, gutters, vertical gaps, content density | Page grid, section wrappers, shared spacing rules |
| A view matches while another falls apart | Actual available width, layout mode, inherited sizes, min-content constraints, rule precedence | Responsive region or component owner |
| Correct elements feel off in scale or alignment | Loaded face and weight, line breaks, line height, baseline, control geometry | Typography roles and space allocated to text and actions |
| Brand feels generic or portraits are clipped | Asset identity, focal point, visible crop, aspect ratio, actual selected media | Brand asset slots and responsive image containers |
| Editor matches visually but edits appear missing | Selected renderer, field consumer, saved state, preview/public destination | Editor grouping, projection or data binding |
| It only looks wrong briefly | First visible frame, applied CSS, font readiness, layout after load | Loading and route handoff |

For substantial work, write a compact map by region and width. Record the
expected columns/order, heading wraps, image crop, section padding, and key
controls wherever these change. Treat supplied desktop, tablet, and mobile
mocks as separate compositions. A tablet may pair a gallery with prices,
while mobile uses a rail and stacked panels. When a width has no reference,
design the reflow around the same content and hierarchy and label it as an
adaptation.

Before a large capture run, state the affected widths, states, evidence, and
the point at which verification will stop. Keep a one-region repair focused
on that region and its neighbors. A page or flow rework covers the specified
pages and all their affected regions.

## 3. Fix the cause at its owner

- Get the section order, grid, proportions, and spacing right before fine
  typography and decoration. Change the underlying composition when the
  existing template cannot express the reference. Keep native, editable
  text and real controls. Reuse the shared shell, themes, and behavior where
  they already fit. Give distinct designs their own scoped composition and
  assets where the brief calls for them.
- Size from the content and its available space. At narrower widths,
  reallocate columns, group related fields, stack, or use the intended
  scroll/rail pattern. Run TH and EN through their real fonts and copy when
  both are in scope. Preserve readability, critical controls, focus and
  selection through a responsive change. Keep well-fitting views in the
  regression set.
- Keep product data connected. A mock establishes visual priority. Real
  routes, editable fields, identifiers, and actions supply the product
  behavior. Use the actual components with appropriate demo data when a
  populated view is needed. Preserve draft/preview/published boundaries
  during CMS work.
- If a change misses again, compare the new render to the same reference and
  revise the diagnosis. Check which rule wins, which renderer mounted, and
  which asset or data value it consumed. Replace a disproven patch with a
  cause-based fix. Keep the change within the owner's scope.

## 4. Verify each affected view independently

1. Re-render after the final edit. Use every supplied in-scope reference
   width. For web views without specified sizes, 1440, 820, and 390 CSS px are
   useful desktop, tablet, and mobile starting points. Check both sides of a
   changed threshold, for example 767 / 768 / 769 when the layout switches at
   768 px. Also exercise each changed layout where its text or controls have
   the least room, plus any reported device/orientation. Verify
   actual viewport or component width in the rendered page. For a shared
   change, check the distinct affected consumers, including the previously
   good view.
2. Inspect Reference / Before / After in matched framing. Pair geometry
   checks with direct visual review of hierarchy, line breaks, padding,
   crop, clipping and alignment. Wait for visible media and intended fonts.
   For a loading complaint, also capture the first visible frame under the
   relevant slow-load condition. For whole pages, look through the full
   section sequence and open detail crops where a full-page image is too
   small to judge.
3. Exercise behavior affected by the change. For example, open a real card
   detail and reach the final rail item, resize an open editor with input
   still present, or save/reopen a field and inspect its actual preview in
   an authorized test workspace. An image of a control and a passing build
   complement this evidence.

Close per view with **verified against reference**, **verified adaptation**,
**mismatch**, or **unverified**. Resolve material in-scope differences that can
be repaired. Name any remaining gap, its reason, and the evidence needed.
Report the important fixes, tested widths/languages/states, and current
visual proof. Each in-scope view earns its own verdict. Describe verified
relationships and measured differences at the available precision.
