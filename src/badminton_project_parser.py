import os

BADMINTON_FILE_NAME = '/badminton_request.py'
BADMINTON_PREFIX = 'badminton_project_'


class BadmintonProjectParser:
    def build_all_project_specs(self, root_dir: str) -> []:
        badminton_project_specs = []
        for root, folders, files in os.walk(root_dir):
            for folder in folders:
                if folder.startswith(BADMINTON_PREFIX):
                    student_id = folder[len(BADMINTON_PREFIX):len(folder)]
                    all_files = self.__list_all_files(os.path.join(root, folder))
                    package_name = self.__parse_package_name(all_files, root_dir)
                    badminton_project_specs.append(BadmintonSpec(student_id, root_dir, package_name))
        return badminton_project_specs

    def __parse_package_name(self, all_files, root_dir):
        badminton_file_path = next(filter(lambda file: file.endswith(BADMINTON_FILE_NAME), all_files), None)
        dir = os.path.dirname(badminton_file_path)
        stash_length = 1
        dir_without_root = dir[len(root_dir) + stash_length: len(badminton_file_path)]
        package_name = dir_without_root.replace('/', '.')
        return package_name

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
    def __init__(self, student_id, root_dir: str, package_name: str):
        self.student_id = student_id
        self.root_dir = root_dir
        self.package_name = package_name
