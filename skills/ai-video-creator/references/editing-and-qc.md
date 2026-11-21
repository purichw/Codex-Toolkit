# Editing and QC

## Plan from scenes and anchors

For work involving several clips, keep a scene list or use the editor's timeline as the source of timing. Useful fields are scene ID, visual source and source in/out, output start and end, visible actions and results, display copy, exact synthesis input, selected take, and cue times measured from the selected take. Add the expected end state and any duration limit from the brief. Record speech and visuals separately when doing so allows a cleaner performance and precise cuts.

For a product demo, a common sequence is what the product is for, first screen, a representative task through its result, then the next action or output. Accounts and admin areas may need authorized data or a safe demo account. Include real navigational context and the finished workflow within scope. Trim unnecessary loading or repeated actions while preserving the transition the audience needs to understand.

For generated images or video, keep the intended aspect ratio and allow room for captions and framing. Label illustrative visuals when viewers could mistake them for real evidence. Keep the supplied brand, palette, and typography when the brief calls for continuity.

## Synthesize and choose a take

Record the provider, voice, locale, synthesis text, and chosen asset alongside the edit. Render complete lines or speech beats. Review sentence starts, stressed terms, and tails. Reuse an approved take when the words, speaker, context, and delivery still fit. Generate a few targeted variations when a reported pronunciation or pause survives one retake.

For Thai speech, place a sentence boundary after a completed idea and separate list items with short beats. Keep prepositions and nouns together in phrases such as “เหนือแผนที่”. Caption “Excel” if that is what the interface displays and give the synthesizer the desired spoken form “เอ็กเซล”. A spelling that looks correct can still produce the wrong tone. Compare candidate takes at the actual syllable and use the pitch contour as supporting evidence when tone is disputed. Review the resulting voice in the adjoining phrase when listening is available. Align new captions to the edited audio after retiming.

Google Chirp is one option. Use the approved voice or project configuration, such as Thai Chirp 3 HD Achird for a demo that already uses it. Check the [Google Chirp documentation](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd) for controls supported by the selected request mode and locale. Apply pause or pronunciation controls only where needed and verify their effect in the generated audio. Preserve the approved provider unless a change is needed or requested.

## Edit and sync

- Measure anchor times from the selected audio. For example, at “พึ่งน้ำฝน” the corresponding filter should be available or its effect should be appearing. Keep the map visible while the narration explains the result.
- Use the editor's actual frame rate and sample rate when deriving offsets. For local fixed-length edits, derive scene boundaries from source frames or timestamps and map them to samples once to avoid cumulative rounding. Keep within the existing duration when the take fits naturally. Trim outer silence carefully so quiet consonants and tails stay intact.
- For a pause and caption change, split the caption at the speech boundary and leave room for delivery. For a pronunciation-only fix, keep the wording on screen when it is still accurate.
- For an isolated narration replacement, match the surrounding voice level, fit the full take in the scene, and reuse the prior video track. If captions are burned into the picture and need edits, render the affected shots and reuse other shots when compatible. Use a new export path.
- Check the chosen anchors in the encoded video. Verify narration around the retake, its neighboring transitions, and the corresponding visible state. Use waveform or transcription timestamps for location and pitch analysis for a disputed tone. These checks complement listening.

## Local technical checks

The helper uses Python 3 and FFmpeg/FFprobe. It probes the exported file and checks for video and, when requested, audio. The optional duration arguments compare the container's duration. `--decode` checks for decoding errors. `--same-video-as` compares the first video stream's encoded packets and timing directly. Use it when the video was copied for an audio-only fix.

```sh
python3 scripts/check_export.py demo.mp4 --require-audio --max-seconds 300 --decode
python3 scripts/check_export.py demo-revised.mp4 --require-audio --decode \
  --same-video-as demo.mp4
```

This helper measures file-level properties. Check actual loudness and peaks if a mix changed, and inspect the affected audio and pictures for silence, clipped speech, and semantic sync. When delivering a sidecar subtitle file, confirm the cues match the delivered runtime and text.
