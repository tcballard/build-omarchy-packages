#!/usr/bin/env python3
"""Validate metadata, relative references, canonical copies and versions."""
import json
import re
import sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent
NAMES = {f'omarchy-package-{name}' for name in ('inspect','build','integrate','test','submit','maintain')}

def validate(root=ROOT):
    errors = []
    version = (root / 'VERSION').read_text().strip()
    if not re.fullmatch(r'\d+\.\d+\.\d+', version):
        errors.append('VERSION is not semantic version syntax')
    skill_dirs = {p.name for p in (root / 'skills').iterdir() if p.is_dir()}
    if skill_dirs != NAMES:
        errors.append('canonical skill inventory differs from six expected stages')
    for name in sorted(NAMES):
        folder = root / 'skills' / name
        path = folder / 'SKILL.md'
        if not path.is_file():
            errors.append(f'{name}: missing SKILL.md'); continue
        raw = path.read_text()
        match = re.match(r'^---\n(.*?)\n---\n', raw, re.S)
        if not match:
            errors.append(f'{name}: missing frontmatter'); continue
        try:
            meta = yaml.safe_load(match[1])
        except yaml.YAMLError as e:
            errors.append(f'{name}: invalid YAML: {e}'); continue
        if not isinstance(meta, dict) or set(meta) != {'name','description'} or meta.get('name') != name or not isinstance(meta.get('description'), str) or len(meta['description']) < 40:
            errors.append(f'{name}: invalid name/description frontmatter')
        if len(raw.splitlines()) > 500 or '[TODO' in raw:
            errors.append(f'{name}: unfinished or oversized skill')
        for md in folder.rglob('*.md'):
            for target in re.findall(r'\]\(([^)]+)\)', md.read_text()):
                if '://' in target or target.startswith('#'):
                    continue
                target_path = (md.parent / target.split('#')[0]).resolve()
                if not target_path.is_relative_to(folder.resolve()) or not target_path.is_file():
                    errors.append(f'{name}: missing or escaping relative reference {target}')
        ui_path = folder / 'agents/openai.yaml'
        if not ui_path.is_file():
            errors.append(f'{name}: missing UI metadata')
        else:
            ui = yaml.safe_load(ui_path.read_text())['interface']
            if not 25 <= len(ui.get('short_description','')) <= 64 or '$'+name not in ui.get('default_prompt',''):
                errors.append(f'{name}: invalid UI description/prompt')
    for path in ('plugin.json','.claude-plugin/plugin.json','plugins/build-omarchy-packages/.codex-plugin/plugin.json'):
        manifest = json.loads((root/path).read_text())
        if manifest.get('name') != 'build-omarchy-packages' or manifest.get('version') != version or manifest.get('license') != 'MIT':
            errors.append(f'{path}: identity/version drift')
    canonical = root / 'skills'
    copied = root / 'plugins/build-omarchy-packages/skills'
    def files(base):
        return {p.relative_to(base): p.read_bytes() for p in base.rglob('*') if p.is_file() and '__pycache__' not in p.parts}
    if files(canonical) != files(copied):
        errors.append('Codex adapter skill content drift; run sync_adapter.py')
    market = json.loads((root/'.agents/plugins/marketplace.json').read_text())
    for item in market['plugins']:
        path = (root/item['source']['path']).resolve()
        if not path.is_relative_to(root.resolve()) or not (path/'.codex-plugin/plugin.json').is_file():
            errors.append('marketplace source missing or outside bundle')
    return errors

if __name__ == '__main__':
    errors = validate()
    for error in errors:
        print(error, file=sys.stderr)
    if errors:
        sys.exit(1)
    print('Six skills, references, metadata, manifests and adapter validated')
