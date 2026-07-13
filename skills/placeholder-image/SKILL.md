---
name: placeholder-image
description: Source, select, replace, crop, and audit placeholder images for websites, apps, decks, or prototypes. Use when the user asks to populate missing images, replace placeholders, find better hero/card/gallery photos, make images match a mood or content type, fix bad crops/object-position, audit responsive image reuse, remove low-quality stock/watermarked images, or create an image sourcing playbook for travel, hospitality, lifestyle, activity, product, or content-heavy pages.
---

# Placeholder Image

Use this skill when images are part of the product experience, not decoration. Treat every image as content with a job: communicate the offer, activity, room, place, product, or mood at a glance while surviving real responsive crops.

## Operating Standard

Do not fill placeholders with merely "nice" images. Match all of these:

- **Meaning:** the photo must show the thing the surrounding text claims.
- **Mood:** the image must reinforce the brand tone, not fight it.
- **Quality:** no watermarks, obvious low-end stock, fake staging, awkward AI artifacts, or visibly low resolution.
- **Crop resilience:** the subject must remain readable across every reused container.
- **Licensing:** use images that are licensed, supplied, generated for the project, or clearly acceptable for the prototype context. Record source and license when using external assets.
- **Implementation:** preserve performance, alt text, responsive layout, and image behavior.

If the task affects a production or partner-facing prototype, inspect the rendered page. Do not rely only on file paths or a mental model of the layout.

## Image Brief

Before searching or replacing, write a compact brief per image slot:

```text
Slot: homepage hero right side
Job: cozy social arrival, not party chaos
Subject: mixed group around shared table, warm interior
Container: wide hero, text on left, subject must live right/center-right
Avoid: luxury restaurant, family dinner, nightclub, dark blur
Crop: 16:9 desktop, tall mobile, right side can be visible behind overlay
```

For repeated cards, include the entity type:

```text
Slot: Thai Cooking Class card
Subject: travelers cooking together in a kitchen or prep table
Avoid: family home cooking, chef portrait, plated food only
Crop: card image, mobile stacked card, detail hero
```

## Sourcing Rules

Use browsing or image search when the user asks to find images or when current assets are unknown. Favor:

- supplied client assets first;
- official venue/partner media when available and allowed;
- reputable open-license or clearly licensed libraries;
- generated images only when realism, rights, and artifacts can be controlled;
- unsplash/pexels-style sources only when the image does not look generic, cheap, or mismatched.

Reject images with:

- watermarks, agency marks, UI overlays, text baked into the image, or screenshots of websites;
- "budget hostel" signals when the brand should feel upper-middle or design-aware;
- wrong activity object, such as bicycles for a scooter route or a family kitchen for a social hostel class;
- composition that depends on faces/actions at the extreme edges;
- overly intense nightlife when the desired tone is cozy socializing;
- luxury-hotel cues when the offer is communal or backpacker-friendly;
- tourist images that fail to sell the location as worth visiting.

For hospitality/travel/activity pages, prefer images with human scale plus place/action:

- rooms: beds, lockers, curtains, lamps, privacy, real dorm/private-room type;
- food: people eating or preparing food together, not food-only unless the section is culinary detail;
- tours: recognizable place, scale, and destination value;
- social: warm eye-level moments, low-pressure groups, shared tables, courtyard drinks;
- wellness: calm group activity, not spa-luxury unless the brand supports it.

## Generated Image Workflow

Use the system `imagegen` skill/tool when generating or editing raster images. Before the image call, state the exact prompt, target slot, crop/aspect requirements, and intended file or use. After the tool returns, do not add extra text in the same response; let the image output stand and continue evaluation in the next turn or next message.

Keep prompts task-local: include subject, mood, crop/aspect needs, brand constraints, and "no text or watermark." Do not paste full audit notes, source lists, or unrelated implementation details into the prompt.

## Selection Criteria

Choose images by scoring them informally:

- **Content accuracy:** Does it literally match the label?
- **Brand fit:** Does it feel like this product, not another category?
- **Centerpiece:** Is there one readable subject or action?
- **Crop tolerance:** Can it work in wide, square, and tall frames?
- **Overlay tolerance:** Can text/chips sit on it without hiding the subject?
- **Color fit:** Does it harmonize with the page palette after overlays?
- **Series consistency:** Do all images in the section look like one brand world?

When two images are close, choose the one with better crop tolerance and stronger content truth.

