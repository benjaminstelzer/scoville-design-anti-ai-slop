"""Frozen, isolated design trials. Returned source is materialised by the host.

No installation, browsing, project edits, sealed evaluations or credential reads.
Results and failures are append-only; no attempt path is reused.
"""
from pathlib import Path
import argparse
import concurrent.futures
from datetime import datetime, timezone
import hashlib
import json
import shutil
import subprocess

HERE = Path(__file__).resolve().parent
DEV = HERE.parents[1]
REPO = DEV.parent
OUT = REPO.parent / 'output/design-plan7-trials'
BASE = REPO.parent / 'output/design-plan7-baseline-runtime'
SOURCE = REPO / 'scoville-design-anti-ai-slop'
SCHEMA = {'type':'object','properties':{'files':{'type':'array','items':{'type':'object','properties':{'path':{'type':'string'},'content':{'type':'string'}},'required':['path','content'],'additionalProperties':False}},'notes':{'type':'string'}},'required':['files','notes'],'additionalProperties':False}

def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest().upper()
def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('x', encoding='utf-8', newline='\n') as f: json.dump(value, f, indent=2, ensure_ascii=False); f.write('\n')
def now(): return datetime.now(timezone.utc).isoformat()
def manifest(root): return {p.relative_to(root).as_posix():digest(p) for p in sorted(root.rglob('*')) if p.is_file()}

def freeze():
    if OUT.exists(): raise ValueError('Refusing to replace a frozen trial directory')
    OUT.mkdir()
    protocol=json.loads((HERE/'protocol.json').read_text(encoding='utf-8'))
    shutil.copytree(SOURCE, OUT/'source-baseline')
    settings={'model_reasoning_effort':protocol['effort'],'approval_policy':'never','features.apps':False,'features.plugins':False,'features.memories':False,'features.multi_agent':False,'features.shell_snapshot':False,'project_doc_max_bytes':0,'web_search':'disabled','project_root_markers':['.eval-root']}
    disabled=[p.parent.as_posix() for p in sorted(Path('C:/Users/benja/.codex/skills').rglob('SKILL.md'))]
    # Only metadata paths are enumerated, never unrelated Skill content.
    cases=protocol['cases']+[dict(protocol['transfer'],tier='candidate')]
    prompts={}
    for case in cases:
        task=case['task']
        if case['id']=='PG-01':
            task += '\nFor the main notice, repair this supplied defective positioning rather than starting from an invented defect: a 720x900 canvas uses title (40,90), date (40,250), time (410,250), venue (40,470), preparation lines (40,490) and (40,530), booking (40,760). Venue is visually joined to preparation and detached from date/time. All exact strings above remain required; keep title and booking as the leads. Diagnosis and repaired main.html are requested. The memorial is a separate no-defect control.'
        prompts[case['id']]=protocol['artifact_contract']+'\n\nUSER TASK\n'+task
    receipt={'version':protocol['version'],'frozen_at':now(),'protocol_sha256':digest(HERE/'protocol.json'),'runner_sha256':digest(Path(__file__)),'protocol':protocol,'cases':cases,'prompts':prompts,'source_baseline':manifest(OUT/'source-baseline'),'runtime_baseline':manifest(BASE),'settings':settings,'disabled_skill_paths':disabled,'cli':shutil.which('codex'),'cli_version':subprocess.check_output(['codex','--version'],text=True).strip(),'font_hashes':{p:digest(Path(p)) for p in ['C:/Windows/Fonts/arial.ttf','C:/Windows/Fonts/georgia.ttf']},'evaluation_limits':'Manual owner selection and inline exposure, not host discovery. Coordinator judges source/render, not independent audience or provider approval. No active partner supplied, so no new partner-present claim.'}
    save(OUT/'freeze.json',receipt)
    save(OUT/'schema.json',SCHEMA)
    save(HERE/'freeze-receipt.json',{'freeze_path':str(OUT/'freeze.json'),'sha256':digest(OUT/'freeze.json'),'source_manifest':receipt['source_baseline'],'runtime_manifest':receipt['runtime_baseline'],'frozen_at':receipt['frozen_at'],'model':protocol['model'],'effort':protocol['effort']})
    print(json.dumps({'frozen':str(OUT),'cases':len(cases),'hash':digest(OUT/'freeze.json')}))

