import enum


class HttpCode(enum.Enum):
    OK = 200
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
