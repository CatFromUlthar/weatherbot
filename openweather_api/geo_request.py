import requests
from connection_handlers.connection import connection_checker


class GeoParser:

    def __init__(self, city: str, appid: str) -> None:
        self.city = city
        self.appid = appid

    def get_json(self) -> list:
        link = f'http://api.openweathermap.org/geo/1.0/direct?q={self.city}&limit=1&appid={self.appid}'
        resp = requests.get(link)
        connection_checker(resp)
        geo_all = resp.json()
        return geo_all
