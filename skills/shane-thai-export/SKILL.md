---
name: shane-thai-export
description: Export Shane and His Thai learner content, scene/dialogue rewrite packets, unit text dumps, Claude/offline HTML handoffs, clickable learner prototypes, and ChatGPT-ready course restructuring briefs. Use when the user asks for /shane-thai-export, Shane Thai exports, ChatGPT content packets, unit exports, learner journey handoffs, dialogue/scene restructure material, or asks what files to give ChatGPT/Claude.
---

# Shane Thai Export

## Scope

Use this skill for export and handoff work in:

`/Users/point/Website Projects/thai-flashcards`

Default to learner-facing content. Do not include Admin Portal material unless the user explicitly asks.

## Decision Tree

1. **ChatGPT content thinking / scene restructure**
   - Export simple Markdown, not code.
   - Give ChatGPT `README.md` plus one unit file at a time.
   - Use `all-units-content.md` only when broad cross-unit context is needed and token size is acceptable.
   - Do not send `.mjs`, app source, test files, or implementation instructions to ChatGPT.

2. **Claude Design / offline HTML / clickable prototype**
   - Use the project export workflow plus `$export-html` if available.
   - Preserve real product behavior and source structure; do not make decorative approximations.
   - Include local assets so Claude can inspect HTML structure and reuse images/media.
   - For UI parity work, pair with `$claude-to-a-tee` and `$snapshot` when those skills are available or requested.

3. **Documentation or handoff**
   - Put generated exports under `docs/content-exports/` or `docs/design-handoffs/`.
   - Include a short README that tells the next reader exactly what to use and what not to use.
   - Keep instructions human-readable; avoid automation-heavy schemas unless the user asks for implementation-ready data.

## ChatGPT Scene Restructure Export

When the user wants ChatGPT to rethink units, scenes, dialogues, or input-first flow, prefer the simple packet format:

```text
docs/content-exports/chatgpt-scene-restructure-simple-YYYY-MM-DD/
  README.md
  all-units-content.md
  unit-01-*.md
  ...
  unit-17-*.md
```

Current generator, if present:

```bash
cd "/Users/point/Website Projects/thai-flashcards"
node tools/export-chatgpt-scene-restructure-content.mjs
```

Before running, inspect the script path/date/output folder. If it hardcodes an old date, patch it or create a fresh output folder so new exports do not overwrite or confuse prior handoffs.

The README should tell ChatGPT:

- The target flow is `Overview -> Scene 1 Dialogue -> Cards from Scene 1 -> Scene 2 Dialogue / Map -> Cards from Scene 2 -> Read -> Story -> Grammar -> Spelling -> Fill -> Quiz -> Listen`.
- The course is moving toward input-first / exposure-first.
- Current dialogues are often too short to maintain context.
- Cards include far more vocabulary/phrases than the dialogue exposes.
- Use prior-unit language for i+1 support.
- Aim for 60-70% of cards to feel like they came from a scene/dialogue.
- Keep 30-40% as expansion cards when they do not fit naturally.
- Do not reduce card count unless a human asks later.
- Keep Listen as assessment/review near the end, not early exposure.
- Do not write code; Codex reconciles implementation later.

## What To Export

For each unit, include text that helps a writer understand the learning material:

- Unit metadata and route.
- Overview/welcome copy.
- Current dialogues/scenes.
- Cards/communication content.
- Vocabulary bank.
- Read and reading activity text.
- Story text.
- Grammar patterns and examples.
- Spelling items.
- Fill/Cloze test text.
- Quiz prompts/options.
- Listening test prompts/options/audio text.

Avoid exporting low-value implementation detail unless the user asks:

- React component code.
- Firebase code.
- Raw audio inventory.
- Asset manifests.
- Test files.
- Internal automation contracts.

## Product Decisions To Preserve

- Do not lower content count by default.
- Do not let a design handoff override established product decisions.
- If a reference/prototype conflicts with prior product choices, preserve the product choice and note the difference.
- Keep Thai, Paiboon, and English available where they are educationally useful.
- Keep Listen/Fill scoring aligned with the current product rule: passing depends on passing required sections, not a single global 75% threshold, unless the user changes this again.

## Verification

After exporting:

1. Run the export command and report success/failure.
2. Confirm the output folder and key files exist.
3. Check unit count and line counts.
4. Spot-check at least one later unit such as Unit 12.
5. Tell the user exactly which files to give ChatGPT or Claude.

For HTML or UI exports, also verify with browser/snapshot evidence and include desktop/mobile when responsive behavior matters.
