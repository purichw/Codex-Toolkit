# AGENTS.md — UI/UX design agent entry point

> Codex/Claude Code: when a task involves designing or building any user-facing
> UI, screen, layout, component, deck, doc, or prototype, **load `SKILL.md` in
> this folder first** and follow it. It is the design brain; this file is just the
> map.

## Files in this skill

- **`SKILL.md`** — the full method: philosophy, process, anti-slop rules, the craft
  levers (type/color/space/grid), a self-review critic pass, and an ENCYCLOPEDIA of
  concrete component specs, motion, responsive, data-viz, forms, microcopy, glossary,
  and a cheat sheet. Read it top-to-bottom once; look up the appendix mid-build.
- **`tokens.css`** — a ready-made, tasteful default design system (neutrals, one
  accent, spacing + type scales, radius, shadow, motion, resets). **Copy this into a
  project** when the user gives no brand, instead of retyping tokens. Re-theme by
  changing only the accent hue.

These defaults are fallbacks, not a universal brand. If a project has brand
tokens, a design system, production UI, or user-provided direction, that local
context wins.

### Implementation-ready artifacts (build from these, not from memory)

- **`references/components.md`** — component gallery spec: every component with default / hover /
  focus / active / disabled / error / loading states, as copyable markup + CSS on the
  tokens. Build `assets/component-gallery.html` from it only when a gallery is requested.
- **`references/layouts.md`** — five layout exemplars (app shell, dashboard, form, content page,
  marketing hero), each with desktop + mobile behavior and breakpoints.
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
- **`assets/component-gallery.html`** — optional visual test bench for the default
  tokens/components. Do not copy it into user projects unless explicitly asked.

Convention across all artifacts: **FACT** (fixed) vs **REC** (default) · **REQ**
(must) vs **OPT** (polish) · **?/UNKNOWN** (ask or labeled placeholder, never invent).

## The 30-second operating loop

1. **Context** — read every file/link/screenshot/brand the user gave before writing.
2. **Ask** — one focused round only if there's no design context and no default fits
   (SKILL §I decides when you may proceed alone).
3. **System first** — copy `tokens.css` (or the brand's tokens); commit to type,
   color, spacing, grid before laying out screens.
4. **Build** — one screen right, then expand. Use the §J component specs and
   `references/components.md` as fallback patterns.
5. **Critic pass** — run SKILL §10 checklist; if it looks off, run the §H triage.
6. **Render and look** — never ship from imagination. Fix, re-look.
7. **Deliver, then suggest** — do exactly what was asked; propose extras, don't apply
   them uninvited (SKILL §11).

For full-site responsive implementation or QA, read
`references/responsive-web-design.md` before the critic pass.

## The rules you must not break

- No slop tells (SKILL §4): no gradient soup, emoji-as-UI, left-border accent cards,
  Inter-everywhere, fake data, filler sections.
- 1–3 fonts · 0–2 accents · 1 background tone. Spacing only on the scale.
- Never fabricate brand facts or real data — use a labeled placeholder and flag it.
- Hierarchy from size/weight/space, not color. Design ideal/empty/loading/error/edge,
  not just the happy path. Accessibility floor (SKILL §G) is non-negotiable.

## Format note

Markdown is intentional: it's what both Codex (`AGENTS.md`) and Claude Code
(`CLAUDE.md` / skills) ingest natively. The judgment lives in prose; the copyable
system lives in `tokens.css`. Keep that split — don't inline the tokens back into
the doc, and don't turn the prose into config.
