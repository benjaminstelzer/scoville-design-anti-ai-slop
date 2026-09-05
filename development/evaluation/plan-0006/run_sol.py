"""Isolated read-only SOL execution; stdout events and final source are retained.

Uses existing authentication without reading/copying it. No global config or
Skill installation is changed. The host separately materialises returned source.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
OLD = Path('C:/Users/benja/AppData/Local/Temp/design-plan6-focused-v1-20260904')
ROOT = Path('C:/Users/benja/AppData/Local/Temp/design-plan6-sol-v1-20260904')
CODEX = 'C:/Users/benja/AppData/Local/OpenAI/Codex/bin/994e8469124a0d31/codex.exe'

def settings():
    # Enumerate only metadata paths; no unrelated Skill contents are inspected.
    disabled = [p.parent.as_posix() for p in sorted(Path('C:/Users/benja/.codex/skills').rglob('SKILL.md'))]
    overrides = {
        'model_reasoning_effort': 'high', 'approval_policy': 'never',
        'features.apps': False, 'features.plugins': False,
        'features.memories': False, 'features.multi_agent': False,
        'features.shell_snapshot': False, 'project_doc_max_bytes': 0,
        'web_search': 'disabled', 'project_root_markers': ['.eval-root'],
    }
    args = []
    for key, value in overrides.items():
        args += ['-c', key + '=' + json.dumps(value)]
    skill_array = '[' + ','.join('{path=' + json.dumps(path) + ',enabled=false}' for path in disabled) + ']'
    args += ['-c', 'skills.config=' + skill_array]
    return overrides, disabled, args

def prepare():
    if ROOT.exists():
        raise ValueError('Refusing to overwrite SOL run root')
    ROOT.mkdir()
    protocol = json.loads((HERE / 'protocol-v1.json').read_text(encoding='utf-8'))
    overrides, disabled, _ = settings()
    freeze = {'protocol': 'P6-sol-v1', 'authorisation': 'ADR-0057', 'requested_model': 'gpt-5.6-sol', 'settings': overrides, 'disabled_skill_paths': disabled, 'sandbox': 'read-only', 'cli': CODEX, 'flags': ['--ignore-user-config', '--ephemeral', '--skip-git-repo-check', '--json'], 'pair_cases': ['C4', 'C5A', 'C5B', 'C6', 'C7'], 'inputs': {}, 'packages': json.loads((OLD / 'freeze.json').read_text(encoding='utf-8'))['packages']}
    for case in freeze['pair_cases']:
        for arm in ['baseline', 'candidate']:
            source = OLD / 'cases' / case / arm
            work = ROOT / 'cases' / case / arm
            work.mkdir(parents=True)
            shutil.copytree(source / 'skill', work / 'skill')
            shutil.copytree(source / 'inputs', work / 'inputs')
            shutil.copyfile(source / 'prompt.txt', work / 'prompt.txt')
            (work / '.eval-root').write_text('Isolated evaluation project boundary.\n', encoding='utf-8')
            freeze['inputs'][case + '/' + arm] = {str(p.relative_to(work)).replace('\\', '/'): hashlib.sha256(p.read_bytes()).hexdigest().upper() for p in [work / 'prompt.txt', *sorted((work / 'inputs').rglob('*'))] if p.is_file()}
    (ROOT / 'freeze.json').write_text(json.dumps(freeze, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'prepared': str(ROOT), 'pairs': freeze['pair_cases'], 'requested_model': freeze['requested_model']}))

def run(case, arm):
    work = ROOT / 'cases' / case / arm
    attempt = work / 'attempt-1'
    if attempt.exists(): raise ValueError('Refusing to overwrite an attempt')
    attempt.mkdir()
    frozen = json.loads((ROOT / 'freeze.json').read_text(encoding='utf-8'))
    overrides, disabled, config = settings()
    if overrides != frozen['settings'] or disabled != frozen['disabled_skill_paths']:
        raise ValueError('Host configuration changed after freeze')
    command = [CODEX, 'exec', '--ignore-user-config', '--ephemeral', '--skip-git-repo-check', '--sandbox', 'read-only', '--model', 'gpt-5.6-sol', '--json', '--color', 'never', *config, '--output-schema', str(HERE / 'sol-output.schema.json'), '--output-last-message', str(attempt / 'answer.json'), '--cd', str(work), '-']
    prompt = (work / 'prompt.txt').read_text(encoding='utf-8')
    receipt = {'case': case, 'arm': arm, 'case_version': 'P6-focused-v1/P6-sol-v1', 'started': datetime.now(timezone.utc).isoformat(), 'requested_model': 'gpt-5.6-sol', 'settings': overrides, 'sandbox': 'read-only', 'prompt_sha256': hashlib.sha256(prompt.encode()).hexdigest().upper(), 'tested_package_sha256': frozen['packages'][arm]['manifest_sha256'], 'command': command}
    with (attempt / 'events.jsonl').open('w', encoding='utf-8') as stdout, (attempt / 'stderr.txt').open('w', encoding='utf-8') as stderr:
        result = subprocess.run(command, cwd=work, input=prompt, text=True, encoding='utf-8', stdout=stdout, stderr=stderr)
    receipt.update(exit_code=result.returncode, finished=datetime.now(timezone.utc).isoformat())
    for line in (attempt / 'events.jsonl').read_text(encoding='utf-8').splitlines():
        try: event = json.loads(line)
        except ValueError: continue
        if event.get('type') == 'thread.started': receipt['session_id'] = event.get('thread_id')
        if event.get('type') == 'turn.completed': receipt['usage'] = event.get('usage')
        if event.get('type') in ['error', 'turn.failed']: receipt.setdefault('errors', []).append(event)
    (attempt / 'receipt.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in receipt.items() if k != 'command'}))
    return result.returncode

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--prepare', action='store_true')
    p.add_argument('--case')
    p.add_argument('--arm', choices=['baseline', 'candidate'])
    args = p.parse_args()
    if args.prepare: prepare()
    else: sys.exit(run(args.case, args.arm))
