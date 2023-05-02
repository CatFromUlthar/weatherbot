import requests
from connection_handlers.connection import connection_checker


def get_geo(link: str, param: str) -> float:
    connection_checker(link)
    geo_all = requests.get(link).json()
    if param == 'lat':
        latitude = geo_all[0][param]
        return latitude
    elif param == 'lon':
        longitude = geo_all[0][param]
        return longitude
    else:
        raise ValueError("Wrong parameter. Only 'lon' or 'lat' allowed")
