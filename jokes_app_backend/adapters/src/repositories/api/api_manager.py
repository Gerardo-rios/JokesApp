from ...config import api_config


class ApiManager:
    def __init__(self):
        self.jokes_apis = api_config()

    def get_url(self, api_name):
        return self.jokes_apis.get(api_name, {}).get("url", None)

    def get_api_key(self, api_name):
        return self.jokes_apis.get(api_name, {}).get("key", None)
