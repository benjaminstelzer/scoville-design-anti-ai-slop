"""Actual isolated Claude host discovery, with no global Skill installation.

Only the existing login credential is temporarily copied into an isolated
configuration outside the model's working directory. Its contents
are never printed, included in a prompt, or retained as evidence. No personal
settings, hooks, plugins, memories or instructions are copied.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
from datetime import datetime, timezone

HERE = Path(__file__).resolve().parent
ROOT = Path('C:/Users/benja/AppData/Local/Temp/design-plan6-focused-v1-20260904')
LAUNCHER = r'''
import runpy, sys
m = runpy.run_path('C:/Users/benja/.codex/skills/ask-claude-for-codex/scripts/ask_claude.py', run_name='p6_host_activation')
g = m['run'].__globals__
g['READ_ONLY_TOOLS'] = 'Read,Grep,Glob,Skill'
original = g['build_command']
def scoped_command(args, claude_command):
    command = original(args, claude_command)
    position = command.index('--max-budget-usd')
    del command[position:position + 2]
    command += ['--setting-sources', 'project', '--strict-mcp-config', '--mcp-config', '{"mcpServers":{}}']
    return command
g['build_command'] = scoped_command
m['configure_standard_streams']()
sys.exit(m['run']())
'''

def main():
    p = argparse.ArgumentParser()
    p.add_argument('case_id')
    p.add_argument('--attempt', default='v2')
    args = p.parse_args()
    cases = json.loads((HERE / 'protocol-v1.json').read_text(encoding='utf-8'))['activation']['cases']
    case = next(c for c in cases if c['id'] == args.case_id)
    base = ROOT / 'activation' / (case['id'] + '-' + args.attempt)
    if base.exists():
        p.error('refusing to overwrite activation attempt')
    work = base / 'workspace'
    config = base / 'isolated-config'
    config.mkdir(parents=True)
    shutil.copytree(ROOT / 'candidate', work / '.claude/skills/scoville-design-anti-ai-slop')
    # A real temporary repository bounds ancestor project discovery. No commits.
    subprocess.run(['git', 'init', '--quiet', str(work)], check=True)
    credential = config / '.credentials.json'
    shutil.copyfile(Path('C:/Users/benja/.claude/.credentials.json'), credential)
    environment = os.environ.copy()
    environment['CLAUDE_CONFIG_DIR'] = str(config)
    command = [sys.executable, '-c', LAUNCHER, '--model', 'claude-fable-5-1', '--effort', 'high', '--persistent', '--with-customizations']
    started = datetime.now(timezone.utc).isoformat()
    try:
        result = subprocess.run(command, cwd=work, input=case['prompt'], text=True, encoding='utf-8', capture_output=True, env=environment)
    finally:
        # Delete only the exact temporary credential created above, never a directory.
        if credential.parent.resolve() != config.resolve() or config.resolve().parent != base.resolve():
            raise ValueError('unexpected credential cleanup target')
        credential.unlink(missing_ok=True)
    (base / 'stdout.json').write_text(result.stdout, encoding='utf-8')
    (base / 'stderr.txt').write_text(result.stderr, encoding='utf-8')
    receipt = {'case': case, 'attempt': args.attempt, 'started': started, 'finished': datetime.now(timezone.utc).isoformat(), 'exit_code': result.returncode, 'credential_removed': not credential.exists(), 'requested_model': 'claude-fable-5-1', 'effort': 'high', 'tools': ['Read', 'Grep', 'Glob', 'Skill'], 'isolation': 'CLAUDE_CONFIG_DIR plus project-only setting sources and bounded temporary repository; empty strict MCP; only project candidate Skill; read-only tools; no safe-mode or restricted mode because those suppress local discovery', 'calls': [], 'skill_listings': []}
    try:
        payload = json.loads(result.stdout)
        receipt.update(session_id=payload.get('session_id'), reported_model=payload.get('reported_model'), permission_denials=payload.get('permission_denials', []))
        sid = receipt['session_id']
        matches = list((config / 'projects').glob(f'*/{sid}.jsonl')) if sid else []
        if len(matches) == 1:
            raw = matches[0].read_bytes()
            (base / 'session.jsonl').write_bytes(raw)
            receipt['trace_sha256'] = hashlib.sha256(raw).hexdigest().upper()
            for line in raw.decode('utf-8').splitlines():
                item = json.loads(line)
                if item.get('attachment', {}).get('type') == 'skill_listing':
                    receipt['skill_listings'].append(item['attachment'].get('names', []))
                content = item.get('message', {}).get('content', [])
                if isinstance(content, list):
                    receipt['calls'] += [b for b in content if isinstance(b, dict) and b.get('type') == 'tool_use']
        else:
            receipt['trace_limit'] = f'Expected one isolated transcript; found {len(matches)}'
    except (ValueError, OSError) as exc:
        receipt['capture_error'] = str(exc)
    (base / 'receipt.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(receipt))
    return result.returncode

if __name__ == '__main__':
    raise SystemExit(main())
