"""Exercise supplied observed transport text, not request/marker presence."""

import importlib.util
import json
from pathlib import Path
import unittest


DEVELOPMENT = Path(__file__).resolve().parents[1]
FIXTURES = DEVELOPMENT / "evaluation/plan-0017/transport"
spec = importlib.util.spec_from_file_location("read_coverage", DEVELOPMENT / "scripts/read_coverage.py")
coverage = importlib.util.module_from_spec(spec)
spec.loader.exec_module(coverage)


class ReadCoverageTests(unittest.TestCase):
    def setUp(self):
        self.source = (FIXTURES / "lesson.txt").read_bytes()
        self.full = json.loads((FIXTURES / "full.json").read_text(encoding="utf-8"))["responses"][0]["observer_received"]

    def test_six_supplied_transport_fixtures(self):
        names = ["full", "tail-cut", "middle-cut", "outer-cut", "recovery", "unavailable"]
        for name in names:
            fixture = json.loads((FIXTURES / f"{name}.json").read_text(encoding="utf-8"))
            self.assertEqual(fixture["evidence_kind"], "synthetic")
            for reference in [None, self.source]:
                with self.subTest(fixture=name, reference=reference is not None):
                    result = coverage.verify_coverage(fixture["responses"], fixture["source_id"], reference)
                    for key, expected in fixture["expected"].items():
                        self.assertEqual(result[key], expected, key)

    def test_recovery_retains_initial_missing_ranges(self):
        fixture = json.loads((FIXTURES / "recovery.json").read_text(encoding="utf-8"))
        result = coverage.verify_coverage(fixture["responses"], "lesson.txt", self.source)
        self.assertTrue(result["complete"])
        self.assertEqual(result["responses"][0]["missing_in_declared_range"], [[4, 9]])
        self.assertEqual(result["observed_ranges"], [[1, 12]])

    def test_filename_last_paragraph_and_high_limit_do_not_supply_coverage(self):
        result = coverage.verify_coverage([{"observer_received": "lesson.txt\nClosing paragraph.\n", "requested_max_output_tokens": 1000000}], "lesson.txt", self.source)
        self.assertEqual(result["status"], "unverified")
        self.assertEqual(result["observed_line_count"], 0)
        self.assertEqual(result["missing_ranges"], [[1, 12]])

    def test_plain_unnumbered_source_remains_unverified(self):
        result = coverage.verify_coverage([self.source.decode("utf-8")], "lesson.txt")
        self.assertFalse(result["complete"])
        self.assertIsNone(result["missing_ranges"])

    def test_unterminated_final_line_is_not_counted(self):
        result = coverage.verify_coverage([self.full.rstrip("\n")], "lesson.txt")
        self.assertFalse(result["complete"])
        self.assertEqual(result["missing_ranges"], [[12, 12]])

    def test_spliced_truncation_marker_line_is_not_counted(self):
        spliced = self.full.replace("4: Use the existing palette.", "4: Use th…20486 tokens truncated…ting palette.")
        result = coverage.verify_coverage([spliced], "lesson.txt")
        self.assertEqual(result["status"], "unverified")
        self.assertEqual(result["missing_ranges"], [[4, 4]])
        self.assertEqual(result["observed_line_count"], 11)

    def test_evaluator_reference_detects_silent_content_substitution(self):
        replaced = self.full.replace("Use the existing palette.", "Use an invented palette.")
        runtime = coverage.verify_coverage([replaced], "lesson.txt")
        self.assertTrue(runtime["complete"], "Line metadata alone cannot detect invisible content substitution")
        evaluator = coverage.verify_coverage([replaced], "lesson.txt", self.source)
        self.assertEqual(evaluator["status"], "contradictory")
        self.assertTrue(any("reference content mismatch at line 4" in item for item in evaluator["contradictions"]))
        self.assertEqual(len(evaluator["reference_source_sha256"]), 64)

    def test_evaluator_reference_detects_false_total_even_when_claimed_range_complete(self):
        short = self.full.replace("TOTAL=12 RANGE=1-12", "TOTAL=11 RANGE=1-11")
        short = short.replace("12: Closing paragraph.\n", "")
        result = coverage.verify_coverage([short], "lesson.txt", self.source)
        self.assertEqual(result["status"], "contradictory")
        self.assertEqual(result["missing_ranges"], [[12, 12]])

    def test_conflicting_source_or_total_metadata_blocks_pass(self):
        for altered in [self.full.replace("SOURCE=lesson.txt", "SOURCE=other.txt"), self.full.replace("TOTAL=12", "TOTAL=13")]:
            with self.subTest(header=altered.splitlines()[0]):
                result = coverage.verify_coverage([self.full, altered], "lesson.txt")
                self.assertEqual(result["status"], "contradictory")
                self.assertFalse(result["complete"])

    def test_outside_declared_range_blocks_pass(self):
        result = coverage.verify_coverage([self.full.replace("RANGE=1-12", "RANGE=1-11")], "lesson.txt")
        self.assertEqual(result["status"], "contradictory")
        self.assertEqual(result["missing_ranges"], [[12, 12]])

    def test_identical_overlap_across_reads_is_counted_once(self):
        result = coverage.verify_coverage([self.full, self.full], "lesson.txt", self.source)
        self.assertTrue(result["complete"])
        self.assertEqual(result["observed_line_count"], 12)
        self.assertEqual(result["duplicate_line_count"], 12)

    def test_conflicting_duplicate_blocks_pass_even_with_all_line_numbers(self):
        changed = self.full.replace("Use the existing palette.", "Different content.")
        result = coverage.verify_coverage([self.full, changed], "lesson.txt")
        self.assertEqual(result["status"], "contradictory")
        self.assertTrue(any("conflicting content at line 4" in item for item in result["contradictions"]))

    def test_repeated_line_within_one_response_blocks_pass(self):
        repeated = self.full.replace("2: \n", "1: # Workshop notes\n2: \n")
        result = coverage.verify_coverage([repeated], "lesson.txt")
        self.assertEqual(result["status"], "contradictory")
        self.assertEqual(result["observed_line_count"], 12)

    def test_out_of_order_lines_block_pass(self):
        shuffled = self.full.replace("3: Keep the supplied name.\n4: Use the existing palette.\n", "4: Use the existing palette.\n3: Keep the supplied name.\n")
        result = coverage.verify_coverage([shuffled], "lesson.txt")
        self.assertEqual(result["status"], "contradictory")

    def test_nested_hidden_response_is_not_received_evidence(self):
        result = coverage.verify_coverage([{"observer_received": "Outer response truncated.\n", "inner_response": {"output": self.full}}], "lesson.txt", self.source)
        self.assertFalse(result["complete"])
        self.assertEqual(result["observed_line_count"], 0)
        with self.assertRaises(ValueError):
            coverage.verify_coverage([{"inner_response": {"output": self.full}}])

    def test_multiple_source_headers_are_ambiguous(self):
        result = coverage.verify_coverage([self.full + self.full], "lesson.txt")
        self.assertEqual(result["status"], "contradictory")
        self.assertEqual(result["observed_line_count"], 0)


if __name__ == "__main__":
    unittest.main()
