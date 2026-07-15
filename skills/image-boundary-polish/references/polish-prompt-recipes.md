# Polish Prompt Recipes

Use these as compact prompt ingredients. Keep the final image prompt task-local and shorter than this reference.

## Generic Edit Recipe

```text
Use case: precise-object-edit
Asset type: quality restoration
Input image: edit target; preserve the same composition, identities, faces, hair, pose, lighting, scene, hands, accepted boundary level, and non-explicit lower-frame structure.

Targeted edit only: restore image quality and clarity. Clean up muddy rendering, noisy artifacts, warped linework, uneven shading, distorted hands, face drift, fractured reflections, and background geometry issues. Repaint with crisp linework, polished faces, clean hair shapes, readable hands, smooth torso modeling, coherent shoulders and arms, clear scene geometry, luminous water/light, and controlled texture.

Keep the boundary level, waterline/crop, and lower-frame structure essentially unchanged. Do not add new body detail, do not lower the water further, do not change poses, do not add clothing bulk, and do not add extra characters. Maintain tasteful non-explicit fantasy art. No text, no logo, no watermark.
```

## Watercolor Trio Recipe

```text
Use case: precise-object-edit
Asset type: watercolor fantasy trio quality restoration
Input image: edit target; preserve the same three adult fantasy characters, same composition, identities, faces, hair colors, direct triangular gaze, pose, waterline, lantern-lit palace setting, jewelry, thin robe-edge lines, hands, and non-explicit lower-frame structure.

Targeted edit only: restore watercolor quality and clarity without changing the boundary level. Clean up broken or muddy rendering, noisy paper texture, warped linework, uneven skin shading, distorted hands, fractured water reflections, and marble geometry noise. Repaint with crisp elegant watercolor linework, polished faces, clean hair shapes, readable hands, smooth torso modeling, coherent shoulders and arms, clear marble steps, luminous blue water, and warm lantern reflections.

Keep the waterline and lower-frame structure essentially the same as the reference image. Do not add new body detail, do not lower the water further, do not change poses, do not add clothing bulk, and do not add extra characters. Maintain tasteful non-explicit fantasy art. No text, no logo, no watermark.
```

## Bedroom Editorial Recipe

```text
Use case: precise-object-edit
Asset type: moonlit bedroom watercolor quality restoration
Input image: edit target; preserve identities, triangular grouping, tight crop, hands, pillows, bedding shadows, arched windows, lantern light, one hairline-thin sash/cord per character, and the accepted non-explicit lower-frame structure.

Targeted edit only: restore clarity. Repair faces, hands, hair, torso modeling, bedding folds, shadow coherence, window geometry, and watercolor texture. Keep crop, pose, and boundary level unchanged. Do not add new lower-frame detail, do not shift the crop to reveal more, do not add bulky bedding or costume, and do not change the intimacy level.
```

## Red Flags

Start a separate boundary iteration instead of using this skill when the prompt needs:

- a lower waterline;
- fewer garments;
- stronger intimacy or a new pose;
- more visible lower-frame anatomy;
- a different scene or camera angle.

If those needs are mixed with quality repair, do quality first and boundary second.
