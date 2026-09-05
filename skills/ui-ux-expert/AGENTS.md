# AGENTS.md — UI/UX design agent entry point

> Codex/Claude Code: when a task involves designing or building any user-facing
> UI, screen, layout, component, deck, doc, or prototype, **load `SKILL.md` in
> this folder first** and follow it. It is the design brain; this file is just the
> map.

## Files in this skill

- **`SKILL.md`** — the lean operating method: process, source-of-truth precedence,
  diagnosis, tradeoffs, reference routing, behavior rules, critic pass, and snapshot
  gate. Read it top-to-bottom first; then load only the references needed for the
  task.
- **`tokens.css`** — optional fallback tokens. Copy only when the project has no
  brand, design system, production UI, or supplied direction. Adapt roles to the
  task; do not reduce every design decision to changing one accent hue.

These defaults are fallbacks, not a universal brand. If a project has brand
tokens, a design system, production UI, or user-provided direction, that local
context wins.

### Implementation-ready artifacts (build from these, not from memory)

- **`references/components.md`** — component gallery spec: every component with default / hover /
  focus / active / disabled / error / loading states, as copyable markup + CSS on the
  tokens. Build `assets/component-gallery.html` from it only when a gallery is requested.
- **`references/layouts.md`** — five layout exemplars (app shell, dashboard, form, content page,
  marketing hero), each with desktop + mobile behavior and breakpoints.
- **`references/craft-defaults.md`** — typography, color, spacing, imagery, motion,
  data-viz, forms, microcopy, accessibility floor, failure recovery, and a compact
  cheat sheet. Read when concrete values are needed.
- **`references/responsive-web-design.md`** — full website responsiveness checklist:
  viewport meta, mobile-first/intrinsic layout, `svh`/`dvh`, iOS/Android quirks,
  OS/browser differences, hover/touch/pointer behavior, responsive media, zoom,
  performance, and cross-engine testing.
- **`references/anti-slop-examples.md`** — before/after fixes for the common generated-UI
  mistakes, plus a literal detection heuristic to scan output.
- **`references/qa-checklist.md`** — screenshot-based QA Codex runs against a render (capture
  protocol, REQ/OPT checks by section, verdict format). Use before claiming done.
- **`references/brand-override.template.md`** — copy into a branded project as `design-brand.md`;
  overrides `tokens.css` (FACT / ASSUMPTION / UNKNOWN fields, never invented).
- **`references/token-map.md`** — where each token should and shouldn't be used (role, not
  appearance) + a role→token lookup table.
- **`references/design-judgment.md`** — cause-directed diagnosis, conflict
  resolution, and selective comparison of alternative structures.
- **`references/contextual-rules.md`** — when defaults apply, when to adapt them,
  and how to test multilingual/content constraints without universalizing examples.
- **`references/evaluation-protocol.md`** — matched baseline/candidate evaluation,
  synthetic scenario pack, human review, and evidence limitations.
- **`references/claude-design-learning-brief.md`** — current coverage and remaining
  evidence gaps; a focused prompt for external design critique.
- **`assets/component-gallery.html`** — optional visual test bench for the default
  tokens/components. Do not copy it into user projects unless explicitly asked.

Read legacy FACT/REC/REQ labels in context. A measured value is not automatically
a universal requirement. Use the shared design-quality conventions for formal
review and the contextual-rules reference for applicability.

## The 30-second operating loop

1. **Context** — read every file/link/screenshot/brand the user gave before writing.
2. **Diagnose/decide** — distinguish symptom from cause; resolve consequential
   uncertainty using `SKILL.md` "When To Ask" and "Judgment And Scope".
3. **System first** — reuse the actual project system. Use fallback tokens only
   under the conditions above; define the small set of roles the task needs.
4. **Build** — one screen right, then expand. Use `references/components.md` and
   `references/layouts.md` as fallback patterns.
5. **Critic pass** — run the `SKILL.md` critic pass; if it looks off, run the
   failure recovery section in `references/craft-defaults.md`.
6. **Render and look** — never ship from imagination. Fix, re-look.
7. **Snapshot gate** — use `$snapshot` automatically for final visual evidence
   before responding; don't wait for the user to ask.
8. **Deliver** — cover the requested outcomes and material tradeoffs, evidence,
   and untested claims. Do not apply unrelated extras.

For full-site responsive implementation or QA, read
`references/responsive-web-design.md` before the critic pass.

## The rules you must not break

- No slop tells (`SKILL.md` "Anti-Slop Rules"): no gradient soup, emoji-as-UI, left-border accent cards,
  Inter-everywhere, fake data, filler sections.
- Font/color counts and spacing examples are fallbacks, not universal pass/fail
  thresholds. Respect the existing roles, scripts, content, and task.
- Never fabricate brand facts or real data — use a labeled placeholder and flag it.
- Hierarchy from size/weight/space, not color. Design ideal/empty/loading/error/edge,
  not just the happy path. Accessibility floor in `references/craft-defaults.md`
  is non-negotiable.

## Format note

Markdown is intentional: it's what both Codex (`AGENTS.md`) and Claude Code
(`CLAUDE.md` / skills) ingest natively. The judgment lives in prose; the copyable
system lives in `tokens.css`. Keep that split — don't inline the tokens back into
the doc, and don't turn the prose into config.
