# Responsive Layout Decisions

## Reference And Behavior Matrix

Start with facts: source viewport in CSS px if known, content bounds, type roles,
alignment, section order, imagery/focal point and primary action. Image pixels may
reflect DPR or a device frame; do not assume a 2x screenshot is a 2x CSS viewport.
Label inferred states/breakpoints separately and preserve approved geometry at
the source viewport. Missing real fonts/assets prevent a faithful-match claim.

Use this matrix only for regions touched by the request:

| Region | Keep | Narrow / medium / wide decision | Trigger and state proof |
| --- | --- | --- | --- |
| Navigation | Destinations, identity, readable labels | Inline if it fits; intentional disclosure when it does not | Real labels, open menu, keyboard and resize focus |
| Main content | Message, order of meaning, CTA | Recompose related content; cap wide text measure | Awkward wrapping, loss of hierarchy, short landscape |
| Repeated items | Content and action reachability | Intrinsic or deliberate column changes | Minimum usable item width, long/empty content |
| Data view | Relationships, fields, filters, selection | Local scroll or equivalent agenda/cards | Data comparison need, shared state, equivalent actions |
| Form/actions | Labels, entered values, errors | Wrap/reflow; move sticky action only if justified | Long errors, keyboard, focus not obscured |

Do not mechanically turn every desktop row into a carousel or every narrow form
into a wizard. Disclosure needs a visible, accessible retrieval path. The user
must still complete the same primary task without lost data or essential actions.

## Content Pressure And Breakpoints

1. Find what becomes unusable: nav collision, insufficient card width, poor
   measure, clipped controls, a crop that loses meaning, or a sidebar consuming
   the main task. A framework's named breakpoint is not evidence by itself.
2. Estimate a grid's required inner width with
   `columns * usableItemWidth + (columns - 1) * gap`; include gutters and adjacent
   regions when translating this into a viewport threshold. Confirm by rendering
   real copy, fonts and controls. Labels and zoom can shift the pressure point.
3. Let unrelated regions change independently. Test B-1/B/B+1 for each touched
   discrete threshold and at least one intermediate width. For rem/em media
   queries, the basis is the browser's initial font size, not the authored root
   size. Do not use a hardcoded 16 multiplier as a universal assumption.
4. Use container queries for reusable components embedded in different slots.
   Measure the actual container and its threshold, including sidebar-open states;
   a viewport sweep alone does not prove container coverage.
5. Preserve the existing cascade/query convention if it works. Mobile-first is
   useful for new work, not permission for a wholesale CSS rewrite in a repair.

Tablet should have intentional line lengths and grouping, not narrow desktop
columns stretched vertically. Wide desktop needs bounded content and related
regions; empty space can be deliberate. Do not add invented product claims.

## Intrinsic CSS Patterns

Check the page's viewport configuration at its framework/document owner:
`<meta name="viewport" content="width=device-width, initial-scale=1">` is the
usual baseline. Do not disable user zoom with `user-scalable=no` or restrictive
scale limits to make the layout appear stable.

Adapt values to the local tokens and real content; these are structural examples,
not a replacement design system or mandatory numeric thresholds.

```css
.content {
  inline-size: min(100% - 2rem, 75rem);
  margin-inline: auto;
}
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 18rem), 1fr));
  gap: 1.5rem;
}
.grid > *, .flex-content { min-inline-size: 0; }
.item { display: flex; flex-direction: column; }
.item-actions { margin-block-start: auto; }
.identifier { overflow-wrap: anywhere; }
```

Choose explicit column counts when the intended composition requires them;
`auto-fit` can make a single item excessively wide. Preserve content-sized height
and constrain the grid/item at its appropriate owner. `min-inline-size: 0` enables
shrinkage but does not itself wrap a long identifier or resize a fixed-width child.

```css
.summary-slot { container-type: inline-size; }
.summary { display: grid; gap: 1rem; }
@container (min-width: 34rem) {
  .summary { grid-template-columns: minmax(0, 1fr) auto; align-items: start; }
}
```

