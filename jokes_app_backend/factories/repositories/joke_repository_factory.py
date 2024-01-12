import os

from adapters.src.repositories import (ApiJokeRepository, JsonJokeRepository,
                                       MemoryJokeRepository)
from core.src.repository import JokeRepository
from factories.config.json import JSONFiles


def json_joke_repository() -> JokeRepository:
    current_directory = os.getcwd()
    file_path = os.path.join(current_directory, JSONFiles.JOKE_FILE)
    return JsonJokeRepository(file_path)


def memory_joke_repository() -> JokeRepository:
    return MemoryJokeRepository()


def api_joke_repository() -> JokeRepository:
    return ApiJokeRepository()
