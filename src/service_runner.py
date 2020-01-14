import importlib.util
import os


class ProjectSpec:
    def __init__(self, student_id, project_file):
        self.student_id = student_id
        self.badminton_request_file = project_file


class ServiceRunner:
    def build_all_project_specs(self, dir: str) -> []:
        prefix = 'badminton_project_'
        badminton_file_name = 'badminton_request.py'
        project_specs = []
        for root, folders, files in os.walk(dir):
            for folder in folders:
                if folder.startswith(prefix):
                    student_id = folder.strip(prefix)
                    all_files = self.__list_all_files(os.path.join(root, folder))
                    badminton_file = next(filter(lambda file: file.endswith(badminton_file_name), all_files), None)
                    project_specs.append(ProjectSpec(student_id, badminton_file))
        return project_specs

    def __list_all_files(self, root_dir):
        _files = []
        names = os.listdir(root_dir)
        for name in names:
            path = os.path.join(root_dir, name)
            if os.path.isdir(path):
                _files.extend(self.__list_all_files(path))
            if os.path.isfile(path):
                _files.append(path)
        return _files

    def find_all_request_service_class(self, file_paths: []) -> []:
        for path in file_paths:
            module_spec = importlib.util.spec_from_file_location('request_service', path)
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
