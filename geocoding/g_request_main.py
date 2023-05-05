import requests
from connection_handlers.connection import connection_checker


def get_json(link: str) -> list:
    connection_checker(link)
    geo_all = requests.get(link).json()
    return geo_all


def get_geo(geo_all: list, param: str) -> float | str:
    if param == 'lat':
        latitude = geo_all[0][param]
        return latitude
    elif param == 'lon':
        longitude = geo_all[0][param]
        return longitude
    elif param == 'local_names':
        name = geo_all[0][param]['ru']
        return name
    else:
        raise ValueError("Wrong parameter. Only 'lon', 'lat' or 'local_names' allowed")
