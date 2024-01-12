from core.src.exceptions import JokeRepositoryException
from core.src.models import Joke
from core.src.repository import JokeRepository


class JsonJokeRepository(JokeRepository):
    def __init__(self, json_path: str):
        self._json_path = json_path

    def get_joke(self, joke_api_name: str = "") -> Joke:
        raise JokeRepositoryException("Not implemented yet.", "get_joke")

    def _load_jokes(self) -> list[Joke]:
        raise JokeRepositoryException("Not implemented yet.", "load_jokes")
