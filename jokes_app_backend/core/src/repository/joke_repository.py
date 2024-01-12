from abc import ABC, abstractmethod

from .. import Joke


class JokeRepository(ABC):
    @abstractmethod
    def get_joke(self) -> Joke:
        raise NotImplementedError("This method should be implemented in a child class")
