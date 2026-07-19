# Bundle Files

Use these files to make a Claude Design handoff precise without shipping standalone HTML.

## MANIFEST.md

Record provenance and inventory:

- bundle name and creation date
- source URL/file and final rendered URL
- project/repo path
- relevant commit or `git status` note
- screenshots with viewport, route, scroll position, state, and filename
- generated metrics file
- source screenshots or handoff files supplied by the user
- known exclusions

## PROJECT-CONTEXT.md

Explain the product surface in plain terms:

- what the page helps the user do
- target audience and primary jobs
- where this page fits in the site journey
- brand/design direction and why it uses those colors/materials
- real data constraints and content model
- design weaknesses or open questions, if relevant

Avoid unrelated product areas unless they affect this page.

## DESIGN-SPEC.md

Write implementation-ready design notes:

- visual direction: mood, density, hierarchy, rhythm
- color tokens with hex values and semantic roles
- typography: family, size, weight, line-height, casing
- layout: container widths, section heights, padding, gaps, breakpoints
- components: header, hero, filters, cards/lists, footer, floating actions, modals
- states: hover, focus, selected, empty, loading, open/closed, disabled
- assets: required images, crop behavior, placeholders, icons, font dependencies
- responsive behavior and mobile-specific differences
- measured parity table for high-risk components

Prefer computed values from browser inspection over eyeballing.

## REFERENCE-STATES.md

List every screenshot/state Claude Design should understand:

```text
state | file | viewport | route | scroll | active UI | expected behavior
```

Include at least:

- desktop default
- mobile default
- any user-mentioned or high-risk state

For each state, say whether it is `matched`, `behavior exception`, `visual exception`, or `needs follow-up`.

## IMPLEMENTATION-CONTRACT.md

Define what must not break:

- routes and deep links
- search/filter/sort/pagination/load-more behavior
- data counts and data source truth
- accordions, modals, drawers, internal scroll containers
- map/geolocation/permission behavior
- responsive constraints and no page-level horizontal overflow
- CMS/admin/runtime overrides, if relevant
- analytics/privacy/consent behavior, if visible

Separate:

- `Claude Design should replicate`
- `Product behavior to preserve even if the screenshot/mock differs`
- `Known intentional exceptions`
- `Needs owner decision`

## CLAUDE-DESIGN-PROMPT.md

Write the actual prompt to paste into Claude Design. Include:

- the desired output format
- the exact files attached
- route/page goal
- "replicate, do not redesign" unless redesign is requested
- product contracts that must be preserved
- visual exceptions and behavior exceptions
- viewport expectations
- what Claude should not invent

Keep the prompt direct. Make the attachments and constraints impossible to miss.
