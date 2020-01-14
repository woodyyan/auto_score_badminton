import unittest

from src.service_runner import ServiceRunner


class TestServiceRunnerCase(unittest.TestCase):
    def test_check_score(self):
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
**Have a good day !**'''
        service_runner = ServiceRunner()
        score = service_runner.check_score(printed_message)

        self.assertEqual(score, 40)


if __name__ == '__main__':
    unittest.main()
