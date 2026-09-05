"""Synthetic capture-helper regression tests; never package case evidence."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).with_name('capture_review.py')

class ReviewCaptureTests(unittest.TestCase):
    def run_capture(self, phases, exact=None, contexts=True):
        with tempfile.TemporaryDirectory(prefix='p6-review-capture-test-') as tmp:
            root=Path(tmp)
            events=[{'type':'session_meta','payload':{'id':'synthetic-test-id','agent_path':'/root/synthetic_review'}}]
            if contexts: events.append({'type':'turn_context','payload':{'model':'gpt-5.6-sol','effort':'high'}})
            for index, phase in enumerate(phases):
                events.append({'timestamp':str(index),'type':'response_item','payload':{'type':'message','role':'assistant','phase':phase,'content':[{'text':'message-'+str(index)}]}})
            trace=root/'trace.jsonl'
            trace.write_text(''.join(json.dumps(e)+'\n' for e in events),encoding='utf-8')
            dest=root/'capture'
            args=[sys.executable,str(SCRIPT),str(trace),'/root/synthetic_review',str(dest)]
            if exact is not None: args.extend(['--review-at',exact])
            result=subprocess.run(args,capture_output=True,text=True)
            return result.returncode, (dest/'review.md').read_text(encoding='utf-8') if dest.exists() else None

    def test_commentary_after_final_is_not_selected(self):
        self.assertEqual(self.run_capture(['commentary','final_answer','commentary']),(0,'message-1\n'))

    def test_latest_completed_final_selected(self):
        self.assertEqual(self.run_capture(['final_answer','commentary','final_answer','commentary']),(0,'message-2\n'))

    def test_exact_older_final_can_be_recovered(self):
        self.assertEqual(self.run_capture(['final_answer','commentary','final_answer'],exact='0'),(0,'message-0\n'))

    def test_exact_commentary_is_rejected(self):
        code, body=self.run_capture(['final_answer','commentary'],exact='1')
        self.assertNotEqual(code,0)
        self.assertIsNone(body)

    def test_no_final_is_rejected(self):
        code, body=self.run_capture(['commentary'])
        self.assertNotEqual(code,0)
        self.assertIsNone(body)

    def test_missing_context_is_rejected(self):
        code, body=self.run_capture(['final_answer'],contexts=False)
        self.assertNotEqual(code,0)
        self.assertIsNone(body)

if __name__=='__main__': unittest.main()
