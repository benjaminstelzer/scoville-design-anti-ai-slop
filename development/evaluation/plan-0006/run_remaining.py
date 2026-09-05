"""Queue the already frozen independent comparison cases; never retry an error."""
from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = Path('C:/Users/benja/AppData/Local/Temp/design-plan6-focused-v1-20260904/cases')

def run(case, arm):
    work = ROOT / case / arm
    result = subprocess.run([sys.executable, str(HERE / 'run_consultation.py'), '--cwd', str(work), '--prompt', str(work / 'prompt.txt'), '--output', str(work / 'attempt-1')], capture_output=True, text=True, encoding='utf-8')
    return case, arm, result

if __name__ == '__main__':
    pending = iter((case, arm) for case in ['C1', 'C3', 'C4', 'C5A', 'C5B', 'C6', 'C7'] for arm in ['baseline', 'candidate'])
    failed = False
    with ThreadPoolExecutor(max_workers=2) as pool:
        active = {pool.submit(run, *next(pending)) for _ in range(2)}
        while active:
            done, active = wait(active, return_when=FIRST_COMPLETED)
            for future in done:
                case, arm, result = future.result()
                print(case, arm, result.returncode, result.stdout, result.stderr, flush=True)
                failed = failed or result.returncode != 0
                if not failed:
                    item = next(pending, None)
                    if item: active.add(pool.submit(run, *item))
    sys.exit(1 if failed else 0)
