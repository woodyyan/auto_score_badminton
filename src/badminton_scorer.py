from src.badminton_service import BadmintonService


class BadmintonScorer:
    def check(self, badminton_service_dir: str) -> int:
        score = 0
        service = BadmintonService()
        part_a_param = 'How much?'
        part_a_message = service.request_service(badminton_service_dir, part_a_param)
        score += self.check_part_a_score(part_a_message)
        return score

    def check_part_b_score(self, badminton_service_dir: str) -> int:
        service = BadmintonService()
        success_param = 'Book 0001 2019-12-01 14:00~15:00 3'
        success_message = service.request_service(badminton_service_dir, success_param)
        score = 0
        success_keyword = 'Success'
        if success_keyword in success_message:
            score += 5
        # Success! You can use the No.3 court during 2019-12-11 14:00~15:00.
        all_keywords = ['No.3', '2019', '12', '11', '14', '15']
        contained_keywords = [True for keyword in all_keywords if keyword in success_message]
        if len(contained_keywords) == len(all_keywords):
            score += 15

        return score

    def check_part_a_score(self, printed_message: str) -> int:

        first_line = '********Price********'
        second_line = 'Welcome to badminton'
        last_line = '**Have a good day !**'
        workday_part = '''-------Workday-------
9:00~12:00 30 yuan/h
12:00~18:00 50 yuan/h
18:00~20:00 80 yuan/h
20:00~22:00 60 yuan/h'''
        weekend_part = '''-------Weekend-------
9:00~12:00 40 yuan/h
12:00~18:00 50 yuan/h
18:00~22:00 60 yuan/h'''
        lines = printed_message.split('\n')
        lines = [line for line in lines if line]
        score = 0
        if first_line in printed_message and second_line in printed_message and last_line in printed_message:
            score += 5
        if workday_part in printed_message:
            score += 15
        if weekend_part in printed_message:
            score += 10
        if len(lines) == 12:
            score += 10
        return score


class ScoreInfo:
    def __init__(self):
        self.part_a_score = 0
        self.part_b_score = 0
        self.part_c_score = 0
        self.test_coverage = 0
