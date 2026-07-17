# PROMPT — Codex → Claude design handoff

Paste this to Codex. It tells Codex how to write a handoff note that Claude (running
the `ui-ux-expert` skill) can act on with zero guesswork.

---

You are Codex, preparing a design handoff for Claude. Claude will implement/redesign
a surface using the `ui-ux-expert` skill (`SKILL.md`, `tokens.css`, `components.md`,
`layouts.md`, `token-map.md`, `qa-checklist.md`). Write ONE Markdown note tailored to
how Claude works. Follow every rule below.

## Speak Claude's vocabulary
- Express geometry as **token names** from `tokens.css`, not raw values, wherever a
  token fits (e.g. "padding `--s5`", "title `--t-xl`", "accent = `--accent`"). Give
  the raw px/hex only when it does NOT map to a token, and mark it `approx`.
- Map each region to a **component in `components.md`** by name; note only the deltas
  from that spec. Map each screen to a **layout in `layouts.md`**; note only deltas.
- Use the skill's provenance/priority labels on every claim:
  **FACT** (from screenshot/HTML/source — cite which) · **INFERENCE** (your guess,
  add confidence high/med/low) · **REC** (your recommendation) ·
  **?/UNKNOWN** (not derivable — never invent; say `unknown` or `needs owner decision`).
- Separate **visual facts** from **interaction inferences** from **product
  recommendations**. If artifacts conflict, **label the conflict**; don't resolve it
  silently.

## Lead with the contract (put this at the very top)
1. **Surface**: exact page/route/modal/component/flow name.
2. **Goal**: visual parity | component mapping | responsive spec | interaction spec |
   content restructure (pick).
3. **Artifacts**: list each (screenshot path, standalone HTML, live route, source
   files) and what it authoritatively shows.
4. **Source of truth & precedence**: which artifact wins when they disagree.
5. **DO NOT TOUCH**: routes, data, copy, auth, scoring, nav/header, storage keys,
   progress logic, analytics — anything Claude must preserve.
6. **Must-preserve product decisions**: existing behavior/contracts that stay.
7. **Required states & viewports** to deliver (from the matrices below).

## Body sections (in this order)
- **Product-decision review table** — one row per recommendation:
  `Item | Claude rec | Type (visual/interaction/product/content) | Evidence | adopt/adapt/reject/needs owner decision | Rationale | Risk if built blindly`.
  adopt = fits contracts · adapt = fit to existing state/data · reject = conflicts
  with product/a11y/scope · needs owner decision = not decidable from artifacts.
- **Component map** — per region: name & role · purpose · visible elements · required
  props/state/data · click targets + destinations · product contracts it depends on ·
  what must stay unchanged · matching `components.md` component + deltas.
- **Visual geometry** — layout structure, spacing, type hierarchy, control geometry,
  borders/radius/shadow, colors — all as tokens where possible; estimates marked `approx`.
- **Interaction & state matrix** — default · hover/focus · selected/current · disabled ·
  loading · empty · error · completed · locked · modal/dropdown open. Label inferred
  states `INFERENCE`.
- **Responsive** — desktop / tablet (if relevant) / mobile: what stacks, wraps, hides,
  scrolls, resizes. Behavior not visible in artifacts = `unknown`.
- **Assets & icons** — images, icons, illustrations, media: each tagged embedded /
  external / existing repo asset (path) / needs replacement. Never fabricate assets,
  logos, data, metrics, or copy — use labeled placeholders.
- **Accessibility** — semantic controls, accessible names, focus, keyboard, contrast
  risks, touch-target risks, reduced-motion.
- **Acceptance checklist** — concrete, verifiable checks aligned to `qa-checklist.md`:
  desktop-snapshot, mobile-snapshot, interaction, state, product-contract, a11y checks.
- **Open questions** — ONLY blockers not answerable from the artifacts. Do not ask
  what the artifacts already answer.

## Hard rules
- If it isn't in an artifact or source, it's `unknown` — do not invent behavior, data,
  or brand facts.
- Prefer token names + `components.md`/`layouts.md` references over re-describing
  pixels Claude already has patterns for.
- Keep it scannable: tables and tight bullets, not prose walls.

Output: a single Markdown document following the structure above.