## Crop And Object Position

Default to `object-fit: cover`, then set `object-position` per image. Do not leave all images at `center center` if the subjects differ.

Use these heuristics:

- **Hero with left copy:** subject on right or center-right; avoid important faces under the headline.
- **Hero with centered copy:** subject can sit behind overlay but must not create noisy contrast under text.
- **Horizontal cards:** keep the action near the central 40-60% of the frame.
- **Vertical cards/mobile:** faces, hands, food, beds, vehicles, or landmarks must remain inside the safe middle band.
- **Room photos:** show the bed type and privacy features; avoid crops that hide the bed count or room class.
- **Activity cards:** the action should be instantly visible above the fold of the card image.
- **Location/tour photos:** show enough environment to feel grand, not just a tight tourist portrait.

Useful `object-position` patterns:

```css
/* face/action slightly right */
object-position: 62% 45%;

/* landmark needs more sky/top */
object-position: center 35%;

/* table/action is lower in the source */
object-position: 50% 62%;

/* hero image pushed away from left text */
object-position: 72% center;
```

If the same asset is reused in different aspect ratios, store per-use crop metadata instead of forcing one global crop.

## Implementation Rules

Make image data semantic and auditable:

```js
{
  id: "thai-cooking-class",
  label: "Thai Cooking Class",
  src: "/images/events/thai-cooking-class.jpg",
  alt: "Travelers preparing food together during a Thai cooking class",
  position: "52% 48%",
  source: "Client asset / licensed source"
}
```

Use descriptive filenames:

```text
hero-communal-dinner.jpg
room-6-bed-social-dorm.jpg
event-scooter-food-route.jpg
location-wat-arun-sunset.jpg
```

Avoid filenames like `image1.jpg`, `stock-photo.jpg`, or stale labels that hide wrong content.

Add alt text that describes the visible content, not the marketing slogan. If an image is decorative only, mark it appropriately in the project style.

Use responsive `srcset` or optimized image components when the framework supports them. For static prototypes, keep files reasonably sized and verify load behavior.

## Responsive Verification

After replacing images, render and inspect every affected route and component:

- desktop wide;
- tablet;
- common mobile;
- the smallest mobile width the project supports;
- scrolled states where cards/galleries appear;
- language variants when text layout can change.

Check:

- no subject is cropped at an obviously wrong place;
- no face/action/landmark is hidden under chips, buttons, text, or overlays;
- cards in a grid feel like one intentional set;
- hero text remains readable;
- no broken assets, console errors, or failed network requests;
- no horizontal overflow from galleries or oversized labels;
- image quality holds up at displayed size.

Use bounding boxes and screenshots when the crop or overlap is user-visible. If a user called out a specific card or route, re-check that exact container after editing.

## Hospitality And Activity Tone Cheatsheet

Use these examples as portable heuristics, not hard-coded hostel rules:

- **Cozy social:** shared table, courtyard drinks, board games, low-pressure conversation, warm lights.
- **Not cozy social:** nightclub chaos, drunk crowd, posed influencer party, anonymous dark bar.
- **Upper-middle hostel:** clean bedding, privacy curtains, warm lighting, real lockers, tidy common areas, active but calm guests.
- **Not upper-middle hostel:** messy bunk room, harsh fluorescent dorm, institutional blue walls, cheap party stock.
- **Grand location:** recognizable landmark, skyline, temple scale, river/city context, golden hour.
- **Weak location:** tight crop of tourists with no sense of place.
- **Cooking class:** multiple travelers preparing ingredients or cooking together.
- **Weak cooking:** family home dinner, chef-only portrait, food plating without people.
- **Scooter/route:** visible scooter/e-scooter/tour route context plus city/food stop.
- **Weak scooter/route:** bicycle, generic motorcycle traffic, parked scooter with no travel story.

## When Images Are Not Available

If suitable external images cannot be found quickly:

- say what is missing and why existing candidates fail;
- propose generated-image prompts that preserve the brand and crop requirements;
- create temporary visual placeholders only if clearly marked in the implementation data, not in visible UI copy;
- prefer abstract pattern blocks only for truly decorative areas, never for product-critical rooms, activities, locations, or hero scenes.

## Closeout

Report:

- routes/components touched;
- image sources or generation method;
- notable crop/object-position choices;
- responsive viewports checked;
- any intentional compromises, such as prototype-only licensing or unavailable exact activity imagery.
