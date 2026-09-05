"""Freeze matched native SOL inputs after a CLI read-policy failure.

Copies only declared prepared package/input trees, never prior outputs.
"""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil

OLD = Path('C:/Users/benja/AppData/Local/Temp/design-plan6-sol-v1-20260904')
ROOT = Path('C:/Users/benja/AppData/Local/Temp/design-plan6-sol-native-v1-20260904')

if ROOT.exists():
    raise ValueError('Refusing to overwrite native run root')
ROOT.mkdir()
frozen = json.loads((OLD / 'freeze.json').read_text(encoding='utf-8'))
manifest = {
    'version': 'P6-focused-v1/P6-sol-native-v1',
    'frozen_at': datetime.now(timezone.utc).isoformat(),
    'authority': 'ADR-0057',
    'requested_model': 'gpt-5.6-sol', 'effort': 'high',
    'executor': 'fresh host-native subagent, fork_turns=none',
    'access': 'read-only generation; host materialises proposed source',
    'limits': 'No fixed token/context/cost/expert ceiling. Native host instructions/tool catalogue are inherited, not a clean CLI catalogue. No other case outcomes are provided. Native transcript availability will be reported, not inferred from self-report.',
    'fallback_reason': 'CLI C4 baseline completed without an artifact because all workspace read commands were rejected by policy. Preserve attempt; do not weaken that policy.',
    'prior_attempt': str(OLD / 'cases/C4/baseline/attempt-1'),
    'packages': frozen['packages'], 'sessions': {},
}
counter = 0
for case in ['C4', 'C6', 'C7', 'C5A', 'C5B']:
    for arm in ['baseline', 'candidate']:
        counter += 1
        label = f'N{counter:02d}'
        source = OLD / 'cases' / case / arm
        work = ROOT / label
        work.mkdir()
        for directory in ['skill', 'inputs']:
            shutil.copytree(source / directory, work / directory)
        shutil.copyfile(source / 'prompt.txt', work / 'prompt.txt')
        manifest['sessions'][label] = {
            'case': case, 'arm': arm,
            'inputs': {p.relative_to(work).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest().upper()
                       for p in [work / 'prompt.txt', *sorted((work / 'inputs').rglob('*'))] if p.is_file()},
            'package': {p.relative_to(work / 'skill').as_posix(): hashlib.sha256(p.read_bytes()).hexdigest().upper()
                        for p in sorted((work / 'skill').rglob('*')) if p.is_file()},
        }
(ROOT / 'freeze.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'root': str(ROOT), 'sessions': {k: [v['case'], v['arm']] for k, v in manifest['sessions'].items()}}))
