from pydantic.main import BaseModel


class JokeApiDTO(BaseModel):
    error: bool
    category: str
    type: str
    setup: str
    delivery: str
    flags: dict
    id: int
    safe: bool
    lang: str
