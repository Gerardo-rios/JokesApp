import pytest

import core

from . import ApiJokeRepository


def test__api_joke_repository_get_joke_method_returns_joke():
    api_joke_repository = ApiJokeRepository()

    joke = api_joke_repository.get_joke()

    assert joke is not None


def test__api_joke_repository_get_joke_method_raises_an_error_when_api_returns_an_error(
    mocker,
):
    api_joke_repository = ApiJokeRepository()

    # mocker.patch.object(
    # api_joke_repository,
    # 'get_joke',
    # side_effect=JokeRepositoryException("Not implemented yet.", "Api Joke Repository get joke")
    # )

    with pytest.raises(core.JokeRepositoryException):
        api_joke_repository.get_joke()
