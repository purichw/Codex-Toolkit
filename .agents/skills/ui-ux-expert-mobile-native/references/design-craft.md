# Native design craft — decisions, not a universal skin

Use this when the visual cause is unclear or a screen needs new structure. These are diagnostic
heuristics and proposed checks, not empirically validated taste rules for every domain.

## Begin with the user's immediate task

State the job in one sentence and identify what must be noticed first, next, and only when needed.
Examples: compare an amount and its status; complete a form without losing a draft; read a story;
select a character whose silhouette and motion matter. Do not make every job a dashboard.

Reference choice: prefer the same domain, content pressure, platform, and task. A portfolio shot
can inform art direction but cannot prove production navigation, error states, or native behavior.
For fidelity requests, preserve the important relationships of the supplied reference; do not invent
a different style. If only one state is supplied, separate faithful reproduction from unobserved adaptation.

Capture a few consequential decisions, not a long mood-board essay:

| Observation | Translation | Owner | Check |
| --- | --- | --- | --- |
| Reference gives one amount clear priority | Reserve a stable amount column; reduce secondary action emphasis without removing actions | Row layout/action menu | Long names and large/negative amounts remain comparable |
| Form separates field groups by purpose | Label-to-control gap is smaller than the gap between groups | Field wrapper/group | In error state, helper text stays attached to its field |
| Editorial image drives the opening | Use approved focal point and aspect policy; keep a readable text plane | Media/article layout | Small-window crop retains the subject and caption context |

## Read the render at three scales

**Composition:** is useful content crowded into a small strip by oversized headers, empty banners,
stacked cards, or repeated navigation? Does the first viewport communicate the task? Does a long screen
retain rhythm below the first fold? Do not cut content merely to fit the first viewport.

**Grouping and typography:** do gaps describe relationships, or does everything receive equal spacing?
Are labels, values, headings, help, and status visually distinct in a way that matches their meaning?
Check actual font coverage, weight, line breaks, numeral alignment, and baseline behavior in the native
render. A token name does not prove which font was used. Keep paragraphs readable, not forced into a
fixed line-count or character-count rule across languages.

**Controls and imagery:** inspect optical centering, icon family/weight, hit areas, focused/selected/
loading/disabled states, borders, crop, and image sharpness. A mathematically centered bounding box can
still look unbalanced. Confirm the parent is correct before applying an optical adjustment; justify
small optical corrections with images rather than banning them categorically.

## Diagnostic prompts

| Symptom | Check before changing | Likely repair | Counterexample |
| --- | --- | --- | --- |
| Screen feels crowded | Repeated affordances, equal emphasis, depth of nesting, real touch spacing | Reduce competition or regroup; preserve frequent actions | A rushed operator may benefit from compact rows, not spacious cards |
| Screen feels empty | Proportion of chrome to useful content; missing real data/image | Rebalance regions and content, not filler ornaments | A confirmation screen may intentionally be quiet |
| Weak hierarchy | Competing weights/sizes, absent grouping, large secondary art | Adjust role relationships and position first | A comparison grid can have intentionally equal peers |
| Typography looks cheap or unstable | Actual glyphs/weights, Thai marks, digit alignment, truncation | Fix role font/line metrics and layout width | A decorative font may suit a short game title, not a dense error paragraph |
| Generic template look | Did reference traits survive beyond accent color? | Recover relevant composition, imagery, material and control character | A neutral settings utility may already be appropriate |

Do not blacklist gradients, glass, shadows, cards, large type, or particular fonts by name. Ask what
role they serve, whether that role fits the product, and whether the actual content remains readable.
Likewise, a system component is not automatically beautifully composed in its surroundings.

Use existing semantic tokens. If none exist, define only needed roles (canvas/surface/text/secondary/
action/status, text roles, relationship-based gaps, control geometry) and adapt them to the brand.
Do not import web CSS or distribute one numeric scale as a law for all apps.

Before sending, compare early and final renders under the same state. Use the paired hypotheses in
[works/fails](../examples/works-fails.md). They teach causal review; they are not visual gold standards.
