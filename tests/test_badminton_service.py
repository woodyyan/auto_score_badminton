import importlib.util
import sys
import unittest

from src.badminton_scorer import BadmintonScorer
from src.badminton_service import BadmintonService


class TestBadmintonService(unittest.TestCase):

    def test_should_return_correct_printed_message_when_run_badminton_py_file(self):
        badminton_service = BadmintonService()
        badminton_dir = './test_data/badminton_project_c001'
        message = badminton_service.request_service(badminton_dir, 'How much?')
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
        self.assertEqual(expected_message, message)


if __name__ == '__main__':
    unittest.main()
