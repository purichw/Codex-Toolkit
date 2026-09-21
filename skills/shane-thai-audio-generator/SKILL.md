---
name: shane-thai-audio-generator
description: Generate, regenerate, audit, and QA Google Chirp audio files for the Shane Thai learning app. Use when the user mentions Shane Thai audio or when Codex works on lesson audio, main-course Chirp generation, audio ID wiring, Thai TTS text, voice selection, full-phrase regeneration, stale/missing audio audits, pronunciation, pacing, or naturalness fixes for this project.
---

# Shane Thai Audio Generator

Use `$tts-audio-assets` for the reusable TTS/audio asset workflow. This skill is
the Shane Thai overlay: project paths, Google Chirp commands, voice
policy, and course-data wiring.

Use this skill for Shane Thai audio asset work, especially Google Chirp TTS for lesson words, phrases, sentences, dialogues, story lines, grammar examples, spelling prompts, read prompts, quiz/listening prompts, and UI audio buttons.

## Core Rule

Never build a phrase, sentence, dialogue line, or listening prompt by stitching separate word files together.

For anything longer than a single standalone vocabulary item, generate one complete Google Chirp take for the exact Thai text that the learner should hear. Reuse an existing audio file only when the Thai text, meaning, speaker/context, politeness particle, pacing expectation, and voice are all compatible and the existing take sounds natural.

If the user says an audio item sounds chopped, rushed, discontinuous, or like reused pieces, treat that as a likely asset bug. Regenerate the exact phrase or sentence as one full take instead of defending the old reuse.

## Project Context

- Repo: `/Users/point/Website Projects/thai-flashcards`
- Main-course Chirp output: `public/audio/chirp/main-course/<unit-id>/<audio-id>.mp3`
- Romanized Thai / Word Bank Chirp output:
  `public/audio/chirp/romanized-thai/<hash-prefix>/<audio-id>.mp3`
- Packed Romanized Thai / Word Bank output:
  `public/audio/chirp/romanized-thai-packs/<hash-prefix>.pack`
- Main-course audio helper: `src/data/mainCourseAudio.ts` via `mainCourseAudio(unitId, itemId, text, labelOrOptions?, options?)`
- Generator: `tools/generate-main-course-chirp-audio.mjs`
- Romanized Thai generator: `tools/generate-romanized-thai-chirp-audio.mjs`
- Romanized Thai packer: `tools/pack-romanized-thai-audio.mjs`
- Romanized Thai audio manifest JSON writer:
  `tools/write-romanized-thai-audio-manifest-json.mjs`
- Audit: `tools/audit-chirp-audio.mjs`
- Naturalness triage: `tools/audio-naturalness-triage.mjs`
- Voice policy: `tools/chirpVoicePolicy.mjs`
- Audio audit report: `docs/audio-audit.json`
- Naturalness report: `docs/audio-naturalness-triage.md`

Common commands:

```bash
npm run audio:main-course
npm run audio:main-course:force
npm run audio:romanized-thai
npm run audio:romanized-thai:pack
npm run romanized:audio-manifest-json
GOOGLE_TTS_FORCE=true GOOGLE_TTS_ONLY='unit-id/audio-id,unit-id/other-audio-id' npm run audio:main-course
GOOGLE_TTS_FORCE=true GOOGLE_TTS_SPEAKING_RATE=0.78 GOOGLE_TTS_ONLY='unit-id/audio-id' npm run audio:main-course
AUDIO_NATURALNESS_ONLY='unit-id/audio-id' npm run audio:naturalness
npm run audio:audit
npm run audio:audit:check
npm run audio:naturalness
npm run audio:naturalness:check
```

Voice overrides are available through environment variables and data-level audio options. Check `tools/chirpVoicePolicy.mjs` before assuming current defaults.

```bash
GOOGLE_TTS_MALE_VOICE='th-TH-Chirp3-HD-Iapetus'
GOOGLE_TTS_FEMALE_VOICE='th-TH-Chirp3-HD-Despina'
GOOGLE_TTS_FORCE_MALE=true
GOOGLE_TTS_FORCE_FEMALE=true
GOOGLE_TTS_SPEAKING_RATE=0.82
GOOGLE_TTS_PITCH=0
GOOGLE_OAUTH_ACCESS_TOKEN='<token>'
```

