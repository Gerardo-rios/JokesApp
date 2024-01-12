from typing import List

from core.src.exceptions import JokeRepositoryException
from core.src.models import Joke
from core.src.repository import JokeRepository


class MemoryJokeRepository(JokeRepository):
    jokes: List[Joke]

    def get_joke(self, joke_api_name: str = "") -> Joke:
        raise JokeRepositoryException(
            "Memory Joke Repository not implemented yet.", "get_joke"
        )
