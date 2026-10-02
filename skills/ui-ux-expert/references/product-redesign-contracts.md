# Product Redesign Contracts

Use this reference for an existing data-backed UI, especially CMS/Admin redesigns
and visitor views that consume the same content. Apply only the sections touched
by the request. These lessons do not make every spacing edit a whole-site audit.

## Reconcile Before Replacing

Compare the existing screen, reference, and actual data/API contract. Identify
what changes presentation, what must remain available, and what has no supported
behavior yet. Preserve existing actions, fields, permissions, and deep links
unless their removal is authorized; progressive disclosure can retain uncommon
fields without recreating a long undifferentiated form.

A reference-only favorite button, notification action, setup link, or metric is
not evidence that its backend exists. Ask only for a consequential unresolved
choice, such as local versus account-backed persistence. When the user defers a
feature, record the decision and prerequisite in the project's backlog so a
later related feature can restore it. Do not generalize that decision to other
products or silently implement a different storage model.

## Shell, Density, And Reachability

- Keep an in-scope Admin module inside the established shell, navigation, and
  visual system across populated, unavailable, and empty states. Separate domain
  storage does not require a disconnected or unstyled interface.
- Distinguish no records, filters with no results, not configured, intentionally
  disabled, permission denied, and fetch failure. Offer an existing permitted
  action for that state; retry does not resolve a service deliberately closed.
  Do not fabricate setup completion percentages or operational counts.
- Diagnose excess height before shrinking text: inspect inherited minimum
  heights, stretched grid rows, stacked margins, and sparse action-only rows.
  Put a single secondary action beside its section heading or relevant filters
  when space permits. Do not reserve a full-width bottom band for it by habit.
- Keep short empty states content-sized. Balance neighboring blocks without
  forcing all of them to match the tallest unrelated panel. Derive density from
  the reference and real copy, preserving readable type and operable targets.
- For a collapsed rail, check the active background, focus outline, icons, and
  hidden labels against its actual width. For short viewports and long menus,
  verify the last item and footer are reachable. In flex shells, the navigation
  commonly needs `min-height: 0` and its own scrolling region while fixed actions
  reserve space. Hiding overflow alone is not a fix for inaccessible controls.

## Shared UI, Separate Boundaries

An Admin surface should reuse the product's brand, controls, empty states, and
feedback conventions while keeping a layout suited to operational work. Sharing
presentation does not require sharing workflow state, permissions, or sessions.

When adding a privileged entry point, resolve material ambiguity about whether
an existing public login grants entry or requires another sign-in. The same
accounts/provider do not answer that question. Separate sessions are a product
choice, not a universal Admin default. If isolation is required, verify sign-in,
reload/token refresh, same-scope cross-tab logout, and the opposite scope remaining
usable. Check cross-scope navigation and return destinations. A different URL,
hidden navigation, or route guard alone proves neither isolation nor server-side
authorization. Use `$admin-ops` for the deeper auth implementation and checks.

## CMS Field Ownership

Trace the touched fields through source -> API projection -> editor -> saved
draft/publication -> public projection -> rendered consumers. A visible form
input or successful save notification proves only part of that path. For a broad
sync request, keep a compact coverage matrix with owner, supported operations,
consumers, and evidence; for one field, trace only that field and shared risks.

Separate editorial content from computed/transient state and private audit data:

- Titles, descriptions, media, and configured labels may be CMS-owned. Runtime
  counts, selected years, calculated results, loading/error state, and disclosure
  labels belong to code unless the product explicitly provides a copy setting.
  Split editorial text from computed text instead of patching a whole mixed node.
- Existing activity, commerce, analytics, and media stores keep their ownership.
  Sharing an editor shell does not make every domain a generic page-text patch.
- Editable internal references or verification notes are not automatically public.
  Preserve the visibility contract as well as the value.

Test these distinctions when supported by the product:

| Operation | Required question |
| --- | --- |
| Change a value | Do the actual API, editor reload, and affected public consumers agree? |
| Clear a value | Does intentional empty content stay empty or show the designed placeholder, without reviving an old value? |
| Remove an override | Does it restore the defined baseline, including section visibility/order? |
| Rename a record | Do source data, references, and visiting/contact information remain attached to a stable identity? |
| Disable then re-enable | Can lists, related cards, details, and maps restore the record without stale DOM or markers? |
| Replace media | Are responsive slots and crop/alt metadata correct, without inheriting the old asset's credit/license? |

Use the product's specified fallback rules. Missing, explicit empty, and removed
overrides are not interchangeable; neither are a missing mobile variant and an
explicitly cleared one. Preserve intentionally empty alt text where appropriate.
Metadata-only edits should not unnecessarily discard attribution for the same
asset. When live publication is authoritative, an outage must not silently
replace it with stale bundled content. If the product supports offline or
last-known-good content, preserve its explicit freshness/error policy. State
build-time boundaries, such as new static routes or SEO metadata, instead of
claiming immediate synchronization.

## Visual Editing Is Part Of The Product Contract

