from fastapi import FastAPI

from core.src.exceptions import JokeBusinessException

from .api_exceptions import (not_found_exception_handler,
                             server_exception_handler,
                             bad_request_exception_handler)


def add_exception_handlers(app: FastAPI) -> None:
    app.exception_handler(JokeBusinessException)(server_exception_handler)
    app.exception_handler(JokeBusinessException)(not_found_exception_handler)
    app.exception_handler(JokeBusinessException)(bad_request_exception_handler)
