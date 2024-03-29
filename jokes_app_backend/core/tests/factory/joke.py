from typing import Any, Callable

from faker import Faker
from pytest import fixture

from core.src.models import Joke


@fixture
def joke_factory(
    faker: Faker,
) -> Callable:
    def _factory(**kwargs: Any) -> Joke:
        return Joke(
            **{
                **{
                    "id": faker.uuid4(),
                    "joke": faker.sentence(),
                },
                **kwargs,
            }
        )

    return _factory
