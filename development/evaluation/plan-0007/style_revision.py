"""One explicit P2 coverage correction, preserving the original PG-12 outcome."""
import copy
import importlib.util
import json
from pathlib import Path

here = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('frozen_runner', here / 'run_cases.py')
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)
original_root = runner.OUT
original = json.loads((original_root / 'freeze.json').read_text(encoding='utf-8'))
runner.OUT = original_root.parent / 'design-plan7-style-revision'
runner.OUT.mkdir(exist_ok=False)
case = {
    'id': 'PG-12S', 'tier': 'candidate', 'modules': ['style-direction'],
    'reason': 'PG-12 made cross-medium translation conditional and did not exercise row 28. Preserve that coverage gap; this is a new explicit task, not another attempt to improve the same output.',
    'task': "Create main.html with an editable poster and a 360px compact screen notice, translating the same supplied fictional visual relation: two interrupted portions of a word are visibly reconnected by a bridge, making repair extend the word's continuity. This is an original supplied graphic relation, with no historical or cultural claim. Preserve the exact proposition Keep it working. and facts Repair evening; 22 November; Bring one unplugged lamp. Recompose the relation for each medium instead of shrinking the complete poster. The compact notice must fit 360px. control.html is a legitimate quiet literal notice using the same facts and no bridging effect. Explain what is invariant and what changes, without claiming audience testing or prior render inspection.",
    'checks': ['supplied relation visible in both media', 'same proposition and exact facts', 'medium-native allocation at 360px', 'quiet literal control', 'no invented historical authority']
}
revision = copy.deepcopy(original)
revision.update(frozen_at=runner.now(), cases=[case], prompts={case['id']: original['protocol']['artifact_contract'] + '\n\nUSER TASK\n' + case['task']}, revision_of=str(original_root / 'freeze.json'), original_freeze_sha256=runner.digest(original_root / 'freeze.json'), revision_reason=case['reason'])
runner.save(runner.OUT / 'freeze.json', revision)
runner.save(runner.OUT / 'schema.json', runner.SCHEMA)
runner.save(here / 'style-revision-freeze.json', {'path': str(runner.OUT / 'freeze.json'), 'sha256': runner.digest(runner.OUT / 'freeze.json'), 'frozen_at': revision['frozen_at'], 'case': case, 'source_hashes': {'SKILL.md':runner.digest(runner.SOURCE/'SKILL.md'), 'references/style-direction.md':runner.digest(runner.SOURCE/'references/style-direction.md')}})
runner.run(case['id'], 'candidate')
