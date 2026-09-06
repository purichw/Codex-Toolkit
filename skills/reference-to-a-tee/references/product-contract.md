# Product Contract

Read before mapping reference visuals into product code. The selected artifact
owns observable presentation; product requirements own real engineering
behavior. Apply the authority rules in [../SKILL.md](../SKILL.md), including
per-surface authority for mixed references.

Read and verify affected contracts, not every product subsystem for a style
repair. Apply the effort matrix in [operating-guide.md](operating-guide.md).
Preserving existing behavior is mandatory; re-testing untouched behavior is not
automatic. Escalate when selectors, shared defaults, geometry, or other changes
could affect that behavior, even if the textual diff is small.

## Separate Appearance And Behavior

Reference JavaScript may demonstrate states but need not become product
architecture. Images show appearance without proving behavior. Preserve existing
data, auth, routing, persistence, permissions, accessibility, i18n, performance,
analytics/test hooks, CMS pipelines, and operations unless intentionally changed.

If an explicit requirement says a control writes real state, map its read/write
path and implement the needed product-owned integration within scope. Do not
downgrade an explicitly requested action to a mock because the endpoint does not
exist yet. Conversely, a suggestive icon or a static image alone does not
authorize a new destructive action, backend feature, or production mutation.

Split tradeoffs into:

- `behavior exception`: real product mechanics differ while observable intent
  and geometry remain faithful;
- `visual exception`: visible layout, spacing, copy, item count/order, media,
  color, or component state intentionally differs.

Document visual exceptions, applying existing accepted constraints. Unresolved
critical divergence requires a decision before release. Unknown properties in
an image are not deviations from observed design; describe the chosen product
behavior and its evidence separately.

## Preserve Proven UX

Support a preservation or hybrid decision with product evidence: working flows,
tests, documented requirements, reliable accessibility, operational safety,
usable containers, or coverage of loading/error/denied/reload states. Do not
preserve old appearance merely because it already exists.

Use a short note for one material choice or the decision ledger in
[../SKILL.md](../SKILL.md) for multiple choices. Prefer `hybrid` when
existing mechanics are needed: adopt reference geometry, hierarchy, rhythm, and
component feel while retaining real behavior. For unobservable reference
behavior, preserve the known product contract and label the evidence limit.

Inspect and protect the contracts affected by the change, using this list as a
menu. Flow reconstruction covers the full agreed flow; isolated visual edits do
not require unrelated auth/data/persistence audits:

- Persistence: selected tabs/filters/items, expanded rows, drafts/progress,
  reload, back/forward, and session return.
- Disclosure: accordions, drawers, side panels, modals, step flows, and details.
- Routing: query/hash/route parameters, deep links, shareable state, anchors,
  redirects, history, and fallback destinations.
- Keyboard/focus: tab order, focus traps, close/escape/outside-click behavior,
  focus restoration, shortcuts, scroll-to-input, and screen-reader semantics.
- States: loading, empty, error, denied, disabled-with-reason, validation,
  partial failure, stale sessions, offline, and retry.
- Safety: server authorization, role visibility, readonly state, confirmation,
  undo/restore, audit, rollback, and irreversible-action copy.
- Density: pagination, load more, virtualization, page-size selection, sorting,
  filters, bulk select, counts, and large-list performance.
- Responsive interaction: touch targets, safe areas, mobile drawers/sheets,
  keyboard viewport, sticky actions, and tablet layout.
- Media: real assets, lazy loading, failure fallbacks, CMS visibility, player
  controls, captions, posters, embeds, and source repair.
- Search: accurate metadata, destination, deep link, selected-item visibility,
  target highlight, and useful fallback.
- Scrolling: nested containers, sticky offsets, active-item auto-scroll,
  manual ownership, restoration, and anchor positioning.

Do not flatten useful containers because a static reference hides their behavior.
Verify retained scroll regions at first and last items, manual/automatic scroll,
keyboard/touch access, and page overflow. Keep regression checks for preserved
selectors, counts, pagination, persistence, and flows. Do not rewrite tests to
bless a lost contract without an intentional decision.

## Component Implementation

Map the changed properties/components to their owner files and affected
selectors, data, and actions. An isolated style repair needs only its owner and
direct dependencies, not a fresh map of all component behavior.
Rework incompatible markup when needed for faithful geometry; inspect shared
consumers and test dependencies before renaming classes, IDs, or data attributes.
Verify affected shared consumers without expanding into unrelated redesign.

Match the selected reference's layout, wrapping, alignment, typography, colors,
borders, radii, shadows, icons, media crops, and visible states. Reuse exact assets
when available and permitted. With image-only references, record uncertain font
identity, unavailable source media, and justified substitutes rather than claim
exact extraction. Preserve product-required assets when references use placeholders.
Use project-specific skills or brand rules for mandated fonts; do not import one
project's typography policy into all products.

For broken CMS/remote media, confirm the specific failed asset. Repair the source
only within authorization; otherwise use a scoped fallback, preserve the admin's
ability to replace it, and disclose the remaining source issue. Avoid broad
suppression or silent unrelated substitutions.

Product mechanics do not justify avoidable changes to media frames, count/order,
navigation spacing, footers, or section rhythm. Record any forced visible change
as an exception. Add motion only when observed, explicitly specified, already
required by the product, or needed for accessibility. A still image cannot prove
transition timing or justify decorative animation.

## Real Controls And Complete Scope

Every visible control within the agreed product scope must have real behavior,
honest passive/status semantics, or a legitimate disabled state with a reason.
Do not create inert substitutes for required controls. Include inherited controls
when reconstructing or changing their behavior; an unchanged control appearing
near a local style fix does not mandate a full action tour.
For requested or behavior-affected actions, verify actual success/failure and
persisted result; for image-implied actions, record the product requirement or assumption that
defines behavior before implementing it.

Do not expose internal tags, IDs, buckets, or schema categories as UI grouping
merely because they exist. Use user-facing concepts and the reference's actual
navigation primitive. Map featured/lead/pinned items and visible counts deliberately.

Build missing connective states within scope, such as empty/error messages,
confirmation flows, and role-aware feedback, using the reference's visual
language. Preserve the requested surfaces and report any actual omission or
deferral. A partial screenshot is not permission to remove unseen product UI,
and a multi-screen bundle is not automatic authorization to redesign all routes.
