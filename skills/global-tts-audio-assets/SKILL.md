---
name: global-tts-audio-assets
description: Global reusable alias for the canonical tts-audio-assets skill. Use when the user asks for $global-tts-audio-assets, says this should be global or non-project-specific, or wants the reusable version of tts audio assets. This alias routes to tts-audio-assets/SKILL.md; keep tts-audio-assets as the source of truth.
---

# Global Tts Audio Assets

This is a global alias for the canonical `tts-audio-assets` skill.

Before acting, read and follow the canonical skill:

```text
../tts-audio-assets/SKILL.md
```

Follow the canonical skill's `$snapshot` and visual-evidence requirements
whenever they apply. Do not treat this global alias as a way to bypass the
canonical snapshot gate.

Use this alias when the user explicitly wants the global, reusable, or non-project-specific variant. Keep `tts-audio-assets` as the source of truth; update the canonical skill first, then regenerate this alias if the routing language needs to change.
