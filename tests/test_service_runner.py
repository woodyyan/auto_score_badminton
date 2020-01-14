import importlib.util
import sys
import unittest

from src.badminton_runner import BadmintonScorer


class TestServiceRunnerCase(unittest.TestCase):
    badminton_dir = './test_data'

    def test_should_return_40_when_check_score_given_correct_printed_message(self):
        printed_message = '''********Price********
Welcome to badminton
-------Workday-------
9:00~12:00 30 yuan/h
12:00~18:00 50 yuan/h
18:00~20:00 80 yuan/h
20:00~22:00 60 yuan/h
-------Weekend-------
9:00~12:00 40 yuan/h
12:00~18:00 50 yuan/h
18:00~22:00 60 yuan/h
**Have a good day !**
'''
        service_runner = BadmintonScorer()
        score = service_runner.check_score(printed_message)

        self.assertEqual(score, 40)

    def test_should_return_25_when_check_score_without_default_messages(self):
        printed_message = '''
-------Workday-------
9:00~12:00 30 yuan/h
12:00~18:00 50 yuan/h
18:00~20:00 80 yuan/h
20:00~22:00 60 yuan/h
-------Weekend-------
9:00~12:00 40 yuan/h
12:00~18:00 50 yuan/h
18:00~22:00 60 yuan/h
'''
        service_runner = BadmintonScorer()
        score = service_runner.check_score(printed_message)

        self.assertEqual(score, 25)

    def test_should_return_1_when_build_all_project_specs_given_dir(self):
        badminton_scorer = BadmintonScorer()
        project_specs = badminton_scorer.build_all_project_specs(self.badminton_dir)
        self.assertEqual(len(project_specs), 1)
        self.assertEqual(project_specs[0].student_id, '001')
        self.assertEqual(project_specs[0].badminton_request_dir,
                         './test_data/badminton_project_c001')

    def test_should_return_correct_printed_message_when_run_badminton_py_file(self):
        badminton_scorer = BadmintonScorer()
        badminton_dir = './test_data/badminton_project_c001'
        spec = badminton_scorer.run_request_service(badminton_dir)
        expected_message = '''********Price********
Welcome to badminton
-------Workday-------
9:00~12:00 30 yuan/h
12:00~18:00 50 yuan/h
18:00~20:00 80 yuan/h
20:00~22:00 60 yuan/h
-------Weekend-------
9:00~12:00 40 yuan/h
12:00~18:00 50 yuan/h
18:00~22:00 60 yuan/h
**Have a good day !**'''
        self.assertEqual(spec, expected_message)

    def test_should_return_one_spec_when_run_badminton_service(self):
        badminton_scorer = BadmintonScorer()

        specs = badminton_scorer.run(self.badminton_dir)
        self.assertEqual(len(specs), 1)
        self.assertEqual(specs[0].score, 40)


if __name__ == '__main__':
    unittest.main()
