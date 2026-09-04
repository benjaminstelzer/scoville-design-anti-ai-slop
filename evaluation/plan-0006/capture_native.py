"""Capture one exact native worker transcript without reasoning or host secrets.

Evidence outputs are generated from real trace events. Source materialisation
is performed separately by the host through apply_patch.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

ROOT = Path('C:/Users/benja/AppData/Local/Temp/design-plan6-sol-native-v1-20260904')
parser = argparse.ArgumentParser()
parser.add_argument('label')
parser.add_argument('trace')
parser.add_argument('--version', default='capture-1')
parser.add_argument('--freeze', default='freeze.json')
parser.add_argument('--extract-first-json', action='store_true', help='Preserve and report trailing envelope material; never repair JSON content')
args = parser.parse_args()
if args.freeze not in ['freeze.json', 'freeze-brand-v1.json', 'freeze-record-scope-r1.json']:
    raise ValueError('Unknown freeze file')
frozen = json.loads((ROOT / args.freeze).read_text(encoding='utf-8'))
entry = frozen['sessions'][args.label]
trace = Path(args.trace)
raw = trace.read_bytes()
events = [json.loads(line) for line in raw.decode('utf-8').splitlines() if line.strip()]
meta = events[0]['payload']
expected_agent = '/root/sol_native_' + args.label.lower()
if meta.get('agent_path') != expected_agent:
    raise ValueError('Exact trace does not belong to requested worker')
contexts = [e['payload'] for e in events if e['type'] == 'turn_context']
if not contexts or any(c.get('model') != 'gpt-5.6-sol' or c.get('effort') != 'high' for c in contexts):
    raise ValueError('Unexpected actual model/effort')
answers = []
selected = []
calls = []
for event in events:
    payload = event.get('payload', {})
    kind = payload.get('type')
    if event['type'] == 'response_item' and kind in ['custom_tool_call', 'custom_tool_call_output', 'function_call', 'function_call_output']:
        selected.append(event)
        if kind in ['custom_tool_call', 'function_call']:
            calls.append({'timestamp': event['timestamp'], 'name': payload.get('name'), 'input': payload.get('input', payload.get('arguments'))})
    if event['type'] == 'response_item' and kind == 'message' and payload.get('role') == 'assistant':
        selected.append(event)
        text = ''.join(c.get('text', '') for c in payload.get('content', []))
        trailing = ''
        parsed_text = text
        try: answer = json.loads(text)
        except ValueError:
            if not args.extract_first_json: continue
            try: answer, end = json.JSONDecoder().raw_decode(text)
            except ValueError: continue
            trailing = text[end:]
            parsed_text = text[:end]
        if isinstance(answer, dict) and isinstance(answer.get('files'), list) and isinstance(answer.get('notes'), str):
            answers.append({'timestamp': event['timestamp'], 'text': parsed_text, 'raw_text': text, 'trailing': trailing, 'answer': answer})
if not answers:
    raise ValueError('No complete returned source/notes envelope found')
answer = answers[-1]
work = ROOT / args.label
for name, expected in entry['inputs'].items():
    if hashlib.sha256((work / name).read_bytes()).hexdigest().upper() != expected:
        raise ValueError('Frozen input changed: ' + name)
for name, expected in entry['package'].items():
    if hashlib.sha256((work / 'skill' / name).read_bytes()).hexdigest().upper() != expected:
        raise ValueError('Package changed: ' + name)
destination = work / args.version
destination.mkdir(exist_ok=False)
(destination / 'answer.json').write_text(answer['text'] + '\n', encoding='utf-8')
(destination / 'raw-answer.txt').write_text(answer['raw_text'], encoding='utf-8')
(destination / 'tool-events.jsonl').write_text(''.join(json.dumps(e, ensure_ascii=False) + '\n' for e in selected), encoding='utf-8')
(destination / 'actual-tool-calls.json').write_text(json.dumps(calls, indent=2) + '\n', encoding='utf-8')
receipt = {
    'case': entry['case'], 'arm': entry['arm'], 'label': args.label,
    'case_version': frozen['version'], 'requested_model': 'gpt-5.6-sol',
    'actual_trace_model': contexts[-1]['model'], 'actual_trace_effort': contexts[-1]['effort'],
    'session_id': meta['id'], 'agent_path': meta['agent_path'],
    'executed_at': answer['timestamp'], 'captured_at': datetime.now(timezone.utc).isoformat(),
    'settings': {'executor': frozen['executor'], 'scope': frozen['access'], 'inherited_host_permissions': contexts[-1].get('sandbox_policy'), 'approval_policy': contexts[-1].get('approval_policy')},
    'tested_package_sha256': frozen['packages'][entry['arm']]['manifest_sha256'],
    'source_trace': str(trace), 'source_trace_sha256_at_capture': hashlib.sha256(raw).hexdigest().upper(),
    'tool_trace': 'tool-events.jsonl', 'tool_trace_scope': 'Actual tool calls/results and assistant messages only; host context and reasoning omitted. No claim of a complete raw transcript.',
    'actual_tool_call_count': len(calls), 'frozen_inputs_and_package_unchanged': True,
    'answer_sha256': hashlib.sha256((destination / 'answer.json').read_bytes()).hexdigest().upper(),
    'transport_extraction': {'first_complete_json_extracted': bool(answer['trailing']), 'trailing_material_preserved_in_raw_answer': answer['trailing']},
    'source_proposals': [{'path': f['path'], 'sha256': hashlib.sha256(f['content'].encode('utf-8')).hexdigest().upper()} for f in answer['answer']['files']],
    'outcome': 'unreviewed',
}
(destination / 'receipt.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'capture': str(destination), 'session_id': meta['id'], 'tool_calls': len(calls), 'files': [f['path'] for f in answer['answer']['files']]}))
