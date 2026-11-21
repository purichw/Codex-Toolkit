---
name: ai-video-creator
description: Create or revise videos with AI narration, including screen-recorded product demos, explainers, and walkthroughs. Use when the job involves planning or recording visuals, generating voiceover, syncing speech to on-screen actions and captions, or fixing timing or pronunciation in an existing video.
---

# AI Video Creator

Use the supplied assets, project brief, and previous approved export to establish the audience, purpose, duration, language, voice, and deliverable. Choose an editor or local pipeline that can preserve the intended quality and timing. For a targeted correction, identify the spoken phrase and scene in the current export and work from that revision.

## Produce the video

1. **Write to the visuals.** Give each scene a job and an ending state. Open with the context the viewer needs, then show a complete example in the order they would use it. Put explanations before or beside the relevant action. Describe verified product behavior, distinguishing mockups, examples, and planned features when that affects what the viewer would infer.
2. **Capture the evidence.** Use the running product for a live-product walkthrough. Start from a clean viewport with a readable size and enough framing for the complete result. Record through the final state of each action. Use provided or generated assets for illustrations where they fit the brief. Check that capture and export omit unrelated windows, notifications, and private data.
3. **Generate narration by complete thought.** Use the approved voice, locale, and speaking style when revising a video. Keep editable caption text separate from the text sent to synthesis so names, numbers, abbreviations, and loanwords can have spoken overrides. Generate each new or revised sentence or coherent passage as one take. Use provider-supported phrasing and pause controls, placing pauses at natural thought or list boundaries. Keep grammatical phrases together. Use `tts-audio-assets` if available for more detailed TTS asset guidance.
4. **Sync to actual speech.** Time the edit from the recorded take. Mark the words that introduce each click, filter, reveal, or resulting state, and place the corresponding shot near those words. Keep the final state visible long enough to read. Derive captions from the same timing and verify line breaks and captions around cuts.
5. **Audit the exported file.** Inspect the opening, ending, affected scenes, and neighboring transitions for readable framing, accidental overlays, long loading, caption fit, synchronization, complete words, and abrupt audio joins. Listen to important lines when playback is available. Otherwise state the scope of any waveform, pitch, transcription, or frame checks. Verify the requested duration and format. Return the actual playable export and any requested sidecars.

## Revise an existing video

Match feedback to the quote, visible action, and latest version. If the time is approximate, search the transcript or captions before changing the timeline. Prefer a new complete take for the affected line. Try different input phrasing or pronunciation controls before applying post-processing. Fit within the existing scene if it still sounds natural. When a change needs room, retime the affected shot or captions and check any shifted anchors.

Keep the previous export recoverable. Reuse the approved media outside the affected scenes. For audio-only fixes, copy the approved video stream when possible. Verify the final export after mixing and encoding.

For scene timing, Thai narration, local revisions, and QA, read [editing and QC](references/editing-and-qc.md). Run [check_export.py](scripts/check_export.py) when technical verification of a local file would help.
