# 07 · Art direction & imagery

Imagery is where a competent build most often turns generic. The code is trivial; the decisions
are not — and they are almost always made by whoever wrote the `<img>` tag.

## What designers notice that developers often miss

- **Crop is composition, not fitting.** A designer chose where the subject sits in the frame.
  `object-fit: cover` re-crops from the center and destroys that choice.
- **The set matters more than the image.** Six photos with consistent light, distance, and grade
  read as art direction. Six good photos from six sources read as a stock library.
- **Aspect-ratio rhythm.** Repeating one ratio down a page is monotonous; random ratios are noise.
  Designers alternate deliberately (wide, wide, tall) and hold the sequence.
- **Faces and product edges have margins.** Cropping through a chin, a logo, or a product's edge is
  visible instantly and reads as careless.
- **Photographs need a treatment decision.** Full-bleed, matted, inset, or masked — one treatment
  per role, applied consistently. Mixed treatments read as accidental.
- **Placeholders communicate.** A gray box says "unfinished". A labelled, correctly-proportioned
  slot says "waiting for the shoot" and prevents layout surprises.
- **Loading behavior is part of the image.** A photo that pops in and shifts the text is a worse
  photo than a slightly slower one that doesn't.

## Bad patterns

| Pattern | Tell `[FACT]` | Fix |
| --- | --- | --- |
| Center-cover everything | Heads cropped at the eyes; products missing an edge | `object-position` from the reference's focal point |
| `object-fit: contain` in a card | Letterboxed image with mismatched bars inside a bordered card | Crop to the card's ratio, or change the card |
| One `<img>` for all viewports | Landscape hero becomes a 40px strip on mobile | `<picture>` with art-directed sources per breakpoint |
| No reserved space | Text jumps when images load | `aspect-ratio` + `width`/`height` attributes |
| Mixed source families | Studio-white product beside candid office beside 3D render | One family per surface; state it in the note |
| Decorative image with alt text | Screen reader reads "hero-bg-3-final.jpg" | `alt=""` for decorative, real description for informative |
| Text baked into images | Unsearchable, untranslatable, blurry at 2× | Live text over the image, or a real caption |
| Text over a busy photo, no scrim | Contrast fails in half the frame | Gradient scrim, matte panel, or crop to a quiet region |
| Stretched image | Faces subtly wide | Never set both dimensions without `object-fit` |
| Gray placeholder boxes at review | Reviewers can't judge the layout | Dominant-color or blur placeholder + a labelled slot |
| Full-bleed everything | No hierarchy between images | One full-bleed per ~3 screens |

## Before / after

### Crop and focal point

```html
<!-- ❌ recrops from the center; subject sits left of frame in the reference -->
<img src="portrait.jpg" style="width:100%;height:320px;object-fit:cover">

<!-- ✅ ratio reserved, focal point preserved, subject stays in frame -->
<img src="portrait.jpg" width="1600" height="1000" alt="Anna Reyes at the bindery bench"
     style="width:100%; aspect-ratio: 16/10; object-fit: cover; object-position: 28% 22%">
```

### Art direction across breakpoints

```html
<!-- ❌ same 21:9 crop everywhere -->
<img src="hero-wide.jpg" style="width:100%">

<!-- ✅ different crop per context, not just a smaller file -->
<picture>
  <source media="(min-width: 900px)" srcset="hero-21x9.jpg 1600w, hero-21x9@2x.jpg 3200w"
          sizes="100vw" width="1600" height="686">
  <source media="(min-width: 600px)" srcset="hero-3x2.jpg 1200w" width="1200" height="800">
  <img src="hero-4x5.jpg" width="800" height="1000" sizes="100vw"
       alt="The press room during a Tuesday run" style="width:100%;height:auto">
</picture>
```

### Placeholder that earns review feedback

```html
<!-- ❌ -->
<div style="background:#eee;height:200px">Image</div>

<!-- ✅ correct ratio, states what belongs there, survives into the shot list -->
<figure style="display:grid;gap:8px;margin:0">
  <div role="img" aria-label="Placeholder: press room photograph"
       style="aspect-ratio:3/2; border:1px solid var(--color-border);
              background: repeating-linear-gradient(45deg,
                transparent 0 6px, color-mix(in oklch, var(--color-text) 4%, transparent) 6px 12px);
              display:grid; place-items:center; text-align:center; padding:16px">
    <span style="font-size:13px;color:var(--color-text-muted);max-width:34ch">
      Press room, wide, subject at left third · 3:2 · needs 1600×1067 min
    </span>
  </div>
  <figcaption style="font-size:13px;color:var(--color-text-muted)">Caption goes here — one line, names the place and year.</figcaption>
</figure>
```

### Text over image

```css
/* ❌ contrast depends on the photo */
.hero h1 { color: #fff; position: absolute; inset: auto 0 24px 24px; }

/* ✅ scrim sized to the text block, not the whole image */
.hero { position: relative; }
.hero::after { content:""; position:absolute; inset:auto 0 0 0; height:55%;
  background: linear-gradient(to top, rgb(0 0 0 / .62), rgb(0 0 0 / 0)); }
.hero h1 { position:relative; z-index:1; color:#fff; text-shadow: 0 1px 2px rgb(0 0 0 / .3); }
/* verify 4.5:1 against the lightest pixel under the text, not the average */
```

## Rules

