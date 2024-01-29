import requests


def get_joke_from_external_api(url, apikey):
    headers = {"Authorization": apikey}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return str(response.status_code)
