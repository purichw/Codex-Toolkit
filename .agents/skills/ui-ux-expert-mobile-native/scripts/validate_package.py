#!/usr/bin/env python3
"""Check installed skill files and local links, not UI/UX quality. Stdlib only."""
from __future__ import annotations
import argparse
import ast
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

NAME = 'ui-ux-expert-mobile-native'
REQUIRED = (
    'SKILL.md', 'agents/openai.yaml', 'source-registry.json',
    'references/user-preferences.md', 'references/design-craft.md',
    'references/native-interactions.md', 'references/accessibility-localization.md',
    'references/ios-ipados.md', 'references/android.md',
    'references/stack-swiftui-uikit.md', 'references/stack-compose-views.md',
    'references/stack-react-native-expo.md', 'references/stack-flutter.md',
    'references/assets-motion.md', 'references/visual-review.md', 'references/tooling.md',
    'references/sources.md', 'examples/works-fails.md', 'templates/design-contract.md',
    'templates/review-record.md', 'templates/evidence-plan.example.json',
    'scripts/native_evidence.py', 'scripts/validate_package.py',
)


def validate(root: Path) -> dict:
    root = root.resolve()
    errors = []
    for rel in REQUIRED:
        p = root / rel
        if not p.is_file(): errors.append(f'Missing required file: {rel}')
    core = (root / 'SKILL.md').read_text(encoding='utf-8') if (root / 'SKILL.md').is_file() else ''
    fm = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)', core, re.S)
    if not fm:
        errors.append('SKILL.md needs YAML frontmatter')
    else:
        fields = dict(re.findall(r'^([a-z_]+):[ \t]*(.+)$', fm.group(1), re.M))
        if fields.get('name') != NAME: errors.append('Skill name mismatch')
        if not fields.get('description', '').strip(): errors.append('Missing description')
    metadata = root / 'agents/openai.yaml'
    if metadata.exists():
        yaml = metadata.read_text(encoding='utf-8')
        # Deliberately format checks for our simple metadata, not a general YAML parser.
        for field in ('interface:', 'display_name:', 'short_description:', 'default_prompt:', 'allow_implicit_invocation:'):
            if field not in yaml: errors.append(f'Metadata missing {field}')
        if '$' + NAME not in yaml: errors.append('default_prompt does not invoke this skill')
    n_json = n_python = n_links = 0
    for p in sorted(root.rglob('*')):
        if not p.is_file() or '__pycache__' in p.parts: continue
        if not p.resolve().is_relative_to(root):
            errors.append(f'File symlink escapes skill: {p.name}'); continue
        if p.suffix not in {'.md', '.json', '.py', '.yaml'}: continue
        try:
            text = p.read_text(encoding='utf-8')
            if any(ord(c) < 32 and c not in '\n\r\t' for c in text):
                errors.append(f'Unexpected control character: {p.relative_to(root)}')
            if p.suffix == '.json': json.loads(text); n_json += 1
            if p.suffix == '.py': ast.parse(text, filename=str(p)); n_python += 1
            if p.suffix == '.md':
                # Actual Markdown links, not inline code paths or shell placeholders.
                for target in re.findall(r'(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)', text):
                    url = urlsplit(target.strip().strip('<>'))
                    if url.scheme or url.netloc or not url.path: continue
                    dst = (p.parent / unquote(url.path)).resolve()
                    n_links += 1
                    if not dst.is_relative_to(root): errors.append(f'Local link escapes installed skill: {p.name}: {target}')
                    elif not dst.exists(): errors.append(f'Broken link: {p.name}: {target}')
        except (OSError, UnicodeError, ValueError, SyntaxError) as exc:
            errors.append(f'Cannot parse {p.relative_to(root)}: {exc}')
    registry = root / 'source-registry.json'
    if registry.exists():
        try:
            data = json.loads(registry.read_text(encoding='utf-8'))
            ids = [s['id'] for s in data['sources']]
            if len(ids) != len(set(ids)): errors.append('Duplicate source IDs')
            for source in data['sources']:
                if not source['url'].startswith('https://'): errors.append(f'Non-HTTPS source {source["id"]}')
                if not source['access_note']: errors.append(f'Missing source access note {source["id"]}')
        except (OSError, ValueError, KeyError, TypeError) as exc:
            errors.append(f'Invalid source registry: {exc}')
    return {'skill': NAME, 'structural_status': 'failed' if errors else 'passed',
            'core_lines': len(core.splitlines()), 'core_word_count_informational': len(core.split()),
            'json_files_parsed': n_json, 'python_files_parsed': n_python,
            'local_markdown_links_checked': n_links, 'errors': errors,
            'limits': ['Not a full YAML/Markdown specification validator.',
                       'Does not load the skill in Codex, compile native code, authenticate evidence, or inspect UI.',
                       'Passing structure is not evidence of design quality or behavioral correctness.']}


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = p.parse_args()
    try:
        result = validate(args.root)
    except (OSError, UnicodeError, ValueError) as exc:
        result = {'structural_status': 'failed', 'errors': [str(exc)]}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result['structural_status'] == 'passed' else 1


if __name__ == '__main__':
    sys.exit(main())
