
def connection_checker(resp) -> None:
    if not resp.ok:
        raise ConnectionError(f'Failed to connect openweather API site. Status code: {resp.status_code}')
