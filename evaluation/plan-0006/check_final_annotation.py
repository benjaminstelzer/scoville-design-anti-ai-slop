"""Verify the exact post-test metadata-only annotation and historical snapshots."""
import hashlib
import json
from pathlib import Path
import re
import sys
import yaml

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO/'scripts'))
from build_package_manifest import build
from build_runtime_package import runtime_bytes

def load(path): return json.loads(path.read_text(encoding='utf-8'))
tested = load(REPO/'docs/evaluation/plan-0006-record-scope-build.json')
final = load(REPO/'docs/evaluation/plan-0006-final-local-build.json')
old, new = Path(tested['runtime_root']), Path(final['runtime_root'])
checks = {}
checks['tested_runtime_unchanged'] = build(old) == tested['runtime']
checks['final_source_manifest_exact'] = build(REPO) == final['source']
checks['final_runtime_manifest_exact'] = build(new) == final['runtime']
changed = []
for item in tested['runtime']['files']:
    name = item['path']
    a, b = (old/name).read_bytes(), (new/name).read_bytes()
    if a != b: changed.append(name)
    checks['build_transform:' + name] = runtime_bytes(name,(REPO/name).read_bytes()) == b
checks['only_registry_changed_after_retest'] = changed == ['modules.yaml']
before, after = (old/'modules.yaml').read_bytes(), (new/'modules.yaml').read_bytes()
deannotated = re.sub(rb'(?m)^(    evidence:) \[[^\r\n]*\]', rb'\1 []', after)
checks['all_bytes_except_evidence_values_identical'] = deannotated == before
a, b = yaml.safe_load(before), yaml.safe_load(after)
for module in b['modules']: module['evidence'] = []
checks['all_non_evidence_fields_identical'] = a == b
attached = yaml.safe_load(after)
registry = load(REPO/'docs/evaluation/plan-0006-case-receipts.json')
checks['annotations_match_observed_mapping'] = all(m['evidence'] == registry['module_annotations'][m['id']] for m in attached['modules'])
checks['no_status_promotion'] = all(m['status']=='draft' for m in attached['modules'])
result = {'pass':all(checks.values()),'changed_files':changed,'tested_runtime_sha256':tested['runtime']['manifest_sha256'],'annotated_runtime_sha256':final['runtime']['manifest_sha256'],'checks':checks,'limit':'Only evidence annotation is being verified here. The earlier five R02 instruction changes are separately tested and are not metadata-only.'}
print(json.dumps(result,indent=2))
raise SystemExit(0 if result['pass'] else 1)
