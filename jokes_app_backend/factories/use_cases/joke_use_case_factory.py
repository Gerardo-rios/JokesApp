from core.src import JokeRepository
from core.src.use_cases import GetJoke

from ..config import JokeRepositoryConfig


def get_joke_repository() -> JokeRepository:
    return JokeRepositoryConfig.get_repository()


def get_joke_use_case() -> GetJoke:
    return GetJoke(joke_repository=get_joke_repository())
