"""Retain an exact named reviewer result and its actual tool events."""
import argparse
import hashlib
import json
from pathlib import Path

p=argparse.ArgumentParser()
p.add_argument('trace')
p.add_argument('agent')
p.add_argument('destination')
p.add_argument('--review-at', help='Select an exact completed review timestamp instead of the latest final answer')
a=p.parse_args()
trace=Path(a.trace)
raw=trace.read_bytes()
events=[json.loads(line) for line in raw.decode('utf-8').splitlines() if line.strip()]
meta=events[0]['payload']
if meta.get('agent_path')!=a.agent: raise ValueError('Wrong reviewer trace')
contexts=[e['payload'] for e in events if e['type']=='turn_context']
if not contexts or any(c.get('model')!='gpt-5.6-sol' or c.get('effort')!='high' for c in contexts): raise ValueError('Unexpected reviewer model/effort')
messages=[e for e in events if e['type']=='response_item' and e['payload'].get('type')=='message' and e['payload'].get('role')=='assistant']
finals=[e for e in messages if e['payload'].get('phase')=='final_answer' or e['payload'].get('channel')=='final']
if a.review_at: finals=[e for e in finals if e['timestamp']==a.review_at]
if not finals: raise ValueError('No matching completed reviewer final answer')
last=finals[-1]
selected=[e for e in events if e['type']=='response_item' and (e['payload'].get('type') in ['custom_tool_call','custom_tool_call_output','function_call','function_call_output'] or e in messages)]
dest=Path(a.destination)
dest.mkdir(parents=True,exist_ok=False)
(dest/'review.md').write_text(''.join(c.get('text','') for c in last['payload'].get('content',[]))+'\n',encoding='utf-8')
(dest/'tool-events.jsonl').write_text(''.join(json.dumps(e,ensure_ascii=False)+'\n' for e in selected),encoding='utf-8')
receipt={'session_id':meta['id'],'agent_path':meta['agent_path'],'requested_model':'gpt-5.6-sol','actual_trace_model':contexts[-1]['model'],'effort':contexts[-1]['effort'],'review_at':last['timestamp'],'selected_response_phase':last['payload'].get('phase',last['payload'].get('channel')),'source_trace_sha256_at_capture':hashlib.sha256(raw).hexdigest().upper(),'trace_scope':'Actual tool events and assistant messages only; excludes reasoning and host context','review_sha256':hashlib.sha256((dest/'review.md').read_bytes()).hexdigest().upper()}
(dest/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt))
