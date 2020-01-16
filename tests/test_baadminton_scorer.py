import unittest

from src.badminton_project_parser import BadmintonSpec
from src.badminton_scorer import BadmintonScorer


class TestBadmintonScorer(unittest.TestCase):
    root_dir = './test_data'
    package_name = 'badminton_project_c001'

    def test_should_return_40_when_check_score_given_correct_printed_message(self):
        badminton_scorer = BadmintonScorer()
        spec = BadmintonSpec('001', self.root_dir, self.package_name)
        score = badminton_scorer.check_part_a_score(spec)
        self.assertEqual(40, score)

    def test_should_return_60_when_check_part_b_given_can_success_message(self):
        badminton_scorer = BadmintonScorer()
        spec = BadmintonSpec('001', self.root_dir, self.package_name)
        score = badminton_scorer.check_part_b_score(spec)
        self.assertEqual(60, score)

    def test_should_return_50_when_check_part_c_given_cancel_message(self):
        badminton_scorer = BadmintonScorer()
        spec = BadmintonSpec('001', self.root_dir, self.package_name)
        score = badminton_scorer.check_part_c_score(spec)
        self.assertEqual(50, score)

    def test_should_return_score_summary_when_check_given_dir(self):
        badminton_scorer = BadmintonScorer()
        spec = BadmintonSpec('001', self.root_dir, self.package_name)
        score_summary = badminton_scorer.check(spec)
        self.assertEqual(40, score_summary.part_a_score)
        self.assertEqual(60, score_summary.part_b_score)
        self.assertEqual(50, score_summary.part_c_score)


if __name__ == '__main__':
    unittest.main()