### Crop strategy
- **AD-1** Never accept the default center crop. Set `object-position` (or the platform equivalent) from the reference's focal point, and re-check it at every breakpoint. `[FACT]`
- **AD-2** Faces keep ≥8% of frame height above the head and below the chin; products keep ≥5% clear on every cropped edge. Never crop through a face, a logo, or a product silhouette. `[FACT]`
- **AD-3** When the layout's ratio changes by more than ~25% across breakpoints, art-direct with a different crop, not a resize. `[CRAFT]`
- **AD-4** Never letterbox inside a bordered container. Either the crop fits the container or the container takes the image's ratio. `[CRAFT]`
- **AD-5** Never distort: set one dimension, or set both with `object-fit`. `[FACT]`

### Image rhythm
- **AD-6** Hold a deliberate ratio sequence per page (e.g. 3:2, 3:2, 4:5 full-bleed). Write the sequence in the implementation note. `[CRAFT]`
- **AD-7** ≤1 full-bleed image per ~3 viewport heights; a full-bleed image is preceded or followed by a narrow-measure element for contrast. `[CRAFT]`
- **AD-8** One image treatment per role (hero / inline figure / thumbnail / avatar), applied to every instance of that role. `[CRAFT]`
- **AD-9** Informative images get a caption; captions are typographic elements (13–14px, muted, ≤80ch), not tooltips. Whether captions are shown is `[PD]`. `[PD]`

### Placeholders and loading
- **AD-10** Every image reserves its space via `aspect-ratio` or intrinsic `width`/`height`. Zero layout shift. `[FACT]`
- **AD-11** Placeholder = correct ratio + dominant color or blur + a label naming the required subject and minimum pixel size. Never a bare gray box, never in a review build. `[CRAFT]`
- **AD-12** `loading="lazy"` below the fold, eager + `fetchpriority="high"` for the one hero image; `decoding="async"` elsewhere. `[FACT]`
- **AD-13** A failed image collapses to the placeholder treatment, never to a broken-icon box or a 0-height gap. `[FACT]`

### Asset selection
- **AD-14** Select by four mood axes and keep them consistent within a set: **light** (hard/soft), **warmth** (cool/neutral/warm), **depth of field** (flat/shallow), **distance** (macro/human/environmental). `[CRAFT]`
- **AD-15** Grade the set to one look (a single filter/curve applied to all, or all shot the same way). One outlier image is visible immediately. `[CRAFT]`
- **AD-16** Where no photography exists, prefer typographic composition, material fields, diagrams, or the real product surface over stock illustration and 3D blobs. `[CRAFT]`
- **AD-17** Decorative images: `alt=""` and `aria-hidden` where appropriate. Informative: alt describes the information, not the file. Never the filename. `[FACT]`
- **AD-18** Licensing, model releases, and whether a photo can be used in this market are `[PD]` — never assume an asset in the repo is cleared. `[PD]`

### Mood → selection quick table `[PD]` on which row applies

| Brand mood | Light | Warmth | DoF | Distance | Avoid |
| --- | --- | --- | --- | --- | --- |
| Editorial / archival | Soft, directional | Warm | Shallow | Human, environmental | Cutouts on white, high saturation |
| Clinical / precise | Even, diffuse | Neutral-cool | Deep | Macro, product-only | Grain, lens flare, candid crowds |
| Industrial / robust | Hard, high contrast | Neutral | Deep | Environmental, wide | Pastels, soft-focus portraits |
| Warm consumer | Golden, backlit | Warm | Shallow | Human, close | Empty offices, screenshots as hero |
| Institutional / civic | Flat daylight | Neutral | Deep | Architectural, wide | Stock handshakes, gradients |

## Screenshot QA

1. For every image, mark the subject's position in the frame. Does it match the reference? (AD-1)
2. Check every cropped edge for a face, logo, or product boundary within the margin thresholds. (AD-2)
3. Screenshot at 390px, 768px, 1440px. Is any image reduced to a strip or blown up to fill? Are crops art-directed? (AD-3)
4. Look for letterboxing inside any bordered container. (AD-4)
5. Compare a known-square subject's proportions: any horizontal stretch? (AD-5)
6. List the aspect ratios down the page in order. Is there a sequence, or noise? (AD-6, AD-7)
7. Put all images from one surface in a contact sheet. Any outlier in light, warmth, DoF, or distance? (AD-14, AD-15)
8. Throttle to slow 3G; screenshot at 300ms, 1s, 3s. Does anything shift? Does anything pop in without a placeholder? (AD-10, AD-12)
9. Block image requests; screenshot. Does each image slot degrade to a labelled placeholder? (AD-13)
10. Sample the lightest pixel under any text-over-image. Does the text still hit 4.5:1? (AD-1, [AX-21](10-accessibility.md))
11. Read the a11y tree: any alt text containing a filename, "image of", or a hash? (AD-17)
12. In a review build, is any image slot an unlabelled gray box? (AD-11)

## Adapt or override

- **AD-6/AD-7 (rhythm)** don't apply to a uniform grid of like objects — a product catalog, a photo
  archive, a team page. There, identical ratios are the design; enforce a single crop rule instead.
- **AD-1 (no center crop)** is fine to relax for user-generated content at thumbnail size, where a
  face-detection or center crop is the only feasible default. Above ~200px, use focal-point metadata.
- **AD-16 (no illustration)** yields when illustration *is* the brand's art direction — then the
  rule becomes AD-14/AD-15 applied to illustration (one line weight, one palette, one perspective).
- **Editorial/journalistic contexts forbid grading** that alters the content of a news photograph.
  Crop and color changes may be restricted by policy. `[PD]`
- **Performance budgets can override AD-3**: if the extra art-directed asset breaks the budget,
  choose the crop that survives all breakpoints (usually a squarer one) rather than shipping a strip.
- **When the reference has no images**, don't invent them. Build the labelled slots (AD-11), list
  what's needed, and ask. Filling a design with stock photography is a `[PD]` you don't get to make.
