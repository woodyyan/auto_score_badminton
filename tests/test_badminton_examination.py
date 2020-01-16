import unittest

from src.badminton_examination import BadmintonExamination


class TestBadmintonExamination(unittest.TestCase):
    def test_should_return_one_spec_when_run_badminton_service(self):
        badminton_examination = BadmintonExamination()
        root_dir = './test_data'
        specs = badminton_examination.check(root_dir)
        self.assertEqual(1, len(specs))
        self.assertEqual(40, specs[0].part_a_score)
        self.assertEqual(60, specs[0].part_b_score)
        self.assertEqual(50, specs[0].part_c_score)
        self.assertEqual('c001', specs[0].student_id)


if __name__ == '__main__':
    unittest.main()
