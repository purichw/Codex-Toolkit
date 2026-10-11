# Component Patterns And Behavior Contracts

Use existing project components first. The
[static gallery](../assets/component-gallery.html) is an optional visual specimen
using [fallback tokens](../tokens.css) plus a separate
[gallery base](../assets/gallery-base.css). It simulates some states; it is not
a production component library, complete accessibility example, or proof that
dialogs, tabs, menus and notifications work. Do not copy its inert markup verbatim.

Apply states that exist in the real contract, not every possible state to every
component. Above-field names, selects/date values, stats and table headers follow
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
Verify the painted hit box, glyph, peer row and whole group's alignment; text
centering alone does not establish any of those.

## Text Fields And Validation

Associate labels, hints and errors programmatically; placeholders are not labels.
Keep entered values through failure. Use appropriate type/inputmode/autocomplete.
A readonly value is not a disabled field, and an async request need not lock
the whole form. Test late responses without overwriting dirty inputs or focus.

Avoid fixed heights around labels/errors. Test actual long multilingual labels,
empty/populated native controls and text enlargement.
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

## Cards

Use for distinct repeated objects or genuinely framed tools, not every section.
Let text determine height; stabilize media aspect ratio and shared peer tracks.
Equal peer geometry does not justify clipping meaningful content.
A link card must not produce nested interactive controls or obscure its action.
Loading placeholders should approximate content geometry without impersonating
real content. Center KPI groups only, not every card's prose.

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
