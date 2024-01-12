from core.src.exceptions import JokeBusinessException, JokeRepositoryException
from core.src.repository import JokeRepository

from .response import GetJokeResponse


class GetJoke:
    pass
    # def __init__(self, joke_repository: JokeRepository):
    #     self.joke_repository = joke_repository

    # async def execute(self) -> GetJokeResponse:
    #     try:
    #         joke = self.joke_repository.get_joke()
    #     except JokeRepositoryException as error:
    #         raise JokeBusinessException(str(error))

    #     return GetJokeResponse(joke=joke)
