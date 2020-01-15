import unittest

from src.badminton_examination import BadmintonExamination


class TestBadmintonExamination(unittest.TestCase):
    def test_should_return_one_spec_when_run_badminton_service(self):
        badminton_examination = BadmintonExamination()
        badminton_dir = './test_data'
        specs = badminton_examination.check(badminton_dir)
        self.assertEqual(1, len(specs))
        self.assertEqual(40, specs[0].score)
        self.assertEqual('001', specs[0].student_id)


if __name__ == '__main__':
    unittest.main()
