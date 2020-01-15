import unittest

from src.badminton_scorer import BadmintonScorer


class TestBadmintonScorer(unittest.TestCase):
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
        score = service_runner.check_part_a_score(printed_message)

        self.assertEqual(40, score)

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
        score = service_runner.check_part_a_score(printed_message)

        self.assertEqual(score, 25)


if __name__ == '__main__':
    unittest.main()
