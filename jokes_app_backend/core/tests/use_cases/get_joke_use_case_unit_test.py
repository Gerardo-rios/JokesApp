import pytest

import core


def test__joke_use_case_creation__returns_joke_use_case_instance():
    joke_use_case = core.GetJoke(joke_repository=None)

    assert isinstance(joke_use_case, core.GetJoke)


@pytest.mark.asyncio
async def test__execute__returns_a_joke_when_successfully_run(mocker, faker):
    expected_joke = faker.sentence(nb_words=5)

    joke_repository = mocker.Mock()

    joke_use_case = core.GetJoke(joke_repository=joke_repository)

    mocker.patch.object(
        joke_use_case.joke_repository, "get_joke", return_value=expected_joke
    )

    joke = await joke_use_case.execute()

    assert joke == expected_joke


@pytest.mark.asyncio
async def test__execute__returns_a_error_when_use_case_raises_an_exception(mocker):
    expected_error = core.JokeRepositoryException("Repository", "get joke")

    print(expected_error)

    joke_repository = mocker.Mock()

    joke_use_case = core.GetJoke(joke_repository=joke_repository)

    mocker.patch.object(
        joke_use_case.joke_repository, "get_joke", side_effect=expected_error
    )

    with pytest.raises(core.JokeRepositoryException) as error:
        await joke_use_case.execute()
        assert isinstance(error, core.GetJokeException)
        assert error.value == expected_error
