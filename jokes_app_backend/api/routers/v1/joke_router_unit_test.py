import json

import pytest
from fastapi.responses import JSONResponse

import core

from . import joke_router


@pytest.mark.asyncio
async def test__get_joke__returns_200__when_use_case_returns_a_joke():
    use_case = core.GetJoke()

    response: JSONResponse = await joke_router.get_joke(use_case)

    assert response.status_code == 200


@pytest.mark.asyncio
async def test__get_joke__returns_joke_data_when_use_case_returns_a_joke(mocker, faker):
    random_joke = faker.word()

    use_case = core.GetJoke()

    mocker.patch.object(use_case, "execute", return_value=random_joke)

    response: JSONResponse = await joke_router.get_joke(use_case)

    response_body = json.loads(response.body)
    assert response_body == {"data": random_joke}


@pytest.mark.asyncio
async def test__get_joke__returns_500__when_use_case_raises_an_exception(mocker):
    expected_response = JSONResponse({"error": "Error getting joke"}, status_code=500)

    use_case = core.GetJoke()

    mocker.patch.object(
        use_case, "execute", side_effect=core.GetJokeException("Error getting joke")
    )

    response: JSONResponse = await joke_router.get_joke(use_case)

    assert response.status_code == expected_response.status_code
    assert response.body == expected_response.body