The npm scripts set `GOOGLE_CLOUD_PROJECT=thai-chirp-20260613`. The generator
can also use `gcloud config get-value project` and `gcloud auth print-access-token`;
if auth is missing, ask the user to run the appropriate Google auth command
instead of faking or hand-writing audio files.

Use adjacent skills when the task crosses boundaries:

- `$tts-audio-assets` for the global TTS asset contract, reuse rules, naturalness
  QA, and closeout.
- `$shane-thai-image-assets` when lesson data, vocabulary IDs, badges, or card
  mappings change alongside audio.
- `$reference-to-a-tee` when audio controls or lesson UI must match a Claude
  Design reference exactly.
- `$mobile-web-qa` and `$snapshot` when audio-button behavior or layout must be
  verified visually across responsive routes.
- `$efficient-execution` for batch scoping, targeted generation, and avoiding
  full-course regeneration when focused IDs are enough.
- `$release-gate` before commit, push, deploy, or handoff.

## Workflow

1. Identify the audio item before generating:
   - unit ID and lesson/component
   - audio ID and target output path
   - displayed Thai text
   - actual spoken Thai text if different
   - English meaning
   - speaker, gender, politeness particle, and dialogue role
   - whether the item is a word, phrase, sentence, story line, dialogue turn, grammar example, quiz prompt, or UI prompt

2. Confirm the source data is wired to the intended full text:
   - Prefer existing helpers such as `mainCourseAudio(...)` and local course data patterns.
   - Search by both `audio ID` and Thai text before editing, because some units use wrapper helpers such as `greetingsAudio`, `daysAudio`, `monthAudio`, or runtime-collected audio objects.
   - For Romanized Thai / Thai Word Bank audio, treat `src/data/romanizedThaiAudioManifest.ts` as the committed source of audio readiness. The ignored `public/data/romanized-thai-audio-manifest.json` is generated for the worker at build time and should not be hand-edited or committed.
   - Do not change lesson IDs, order, routes, progress keys, quiz IDs, audio IDs, image IDs, or Firebase keys unless explicitly asked.
   - If adding a new kind of audio source, update the generator and audit collectors together.

3. Check reuse safely:
   - Search existing data and files for the same Thai text and same audio ID pattern.
   - Reuse only when the existing take is exactly appropriate.
   - If text is the same but speaker, context, listening task, politeness, or pacing differs, generate a separate file.

4. Generate or regenerate with a narrow target:
   - Use `GOOGLE_TTS_ONLY` for targeted work.
   - Use `GOOGLE_TTS_FORCE=true` only for files intentionally being replaced.
   - Use speaking-rate overrides only for the targeted generation batch unless a broader policy change is requested.

5. Audit and verify:
   - Run `npm run audio:audit` after generating files so `docs/audio-audit.json` reflects current durations and hashes.
   - Run `npm run audio:naturalness` when checking phrase continuity, duration outliers, clipping, or rushed speech. Use `AUDIO_NATURALNESS_ONLY='unit-id/audio-id'` for focused triage.
   - Use `:check` commands in release gates, but remember check mode should not be the only step after new generation if reports need updating.

## Fast Targeted Loop

Use this loop for user-reported bad audio or small batches:

1. Locate the data entry with `rg` using the audio ID and Thai text.
2. Confirm the spoken Thai text, label text, voice, and output path.
3. Regenerate only the affected IDs with `GOOGLE_TTS_ONLY`; add `GOOGLE_TTS_FORCE=true` only when replacing existing files.
4. If the generator says no metadata matched `GOOGLE_TTS_ONLY`, treat the unit ID or audio ID as wrong and fix the source mapping before generating.
5. Run `npm run audio:audit` and targeted/full `npm run audio:naturalness`.
6. If the phrase still sounds unnatural, try a targeted speaking-rate or voice override; do not make a global voice-policy change for one rough file.

## Reuse Rules

Reuse is allowed when all are true:

- The Thai script text is identical.
- The heard form is identical, including particles such as `ครับ` and `ค่ะ`.
- The English meaning and lesson context match.
- The speaker/voice expectation matches.
- The existing audio sounds natural in the new context.

Generate a new full take when any are true:

