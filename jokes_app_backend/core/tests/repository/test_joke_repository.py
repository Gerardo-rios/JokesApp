import pytest

import core


def test__joke_repository_is_an_abstract_class():
    assert core.JokeRepository.__abstractmethods__ == frozenset({"get_joke"})


def test__joke_repository_get_joke_is_an_abstract_method():
    assert core.JokeRepository.get_joke.__isabstractmethod__


def test__joke_repository_get_joke_abract_method_raises_not_implemented_error(mocker):
    joke_repository = mocker.Mock()

    mocker.patch.object(joke_repository, "get_joke", side_effect=NotImplementedError)

    with pytest.raises(NotImplementedError):
        joke_repository.get_joke()
