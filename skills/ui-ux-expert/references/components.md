# Component Patterns And Behavior Contracts

Use existing project components first. The
[static gallery](../assets/component-gallery.html) is an optional visual specimen
using [fallback tokens](../tokens.css) plus a separate
[gallery base](../assets/gallery-base.css). It simulates some states; it is not
a production component library, complete accessibility example, or proof that
dialogs, tabs, menus and notifications work. Do not copy its inert markup verbatim.

Apply states that exist in the real contract, not every possible state to every
component. Type roles, card identity, field names, selects/date values and tables follow
[user-preferences.md](user-preferences.md). Accessibility thresholds live in
[accessibility-checks.md](accessibility-checks.md).

## Buttons And Action Links

Match hierarchy to decision scope; several independent objects can each have an
action without requiring deletion to reach "exactly one primary per view."
Use buttons for actions, anchors for navigation/downloads. Preserve accessible
names during loading and prevent duplicate operations, not all interaction.

Valid fallback typography (the font shorthand cannot end in `inherit`):
```css
.btn {
  font-family: inherit;
  font-size: var(--t-base);
  font-weight: 600;
  line-height: 1.3;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--s2);
  min-height: 44px;
  max-width: 100%;
  padding: var(--s3) var(--s5);
}
```
The 44px height is a comfort default, not the definition of WCAG AA.
Use the project's icon library for familiar tools, with tooltips where useful.
Center the label and icon vertically as a group inside the painted button. Check
actual loaded Thai/Latin text, line height and glyph bounds; `align-items: center`
alone is not proof of visual balance. Fix shared metrics/padding before adding
page-specific offsets. Keep the icon gap compact and consistent; do not stretch
a short label and arrow to opposite edges merely because the button is wide.
An intentional row-navigation pattern may use edge-aligned indicators.

Use a separate gap between neighboring buttons; let the action group wrap or
stack before controls collide. Verify the label/icon group, painted hit box, peer
row and whole group, including loading and icon-only variants when affected.

## Text Fields And Validation

Associate labels, hints and errors programmatically; placeholders are not labels.
Keep entered values through failure. Use appropriate type/inputmode/autocomplete.
A readonly value is not a disabled field, and an async request need not lock
the whole form. Test late responses without overwriting dirty inputs or focus.

