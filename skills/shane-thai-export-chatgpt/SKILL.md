---
name: shane-thai-export-chatgpt
description: Export Shane and His Thai learner lesson content into ChatGPT-ready patch packets. Use when the user invokes /shane-thai-export-ChatGPT, $shane-thai-export-chatgpt, asks to export all lessons for ChatGPT, asks for lesson patch packets, wants ChatGPT to patch lesson content easily, or needs packets flexible enough for future learner tabs/modules such as Passage Reading.
---

# Shane Thai Export ChatGPT

## Purpose

Create a self-contained Markdown export of Shane and His Thai learner lesson content for ChatGPT. The export is optimized for patching lesson data, not design parity or admin work.

Default project:

```text
/Users/point/Website Projects/thai-flashcards
```

Default output:

```text
docs/content-exports/chatgpt-lesson-patch-YYYY-MM-DD/
```

## Workflow

1. Inspect repo status first.
   - Do not commit, push, deploy, or revert changes unless the user asks.
   - Exporting docs is safe even with source changes, but state if the export reflects a dirty worktree.
2. Run the bundled generator:

```bash
node /Users/point/.codex/skills/shane-thai-export-chatgpt/scripts/export-chatgpt-lesson-patch.mjs \
  --repo "/Users/point/Website Projects/thai-flashcards" \
  --overwrite
```

3. Verify:
   - Output folder exists.
   - 17 `unit-*.md` files exist.
   - `README.md`, `PATCH_PROTOCOL.md`, `TAB_EXTENSION_PROTOCOL.md`, `SOURCE_MAP.md`, `ALL_UNITS_COMPACT.md`, and `all-units-content.md` exist.
   - Spot-check Unit 13 or another requested unit.
4. Tell the user exactly which files to give ChatGPT.

## Export Contents

Each unit packet includes:

- Unit metadata and route.
- Owner source file(s) and shared source files.
- Stable ID map by section.
- Current data keys for welcome/overview, dialogue, cards, vocabulary, read, story, grammar, spelling, quiz, fill/cloze, listening, scene-first plan, and QA/design notes.

The folder-level files are:

- `README.md`: how to use the packet and prompt templates.
- `PATCH_PROTOCOL.md`: how ChatGPT should respond for normal lesson patches.
- `TAB_EXTENSION_PROTOCOL.md`: how ChatGPT should propose future learner tabs/modules.
- `SOURCE_MAP.md`: source ownership and current tab registry.
- `ALL_UNITS_COMPACT.md`: broad cross-unit context.
- `all-units-content.md`: full combined packet.

## ChatGPT Usage Guidance

For normal single-lesson edits, give ChatGPT:

```text
README.md
PATCH_PROTOCOL.md
unit-XX-*.md
```

For cross-unit ordering or difficulty work, add:

```text
ALL_UNITS_COMPACT.md
```

For new learner-facing tabs/modules, add:

```text
TAB_EXTENSION_PROTOCOL.md
SOURCE_MAP.md
```

New tabs are product/implementation proposals, not content-only patches. ChatGPT should propose section id, label, data model, tab order, progress/completion/reset behavior, affected source files, and tests for Codex to implement.

## Critical ChatGPT Output Rule

The packet must instruct ChatGPT to write the actual revised lesson content itself. ChatGPT should use the exported lesson material to return finished replacement content/objects with Thai, Paiboon, English, audio text, prompts, answers, tags, and metadata aligned.

Do not accept responses that only give directions, suggestions, placeholders, or instructions for Codex to author the lesson later. Codex can apply and verify a patch, but ChatGPT must do the lesson-writing work in the response.

## Guardrails

- Preserve stable IDs by default.
- Prefer targeted object/array replacement over whole-unit rewrites.
- Keep Thai, Paiboon, English, audio text, quiz answers, labels, tags, and group IDs aligned.
- Require finished replacement lesson content for every touched object/array; patch plans alone are incomplete.
- Do not let ChatGPT patch generated Markdown as source of truth.
- Do not let ChatGPT silently add product surface. Use `TAB_EXTENSION_PROTOCOL.md`.
- Default to learner-facing Main Course content only. Admin Portal exports need a separate request.
