from pydantic.main import BaseModel


class ChuckNorrisDTO(BaseModel):
    icon_url: str
    id: str
    url: str
    value: str
