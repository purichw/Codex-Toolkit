# Maintenance Guide

Use this guide when refreshing the toolkit, adding a skill, or publishing a
change to GitHub.

## Refresh From Local Skills

From the repository root:

```sh
rsync -ani --delete --exclude '.system' --exclude '/README.md' --exclude '__pycache__/' --exclude '*.orig' ~/.codex/skills/ skills/
git status --short
git diff --check
```

Then inspect the dry-run diff. Do not commit generated cache folders, system
skills, or anything that belongs to a plugin bundle rather than the personal
skill set.

If the dry run would delete repo-only `global-*` aliases, do not apply the broad
delete sync. Sync changed canonical folders selectively instead:

```sh
rsync -a ~/.codex/skills/<skill-name>/ skills/<skill-name>/
```

Before editing, future Codex sessions should read [CODEX_CONTEXT.md](CODEX_CONTEXT.md)
and root [../AGENTS.md](../AGENTS.md). Those files explain the repository's
source-of-truth assumptions and the safest update path.

## Add A New Skill

1. Create a folder under `skills/<skill-name>/`.
2. Add `SKILL.md` with frontmatter `name` and `description`.
3. Add only the supporting files the skill actually needs:
   - `references/` for required reading or domain notes.
   - `scripts/` for reusable helpers.
   - `assets/` for reusable templates or media.
   - `agents/` for agent metadata.
4. Add the skill to:
   - [../README.md](../README.md)
   - [../skills/README.md](../skills/README.md)
   - [SKILL_CATALOG.md](SKILL_CATALOG.md)
5. If the new skill changes how future agents should maintain this repository,
   update [CODEX_CONTEXT.md](CODEX_CONTEXT.md) and [../AGENTS.md](../AGENTS.md).

## Privacy Review

This repository is private, but treat every commit as something that might later
be shared. Before pushing, scan for:

- API keys, access tokens, service-account JSON, private keys, or passwords.
- Client names, private URLs, emails, user identifiers, and personal data.
- Local absolute paths that are too sensitive or too brittle.
- Project-specific operational details that should stay local.

A quick first-pass scan:

```sh
rg -n -i "(api[_-]?key|secret|token|password|private[_-]?key|service_account|BEGIN .*PRIVATE KEY|sk-[A-Za-z0-9_-]+)" .
```

False positives are normal. Read the matches before deciding.

## Verification Before Push

For most changes, run the toolkit verifier:

```sh
python3 scripts/verify_skills.py --expected-count 136
```

It checks skill frontmatter, folder/name consistency, local Markdown links,
helper script syntax, accidental bundled/system paths, and high-confidence secret
patterns.

For docs-only changes, also run:

```sh
git diff --check
find skills -name SKILL.md | sort | wc -l
```

If you add scripts, run their basic help or smoke-test path before committing.

The imported iOS inventory helper is invoked with `python3`, not executed
directly. It retains the live source's non-executable file mode; the verifier's
executable-bit warning is informational for this helper. Check its CLI with
`python3 skills/ios-app-development/scripts/check-environment.py --help`.

For `ui-ux-expert` evaluation-pack changes, also run:

```sh
python3 skills/ui-ux-expert/evals/validate.py
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s skills/ui-ux-expert/evals/tests -v
```

These validate the input pack and brief/rubric separation, not design quality.
Use its [evaluation protocol](../skills/ui-ux-expert/references/evaluation-protocol.md)
for matched rendered runs and human review; never report those runs as completed
just because the Python checks pass.

## Commit Style

Use concise messages that describe the toolkit change:

```sh
git commit -m "Add custom Codex skills catalog"
git commit -m "Document skill installation workflow"
git commit -m "Update Notenwert maintainer skill"
```

Push only after the diff matches the intended scope.
