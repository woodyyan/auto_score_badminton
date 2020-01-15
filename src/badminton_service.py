import sys


class BadmintonService:
    def request_service(self, badminton_dir: str, param: str) -> str:
        try:
            sys.path.append(badminton_dir)
            import badminton_request
            return badminton_request.request_service(param)
        except:
            return ''
