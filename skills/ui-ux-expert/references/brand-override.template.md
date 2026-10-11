# Brand Override Template

> Copy this file into a project as `design-brand.md` (or paste into the project's
> `CLAUDE.md` / `AGENTS.md`) when the project HAS a brand. It OVERRIDES the global
> `tokens.css` defaults. Fill only what you can source; leave the rest marked
> `UNKNOWN — ask`. **Do not invent brand facts.**
>
> Precedence: current explicit direction and established product contracts win;
> sourced brand facts override fallback defaults. Blank fields do not authorize
> replacing the existing system. Inspect local tokens/components first.
>
> Legend for every field: **FACT** = sourced from a real brand asset (link it) ·
> **ASSUMPTION** = reasonable default you chose, flag it for review ·
> **UNKNOWN** = not provided; ask only if consequential, otherwise preserve the
> current product or record a reversible assumption.

---

## 0. Source of brand truth (fill first)

- Brand assets provided: `<links: brand guide / Figma / logo files / live site>` — or **UNKNOWN**
- If UNKNOWN, inspect existing production UI and project assets. Ask only when
  missing direction materially changes the work. Use fallback tokens only when
  no applicable system/direction exists; do not rebrand while waiting.

## 1. Logo & name

- Product/brand name: `<exact string>` — **FACT / UNKNOWN**
- Logo files (svg preferred): `<path>` — copy into project, don't hotlink
- Clear space / min size / on-dark variant: `<rules>` — **FACT / UNKNOWN**
- **REQ** never recreate a logo by hand; if missing, placeholder + ask.

## 2. Color tokens (override tokens.css)

Record real values using the project's variable names. The block below is a
role-mapping worksheet, not executable CSS; do not paste empty declarations.
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
- If only a primary is given, retain existing neutral/feedback roles. In truly
  unbranded work, propose missing roles as assumptions and verify actual pairs.
- **REQ** verify text-on-accent and body contrast after overriding.
- Semantic colors (success/danger/warning): `<brand values>` — **FACT / ASSUMPTION**

## 3. Typography (override tokens.css)

- Display/heading font: `<family + source: Google/self-hosted/license>` — **FACT / UNKNOWN**
- Body font: `<family + source>` — **FACT / UNKNOWN**
- Mono (if used): `<family>` — **FACT / UNKNOWN**
- Load via a licensed source; otherwise preserve an available project fallback
  and disclose the limitation. Do not invent a global font pairing.
- Keep the existing type roles/scale; adapt only where the task supplies a reason.
- Casing rules (e.g. buttons sentence case, headings title case): `<rule>` — **FACT / ASSUMPTION**

## 4. Shape, depth, spacing

- Radius: `<value>` — **FACT / ASSUMPTION** (else keep `--radius`)
- Shadow philosophy: `<flat / one soft / layered>` — **FACT / ASSUMPTION**
- Spacing scale: retain the existing project scale; record justified role changes → `<values>`
- Iconography set: `<name + source>` — **FACT / UNKNOWN** (**REQ** one family, don't mix)

## 5. Voice & microcopy

- Tone: `<e.g. plain, warm, technical>` — **FACT / ASSUMPTION**
- Terminology (canonical nouns; e.g. "member" not "user"): `<list>` — **FACT / UNKNOWN**
- Button/label conventions, do-not-use words: `<rules>` — **FACT / UNKNOWN**
- **REQ** no invented taglines, testimonials, stats, or legal/marketing claims.

## 6. Imagery & illustration

- Photography/illustration style: `<rule + source library>` — **FACT / UNKNOWN**
- Missing imagery → a clearly identified temporary placeholder,
  never stock gradients or fabricated screenshots.

## 7. Component deviations from global spec

List only where the brand differs from `components.md`:
- `<component>`: `<brand-specific state/style>` — **FACT / ASSUMPTION**
- Everything not listed retains the existing component contract. The skill's
  components reference is optional fallback guidance, not a production library.

## 8. Domain / behavior facts

- Product-specific flows, rules, or data shapes: `<link to real spec>` — **FACT / UNKNOWN**
- **REQ** never invent product behavior or data. Unknown → placeholder + ask.

---

## Ready-to-use header for the agent

Paste at the top of the project instructions:

> **Design:** Follow the global `ui-ux-expert` skill. This project overrides its
> defaults per `design-brand.md`. Treat `FACT` fields as truth, surface `ASSUMPTION`
> fields for review. Resolve consequential unknowns without erasing existing
> product choices. Use fallback tokens only when no applicable system exists.
> Do not invent brand facts, data, or product behavior.

## Scoped Handoff Check

- [ ] Colors: all six neutrals + accent set (or explicitly falling back), contrast verified.
- [ ] Fonts: heading + body chosen and licensed-loadable (or global fallback flagged).
- [ ] Logo present or placeholdered.
- [ ] Voice/terminology captured or defaulted-and-flagged.
- [ ] All remaining gaps marked `UNKNOWN — ask`, none silently assumed.
