# User Preferences And Alignment

Read for forms, selects, date/time fields, stat/KPI cards, tables, or alignment work.
These are this user's defaults, not universal design laws. Preserve them unless the
user explicitly overrides them; resolve a conflict with a supplied reference rather
than silently substituting generic advice.

- Stat/KPI cards always center their content horizontally and vertically:
  center the icon, value, label, and supporting text as a balanced group, with
  centered text on desktop and mobile. Prefer a centered vertical stack; keep
  wrapping and equal peer sizing stable. This is the user's explicit design
  preference, not a rule for tables, forms, prose, or every card. Only depart
  from it when the user explicitly requests a different stat-card alignment.
- Dropdown/select alignment follows this user's explicit preference: center the
  field label directly above the dropdown, the selected value, and option labels
  on desktop and mobile unless explicitly overridden. Align each to the painted
  field/menu, not to a wider label/helper wrapper. Reserve balanced space for
  chevrons/checkmarks. Verify closed and open states in editors/dialogs as well
  as filter bars; a centered native select does not prove its custom overlay is
  centered. Preserve readable wrapping, keyboard behavior and native platform
  limitations. Field-name alignment is shared with text inputs, not determined
  by control type; keep entered freeform text and helper prose left-aligned.
- Center above-field names consistently across a form, including text inputs,
  textareas, selects and date/time fields. Center on the actual field width,
  not its adjacent action buttons. Keep required markers with the name; counters
  and auxiliary actions must not push it off-center. Section headings, helper
  and validation prose, and captions beside checkboxes/radios/switches retain
  readable leading alignment. This is not blanket centering of form contents.
- Native date, time, datetime-local, month and week fields follow the same
  centered-label and centered-displayed-value preference, including empty and
  populated states on desktop and mobile. Preserve native editing, validation,
  keyboard and calendar behavior; do not replace a native picker just to center
  it. Verify rendering in the relevant browser engine: Chromium at a mobile
  viewport does not establish Safari/iOS picker behavior. State untested limits.
- Table/grid column headings are centered by default as the user's stated
  preference, including headings with sorting or filtering controls. Balance
  indicator space so the label remains visually centered. Keep body cells
  aligned for their content; this does not center every cell or form label.
  When the user requests this across the site, update the relevant shared
  owners and in-scope consumers, including Admin and public variants, rather
  than applying an Articles-only override or a blanket centering selector.

### Alignment And Action Affordance

- `text-align: center` alone is not alignment proof: flex/grid content and native
  picker internals can remain off-center. Inspect actual layout and a rendered
  screenshot. Center a field label over the painted field itself, excluding any
  adjacent clear/reset/action button; balance calendar/chevron insets. Fix the
  shared component or layout owner rather than adding arbitrary offsets.
- For icon-only controls, center the glyph in both axes of the actual painted
  button and hit area, then check the button within its toolbar or surrounding
  frame. Inspect computed border-box sizes, padding, grid tracks and minimum
  sizes: a centered SVG can still sit off-center in a mismatched parent. Keep
  intrinsic SVG proportions and balanced insets; do not compensate for a broken
  layout with an arbitrary glyph translation. Verify disabled/loading variants
  and narrow viewports as relevant.
- For layered controls such as enhanced native selects, measure the painted
  field and overlaid hit area separately: their bounds must agree before
  centering labels or chevrons. A taller transparent button can look centered
  internally while its icon sinks below the visible field. Check closed/open
  indicators, text clearance, adjacent controls and mobile touch sizing; use
  the existing icon library and fix the sizing owner rather than adding offsets.
- When alignment is requested across a product, inspect the shared owners and
  representative public/Admin consumers, including open menus and dialogs.
  Fix proven shared causes at their owner rather than adding page-by-page
  offsets. Preserve intentional leading/trailing icons and left-aligned prose;
  report which surfaces were actually rendered instead of claiming exhaustive
  coverage from a source search alone.
- Size noninteractive legends and captions around their content, not inherited
  button hit-target heights. Remove excess reserved space without shrinking the
  primary visualization. Recheck wrapping, filters and alternate layers so a
  compact default does not cause clipping or unexpected layout shifts.
- Check three distinct relationships: content inside a control, peer controls
  beside one another, and the whole group inside its parent. When the user says
  "center" on a pictured action group, check the group's position in the card
  or section as well as its labels/icons. Centered text does not center a group.
  Use balanced surrounding space and a suitable group width; preserve readable
  alignment of nearby prose, labels and tables.
- Align the actual interactive boxes in a row. A select's label/helper wrapper
  is taller than the select itself; centering a neighboring upload button against
  that wrapper can visibly lift it. Use compatible control heights and align
  their edges within the existing design system. Check wrapping and responsive
  stacking; equal peer widths are appropriate when the design calls for them,
  not for every action. Do not generalize one screen's pixel dimensions.
- Make task actions such as upload, download and save visibly recognizable as
  controls, with the intended surface/border, padding, shape and focus treatment.
  A button class on an anchor does not prove it renders as a button: tag-specific
  CSS may supply only part of the appearance. Keep correct semantics, including
  real links for downloads/navigation and buttons for in-page actions; ordinary
  prose links need not become buttons. Inspect the rendered result and verify
  the relevant action still works after changing its element or styling.
