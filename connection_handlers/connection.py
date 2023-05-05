import requests


def connection_checker(link: str):
    resp = requests.get(link)
    if not resp.ok:
        raise ConnectionError(f'Failed to connect openweather API site. Status code: {resp.status_code}')
