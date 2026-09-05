"""Collect actual local evidence; fail on changed exposures or missing outcomes."""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEV = HERE.parents[1]
REPO = DEV.parent
SOURCE = REPO / 'scoville-design-anti-ai-slop'
OUTPUT = REPO.parent / 'output'
sys.path.insert(0, str(DEV / 'scripts'))
from build_package_manifest import build

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()

def read(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))

trials = []
for root in [OUTPUT / 'design-plan7-trials', OUTPUT / 'design-plan7-style-revision']:
    for receipt in sorted(root.glob('PG-*/*/receipt.json')):
        value = read(receipt)
        assert value['exit_code'] == 0 and not value.get('capture_error') and not value.get('errors'), receipt
        if value['arm'] == 'candidate':
            for relative, expected in value['source_hashes'].items():
                assert sha(SOURCE / relative) == expected.upper(), (receipt, relative, 'exposure drift')
        for name, expected in value['artifacts'].items():
            assert sha(receipt.parent / name) == expected.upper(), (receipt, name, 'artifact drift')
        trials.append({k: value[k] for k in ['case','arm','tier','requested_model','effort','session_id','started','finished','exit_code','source_hashes','prompt_sha256','answer_sha256','artifacts','usage']})
        trials[-1].update(receipt_path=str(receipt), receipt_sha256=sha(receipt))
assert len(trials) == 28, f'Expected 28 completed executions, got {len(trials)}'
assert len({t['session_id'] for t in trials}) == 28

render_root = OUTPUT / 'playwright/design-plan7'
renders = []
for receipt in sorted(render_root.glob('V*.json')):
    value = read(receipt)
    assert not value['errors'], (receipt, value['errors'])
    assert sha(Path(value['source'])) == value['source_sha256'].upper(), receipt
    images = [c['image'] for c in value['captures']] + [c['image'] for c in value.get('playback', [])]
    if value.get('reduced'): images.append(value['reduced']['image'])
    renders.append({k:value[k] for k in ['label','family','arm','file','source','source_sha256','chrome']})
    renders[-1].update(receipt_path=str(receipt),receipt_sha256=sha(receipt),images={p:sha(render_root/p) for p in images},overflow=[c['width'] for c in value['captures'] if c['dom']['scrollWidth'] > c['dom']['clientWidth']])

original = read(OUTPUT / 'scoville-design-plan-0007-original-hashes.json')
changed = [r['Path'] for r in original if sha(Path(r['Path'])) != r['Hash']]
old_plan = subprocess.check_output(['git','show','HEAD:development/docs/plans/0006-implement-fable-design-improvements.md'], cwd=REPO).decode('utf-8')
now_plan = (DEV/'docs/plans/0006-implement-fable-design-improvements.md').read_text(encoding='utf-8')
def item4(text):
    return text.split('### W-004',1)[1].split('### W-005',1)[0]
assert item4(old_plan) == item4(now_plan), 'PLAN-0006 W-004 drift'
receipt = read(DEV/'docs/evaluation/plan-0007-final-build.json')
assert build(SOURCE) == receipt['source']
assert build(Path(receipt['runtime_root'])) == receipt['runtime']
assert read(HERE/'freeze-receipt.json')['sha256'] == sha(OUTPUT/'design-plan7-trials/freeze.json')
assert read(HERE/'style-revision-freeze.json')['sha256'] == sha(OUTPUT/'design-plan7-style-revision/freeze.json')
baseline = read(DEV/'docs/evaluation/plan-0007-baseline-tokens.json')
final = read(DEV/'docs/evaluation/plan-0007-final-tokens.json')
result = {
    'scope':'Local source/render/interaction observations; original PG-06 candidate render failed and has a separately identified coordinator repair. Not 28 autonomous design passes.',
    'trials':trials,'renders':renders,
    'followup_receipt':{'path':str(render_root/'followup-v2/receipt.json'),'sha256':sha(render_root/'followup-v2/receipt.json')},
    'integrity':{'source_and_runtime_match_build_receipt':True,'original_monitored':len(original),'unchanged':len(original)-len(changed),'changed':changed,'plan6_w004_unchanged':True,'freezes_unchanged':True,'final_candidate_exposure_hashes_match':True},
    'tokens':{'tokenizer':'o200k_base','core_plus_index':[baseline['core_plus_index'],final['core_plus_index']], 'runtime_instruction_total':[baseline['runtime_instruction_total'],final['runtime_instruction_total']], 'modules':{k:{'before':v,'after':final['modules'][k],'delta':final['modules'][k]-v} for k,v in baseline['modules'].items()}, 'common_loads':{k:{'before':v,'after':final['common_loads'][k],'delta':final['common_loads'][k]-v} for k,v in baseline['common_loads'].items()}}
}
destination = DEV/'docs/evaluation/plan-0007-trial-receipts.json'
with destination.open('x',encoding='utf-8',newline='\n') as f:
    json.dump(result,f,indent=2,ensure_ascii=True);f.write('\n')
print(json.dumps({'trials':len(trials),'rendered_artifacts':len(renders),'overflow':[(r['label'],r['overflow']) for r in renders if r['overflow']],'integrity':result['integrity'],'receipt_sha256':sha(destination)}))
