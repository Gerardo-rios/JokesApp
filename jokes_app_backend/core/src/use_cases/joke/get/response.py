from typing import NamedTuple

from core.src.models import Joke


class GetJokeUseCaseResponse(NamedTuple):
    joke: Joke
