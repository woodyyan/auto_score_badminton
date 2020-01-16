from src.badminton_project_parser import BadmintonSpec
from src.badminton_service import BadmintonService
from src.student_score import StudentScore


class BadmintonScorer:
    def check(self, badminton_spec: BadmintonSpec) -> StudentScore:
        student_score = StudentScore(badminton_spec.student_id)
        student_score.part_a_score = self.check_part_a_score(badminton_spec)
        student_score.part_b_score = self.check_part_b_score(badminton_spec)
        student_score.part_c_score = self.check_part_c_score(badminton_spec)
        return student_score

    def check_part_b_score(self, badminton_spec: BadmintonSpec) -> int:
        service = BadmintonService()
        success_param = 'Book 0001 2019-12-01 14:00~15:00 3'
        success_message = service.request_service(badminton_spec.root_dir, badminton_spec.package_name, success_param)
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
        score += self.__check_invalid_case(badminton_spec, invalid_time_param, 6)

        duplicated_book_param = 'Book 0001 2019-12-01 14:00~16:00 3'
        score += self.__check_invalid_case(badminton_spec, duplicated_book_param, 16)

        end_earlier_than_start_param = 'Book 0001 2019-12-01 15:00~14:00 3'
        score += self.__check_invalid_case(badminton_spec, end_earlier_than_start_param, 6)

        start_time_earlier_param = 'Book 0001 2019-12-01 08:00~10:00 3'
        score += self.__check_invalid_case(badminton_spec, start_time_earlier_param, 6)

        end_time_later_param = 'Book 0001 2019-12-01 20:00~23:00 3'
        score += self.__check_invalid_case(badminton_spec, end_time_later_param, 6)

        return score

    def __check_invalid_case(self, badminton_spec: BadmintonSpec, invalid_param, expected_score):
        fail_sentence = 'Sorry! Something wrong, please call the manager!'
        service = BadmintonService()
        fail_message = service.request_service(badminton_spec.root_dir, badminton_spec.package_name, invalid_param)
        if fail_message == fail_sentence:
            return expected_score
        return 0

    def check_part_a_score(self, badminton_spec: BadmintonSpec) -> int:
        first_line = '********Price********'
        second_line = 'Welcome to badminton'
        last_line = '**Have a good day !**'
        workday_part = '-------Workday-------9:00~12:00 30 yuan/h12:00~18:00 50 yuan/h18:00~20:00 80 yuan/h20:00~22:00 60 yuan/h'
        weekend_part = '-------Weekend-------9:00~12:00 40 yuan/h12:00~18:00 50 yuan/h18:00~22:00 60 yuan/h'

        part_a_param = 'How much?'
        service = BadmintonService()
        printed_message = service.request_service(badminton_spec.root_dir, badminton_spec.package_name, part_a_param)
        score = 0
        if printed_message:
            one_line = printed_message.replace('\r', '').replace('\n', '').strip()
            first_line_index = 0
            second_line_index = 0
            last_line_index = 0
            workday_index = 0
            weekend_index = 0
            if first_line in one_line and second_line in one_line and last_line in one_line:
                score += 5
                first_line_index = one_line.index(first_line)
                second_line_index = one_line.index(second_line)
                last_line_index = one_line.index(last_line)
            if workday_part in one_line:
                score += 15
                workday_index = one_line.index(workday_part)
            if weekend_part in one_line:
                score += 10
                weekend_index = one_line.index(weekend_part)
            is_order_correct = first_line_index < second_line_index < workday_index < weekend_index < last_line_index
            if is_order_correct:
                score += 10
        return score

    def check_part_c_score(self, badminton_spec: BadmintonSpec):
        service = BadmintonService()
        cancel_param = 'Cancel 0001 2019-12-01 14:00~15:00 3'
        success_message = service.request_service(badminton_spec.root_dir, badminton_spec.package_name, cancel_param)
        success_sentence = 'Cancel Success! Look forward to your next visit!'
        score = 0
        if success_message == success_sentence:
            score += 15

        penal_sum_param = 'Cancel 0001 2019-12-11 14:00~16:00 3'
        penal_sum_message = service.request_service(badminton_spec.root_dir, badminton_spec.package_name,
                                                    penal_sum_param)
        first_penal_sum_keyword = 'Cancel Success! You need pay'
        second_penal_sum_keyword = 'yuan as penalty. Look forward to your next visit!'
        if first_penal_sum_keyword in penal_sum_message and second_penal_sum_keyword in penal_sum_message:
            score += 15

        fail_sentence = 'Sorry! Something wrong, please try again!'
        wrong_book_time_param = 'Cancel 0001 2019-12-11 14:00~17:00 3'
        something_wrong_message = service.request_service(badminton_spec.root_dir, badminton_spec.package_name,
                                                          wrong_book_time_param)
        if fail_sentence == something_wrong_message:
            score += 10

        no_book_param = 'Cancel 0002 2019-12-11 20:00~21:00 2'
        something_wrong_message = service.request_service(badminton_spec.root_dir, badminton_spec.package_name,
                                                          no_book_param)
        if fail_sentence == something_wrong_message:
            score += 10

        return score