Apply this section when the requested design must be authored in an editor.
Trace each touched feature through schema/node model -> editing controls ->
serialization/sanitization -> saved content -> canvas, preview, and public
renderers. A front-end component or a richer fixture does not prove the editor
can produce it. Prefer shared block definitions, typography, and rendering rules
where semantics match; if the editor needs a separate rendering adapter, verify
its parity explicitly instead of maintaining unrelated visual defaults.

The live editable canvas must show the authored type, block treatments, media
frames, spacing, and supported composition while typing. Selection outlines,
handles, and toolbars may surround the content without changing its geometry.
Compare at an equivalent content width and responsive mode. Preview checks the
complete page shell and surrounding layout at realistic desktop/mobile widths;
it must not be the first place the authored design becomes visible.

Make the requested composition genuinely authorable:

- Map supported operations for each in-scope block: insert, edit, reorder,
  remove, visibility, and placement. Examples include moving a summary into the
  middle, inserting an illustration at the selected position, editing a sidebar
  quote, and editing or hiding decorative copy. Expose real controls rather than
  requiring raw JSON or code. Do not imply unrestricted placement when only
  specific regions or ordering are supported; implement the requested freedom
  or resolve the material limitation instead of silently narrowing the request.
- Define how sidebar/column content relates to the main flow and where it moves
  on mobile. Persist ordering and visibility consistently across renderers.
- Give each authored block one canonical owner. A removed/hidden summary or
  quote must not survive as a second metadata-generated block or return through
  a default fallback. Keep explicit off/empty distinct from never configured;
  any retained legacy content must be reachable and understandable in the editor.
- Match the approved reference by default, using role-specific typography.
  When requested, provide semantic H1/H2/H3/H4/P choices and independent custom
  font-size controls. Preserve valid overrides through saving and sanitization;
  resetting restores the defined role baseline. Confirm actual font loading,
  weights, and script coverage, not just a CSS family name. Project-specific
  choices such as CoverMate's Google Sans do not become a global skill default.

Verify the touched operations through the real editor UI using isolated content:
create/edit -> move or insert -> hide/remove -> save/reopen -> preview -> public
renderer. Include the relevant size override and a clear/delete case when these
contracts change. Use the actual save/projection path; a direct database seed
alone cannot prove authorability. Do not mutate production content solely for
QA. Personally inspect the canvas and rendered results at matching widths, and
report which operations were exercised rather than claiming "anything anywhere."
For a narrow fix, test the affected block and shared risk, not every editor feature.

## Import, Editor, And Export Parity

When no-code data management is in scope, trace the same records through API
ingestion, file import, UI correction, validation, publication, and export. Use
the existing domain schema and validation rules across these paths; document any
necessary transport-specific differences instead of creating competing meanings.
Preserve stable identities, types, periods, units, null versus zero, and provenance.
Users must be able to locate and correct supported validation errors in the UI,
retain valid edits, and revalidate without a compulsory external-file round trip.

A seeded database or working editor is not proof that consumers use it. For an
authorized cutover, compare old and new projections by identity and field values,
not row totals alone, and verify affected consumers plus outage/fallback behavior.
Separate editable, read-only, unsupported, and deferred operations in UI and
closeout; do not claim complete no-code ownership while required tasks still need
scripts. Migration, restore, and live writes require their own authorized scope.

## Stable Editing During Async Updates

Late option/catalog responses should update the affected controls, not remount
the entire drawer or form. Preserve unsaved values, valid current selections,
focus, caret, open disclosures, dropdown state, and scroll position. Invalidate
a dependent value according to the product's dependency rules, not merely
because its options are still loading.

When custom selects are required, reuse the existing accessible primitive or
library and preserve native value/form semantics. Test delayed option loading
while the user is typing or the menu is open, including keyboard selection and
Escape. Fix the state/DOM replacement cause rather than adding arbitrary waits
or suppressing focus behavior.

## Evidence That Can Catch The Defect

- Exercise the real serializer/projection/publication code in an isolated
  fixture when practical. A hand-written fixture with extra fields can conceal
  omissions in the deployed API. Include clear/remove/reload and relevant
  failure cases, not only initial populated rendering.
- For live updates, cover the affected consumers, not only the edited detail:
  cards, related records, open maps, and already-mounted controls can hold stale
  copies. Reuse existing shared projections where they own the same semantics.
- Diagnose lazy-media failures by state. An inactive carousel image may have a
  deferred URL and no `src`; nonzero geometry alone does not make it a broken
  visible asset. Activate each relevant slide, then check decoded dimensions,
  `currentSrc`, and requests. Use the controls actually exposed at that viewport
  rather than force-clicking desktop-only dots on mobile.
- Green DOM/functional checks do not prove visual fidelity. Open the captured
  images and inspect clipping, overlap, density, and the final reachable controls.
  Keep fixture-backed, deployed read-only, and authenticated production evidence
  distinct in the closeout.
- For an authorized release, use `$release-gate` and `$production-asset-smoke`
  for the deployed artifact. Do not edit live CMS records merely to prove a UI
  redesign works. Reuse matching evidence and stop once the touched high-risk
  contracts are covered; name skipped broader checks rather than running them
  by habit.
