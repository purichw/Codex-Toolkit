# Rework Patterns

Read the cases relevant to the current defect or a broad page reconstruction.
These are decision examples, not mandatory components, dimensions or aesthetics.

| Situation | Weak response | Better adaptation | Evidence to inspect |
| --- | --- | --- | --- |
| User says the page has the right sections but does not feel like the mockup | Adjust color and radius again | Compare dominant heading, image/text balance, section weight, rhythm, icon/material language and footer treatment | Whole requested page plus an actual-size crop |
| Mockup has an illustrated forest/temple hero; product requires real photos | Use any temple and darken it heavily | Select a real subject with compatible light, focal position and negative space; adapt crop/overlay without obscuring the subject | Desktop and phone crops, all changed carousel slides |
| Image-only mockup lacks source CSS | Stall, or pretend to know exact CSS values | Infer visible relationships, state uncertainty, implement a coherent responsive composition | Labeled current comparison; no unsupported pixel-parity claim |
| Daily summary mockup has a moon, lunar text, favorable-day pill and lucky tiles; product only supports some data | Replace the entire layout with a generic text card, or invent the missing facts | Preserve supported heading/date/icon/meta grouping, rebalance the available data and qualify approximate values; reconsider unsupported tiles rather than filling them arbitrarily | Long date, missing optional data, real small-screen card |
| Mobile carousel controls dominate or overlap the heading | Shrink every control indiscriminately | Use a compact grouped variant, possibly a counter instead of many dots, place it in reserved space; preserve swipe/pause/keyboard and a usable hit area | Whole control group and adjacent headline/action geometry |
| Category cards are tall while the reference shows compact horizontal links | Change only card height | Adjust media frame, image/text share, wrapping and action clearance together; use a mobile composition appropriate to the content | Longest real title, narrow phone, arrow clearance |
| A portrait image enlarges a grid row | Add a one-off max-height to that image | Give the media wrapper a responsive ratio/size and constrain the child image independently; inspect the shared card pattern | Portrait, landscape and fallback in the same row |
| Long selected-place text hides its remove control | Clip the entire chip or shrink the close icon | Let only the text flex/wrap/truncate as appropriate; keep the action visible, accessible and non-shrinking | Long names, horizontal scroll, keyboard removal |
| Footer is too tall and lacks the reference's visual character | Reduce padding only | Recompose brand/nav/action groups, adopt relevant material/motifs, and use progressive disclosure if appropriate without losing destinations | Context above/footer, expanded mobile state and keyboard |
| User asks for shared header across routes | Restyle Home and create an unused shared file | Change the actual owner, migrate authorized consumers, preserve necessary variants and verify representative uses | Consumer map, current routes, menu/search behavior |
| Mockup looks compact, but real copy is longer | Apply tiny fonts or fixed heights until the screenshot is short | Improve grouping and measure, use appropriate concise copy or wrapping, keep readable text and accessible controls | Actual-size rendering, long-content state, section rhythm |
| Functional tests pass but the user keeps identifying visual omissions | Add more unrelated tests | Perform an explicit design critic pass and fix observed omissions; turn repeatable geometry defects into focused assertions | Current reference/development evidence, separate behavior results |

## A Compact Working Note

For substantial work, a short note can prevent repeated discovery. Use only the
fields that help; do not create a report for every small repair.

```text
Requested scope and selected desktop/mobile references:
Design qualities to preserve:
Authorized freedom and real product constraints:
Largest current gaps, including visual details:
Shared owners/consumers and asset/data dependencies:
Chosen adaptations and unresolved material decisions:
Evidence/checks needed to stop, and broader checks intentionally skipped:
```

Track broad-page coverage as adopted, adapted, pending or outside scope. An
adapted element is not inherently a failure; its reason and visual outcome
matter. A pending obvious detail is not complete merely because the route works.

## Avoid Overgeneralizing

- A Thai cultural site may need botanical ornament and gold; an operations
  dashboard may need neither. Derive the vocabulary from the selected reference.
- Three horizontal category cards suited one mobile design. This is not a global
  column-count rule, nor permission to make text unreadable elsewhere.
- Some mobile references omit a desktop section. Check whether another visible
  path preserves its task before hiding it; omission in an image alone is not
  approval to remove a product capability.
- Real data may require more height than illustrative copy. Explain that outcome
  only after addressing avoidable spacing and grouping problems; do not use it
  as a blanket excuse for poor proportions.
- Large centered text is not inherently better. Center icons or tiles when the
  design calls for it; keep prose and data aligned for reading.
- Exact reproduction and flexible adaptation are both valid, different requests.
  Never use this skill to override an explicit exact constraint.
