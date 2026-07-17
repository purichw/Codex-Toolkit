---
name: image-boundary-safety-map
description: Map risk and choose safe routes for boundary-forward adult non-explicit image prompting. Use when the user asks for stronger sensuality, nudity-adjacent styling, intimate poses, fewer garments, transparent water, bedroom/bathhouse scenes, anything near safety limits, or a risk check before generating; preserve intent without explicit content or safety evasion.
---

# Image Boundary Safety Map

## Core Contract

Map the request to a safe non-explicit route before prompting. The goal is not to bypass safety systems; the goal is to keep the strongest allowable sensual/artistic intent while avoiding explicit anatomy, sexual acts, and repeated blocked prompt families.

When this triggers in `/Users/point/outputs/nudity_reference_prompting`, combine with `$image-boundary-iteration`. Use `$image-boundary-nonexplicit-max` after mapping when the user wants the strongest safe result.

Use simple Thai with the user.

Do not use this map as an excuse to over-refuse or become discreet. Zone 2 and Zone 3 are valid working zones for this project, not warning states. Only Zone 4 and Zone 5 require refusal, backtracking, or recovery.

## Risk Zones

### Zone 1: Stable Safe

Style calibration, identity preservation, ordinary pose, quality polish, or a stable base. A stable adult non-explicit base does not have to be fully clothed: shirtless / bare-torso / open-robe starts are usually the preferred efficient base when lower-frame structure stays non-explicit.

Action: normal prompt or edit.

### Zone 2: Sensual Non-Explicit

Bare shoulders, open robes, close gaze, romantic lighting, pool/bath/bedroom atmosphere, mild intimacy, visible torso.

Action: one controlled push axis is fine.

### Zone 3: Max Non-Explicit

Minimal costume bulk, hairline cords, transparent water, strong skin-read, seated/reclining leg silhouettes, close triangular group, non-explicit lower-frame structure.

Action: use `$image-boundary-nonexplicit-max`; preserve crop/water/shadow/refraction as safety structure. Do not downgrade to fully clothed or distant composition unless a block/reject requires recovery. Generate once and wait for verdict.

### Zone 4: Risk Cliff

Requests focus on explicit lower-frame detail, direct underwear removal, porn-like goals, sexual acts, arousal detail, or repeated stronger variants after blocks.

Action: translate to allowed visual design language or refuse the explicit part. Do not retry as euphemism.

### Zone 5: Blocked Family

A prompt family has blocked once or twice, or local edits repeatedly create unsafe/ugly lower-frame artifacts.

Action: use `$image-boundary-rejection-recovery`; backtrack or redraw.

## Route Selection

- User asks `แรงสุดแต่ non-explicit`: use `$image-boundary-nonexplicit-max`.
- User asks `ทำไมโดน block / reject`: use `$image-boundary-rejection-recovery`.
- User asks quality/anatomy/water polish: use `$image-boundary-polish`.
- User asks normal PASS/PARTIAL/REJECT continuation: use `$image-boundary-iteration`.
- User is unsure which skill applies: use global `$image-boundary`.

## Base Mapping

- `safe base`: adult non-explicit, identity-stable, quality-stable. It may be shirtless/open-robe with clear torso visibility.
- `conservative reset`: fully clothed or armored only when recovering from repeated blocks, matching costume identity, or explicitly requested.
- `max non-explicit base`: shirtless/open torso, low costume bulk, strong skin-read, lower-frame protected by crop/water/bedding/shadow/refraction.

Prefer a shirtless/open-torso base over a fully clothed base when the user's goal is boundary-forward sensual iteration. Do not add unnecessary shirts, armor, pants, or bulky drapery just to make a base feel safe.

## Translation Table

Keep intent strong, but change the wording surface:

- `porn-like / explicit`: cannot fulfill directly; translate to `max-boundary non-explicit sensual figure-study`.
- `ถอดหมด`: `minimal visible costume bulk with non-explicit crop/refraction/light structure`.
- `เห็นหว่างขา`: `clear upper-leg separation / negative space, featureless and non-explicit`.
- `เห็น body parts ใต้น้ำ`: `soft broad underwater silhouette and marble-floor visibility; no precise anatomical detail`.
- `ลดผ้า`: `remove bulky fabric forms; preserve hairline cords or light accents`.
- `intimate มากขึ้น`: `closer gaze, leaned-in posture, triangle composition, restrained sensual tension`.

## Prompt Hygiene

Do:

- name the artistic mechanism;
- preserve accepted identity and branch;
- push one axis at a time;
- keep lower-frame structure non-explicit;
- use positive visual goals.

Do not:

- include jailbreak, bypass, or evasion instructions;
- stack bedroom + lower-frame reveal + anatomy sharpening;
- repeat blocked language with synonyms;
- use long negative lists that make the prompt read like a workaround;
- let quality degrade while chasing boundary.

## Output Before Generation

Before image generation, tell the user:

- selected zone;
- selected route/skill;
- one-sentence translated goal;
- exact prompt.

After generation, wait for `PASS / PARTIAL / REJECT`.
