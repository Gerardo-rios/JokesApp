from ..utils import parse_env_variable


class JSONFiles:
    JOKE_FILE: str = parse_env_variable("JOKE_JSON_FILE")
