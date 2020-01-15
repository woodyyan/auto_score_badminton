from src.badminton_service import BadmintonService


class ScoreSummary:
    def __init__(self):
        self.part_a_score = 0
        self.part_b_score = 0
        self.part_c_score = 0
        self.test_coverage = 0


class BadmintonScorer:
    def check(self, badminton_service_dir: str) -> ScoreSummary:
        score_summary = ScoreSummary()
        score_summary.part_a_score = self.check_part_a_score(badminton_service_dir)
        score_summary.part_b_score = self.check_part_b_score(badminton_service_dir)
        score_summary.part_c_score = self.check_part_c_score(badminton_service_dir)
        return score_summary

    def check_part_b_score(self, badminton_service_dir: str) -> int:
        service = BadmintonService()
        success_param = 'Book 0001 2019-12-01 14:00~15:00 3'
        success_message = service.request_service(badminton_service_dir, success_param)
        score = 0
        if success_message:
            success_keyword = 'Success'
            if success_keyword in success_message:
                score += 5

            all_keywords = ['No.3', '2019', '12', '11', '14', '15']
            contained_keywords = [True for keyword in all_keywords if keyword in success_message]
            if len(contained_keywords) == len(all_keywords):
                score += 15

        invalid_time_param = 'Book 0001 2019-12-01 14:00~14:20 3'
        score += self.__check_invalid_case(badminton_service_dir, invalid_time_param, 6)

        duplicated_book_param = 'Book 0001 2019-12-01 14:00~16:00 3'
        score += self.__check_invalid_case(badminton_service_dir, duplicated_book_param, 16)

        end_earlier_than_start_param = 'Book 0001 2019-12-01 15:00~14:00 3'
        score += self.__check_invalid_case(badminton_service_dir, end_earlier_than_start_param, 6)

        start_time_earlier_param = 'Book 0001 2019-12-01 08:00~10:00 3'
        score += self.__check_invalid_case(badminton_service_dir, start_time_earlier_param, 6)

        end_time_later_param = 'Book 0001 2019-12-01 20:00~23:00 3'
        score += self.__check_invalid_case(badminton_service_dir, end_time_later_param, 6)

        return score

    def __check_invalid_case(self, badminton_service_dir, invalid_param, expected_score):
        fail_sentence = 'Sorry! Something wrong, please call the manager!'
        service = BadmintonService()
        fail_message = service.request_service(badminton_service_dir, invalid_param)
        if fail_message == fail_sentence:
            return expected_score
        return 0

    def check_part_a_score(self, badminton_service_dir: str) -> int:
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

        part_a_param = 'How much?'
        service = BadmintonService()
        printed_message = service.request_service(badminton_service_dir, part_a_param)
        score = 0
        if printed_message:
            lines = printed_message.split('\n')
            lines = [line for line in lines if line]
            if first_line in printed_message and second_line in printed_message and last_line in printed_message:
                score += 5
            if workday_part in printed_message:
                score += 15
            if weekend_part in printed_message:
                score += 10
            if len(lines) == 12:
                score += 10
        return score

    def check_part_c_score(self, badminton_service_dir: str):
        service = BadmintonService()
        cancel_param = 'Cancel 0001 2019-12-01 14:00~15:00 3'
        success_message = service.request_service(badminton_service_dir, cancel_param)
        success_sentence = 'Cancel Success! Look forward to your next visit!'
        score = 0
        if success_message == success_sentence:
            score += 15

        penal_sum_param = 'Cancel 0001 2019-12-11 14:00~16:00 3'
        penal_sum_message = service.request_service(badminton_service_dir, penal_sum_param)
        first_penal_sum_keyword = 'Cancel Success! You need pay'
        second_penal_sum_keyword = 'yuan as penalty. Look forward to your next visit!'
        if first_penal_sum_keyword in penal_sum_message and second_penal_sum_keyword in penal_sum_message:
            score += 15

        fail_sentence = 'Sorry! Something wrong, please try again!'
        wrong_book_time_param = 'Cancel 0001 2019-12-11 14:00~17:00 3'
        something_wrong_message = service.request_service(badminton_service_dir, wrong_book_time_param)
        if fail_sentence == something_wrong_message:
            score += 10

        no_book_param = 'Cancel 0002 2019-12-11 20:00~21:00 2'
        something_wrong_message = service.request_service(badminton_service_dir, no_book_param)
        if fail_sentence == something_wrong_message:
            score += 10

        return score


