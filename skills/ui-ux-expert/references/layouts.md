# Layout Decisions By Task

These are alternatives to reason from, not fixed grids, breakpoints or templates
to paste into every product. Direction and constraints in [../SKILL.md](../SKILL.md)
take precedence. Choose breakpoints from content pressure and keep important
content, actions, focus and reading order intact.

## App Shell

Use a persistent rail when repeated navigation and context justify its width.
Use `minmax(0, 1fr)` for the content track; constrain content children too.
Test intermediate widths, not just a wide rail and a narrow drawer. A compact
rail, top navigation, drawer or small bottom navigation each has tradeoffs.
A modal drawer needs modal behavior; a permanently visible rail does not.
At short heights, the last item and sign-out/settings remain reachable.
Do not choose navigation based only on a destination-count rule.

## Operational Dashboard / Table

Start with the question an operator must answer, not a row of decorative KPIs.
Place filters, units, freshness and actions near the records they affect.
Use aligned columns for comparison; a 12-column grid is one option, not a law.
Center stat groups per [user-preferences.md](user-preferences.md), without
centering table body data or making each KPI a hero.

At narrow widths, preserve key comparisons. Options include a prioritized table
with local horizontal scroll, a summary/detail pattern, or cards when row-wise
comparison is not the main job. Do not silently drop important columns/actions.
Keep unknown, stale, partial-error and zero values distinct.
Carbon's [data-table guidance](https://www.carbondesignsystem.com/building-blocks/core/components/data-table/guidelines)
is a product-system example of selectable density and table features, not a
requirement to import Carbon's sizes or styling.

## Form Journey

Use one readable field sequence by default; related short inputs may share a row
when labels, errors, tab order and mobile reflow remain clear. Above-field names
follow the user's centered preference, while values and helper/error prose retain
appropriate reading alignment. Validation timing depends on the input and state;
do not force blur-time validation on every field.

Keep actions close to the decision. Stack only when they no longer fit; sticky
actions must not obscure fields, errors, final content, or the software keyboard.
Preserve entries through invalid submission. For consequential multi-step forms,
consider a review/edit stage; it is not necessary for every small preference edit.
GOV.UK [check answers](https://design-system.service.gov.uk/patterns/check-answers/)
illustrates an explicit review opportunity, not a universal screen requirement.

## Editorial / Content

Use a readable body measure and a typographic hierarchy appropriate to the script.
Treat title, deck, byline, media, caption and article as a sequence rather than
separate decorative cards. Preserve the actual publication's visual identity.
A wider image and narrower reading column can be intentional.
Centering short display text may fit; long centered paragraphs usually need
a task-specific reason. Inline prose links do not need 44px line-height.
Test long titles, captions, text enlargement and actual image crops.

## Public / Hero Surface

Only create a hero when the request needs one; operational tools open on the task.
Make the actual brand/product/place/offer visible at first glance and use relevant
real or generated bitmap media under the applicable project instructions.
Do not substitute a generic split-card composition, filler headline, gradient
backdrop, or fake screenshot for art direction. Preserve a glimpse of following
content where required. Size display text for its container, not from viewport
width, and avoid turning compact panel titles into hero typography.

## Composition Review

Check the full section/page before polishing a single control:
- Does the entry point lead to the task, then supporting evidence, then action?
- Are groups differentiated by meaningful proximity and shared axes?
- Does an oversized title/media block crowd out the useful content?
- Are repeated items comparable without all becoming equal-weight boxes?
- Is whitespace separating tasks or merely stretching the page?
- Does the narrow layout preserve meaning and priority, not just fit?

These are diagnostic questions, not a numeric quality score. For concrete
same-content counterexamples see
[composition-and-calibration.md](composition-and-calibration.md).
