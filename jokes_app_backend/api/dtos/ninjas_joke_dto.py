from pydantic.main import BaseModel


class NinjasJokeDTO(BaseModel):
    joke: str
