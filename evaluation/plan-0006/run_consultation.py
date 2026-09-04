"""Persist read-only Fable consultation and exact session transcript as test outputs.

No source materialisation occurs here. Model-produced source is inspected and
materialised by the authorised host separately. No installed wrapper is edited.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
from datetime import datetime, timezone

LAUNCHER = r'''
import runpy, sys
m = runpy.run_path('C:/Users/benja/.codex/skills/ask-claude-for-codex/scripts/ask_claude.py', run_name='p6_readonly_wrapper')
g = m['run'].__globals__
g['READ_ONLY_TOOLS'] = 'Read,Grep,Glob'
original = g['build_command']
def scoped_command(args, claude_command):
    command = original(args, claude_command)
    position = command.index('--max-budget-usd')
    del command[position:position + 2]
    return command
g['build_command'] = scoped_command
m['configure_standard_streams']()
sys.exit(m['run']())
'''

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--cwd', type=Path, required=True)
    p.add_argument('--prompt', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    p.add_argument('--resume')
    args = p.parse_args()
    if args.output.exists():
        p.error('refusing to overwrite an attempt')
    args.output.mkdir(parents=True)
    prompt = args.prompt.read_text(encoding='utf-8')
    command = [sys.executable, '-c', LAUNCHER, '--model', 'claude-fable-5-1', '--effort', 'high', '--without-customizations']
    command += ['--resume', args.resume] if args.resume else ['--persistent']
    started = datetime.now(timezone.utc).isoformat()
    result = subprocess.run(command, cwd=args.cwd, input=prompt, text=True, encoding='utf-8', capture_output=True)
    (args.output / 'stdout.json').write_text(result.stdout, encoding='utf-8')
    (args.output / 'stderr.txt').write_text(result.stderr, encoding='utf-8')
    receipt = {'started': started, 'finished': datetime.now(timezone.utc).isoformat(), 'exit_code': result.returncode, 'cwd': str(args.cwd.resolve()), 'prompt_sha256': hashlib.sha256(prompt.encode()).hexdigest().upper(), 'requested_model': 'claude-fable-5-1', 'effort': 'high', 'tools': ['Read', 'Grep', 'Glob'], 'customizations': False, 'hard_budget': None, 'resume': args.resume}
    try:
        payload = json.loads(result.stdout)
        receipt['session_id'] = payload.get('session_id')
        receipt['reported_model'] = payload.get('reported_model')
        receipt['permission_denials'] = payload.get('permission_denials', [])
        receipt['cost_usd'] = payload.get('total_cost_usd')
        sid = receipt['session_id']
        if sid:
            matches = list((Path('C:/Users/benja/.claude/projects')).glob(f'*/{sid}.jsonl'))
            if len(matches) == 1:
                raw = matches[0].read_bytes()
                (args.output / 'session.jsonl').write_bytes(raw)
                receipt['trace_sha256'] = hashlib.sha256(raw).hexdigest().upper()
                reads = []
                for line in raw.decode('utf-8').splitlines():
                    item = json.loads(line)
                    content = item.get('message', {}).get('content', [])
                    if isinstance(content, list):
                        for block in content:
                            if isinstance(block, dict) and block.get('type') == 'tool_use':
                                reads.append({'name': block.get('name'), 'input': block.get('input'), 'id': block.get('id')})
                receipt['tool_calls'] = reads
            else:
                receipt['trace_limit'] = f'Expected one transcript; found {len(matches)}'
    except (ValueError, OSError, TypeError) as exc:
        receipt['capture_error'] = str(exc)
    (args.output / 'receipt.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in receipt.items() if k != 'tool_calls'}))
    return result.returncode

if __name__ == '__main__':
    raise SystemExit(main())
