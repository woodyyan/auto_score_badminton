import sys
import importlib.util

MODULE_NAME = 'badminton_request'
REQUEST_SERVICE_FUNCTION_NAME = 'request_service'


class BadmintonService:
    def request_service(self, root_dir: str, package_name: str, param: str) -> str:
        packages = package_name.split('.')
        package_dir = root_dir
        all_package_dirs = []
        for package in packages:
            package_dir = '/'.join([package_dir, package])
            all_package_dirs.append(package_dir)

        package_module_name = '.'.join([package_name, MODULE_NAME])

        sys.path.append(root_dir)
        for dir in all_package_dirs:
            sys.path.append(dir)
        try:
            badminton_request_module = importlib.import_module(package_module_name)
            request_service = getattr(badminton_request_module, REQUEST_SERVICE_FUNCTION_NAME)
            return request_service(param)
        except Exception as error:
            print(package_name)
            print(error)
            return ''
        finally:
            for dir in all_package_dirs:
                sys.path.remove(dir)
