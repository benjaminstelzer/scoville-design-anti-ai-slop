"""Freeze public inputs and create package-only comparison workspaces once."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys

PROJECT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
ROOT = Path('C:/Users/benja/AppData/Local/Temp/design-plan6-focused-v1-20260904')
BASELINE = Path('C:/Users/benja/AppData/Local/Temp/design-plan6-baseline-56c4166e6b414f339dd882944b052091/scoville-design-anti-ai-slop')
NODE = 'C:/Users/benja/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node.exe'
sys.path.insert(0, str(PROJECT / 'scripts'))
from build_package_manifest import build, executable_paths

def main():
    protocol = json.loads((HERE / 'protocol-v1.json').read_text(encoding='utf-8'))
    target = ROOT / 'cases'
    if target.exists():
        raise ValueError('Cases already prepared; refusing overwrite')
    frozen = {str(p.relative_to(HERE)).replace('\\', '/'): hashlib.sha256(p.read_bytes()).hexdigest().upper() for p in [HERE / 'protocol-v1.json', *sorted((HERE / 'inputs').glob('*'))]}
    manifests = {'baseline': build(BASELINE), 'candidate': build(ROOT / 'candidate')}
    (ROOT / 'freeze.json').write_text(json.dumps({'inputs': frozen, 'packages': manifests}, indent=2) + '\n', encoding='utf-8')
    # Render exactly the same supplied input before either arm responds.
    for filename in ['small.html', 'generic.html', 'quiet.html', 'motion.html', 'mixed.html']:
        kind = 'motion' if filename == 'motion.html' else 'static'
        width = {'small.html': '600', 'quiet.html': '960', 'motion.html': '1000', 'mixed.html': '1000'}.get(filename, '1440')
        subprocess.run([NODE, str(HERE / 'render.mjs'), str(HERE / 'inputs' / filename), str(ROOT / 'input-proofs' / Path(filename).stem), kind, width], check=True)
    for case in protocol['cases']:
        for arm, package in [('baseline', BASELINE), ('candidate', ROOT / 'candidate')]:
            work = target / case['id'] / arm
            (work / 'inputs').mkdir(parents=True)
            for relative in executable_paths(package):
                dest = work / 'skill' / relative
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(package / relative, dest)
            shutil.copyfile(HERE / 'inputs' / case['input'], work / 'inputs' / case['input'])
            if case['id'] in ['C2', 'C7']:
                shutil.copyfile(HERE / 'inputs' / 'facts.txt', work / 'inputs' / 'facts.txt')
            if case['id'] != 'C6':
                shutil.copytree(ROOT / 'input-proofs' / Path(case['input']).stem, work / 'inputs' / 'proof')
            prompt = 'Use the installed-form design package in skill/SKILL.md for this task, reading only the actual linked modules you need. Work only with files inside this workspace.\n\n' + case['prompt']
            if case['id'] != 'C6':
                prompt += '\nActual screen/playback proofs of the supplied input are in inputs/proof; inspect applicable PNGs and observations.json.'
            prompt += '\n\nYou have read-only file tools. Return proposed source for the authorised host to materialise, not a claim of already edited files. Output one JSON object only, with files (array of {path, content}, a single artifact.html for source tasks; empty for critique) and notes (a string containing the concise task response and limits). No code fences. Do not render by assertion. The host will return actual rendered evidence where available.'
            (work / 'prompt.txt').write_text(prompt + '\n', encoding='utf-8')
    print(json.dumps({'root': str(ROOT), 'cases': len(protocol['cases']), 'arms': 2, 'frozen_inputs': len(frozen), 'baseline': manifests['baseline']['manifest_sha256'], 'candidate': manifests['candidate']['manifest_sha256']}))

if __name__ == '__main__':
    main()
