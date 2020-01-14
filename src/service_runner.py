class ServiceRunner:

    def find_request_service_class(self):
        pass

    def run_request_service(self) -> str:
        pass

    def check_score(self, printed_message: str) -> int:
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


if __name__ == '__main__':
    service_runner = ServiceRunner()

