import sys


class BadmintonService:
    def request_service(self, badminton_dir: str, param: str) -> str:
        try:
            sys.path.append(badminton_dir)
            import badminton_request
            message = badminton_request.request_service(param)
            sys.path.remove(badminton_dir)
            return message
        except:
            return ''
