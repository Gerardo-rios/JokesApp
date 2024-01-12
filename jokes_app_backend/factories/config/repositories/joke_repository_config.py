import os

from factories.repositories import (api_joke_repository, json_joke_repository,
                                    memory_joke_repository)

from .base import RepositoryConfig


class JokeRepositoryConfig(RepositoryConfig):
    _REPOSITORY = os.getenv("JOKE_REPOSITORY", "JSON")
    _AVAILABLE_REPOSITORIES = [
        "JSON",
        "API",
        "MEMORY",
    ]

    @classmethod
    def _get_repository_instances(cls) -> dict:
        return {
            "JSON": json_joke_repository(),
            "API": api_joke_repository(),
            "MEMORY": memory_joke_repository(),
        }