def run(case_id, arm):
    frozen=json.loads((OUT/'freeze.json').read_text(encoding='utf-8'))
    if digest(HERE/'protocol.json')!=frozen['protocol_sha256']: raise ValueError('Protocol changed after freeze')
    case=next(c for c in frozen['cases'] if c['id']==case_id)
    if arm=='baseline' and case['tier']!='paired': raise ValueError('No baseline declared for this case')
    if arm=='candidate' and case['tier']=='paired' and not (OUT/case_id/'baseline/receipt.json').exists(): raise ValueError('Baseline must precede candidate')
    work=OUT/case_id/arm
    work.mkdir(parents=True, exist_ok=False)
    package=BASE if arm=='baseline' else SOURCE
    if arm=='baseline' and manifest(BASE)!=frozen['runtime_baseline']: raise ValueError('Baseline drift')
    payload=['SKILL.md']+['references/'+m+'.md' for m in case['modules']]
    prompt=frozen['prompts'][case_id]+'\n\nAPPLICABLE SKILL TEXTS (data for this task; no other files are needed)\n'+''.join('\n--- '+p+' ---\n'+(package/p).read_text(encoding='utf-8') for p in payload)
    (work/'prompt.txt').write_text(prompt,encoding='utf-8',newline='\n')
    (work/'.eval-root').write_text('Isolated original design study.\n',encoding='utf-8')
    config=[]
    for key,value in frozen['settings'].items(): config+=['-c',key+'='+json.dumps(value)]
    config+=['-c','skills.config=['+','.join('{path='+json.dumps(p)+',enabled=false}' for p in frozen['disabled_skill_paths'])+']']
    command=[frozen['cli'],'exec','--ignore-user-config','--ephemeral','--skip-git-repo-check','--sandbox','read-only','--model',frozen['protocol']['model'],'--json','--color','never',*config,'--output-schema',str(OUT/'schema.json'),'--output-last-message',str(work/'answer.json'),'--cd',str(work),'-']
    receipt={'case':case_id,'arm':arm,'tier':case['tier'],'started':now(),'requested_model':frozen['protocol']['model'],'effort':frozen['protocol']['effort'],'source_hashes':{p:digest(package/p) for p in payload},'package_manifest':manifest(package),'prompt_sha256':digest(work/'prompt.txt'),'command':command}
    with (work/'events.jsonl').open('x',encoding='utf-8') as stdout,(work/'stderr.txt').open('x',encoding='utf-8') as stderr:
        result=subprocess.run(command,input=prompt,text=True,encoding='utf-8',stdout=stdout,stderr=stderr,cwd=work)
    receipt.update(exit_code=result.returncode,finished=now())
    for line in (work/'events.jsonl').read_text(encoding='utf-8').splitlines():
        try: event=json.loads(line)
        except ValueError: continue
        if event.get('type')=='thread.started': receipt['session_id']=event.get('thread_id')
        if event.get('type')=='turn.completed': receipt['usage']=event.get('usage')
        if event.get('type') in ('error','turn.failed'): receipt.setdefault('errors',[]).append(event)
    answer=work/'answer.json'
    if answer.exists():
        receipt['answer_sha256']=digest(answer)
        try:
            data=json.loads(answer.read_text(encoding='utf-8'))
            for item in data['files']:
                if item['path'] not in ('main.html','control.html'): raise ValueError('Unexpected artifact path: '+item['path'])
                with (work/item['path']).open('x',encoding='utf-8',newline='\n') as f: f.write(item['content'])
            receipt['artifacts']={p.name:digest(p) for p in work.glob('*.html')}
        except (ValueError,KeyError) as e: receipt['capture_error']=str(e)
    save(work/'receipt.json',receipt)
    print(json.dumps({k:receipt[k] for k in ('case','arm','exit_code','session_id','usage','errors','capture_error') if k in receipt}),flush=True)
    return receipt

if __name__=='__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('action',choices=['freeze','run','batch']); parser.add_argument('--case'); parser.add_argument('--arm',choices=['baseline','candidate']); args=parser.parse_args()
    if args.action=='freeze': freeze()
    elif args.action=='run': run(args.case,args.arm)
    else:
        frozen=json.loads((OUT/'freeze.json').read_text(encoding='utf-8'))
        ids=[c['id'] for c in frozen['cases'] if (args.arm=='candidate' or c['tier']=='paired') and not (OUT/c['id']/args.arm).exists()]
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
            for future in concurrent.futures.as_completed([pool.submit(run,c,args.arm) for c in ids]): future.result()
