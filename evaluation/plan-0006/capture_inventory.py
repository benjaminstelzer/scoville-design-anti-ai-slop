"""Read retained attempts without making a model call; preserve partial failures."""
import hashlib
import json
from pathlib import Path

ROOT = Path('C:/Users/benja/AppData/Local/Temp/design-plan6-focused-v1-20260904')

def capture(directory, trace_root):
    record = json.loads((directory / 'receipt.json').read_text(encoding='utf-8'))
    payload = None
    for name in ['stdout.json', 'stderr.txt']:
        try:
            payload = json.loads((directory / name).read_text(encoding='utf-8'))
            break
        except (ValueError, OSError):
            pass
    if not payload:
        return {'directory': str(directory), 'limit': 'No parseable CLI result'}
    sid = payload.get('session_id') or record.get('session_id')
    summary = {'directory': str(directory), 'session_id': sid, 'exit_code': record['exit_code'], 'requested_model': record.get('requested_model'), 'effort': record.get('effort'), 'api_error_status': payload.get('api_error_status'), 'api_error': payload.get('result') if record['exit_code'] else None, 'tool_calls': [], 'tool_errors': [], 'skill_listings': [], 'trace_models': [], 'artifact_hashes': []}
    if (directory / 'session.jsonl').exists():
        trace = directory / 'session.jsonl'
    else:
        matches = list(trace_root.glob(f'*/{sid}.jsonl')) if sid else []
        trace = matches[0] if len(matches) == 1 else None
    if trace:
        raw = trace.read_bytes()
        summary['trace_sha256'] = hashlib.sha256(raw).hexdigest().upper()
        if not (directory / 'session.jsonl').exists():
            (directory / 'session-recovered.jsonl').write_bytes(raw)
        for line in raw.decode('utf-8').splitlines():
            item = json.loads(line)
            message = item.get('message', {})
            if message.get('model') and message['model'] not in summary['trace_models']:
                summary['trace_models'].append(message['model'])
            if item.get('attachment', {}).get('type') == 'skill_listing':
                summary['skill_listings'].append(item['attachment'].get('names', []))
            content = message.get('content', [])
            if isinstance(content, list):
                for block in content:
                    if not isinstance(block, dict): continue
                    if block.get('type') == 'tool_use':
                        summary['tool_calls'].append({'name': block.get('name'), 'input': block.get('input')})
                    elif block.get('type') == 'tool_result' and block.get('is_error'):
                        summary['tool_errors'].append({'id': block.get('tool_use_id'), 'content': block.get('content')})
    for artifact in sorted(directory.parent.glob('artifact*.html')):
        summary['artifact_hashes'].append({'path': str(artifact), 'sha256': hashlib.sha256(artifact.read_bytes()).hexdigest().upper()})
    (directory / 'capture-v2.json').write_text(json.dumps(summary, indent=2) + '\n', encoding='utf-8')
    return summary

if __name__ == '__main__':
    inventory = []
    for directory in sorted((ROOT / 'cases').glob('*/*/attempt-1')):
        if (directory / 'receipt.json').exists():
            inventory.append(capture(directory, Path('C:/Users/benja/.claude/projects')))
    for directory in sorted((ROOT / 'activation').glob('*')):
        if (directory / 'receipt.json').exists():
            inventory.append(capture(directory, directory / 'isolated-config/projects'))
    (ROOT / 'inventory-v1.json').write_text(json.dumps(inventory, indent=2) + '\n', encoding='utf-8')
    for item in inventory:
        print(json.dumps({**{k: v for k, v in item.items() if k not in ['tool_calls', 'artifact_hashes']}, 'reads': [call['input'].get('file_path') for call in item.get('tool_calls', []) if call['name'] == 'Read']}))
