import requests
from connection_handlers.connection import connection_checker


class GeoParser:

    def __init__(self, city, appid):
        self.city = city
        self.appid = appid
        self.link = None
        self.geo_all = None

    def get_json(self):
        self.link = f'http://api.openweathermap.org/geo/1.0/direct?q={self.city}&limit=1&appid={self.appid}'
        connection_checker(self.link)
        self.geo_all = requests.get(self.link).json()