import sys
import importlib.util

MODULE_NAME = 'badminton_request'
REQUEST_SERVICE_FUNCTION_NAME = 'request_service'


class BadmintonService:
    def request_service(self, root_dir: str, package_name: str, param: str) -> str:
        # root_dir = '/Users/songbai.yan/Downloads/Python/auto'
        # package_name = 'badminton_project_c00475177.badminton'

        badminton_dir = '/'.join([root_dir, package_name.replace('.', '/')])
        # badminton_dir = '/Users/songbai.yan/Downloads/Python/auto/badminton_project_c00475177/badminton'
        package_module_name = '.'.join([package_name, MODULE_NAME])
        # package_module_name = 'badminton_project_c00475177.badminton.badminton_request'

        sys.path.append(root_dir)
        sys.path.append(badminton_dir)
        badminton_request_module = importlib.import_module(package_module_name)
        request_service = getattr(badminton_request_module, REQUEST_SERVICE_FUNCTION_NAME)
        message = request_service(param)
        sys.path.remove(badminton_dir)
        return message

        # try:
        #     sys.path.append(badminton_dir)
        #     import badminton_request
        #     message = badminton_request.request_service(param)
        #     sys.path.remove(badminton_dir)
        #     del badminton_request
        #     return message
        # except:
        #     return ''




