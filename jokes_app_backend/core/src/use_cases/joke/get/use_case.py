from core.src.exceptions import JokeRepositoryException
from core.src.repository import JokeRepository


class GetJoke:
    def __init__(self, joke_repository: JokeRepository):
        self.joke_repository = joke_repository

    async def execute(self):
        try:
            joke = self.joke_repository.get_joke()
        except JokeRepositoryException:
            raise JokeRepositoryException("Use case", "execute")
        return joke
