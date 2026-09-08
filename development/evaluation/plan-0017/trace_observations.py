"""Bounded trace observations, never semantic proof or an acceptance grader."""
import base64
import hashlib
import json
import re


def observe(events):
    calls = {}
    views, note_writes, browser_runs = [], [], []
    for index, event in enumerate(events):
        p = event.get('payload', {})
        if event.get('type') != 'response_item':
            continue
        if p.get('type') in ('custom_tool_call', 'function_call'):
            raw = str(p.get('input', p.get('arguments', '')))
            calls[p['call_id']] = (index, raw)
            # Decode literal patch strings, not arbitrary JavaScript execution.
            literals = []
            for match in re.finditer(r'"(?:\\.|[^"\\])*"', raw):
                try:
                    literals.append(json.loads(match.group()))
                except ValueError:
                    pass
            material = '\n'.join([raw, *literals])
            paths = sorted(set(re.findall(
                r'^\*\*\* (?:Add|Update) File: ([^\r\n]*notes?[^\r\n]*\.md)\s*$',
                material, re.M | re.I)))
            if paths and 'apply_patch' in raw:
                note_writes.append({'call_event_index': index, 'call_id': p['call_id'],
                                    'literal_patch_targets': paths})
            if ('exec_command' in raw and re.search(r'\bnode(?:\.exe)?[\s"\']', raw, re.I)
                    and re.search(r'\.(?:mjs|cjs|js)\b', raw)):
                browser_runs.append({'call_event_index': index, 'call_id': p['call_id']})
        if p.get('type') not in ('custom_tool_call_output', 'function_call_output'):
            continue
        call_index, raw = calls.get(p.get('call_id'), (None, ''))
        output = p.get('output', [])
        blocks = [b for b in output if isinstance(b, dict) and b.get('type') == 'input_image'] if isinstance(output, list) else []
        if not blocks:
            continue
        requested = []
        for match in re.finditer(r'view_image\s*\(\s*\{[\s\S]*?["\']?path["\']?\s*:\s*("(?:\\.|[^"\\])*")', raw):
            try:
                requested.append(json.loads(match.group(1)))
            except ValueError:
                pass
        hashes = []
        for block in blocks:
            url = block.get('image_url', '')
            try:
                value = hashlib.sha256(base64.b64decode(url.split(',', 1)[1], validate=True)).hexdigest() if url.startswith('data:image/') and ';base64,' in url else None
            except (ValueError, IndexError):
                value = None
            hashes.append(value)
        views.append({'call_event_index': call_index, 'output_event_index': index,
                      'call_id': p.get('call_id'), 'received_image_count': len(blocks),
                      'literal_requested_paths': requested, 'received_image_sha256': hashes,
                      'path_pairing': 'literal-count-match; verify bytes' if len(requested) == len(blocks) else 'unverified'})
    return {'received_image_calls': views, 'note_patch_candidates': note_writes,
            'node_execution_candidates': browser_runs,
            'first_note_patch_candidate_index': note_writes[0]['call_event_index'] if note_writes else None,
            'first_node_execution_candidate_index': browser_runs[0]['call_event_index'] if browser_runs else None,
            'ceiling': 'Actual image payload hashes plus bounded literal-call observations. A note write is not proof that a semantic map existed; Node may perform non-browser work; dynamic paths/other write methods remain unresolved. Never infer execution order, version correspondence or design acceptance without inspecting the relevant actual calls and content.'}
