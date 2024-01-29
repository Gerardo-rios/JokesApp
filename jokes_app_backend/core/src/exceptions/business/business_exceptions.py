class BusinessException(Exception):
    def __init__(self, message=""):
        super().__init__(message)


class JokeBusinessException(BusinessException):
    """Jokes business exception"""


class GetJokeException(BusinessException):
    """Get joke exception"""
