#!/usr/bin/env python3
"""Generate a self-contained Codex plugin adapter from canonical skills."""
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def sync():
    manifest = json.loads((ROOT / '.claude-plugin/plugin.json').read_text())
    adapter = ROOT / 'plugins/build-omarchy-packages'
    skills = adapter / 'skills'
    if skills.exists():
        shutil.rmtree(skills)
    skills.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(ROOT / 'skills', skills, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
    manifest['skills'] = './skills/'
    manifest['interface'] = {
        'displayName': 'Build Omarchy Packages',
        'shortDescription': 'Package and maintain upstream apps for Omarchy',
        'longDescription': 'Six skills for upstream inspection, pinned Arch recipes, desktop and data integration, clean builds, evidenced PRs and maintenance.',
        'developerName': 'Tom Ballard',
        'category': 'Developer Tools',
        'capabilities': ['Read', 'Write'],
        'websiteURL': manifest['homepage'],
        'privacyPolicyURL': manifest['homepage'] + '/blob/main/PRIVACY.md',
        'termsOfServiceURL': manifest['homepage'] + '/blob/main/TERMS.md',
        'defaultPrompt': ['Package this upstream application for Omarchy.', 'Validate this package and prepare its contribution PR.', 'Update this Omarchy package to the latest upstream release.'],
    }
    target = adapter / '.codex-plugin/plugin.json'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(manifest, indent=2) + '\n')
    market = ROOT / '.agents/plugins/marketplace.json'
    market.parent.mkdir(parents=True, exist_ok=True)
    market.write_text(json.dumps({'name': 'tcballard-omarchy-packages', 'interface': {'displayName': 'Build Omarchy Packages'}, 'plugins': [{'name':'build-omarchy-packages','source':{'source':'local','path':'./plugins/build-omarchy-packages'},'policy':{'installation':'AVAILABLE','authentication':'ON_INSTALL'},'category':'Developer Tools'}]},indent=2)+'\n')

if __name__ == '__main__':
    sync()
    print('Generated Codex adapter')
