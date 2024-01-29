import factories


def api_config():
    return {
        "jokes_api": {
            "url": factories.parse_env_variable("JOKES_API"),
            "key": "",
        },
        "ninjas_api": {
            "url": factories.parse_env_variable("NINJAS_API"),
            "key": factories.parse_env_variable("NINJAS_API_KEY"),
        },
        "chuck_norris_api": {
            "url": factories.parse_env_variable("CHUCK_NORRIS_API"),
            "key": "",
        },
    }
