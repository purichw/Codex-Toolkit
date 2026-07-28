# Before / After — Anti-Slop Examples

> Source of truth: `tokens.css`. Each entry: the slop pattern, why it reads as
> generated, and a corrected version using tokens. `❌` = don't ship · `✅` = ship.
> These map to `SKILL.md` "Anti-Slop Rules" and the failure recovery section in
> `references/craft-defaults.md`. All fixes are
> **REQUIRED** unless marked OPT.

---

## 1. The gradient hero background

❌
```html
<section style="background:linear-gradient(135deg,#7c3aed,#2563eb);color:#fff;text-align:center;padding:120px 20px">
  <h1 style="font-size:64px">Welcome to the Future ✨</h1>
</section>
```
Why slop: rainbow gradient, centered-everything, emoji headline, vague copy.

✅
```html
<section class="wrap" style="display:grid;grid-template-columns:1.1fr .9fr;gap:var(--s8);align-items:center;padding-block:var(--s9)">
  <div>
    <h1 style="font-size:clamp(2.5rem,5vw,var(--t-4xl));line-height:var(--lh-tight);max-width:16ch">Ship design that doesn't look generated</h1>
    <p style="font-size:var(--t-lg);color:var(--muted);max-width:48ch;margin-top:var(--s4)">A concrete component and token system your agents can build from.</p>
    <div style="display:flex;gap:var(--s3);margin-top:var(--s5)">
      <button class="btn btn--primary">Get started</button>
      <button class="btn btn--ghost">See how it works</button>
    </div>
  </div>
  <div style="aspect-ratio:4/3;border:1px solid var(--border);border-radius:var(--radius);background:repeating-linear-gradient(45deg,var(--bg),var(--bg) 10px,var(--surface) 10px,var(--surface) 20px);display:grid;place-items:center;font-family:monospace;color:var(--faint)">product screenshot</div>
</section>
```
Fix: solid tone, left-aligned, real specific copy, no emoji, labeled placeholder for the missing image.

## 2. The left-border accent card

❌
```html
<div style="border-left:4px solid #6366f1;border-radius:12px;box-shadow:0 10px 40px rgba(99,102,241,.3);padding:24px">
  <div style="font-size:28px">🚀</div><h3>Fast</h3><p>Blazing fast performance</p>
</div>
```
Why slop: the signature AI card — colored left stripe, glowing tinted shadow, emoji-in-a-badge, filler copy.

✅
```html
<div style="background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:var(--s5);box-shadow:var(--shadow-sm)">
  <h3 style="font-size:var(--t-lg)">Sub-100ms responses</h3>
  <p style="color:var(--muted);margin-top:var(--s2)">Median API latency measured across the last 30 days.</p>
</div>
```
Fix: hairline border, one soft neutral shadow, hierarchy from title/muted meta, specific claim (**?** replace the number with a real one — don't invent).

## 3. Rainbow status colors / color-only meaning

❌ Six different bright hues for six tags; status shown by color alone.

✅ One accent hue for interactive/selected state; status via the soft tint + **a text label**:
```html
<span class="chip" style="background:var(--accent-soft);color:var(--accent)">Active</span>
<span class="chip" style="background:color-mix(in oklch,var(--danger) 12%,transparent);color:var(--danger)">Failed</span>
```
Fix: meaning never encoded in color alone (**REQ**, accessibility); consistent chroma.

## 4. Type soup

❌ `font-family:Inter` everywhere, 5 arbitrary sizes (13/17/22/28/33px), 4 weights, centered.

✅ One personality + one workhorse font, sizes only from the scale (`--t-sm`…`--t-3xl`), max 2 weights (400/600), left-aligned. Hierarchy from size/weight/space (`SKILL.md` "Craft Rules").

## 5. Everything centered

❌ Centered headings, centered paragraphs at full width, centered nav.

✅ Left-align text; constrain measure `max-width:68ch`; center only genuinely symmetric, short elements (a single CTA, an empty state). Deliberate left alignment reads as designed.

## 6. Fake data / fabricated charts

❌ A pie chart with invented "42% / 31% / 27%", counters animating to made-up numbers.

✅ **REQ** no real data → a labeled placeholder describing the intended chart:
```html
<div style="aspect-ratio:16/9;border:1px solid var(--border);border-radius:var(--radius);display:grid;place-items:center;font-family:monospace;color:var(--faint)">bar chart · weekly active users · needs real data</div>
```
Never fabricate numbers, logos, testimonials, or metrics.

## 7. Shape/depth pileup

❌ Card with `border` + `box-shadow` + inner `border` + gradient fill + pill corners next to sharp corners.

✅ One radius token everywhere; one depth philosophy (border **or** one shadow); no gradient fills on surfaces. Pill radius allowed only on chips/toggles.

## 8. Button overload

❌ Three "primary" buttons in one view, all pill-shaped with glowing shadows and emoji.

✅ Exactly one primary; others secondary/ghost; `var(--radius)` corners; no glow; sentence-case verb+object labels ("Save changes", not "SUBMIT ✅").

## 9. Motion decoration

❌ Bouncy spring on every card hover; 800ms fades; elements sliding in on scroll everywhere.

✅ Purposeful only: `transition:var(--dur-fast) var(--ease-out)` on hover; enter/exit ≤ `var(--dur)`; animate `transform`/`opacity` only; honor `prefers-reduced-motion` (**REQ**).

## 10. Empty section stuffed with filler

❌ A "Features" grid padded to 6 cards with generic copy to fill the row.

✅ Show only real content; if a section feels empty it's a **layout** problem —
merge, resize, or cut (`SKILL.md` "Scoping Rules"). Ask the user before adding
material.

---

## Detection heuristic (run before shipping)

Scan the output for these literal tells and fix each: `linear-gradient(` on a large background · `border-left:` + `px solid` on a card · emoji in headings/buttons · `text-align:center` on paragraphs · more than 2 accent hues · pill + sharp radii mixed · any number/logo/quote you can't source · `box-shadow` with a colored (non-neutral) rgba. Each hit = one of the patterns above.
