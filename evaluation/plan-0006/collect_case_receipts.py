"""Resolve observed executions and preserved stages to durable artifact hashes.

This is a development-evidence collector, not a scorer or an execution harness.
The explicit judgments below come from the captured independent reviews and
host checks. No transport-success value is converted into a behavioural pass.
"""
import hashlib
import json
from pathlib import Path
import re
import yaml

REPO = Path(__file__).resolve().parents[2]
ARCHIVE = Path('Z:/Projekts/AI/scoville-design-eval-local/plan-0006-native-completion-20260904')
NATIVE = ARCHIVE / 'native'
FABLE = Path('Z:/Projekts/AI/scoville-design-eval-local/plan-0006-progress-20260904')
BASELINE = '2D8718FF68019BA7D4AC21943F8A98D7823629B4B07C5BD7AE9EFFC06FE8D91B'
TESTED = '246B03A84383C1E2AB7A4928F597F1F5A32B014734D6AD3A6ED1FBEE65368655'
registry = yaml.safe_load((REPO / 'modules.yaml').read_text(encoding='utf-8'))
module_ids = {m['id'] for m in registry['modules']}

def load(path):
    return json.loads(path.read_text(encoding='utf-8'))

def artifact(path):
    return {'path': str(path), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest().upper()}

def sources_and_proofs(work):
    selected = list(work.glob('artifact*.html'))
    for directory in work.glob('proof*'):
        if directory.is_dir(): selected.extend(p for p in directory.rglob('*') if p.is_file())
    return sorted(set(selected))

# Ordered history is retained, including every corrected initial defect.
history = {
    'N02': [
        {'source':'artifact.html','outcome':'fail','finding':'Previous-sample legend incorrectly visible initially; actual proof and generator diagnosis.'},
        {'source':'artifact-v2.html','outcome':'pass','finding':'Only hidden-legend CSS added; actual initial/advanced/reduced proof checked; independent judgment still narrowly favours baseline.'}],
    'N11': [
        {'source':'artifact.html','outcome':'fail','finding':'Compact wordmark selector leakage and inconsistent type sample; source/render-backed findings.'},
        {'source':'artifact-v2.html','outcome':'fail','finding':'Those defects corrected, but independent review identifies incomplete palette ownership.'},
        {'source':'artifact-v3.html','outcome':'pass','finding':'Palette owner binding corrected; real propagation test and independent verification; all v2/v3 PNG hashes identical.'}],
    'N12': [
        {'source':'artifact.html','outcome':'fail','finding':'Rule/corner and offset descriptions do not exactly match source; source-time proof limit corrected separately. Extra trailing JSON envelope bytes retained.'},
        {'source':'artifact-v2.html','outcome':'fail','finding':'Descriptions corrected, but independent review identifies incomplete palette ownership.'},
        {'source':'artifact-v3.html','outcome':'pass','finding':'Palette owner bindings corrected; eleven real propagation checks and independent verification; all v2/v3 PNG hashes identical.'}],
}
comparison = {
    'C4':'Baseline narrow advantage, medium confidence; not erased by candidate correction.',
    'C5A':'Original pair tie, high confidence.',
    'C5B':'Candidate narrow advantage, medium confidence; actual host return and design verification supplied.',
    'C6':'Tie, high confidence; no visual ranking without renderer.',
    'C7':'Tie, medium-high confidence; critique only, no mutation.',
    'C8':'Original pair tie, moderate-high confidence, retained after corrections.',
}
receipts = []
for number in range(1, 15):
    label = f'N{number:02}'
    work = NATIVE / label
    captures = sorted(work.glob('capture-*'), key=lambda p:int(p.name.split('-')[1]))
    first, latest = load(captures[0] / 'receipt.json'), load(captures[-1] / 'receipt.json')
    calls = load(captures[0] / 'actual-tool-calls.json')
    call_text = '\n'.join(str(c.get('input','')) for c in calls)
    notes = load(captures[0] / 'answer.json')['notes']
    reported = set(re.findall(r'references/([a-z0-9-]+)\.md', notes))
    # Require both an explicit first-answer read disclosure and the identifier
    # in actual executed read-call input. This is conservative, not inferred routing.
    reads = sorted(m for m in reported & module_ids if m in call_text)
    actual_tools = sorted(set(re.findall(r'tools\.([a-z_]+)\(', call_text)))
    settings = dict(first['settings'], effort=first['actual_trace_effort'], tools=actual_tools,
                    tool_list_scope='Observed nested tool calls; host catalogue and permissions were inherited, not reduced to these names.')
    paths = sources_and_proofs(work)
    for capture in captures:
        paths.extend(capture / name for name in ['answer.json','receipt.json','actual-tool-calls.json','tool-events.jsonl'])
        if (capture / 'raw-answer.txt').exists(): paths.append(capture / 'raw-answer.txt')
    case = first['case']
    record = {
        'id':f'P6-SOL-{label}', 'executed':True, 'case_version':first['case_version'],
        'case':case, 'arm':first['arm'], 'requested_model':first['requested_model'],
        'session_id':first['session_id'], 'executed_at':first['executed_at'],
        'last_captured_execution_at':latest['executed_at'], 'settings':settings,
        'outcome':'limited' if case == 'C6' else 'pass',
        'outcome_scope':'Bounded task/source and supplied render conditions only; not whole-package qualification.',
        'tested_package_sha256':first['tested_package_sha256'],
        'observed_module_reads':reads, 'read_evidence':'First-answer complete-read disclosures corroborated by actual read-call inputs; full actual event extracts retained.',
        'stages':history.get(label,[{'source':'no artifact; read-only critique' if case == 'C7' else 'artifact.html','outcome':'limited' if case == 'C6' else 'pass','finding':'Initial proposal retained unchanged after applicable actual proof and review.'}]),
        'comparative_judgment':comparison[case], 'artifacts':[artifact(p) for p in sorted(set(paths))],
    }
    if label == 'N13': record['comparative_judgment'] = 'R02 targeted retest: slight candidate preference for label legibility, high compliance confidence; original C5A tie retained.'
    if label == 'N14': record['comparative_judgment'] = 'R02 targeted retest: narrow initial candidate preference; tie after previously identified baseline corrections. Candidate unchanged. Original C8 pair remains a separate tie.'
    if label in ['N13','N14']:
        record['retest_reason'] = 'Five module-local relevance clauses changed after independent R02 fidelity finding. Same raw task/inputs; fresh candidate session; retained baseline, not rerun. No attribution of aesthetic differences to this small instruction change.'
    receipts.append(record)

