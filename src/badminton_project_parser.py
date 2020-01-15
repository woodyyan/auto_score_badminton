import os


class BadmintonProjectParser:
    def build_all_project_specs(self, dir: str) -> []:
        prefix = 'badminton_project_'
        badminton_file_name = '/badminton_request.py'
        project_specs = []
        for root, folders, files in os.walk(dir):
            for folder in folders:
                if folder.startswith(prefix):
                    student_id = folder[len(prefix):len(folder)]
                    all_files = self.__list_all_files(os.path.join(root, folder))
                    badminton_file = next(filter(lambda file: file.endswith(badminton_file_name), all_files), None)
                    project_specs.append(BadmintonSpec(student_id, os.path.dirname(badminton_file)))
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


class BadmintonSpec:
    def __init__(self, student_id, badminton_service_dir):
        self.student_id = student_id
        self.badminton_service_dir = badminton_service_dir