Avoid fixed heights around labels/errors. Test actual long multilingual labels,
empty/populated native controls and text enlargement.
Match single-line input, select and date-trigger heights through the shared size
variant; different label/helper heights must not distort the controls themselves.
Check native date/select bounds in the relevant engine, not only a desktop resize.
Bound short reference/code fields to their expected format instead of stretching
them across the page. Let that bounded group stay centered when the composition
calls for it, while allowing full available width on narrow screens. Preserve
the project's value alignment and enough room for editing, icons and validation.
Long prose fields may need wider/taller geometry; uniformity is not one size for
every kind of input. Use concise format hints, not sample sentences as labels.
Validation timing must serve correction, not interrupt every keystroke.
GOV.UK's [validation guidance](https://design-system.service.gov.uk/patterns/validation/)
distinguishes invalid input from service problems; do not tell users to fix a
field when the server is unavailable. Its [error summary](https://design-system.service.gov.uk/components/error-summary/)
pairs navigable summary errors with field messages. Adapt that pattern to the
product rather than importing GOV.UK's exact wording or blanket summary rule.

## Selects, Choices And Switches

Prefer native elements or the project's tested primitive. A custom combobox,
listbox and action menu have different keyboard/selection contracts; a generic
div menu plus arrow keys is not interchangeable with all three.
Preserve value/label association, selection, escape/dismissal and focus behavior.
Test open and closed states; centered native text does not prove popup alignment.
Keep checkbox/radio/switch captions leading-aligned. Use a switch when the on/off
meaning and commit behavior are clear; do not replace a mutually exclusive radio
group just because switches look cleaner.

### Dropdown Chevron Geometry

- The painted trigger owns the arrow, its slot and padding. Position it against
  that trigger's border box, not the outer label/helper wrapper. Center it
  vertically and keep a consistent inset from the trailing inner edge, using
  the shared control spacing token. No part of the glyph may escape the field
  or appear pushed against its border.
- Reserve enough text space for the icon slot and clearance. For centered values,
  balance leading/trailing reservations so the chevron does not shift the text
  off the field's center. Long values must not push or overlap the arrow; narrow
  controls must shrink within their layout rather than overflow it.
- Render one indicator: use the native arrow, or suppress its visual appearance
  when supplying a custom chevron. Preserve native semantics and keyboard/touch
  behavior. Reuse the shared select/trigger rather than drawing a new arrow per
  page or per day/month/year field.
- An overlaid control's hit area must match the visible field. Inspect border-box
  bounds, icon bounds and computed insets before changing offsets. Fix the sizing
  or positioning owner; do not hide the defect with clipping or page-specific
  nudges. Centering an icon inside the wrong wrapper is still a failure.
- Verify the affected closed/open, populated/long-value and disabled states at
  desktop and narrow mobile widths, including the narrowest date-picker/filter
  variant in scope. Check the relevant browser engine for native-control claims.
  Pass only when arrows remain inside the field, vertically centered, consistently
  inset across peer controls and clear of the text.

## Cards

Use for distinct repeated objects or genuinely framed tools, not every section.
Let text determine height; stabilize media aspect ratio and shared peer tracks.
Equal peer geometry does not justify clipping meaningful content.
A link card must not produce nested interactive controls or obscure its action.
Loading placeholders should approximate content geometry without impersonating
real content. Center icons and short headings on one shared axis; a two-line
short title still belongs in this treatment. Long titles may use a coherent
leading-aligned variant. Keep long prose, lists and data readable rather than
centering the entire card. KPI cards retain full group centering. See
[card preferences](user-preferences.md#card-icon-and-heading) for exceptions;
implement them at the shared owner.

## Banners And Carousels

Share banner anatomy, spacing and media treatment; keep static and carousel
behavior as deliberate variants. Use the existing carousel owner for gestures,
active slide and controls rather than separate page implementations.

- Exercise horizontal touch swipes without trapping vertical page scrolling or
  turning a drag into a CTA click. Verify buttons, keyboard/focus and active-slide
  indicators agree after manual navigation; a screenshot cannot prove this.
- When autoplay exists, provide usable pause/resume and respect reduced motion.
  Check that manual interaction and rerenders do not silently restart a paused
  carousel or create competing timers. Timing and indicator style are product
  settings, not universal values copied from one project.
- Controls must fit an existing safe area or deliberate overlay without adding
  height to the banner solely for the controls. Do not cover copy, CTAs or key
  imagery, clip focus rings, or shrink touch targets to force a fit. Verify the
  mobile composition separately and preserve the content-driven media/layout
  rules in [responsive guidance](responsive-web-design.md#content-banners-and-sticky-regions).

## Modal Dialogs

Use the established dialog primitive and verify actual focus containment,
background inertness, Escape, accessible title, reachable long content, close
action and appropriate focus return. Backdrop dismissal is a product decision,
not a universal requirement, especially with unsaved work.
Do not mark a static specimen `aria-modal="true"` without modal behavior.
The [WAI-ARIA dialog pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)
describes these contracts and context-sensitive initial/return focus.
The gallery frame grows with content only to display the specimen; a production
dialog needs bounded viewport height and a usable scrolling region.

## Navigation

Primary navigation needs readable type proportional to the page, following
[type roles](user-preferences.md#readable-type-by-role). A header that fits only
after shrinking its labels needs a spacing, grouping or breakpoint repair.
Keep label scale coherent in dropdowns/drawers, with room for icons and focus.

## Tabs

Use links for navigation, tabs for switching related panels. Real tabs need
selection state, panel association and the correct keyboard model. Test focus
and activation rather than adding tab roles to inert text.
Wrap, scroll or change the navigation pattern deliberately when labels no
longer fit; do not hide destinations behind page-level overflow clipping.

## Tables

Preserve table semantics: styling a `td` as grid/flex can break column geometry.
Style an inner wrapper when needed. Center headers including balanced sort
indicators; align body numbers for comparison and text for reading.
Keep units, freshness, selection scope and actions visible where needed.
Row density, vertical rules, zebra stripes and sticky headers are contextual.
Verify empty/loading/error states, sorting, selection and keyboard access when
those capabilities exist. Use a local scroll container for genuinely wide data,
with discoverability and focus visibility; never hide page overflow as a fix.

## Status, Toasts And Progress

Status text must remain readable on its actual composited fill. Use words/icons
as well as hue. If a chip is removable, its remove control needs a usable target
and an accessible name.

Notifications must reflow at narrow widths and longer translations. Use live
regions appropriate to urgency without announcing every static gallery item.
Do not auto-dismiss an important error or sole recovery action. Timing, stacking,
pause and dismissal depend on content and task, not a universal four-second rule.

Use determinate progress only when the amount is known; announce meaningful
progress without excessive updates. Skeletons/spinners are options, not required
for every load. Reduced motion must preserve a clear loading status when motion
stops. A simulated skeleton proves neither request handling nor loading recovery.

## Verification Boundary

Use the real app's rendered states and behavior for delivery. Build a gallery
only when requested or a shared-component change makes it useful. Copy visual
patterns selectively, preserve the framework's APIs, and test affected consumers.
