import random

import core

from . import ApiManager, get_joke_from_external_api


class ApiJokeRepository(core.JokeRepository):
    def get_joke(self) -> core.Joke:
        api_manager = ApiManager()
        joke_apis = ["JOKES_API", "NINJAS_API", "CHUCK_NORRIS_API"]
        random_api = random.choice(joke_apis)
        try:
            joke = get_joke_from_external_api(
                api_manager.get_url(random_api), api_manager.get_api_key(random_api)
            )
            print(joke)
            return joke
        except JokeRepositoryException:
            raise core.JokeRepositoryException(
                "Not implemented yet.", "Api Joke Repository get joke"
            )
