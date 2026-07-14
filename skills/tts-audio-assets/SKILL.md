---
name: tts-audio-assets
description: Generate, regenerate, reuse, audit, and QA text-to-speech audio assets across projects. Use for lesson audio, prompts, UI playback, dialogues, story lines, voice/pacing policy, stale or missing audio audits, naturalness fixes, and audio ID/data wiring.
---

# TTS Audio Assets

Use this skill when spoken audio is a product asset, especially for learning
apps, prompts, dialogue, accessibility playback, or quiz/listening flows.

## Core Rule

Never build a phrase, sentence, dialogue line, or listening prompt by stitching
separate word files together. For anything longer than a standalone vocabulary
item, generate one complete take for the exact text the user should hear.

Reuse an existing audio file only when text, meaning, speaker/context,
politeness/voice form, pacing expectation, and voice all match and the take
sounds natural in the new context.

## Asset Contract

Identify before generating:

- audio ID, source data entry, target file path, and output format;
- displayed text vs spoken text;
- language/script, pronunciation overrides, digits/abbreviations/names;
- meaning, lesson/component, dialogue role, speaker/voice, politeness, pacing;
- generator/provider, credentials/project, voice policy, and audit reports.

Project-specific audio skills should provide exact paths, commands, voices, and
provider settings.

## Workflow

1. Locate the data entry by audio ID and spoken text.
2. Confirm the source data is wired to the intended full text.
3. Search existing files/data for safe reuse.
4. Generate or regenerate only targeted IDs unless the user requests a batch.
5. Avoid broad force regeneration or global voice-policy changes for one rough
   file.
6. Run audio audits and naturalness/duration checks defined by the project.
7. Browser-test playback when UI controls or routing changed.

Use `$course-image-assets` when course data/images change with audio,
`$mobile-web-qa`/`$snapshot` for UI playback evidence, and `$release-gate`
before commit, push, deploy, or handoff.

Use `$efficient-execution` for batches: audit IDs first, regenerate only the
confirmed stale or unnatural takes, and defer human listening to the changed
items plus representative neighbors.

## Text And Voice Rules

- Send the intended spoken text to the TTS provider, not romanization or display
  helper text unless that is what should be heard.
- Preserve learner-facing particles and speaker voice consistency.
- Add spoken overrides for abbreviations, digits, initials, brand terms, mixed
  language, or words the engine may misread.
- For quiz/listening audio, generate what the learner should hear, not merely a
  label or answer key.
- Tune speed/voice only for targeted items unless a broader policy change is
  requested.

## Naturalness QA

Prioritize:

- user-reported chopped, rushed, clipped, discontinuous, or stitched audio;
- suspiciously short/long durations;
- phrase-internal pauses and dialogue voice inconsistency;
- prompts where pacing reveals the answer or hurts comprehension.

Reports and heuristics are triage aids; human listening remains the final check
for naturalness.

## Closeout

Report audio IDs changed, generated/regenerated/reused/left unchanged status,
commands and audits run, UI playback evidence when relevant, voice/pacing
exceptions, and items needing human listening review.
