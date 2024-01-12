from factories.config import parse_env_variable


class EnvConfig:
    ENV: str = parse_env_variable("ENV")

    @classmethod
    def is_dev(cls) -> bool:
        return cls.ENV == "DEV"