for case in ['C1','C2','C3']:
    for arm in ['baseline','candidate']:
        work = FABLE / 'cases' / case / arm
        actual = load(work / 'attempt-1/receipt.json')
        reads = sorted({Path(c['input']['file_path']).stem for c in actual['tool_calls']
                        if c['name']=='Read' and '/references/' in c['input'].get('file_path','').replace('\\','/')} & module_ids)
        paths = sources_and_proofs(work) + [work / 'attempt-1' / name for name in ['receipt.json','session.jsonl','stdout.json']]
        stages = [{'source':'artifact.html','outcome':'pass','finding':'Bounded correction or preservation confirmed in independent source/render review.'}]
        if case == 'C2':
            stages = [{'source':'artifact.html','outcome':'fail','finding':'Initial factual/claim defects in both arms; candidate also mobile cascade defect. Full findings retained in plan-0006-sol-interim-reviews.md.'},
                      {'source':'artifact-v2.html','outcome':'pass','finding':'Minimal host corrections verified by same still-blinded reviewer; modest baseline preference unchanged. Not a fresh generation.'}]
        receipts.append({
            'id':f'P6-FABLE-{case}-{arm.upper()}', 'executed':True, 'case_version':'P6-focused-v1',
            'case':case, 'arm':arm, 'requested_model':actual['requested_model'],
            'session_id':actual['session_id'], 'executed_at':actual['finished'],
            'settings':{'effort':actual['effort'],'tools':actual['tools'],'customizations':actual['customizations'],'hard_budget':actual['hard_budget'],'model_identity_limit':'Actual assistant traces carry requested string; no further backend identity asserted.'},
            'outcome':'pass','outcome_scope':'Bounded final task outcome after any listed correction, not comparative superiority.',
            'tested_package_sha256':TESTED if arm=='candidate' else BASELINE,
            'observed_module_reads':reads, 'stages':stages,
            'comparative_judgment':'Modest baseline preference, medium confidence.' if case=='C2' else 'Tie, high confidence.',
            'artifacts':[artifact(p) for p in sorted(set(paths))],
        })

recovery = Path('Z:/Projekts/AI/scoville-design-eval-local/plan-0006-review-recovery-20260904/scope-r1')
superseded = sorted(p for p in (NATIVE/'reviews/scope-r1').iterdir() if p.is_file())
review_files = sorted(p for p in (NATIVE/'reviews').rglob('*') if p.is_file() and p not in superseded)
recovered = sorted(p for p in recovery.iterdir() if p.is_file())
review_files.extend(recovered)
evidence = {m:[] for m in sorted(module_ids)}
for record in receipts:
    if record['arm']=='candidate':
        for m in record['observed_module_reads']: evidence[m].append(record['id'])
payload = {
    'schema_version':1,
    'status':'Observed development receipts; W-004 remains open for genuine host activation and retained Fable final review.',
    'scope':'Original Fable C1-C3, matched native SOL C4-C8, and two justified R02 candidate retests. Failed transport/provider lanes remain in the referenced archives, never counted as passes.',
    'receipts':receipts, 'independent_review_artifacts':[artifact(p) for p in review_files],
    'review_capture_corrections':[{
        'reason':'The original standalone scope-r1 capture selected a subsequent commentary, not the completed initial verdict. The original final_answer remains in its event extract. Recovery selects that exact existing event; no model rerun or outcome change.',
        'original_capture_preserved':[artifact(p) for p in superseded],
        'corrected_capture':[artifact(p) for p in recovered],
        'corrected_review_at':'2026-09-04T08:16:44.658Z',
        'source_session_id':'01a06b7b-6d8b-7fd2-a18e-99d67e09b5de',
    }],
    'other_review_record':artifact(REPO/'docs/evaluation/plan-0006-sol-interim-reviews.md'),
    'archive_manifest':artifact(ARCHIVE/'archive-manifest.json'),
    'module_annotations':evidence,
    'limits':['No full holdout rerun or general model/Skill superiority claim.','Artifact corrections are distinct versions, not rewritten initial outcomes.','R02 instruction changes are not metadata-only; old receipts retain their old tested manifest.','Read and artifact reviewers inherit host methods/permissions as disclosed in their receipts.','No host-trigger pass, Fable final approval, installation or release is inferred.'],
}
print(json.dumps(payload,indent=2))
