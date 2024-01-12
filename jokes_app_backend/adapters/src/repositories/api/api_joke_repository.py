from core.src.exceptions import JokeRepositoryException
from core.src.models import Joke
from core.src.repository import JokeRepository


class ApiJokeRepository(JokeRepository):
    def get_joke(self) -> Joke:
        raise JokeRepositoryException("Api Joke Repository", "Not implemented yet.")
