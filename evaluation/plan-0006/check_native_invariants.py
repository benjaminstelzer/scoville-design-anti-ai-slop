"""Read-only exact-source checks; these do not imply rendered quality."""
import argparse
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re

ROOT = Path('C:/Users/benja/AppData/Local/Temp/design-plan6-sol-native-v1-20260904')

def sha(data):
    return hashlib.sha256(data).hexdigest().upper()

def group(source, name):
    match = re.search(r'<g\b[^>]*\bid="' + re.escape(name) + r'"[^>]*>.*?</g>', source, re.S)
    if not match: raise ValueError('Missing group ' + name)
    return match.group()

class Words(HTMLParser):
    def __init__(self):
        super().__init__()
        self.skip = 0
        self.words = []
    def handle_starttag(self, tag, attrs):
        if tag in ['style', 'script']: self.skip += 1
    def handle_endtag(self, tag):
        if tag in ['style', 'script']: self.skip -= 1
    def handle_data(self, data):
        if not self.skip: self.words.extend(data.split())

parser = argparse.ArgumentParser()
parser.add_argument('label')
parser.add_argument('--freeze', default='freeze.json')
args = parser.parse_args()
freeze = json.loads((ROOT / args.freeze).read_text(encoding='utf-8'))
entry = freeze['sessions'][args.label]
work = ROOT / args.label
answer = json.loads((work / 'capture-1/answer.json').read_text(encoding='utf-8'))
checks = {}
for name, expected in entry['inputs'].items():
    checks['frozen:' + name] = sha((work / name).read_bytes()) == expected
if entry['case'] == 'C7':
    checks['critique_has_no_proposed_files'] = answer['files'] == []
elif entry['case'] in ['C5A', 'C5B', 'C6']:
    before = (work / 'inputs/mixed.html').read_text(encoding='utf-8')
    after = (work / 'artifact.html').read_text(encoding='utf-8')
    for name in ['pack-fixed', 'sign-fixed']:
        checks[name + '_exact_bytes'] = group(before, name) == group(after, name)
    old_words, new_words = Words(), Words()
    old_words.feed(before)
    new_words.feed(after)
    checks['visible_words_including_title_unchanged'] = old_words.words == new_words.words
    if entry['case'] == 'C6':
        checks['everything_outside_pack_text_unchanged'] = before.replace(group(before, 'pack-text'), '') == after.replace(group(after, 'pack-text'), '')
        checks['no_render_supplied_or_generated'] = not (work / 'inputs/proof').exists() and not any(work.glob('proof*'))
print(json.dumps({'label': args.label, 'case': entry['case'], 'checks': checks, 'pass': all(checks.values()), 'limit': 'Source invariants only; no rendered, production or preference claim.'}))
raise SystemExit(0 if all(checks.values()) else 1)
