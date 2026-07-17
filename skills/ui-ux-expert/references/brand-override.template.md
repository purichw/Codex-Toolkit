# Brand Override Template

> Copy this file into a project as `design-brand.md` (or paste into the project's
> `CLAUDE.md` / `AGENTS.md`) when the project HAS a brand. It OVERRIDES the global
> `tokens.css` defaults. Fill only what you can source; leave the rest marked
> `UNKNOWN — ask`. **Do not invent brand facts.**
>
> Precedence: **brand facts here > global ui-ux-expert defaults**. Where this file
> is blank/UNKNOWN, fall back to `tokens.css`.
>
> Legend for every field: **FACT** = sourced from a real brand asset (link it) ·
> **ASSUMPTION** = reasonable default you chose, flag it for review ·
> **UNKNOWN** = not provided, must ask before shipping anything that depends on it.

---

## 0. Source of brand truth (fill first)

- Brand assets provided: `<links: brand guide / Figma / logo files / live site>` — or **UNKNOWN**
- If UNKNOWN → **REQ** ask the user for the brand guide/site before styling; use `tokens.css` meanwhile and flag output as unbranded.

## 1. Logo & name

- Product/brand name: `<exact string>` — **FACT / UNKNOWN**
- Logo files (svg preferred): `<path>` — copy into project, don't hotlink
- Clear space / min size / on-dark variant: `<rules>` — **FACT / UNKNOWN**
- **REQ** never recreate a logo by hand; if missing, placeholder + ask.

## 2. Color tokens (override tokens.css)

Provide real values; keep the same variable NAMES so components keep working.
```css
:root {
  --bg:        /* FACT|ASSUMPTION: */ ;
  --surface:   ;
  --ink:       ;
  --muted:     ;
  --faint:     ;
  --border:    ;
  --accent:    /* brand primary */ ;
  --accent-ink:/* text on accent — verify contrast ≥4.5:1 */ ;
  --accent-soft: color-mix(in oklch, var(--accent) 12%, transparent);
  --success:   ;
  --danger:    ;
}
```
- **REQ** if only a primary is given, derive neutrals/soft/feedback from it but **flag as ASSUMPTION**.
- **REQ** verify text-on-accent and body contrast after overriding.
- Semantic colors (success/danger/warning): `<brand values>` — **FACT / ASSUMPTION**

## 3. Typography (override tokens.css)

- Display/heading font: `<family + source: Google/self-hosted/license>` — **FACT / UNKNOWN**
- Body font: `<family + source>` — **FACT / UNKNOWN**
- Mono (if used): `<family>` — **FACT / UNKNOWN**
- **REQ** load via the brand's licensed source; if unlicensed/unknown, keep the global pairing and flag it.
- Keep the global **type scale** unless the brand specifies its own (then list it here).
- Casing rules (e.g. buttons sentence case, headings title case): `<rule>` — **FACT / ASSUMPTION**

## 4. Shape, depth, spacing

- Radius: `<value>` — **FACT / ASSUMPTION** (else keep `--radius`)
- Shadow philosophy: `<flat / one soft / layered>` — **FACT / ASSUMPTION**
- Spacing scale: keep global unless brand defines one → `<values>`
- Iconography set: `<name + source>` — **FACT / UNKNOWN** (**REQ** one family, don't mix)

## 5. Voice & microcopy

- Tone: `<e.g. plain, warm, technical>` — **FACT / ASSUMPTION**
- Terminology (canonical nouns; e.g. "member" not "user"): `<list>` — **FACT / UNKNOWN**
- Button/label conventions, do-not-use words: `<rules>` — **FACT / UNKNOWN**
- **REQ** no invented taglines, testimonials, stats, or legal/marketing claims.

## 6. Imagery & illustration

- Photography/illustration style: `<rule + source library>` — **FACT / UNKNOWN**
- **REQ** missing imagery → labeled placeholder (SKILL §7), never stock gradients or fabricated screenshots.

## 7. Component deviations from global spec

List only where the brand differs from `components.md`:
- `<component>`: `<brand-specific state/style>` — **FACT / ASSUMPTION**
- Everything not listed → follow `components.md` as-is.

## 8. Domain / behavior facts

- Product-specific flows, rules, or data shapes: `<link to real spec>` — **FACT / UNKNOWN**
- **REQ** never invent product behavior or data. Unknown → placeholder + ask.

---

## Ready-to-use header for the agent

Paste at the top of the project instructions:

> **Design:** Follow the global `ui-ux-expert` skill. This project overrides its
> defaults per `design-brand.md`. Treat `FACT` fields as truth, surface `ASSUMPTION`
> fields for review, and **ask** before shipping anything that depends on an
> `UNKNOWN`. Fall back to `tokens.css` only where this file is blank. Do not invent
> brand facts, data, or product behavior.

## Fill-completeness gate (REQ before styling)

- [ ] Colors: all six neutrals + accent set (or explicitly falling back), contrast verified.
- [ ] Fonts: heading + body chosen and licensed-loadable (or global fallback flagged).
- [ ] Logo present or placeholdered.
- [ ] Voice/terminology captured or defaulted-and-flagged.
- [ ] All remaining gaps marked `UNKNOWN — ask`, none silently assumed.
