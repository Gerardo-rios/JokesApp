from typing import NamedTuple

from core.src.models import Joke


class GetJokeResponse(NamedTuple):
    joke: Joke
