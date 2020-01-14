import importlib.util
import sys
import unittest

from src.service_runner import ServiceRunner


class TestServiceRunnerCase(unittest.TestCase):
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
        service_runner = ServiceRunner()
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
        service_runner = ServiceRunner()
        score = service_runner.check_score(printed_message)

        self.assertEqual(score, 25)

    def test_should_return_1_when_build_all_project_specs_given_dir(self):
        dir = './test_data'
        service_runner = ServiceRunner()
        project_specs = service_runner.build_all_project_specs(dir)
        self.assertEqual(len(project_specs), 1)
        self.assertEqual(project_specs[0].student_id, '001')
        self.assertEqual(project_specs[0].badminton_request_file,
                         './test_data/badminton_project_c001/badminton_request.py')

    def test_should_return_correct_printed_message_when_run_badminton_py_file(self):
        service_runner = ServiceRunner()
        badminton_dir = './test_data/badminton_project_c001'
        spec = service_runner.run_request_service(badminton_dir)
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







if __name__ == '__main__':
    unittest.main()