Here `.summary` must be a descendant of `.summary-slot`. Base stacking remains
usable without container-query support. Do not introduce a container only to
paper over a fixed-width child or lose necessary intrinsic sizing.

## Find The Owning Constraint

Reproduce the exact route/state/viewport and inspect computed styles and bounds.
Walk from the offending descendant toward its layout owner; an overflowing
ancestor may be a symptom of intrinsic child sizing.

| Symptom | Inspect first | Typical causal repair |
| --- | --- | --- |
| Whole document too wide | Fixed width/min-width, flex/grid min-content, long identifier, offscreen transform | Repair the responsible constraint; wrap targeted text or permit shrinkage |
| No scrollbar but missing text | Fixed height, line clamp, overflow clip/hidden, absolute siblings | Grow/reflow or use an explicit permitted truncation contract |
| Navigation too small | Type role, total label width, gaps, disclosure threshold | Keep readable type; change available space or arrangement |
| Control text collides | Label length, icon/chevron reservation, white-space, box sizing | Allocate content/icon space and allow intended wrapping |
| Wide table dominates mobile | Essential row/column relationships and tasks | Local scroller with accessible name/keyboard access, or equivalent representation |
| Sticky region covers content | Height/offset, ancestor overflow, safe-area, keyboard | Correct offsets/reserved space or disable stickiness where inappropriate |

Do not hide overflow at the body to make assertions pass. Local clipping is valid
for intentional decorative crops only when meaningful content/focus stays safe.
Do not use global `break-all`, whole-page `transform: scale`, fixed-height text
boxes or absolute positioning of ordinary content to force one screenshot.

## Typography And Real Content

- Use the real brand fonts and required weights, correct document/inline `lang`,
  and role-based rem sizes. Keep letter spacing consistent with current design
  constraints. No viewport-scaled font size or shrinking essential text to fit.
- Inspect Thai marks and mixed Thai/Latin baselines at normal viewing size and
  enlarged text. Let text-bearing containers grow with appropriate line-height;
  keep normal language wrapping. Use `overflow-wrap: anywhere` for genuinely
  unbreakable identifiers, not blanket `word-break: break-all` on prose.
- Cap prose by comfortable rendered measure. A Latin `ch` measure is only a
  starting point, not a Thai character count. Do not insert manual `<br>` just
  to imitate one width unless the authored line break carries real meaning.
- Stress long titles/actions, validation messages, amounts/dates/status, and
  realistic 0/1/few/many-result cases. Preserve essential values; ellipsis needs
  a usable full-value path where the task depends on the hidden content.
- Keep button/icon alignment and component dimensions stable across hover,
  loading and label changes without clipping legitimate content.

## Media And Interaction

Use `srcset` with accurate descriptors and `sizes` reflecting the actual slot for
resolution selection. Use `<picture>` when different compositions/crops are
needed. Preserve subject/focal point, reserve intrinsic dimensions/aspect ratio,
and inspect each crop. Avoid blindly lazy-loading the primary critical image.
Do not import the source demo's colors, hero composition or artwork as a theme.

Keep DOM reading and tab order logical; visual CSS `order` is not a substitute.
Navigation links normally use semantic nav/list/disclosure patterns, not an ARIA
application menu. An in-flow disclosure usually needs no focus trap. A modal
needs correct initial focus, containment, Escape/close and focus return; prefer
the project's tested primitive or suitable native dialog behavior.

Use one data/state owner across responsive presentations. Avoid duplicate IDs,
active tab stops and competing requests. Hidden alternatives must not remain
keyboard-accessible. Respect the user's explicit view choice when adapting the
default. On resize, keep input/filter/date/page state and an open dialog's record.
If a focused trigger disappears, return to its visible equivalent or a logical
task anchor, not the top of the page.

Do not infer input modality from width. Keep essential actions available without
hover. Verify short landscape heights, sticky controls, safe areas and virtual
keyboard overlap when relevant. `dvh`/`svh` alone do not guarantee keyboard safety.
Reduced-motion alternatives must preserve state-change feedback.