- A sentence is currently represented by word-level or phrase-level pieces.
- The phrase has an unnatural pause inside a compound or between noun/adjective pieces, such as `ห้อง เรียนใหญ่`.
- The audio sounds clipped, too fast, too slow, monotone in a distracting way, or cut off at the start/end.
- A dialogue line needs a specific speaker voice.
- The item is a listening prompt, quiz answer, story line, or grammar example where natural whole-line delivery matters.
- The same Thai appears in a different role where pacing should change.

## TTS Text Rules

- Send Thai script or explicit spoken Thai to Google Chirp, not Paiboon romanization.
- Do not use IPA.
- Preserve learner-facing particles exactly unless the source content explicitly says otherwise.
- Use a data-level spoken override for abbreviations, initials, digits, English names, brand-like tokens, or terms Chirp may misread.
- For school names, company names, UI labels, and mixed-language phrases, add a spoken Thai form if the raw text will be pronounced poorly.
- For quiz/listening audio, generate what the learner should hear, not merely the answer label or display heading.
- For alphabet/letter-name audio, use the intended Thai letter name, not a bare consonant if the learning task expects the letter-name pronunciation.

## Voice And Pacing

- Check `tools/chirpVoicePolicy.mjs` for current default male/female Chirp voices.
- Keep named speaker voices consistent inside a dialogue or story sequence.
- Use explicit voice options when a line belongs to a named speaker or the lesson data already encodes role/gender.
- Do not globally change the voice policy to fix one rough file.
- For a rough phrase, regenerate that exact audio ID as full Thai text first; then try a targeted speaking rate or alternate Chirp voice only if needed.
- When tuning speed, keep beginner listening needs in mind: clear and natural beats, not robotic over-enunciation.
- Use `GOOGLE_TTS_FORCE_MALE=true` or `GOOGLE_TTS_FORCE_FEMALE=true` only for intentional same-voice regeneration passes.

## Naturalness Audit

The naturalness report is a triage aid, not a substitute for listening judgment.

Prioritize:

- user-reported audio bugs
- phrases/sentences with suspiciously short durations
- files flagged as likely stitched or internally paused
- dialogue sequences with inconsistent voices
- grammar and story lines that sound like isolated word chunks
- quiz/listening prompts where the answer is unintentionally obvious from odd pacing

If a naturalness check flags many files, fix the lesson-critical and user-visible items first. Record what was regenerated and what was intentionally left unchanged.

## Generation Checklist

Before generating:

- Confirm data and audio IDs are correct.
- Confirm the Thai text should be spoken exactly as written or add a spoken override.
- Confirm speaker/voice and politeness particle.
- Confirm the file is not being safely reused already.

During generation:

- Use `GOOGLE_TTS_ONLY` for the specific IDs.
- Use `GOOGLE_TTS_FORCE=true` only when replacing existing files.
- Avoid broad force regeneration unless the user explicitly asks for a whole-unit or whole-course pass.

After generation:

- Run `npm run audio:audit`.
- Run `npm run audio:romanized-thai:pack` and
  `npm run romanized:audio-manifest-json` when Romanized Thai / Thai Word Bank
  audio files changed.
- Run `npm run audio:naturalness` for phrase/sentence batches.
- Inspect changed files and data references.
- Verify audio buttons in the UI when practical, especially for the component the user reported.

## Release Gate

Before commit, push, deploy, or handoff after audio changes:

```bash
npm run audio:audit:check
npm run audio:naturalness:check
npm run test:data
npm run build
```

Use narrower validation only when the change is tiny and clearly isolated, such as a single regenerated file with no data change. Say what was not run and why.

For UI-affecting audio work, browser-test the affected routes and check:

- the audio button is present
- the requested file loads successfully
- no console/page errors occur
- replay works
- active/completed tab state is unchanged by merely playing audio unless the product behavior requires it

If audio and image/course-data mappings changed together, run the relevant image
audit from `$shane-thai-image-assets` as well; keep one combined asset report
instead of separate partial summaries.

## Reporting

When finishing audio work, summarize:

- which unit/component/audio IDs changed
- whether each item was generated, regenerated, reused, or left unchanged
- which commands were run
- adjacent Shane image/course-data checks when relevant
- any items still needing human listening review
