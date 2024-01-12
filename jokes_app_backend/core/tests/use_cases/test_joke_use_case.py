# import pytest

# from core.src.exceptions import JokeBusinessException
# from core.src.use_cases import GetJoke
# from factories.repositories import api_joke_repository


# def test__joke_use_case_creation__returns_joke_use_case_instance():
#     joke_use_case = GetJoke(joke_repository=None)

#     assert isinstance(joke_use_case, GetJoke)


# @pytest.mark.asyncio
# async def test__joke_use_case_execute__returns_joke():
#     repository = api_joke_repository()

#     joke_use_case = GetJoke(joke_repository=repository)

#     with pytest.raises(
#         JokeBusinessException,
#         match="Something was wrong trying to Not implemented yet. the Api Joke Repository",
#     ):
#         await joke_use_case.execute()
#     # joke = await joke_use_case.execute()

#     # assert joke is not None
#     # assert isinstance(joke, GetJokeResponse)
