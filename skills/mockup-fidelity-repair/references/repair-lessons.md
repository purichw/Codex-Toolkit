# Lessons from repeated design repairs

These cases document how to choose a fix and prove it. Use the pattern that
fits the current failure. The DeepX file names are provenance for the examples.

## Recover the composition before polishing individual cards

**Colour Club and Waanjai.** The existing general salon template had much
more vertical space and repeated similar content patterns. In Colour Club,
the desktop service intro sits beside a photographic 3 × 2 grid, the tablet
puts the intro above a 2 × 3 icon grid, and mobile uses a service rail.
Waanjai pairs work with pricing on wider views and recomposes both on mobile.

**Repair decision.** List the major section relationships per reference before
changing a heading size. Build scoped compositions around the already working
service details, gallery, navigation, and booking controls. Use the actual
asset or text slot for the selected design. Inspect the sequence from the hero
through booking and footer so that shortening one section does not merely
move excess spacing to the next.

**Proof.** Compare the actual content area of each reference at a uniform
scale. Check local section heights against neighboring ones, and exercise the
rail's last item, gallery, and selected service in booking. The shared white
Studio switcher was an established product decision in these repairs. It
accounts for a real difference from the black mockup strip.

Source records: `docs/COLOUR_CLUB_CAMPAIGN_REWORK.md`, `docs/WAANJAI_POP.md`.

## Treat portrait framing and brand identity as layout requirements

**Salon concepts and Korean Soft on iPad.** Borrowed salon photography and
logos blurred the distinctions between the concepts. New concept-specific
sets included logos, primary and secondary hero art, service imagery, gallery
and team portraits. In Korean Soft, fixed hero heights increasingly trimmed
hair as columns widened on tablets.

**Repair decision.** When the brief calls for original, exclusive artwork,
generate the required brand and photo assets with the requested tool and
assign them by slot. Check stale media references as well as immediately
visible ones. Preserve transparent cutouts and meaningful before/after
identity. For crop problems, compare the frame ratio, focal point, and visible
subject against the reference. Korean Soft used a stable 7:4 hero frame and
top-centered imagery within that concept.

**Proof.** Inspect decoded art inside its real frame at each relevant width.
Exercise both slides where they have different focal points. Korean Soft's
recheck included tablet portrait and landscape and a resize from the second
mobile slide into tablet. Record generated assets and their rendered slots
when they are part of the assignment.

Source records: `docs/KOREAN_SOFT_REWORK.md`,
`docs/COLOUR_CLUB_CAMPAIGN_REWORK.md`, `docs/PLIAN_LOOK_CAMPAIGN.md`.

## Align editor hierarchy with both the mock and the actual workflow

**Fitness CMS and cross-category editors.** The Fitness pack supplied nine
desktop pages and guidance for smaller screens. The repair addressed each
work surface, including the calendar, editors, library and settings. A hidden
preview returned a zero-width measurement during a responsive transition.
Separately, editors offered fields whose applicability depended on the design
and which site the CMS managed.

**Repair decision.** Match each page's working hierarchy. At narrow widths,
the week grid can become a real day agenda and a detail pane can take the full
width with Back. Retain a usable preview width across a hide/show transition
when the first measurement is zero. When field ownership is unclear, name
the website and selected design, link the actual connected route, group
primary fields first, and disclose extra or unused fields. Keep the authored
values. Trace each relevant field through the actual renderer. A catalogue
demo and a managed site can have different consumers even with the same name.

**Proof.** Label tablet/mobile as adaptations when only desktop references
exist. Inspect the actual pages in both UI languages where supported. Edit a
field, open the preview that owns it, and verify save/reopen when in scope.
Resize with a dirty form or open inspector to check state. Use truthful
workspace data for metrics and an isolated fixture when useful. Treat the UI
language and the language of the CMS content as independent dimensions.

Source records: `docs/qa/FITNESS_CMS_REFERENCE_2026-11-15.md`,
`docs/CMS_CONNECTION_CLARITY.md`, `docs/HAIR_SALON_CMS.md`.

## Distinguish a styling error from bad evidence or a load transition

**Ideas directory and demo typography.** Early evidence included a wrong tab
or width and captures before lazy images painted. In live demos a headline
wrapped differently for a moment even though a settled screenshot matched.
Holding the stylesheet and font separately isolated an early reveal before
the display type was ready. During verification, Rhythm's heading used
`display: contents`; the parent lacked a box while its letters were visible.

**Repair decision.** Read the URL, actual CSS width, active language and
resource state back from the same page used for the screenshot. For transient
drift, change the load handoff once evidence identifies the pending resource.
Choose evidence that measures what paints. A text range or visible children
can measure a heading with no box of its own. Use the same visible region and
state when comparing runs.

**Proof.** Show the loaded destination and the actual transition if it is
part of the complaint. Separate tooling artifacts from verified product bugs
with a targeted real-browser recheck. Viewport emulation proves the tested
layout in that engine. Record physical-device or other-engine evidence only
when exercised.

Source records: `docs/IDEAS_DIRECTORY_QA.md`, `docs/LOADING.md`, and the
2026-11-21 production demo typography audit for runtime `b7f7ffa`.
