import sys
import importlib.util

MODULE_NAME = 'badminton_request'
REQUEST_SERVICE_FUNCTION_NAME = 'request_service'


class BadmintonService:
    def request_service(self, root_dir: str, package_name: str, param: str) -> str:
        badminton_dir = '/'.join([root_dir, package_name.replace('.', '/')])
        package_module_name = '.'.join([package_name, MODULE_NAME])

        sys.path.append(root_dir)
        sys.path.append(badminton_dir)
        try:
            badminton_request_module = importlib.import_module(package_module_name)
            request_service = getattr(badminton_request_module, REQUEST_SERVICE_FUNCTION_NAME)
            return request_service(param)
        except:
            return ''
        finally:
            sys.path.remove(badminton_dir)





