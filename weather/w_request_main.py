import requests
from weather.w_request_forming import w_make_request
from weather.w_recompile import recompile
import configparser
from geocoding.g_request_forming import g_make_request
from geocoding.g_request_main import get_geo
import os
from connection_handlers.connection import connection_checker


def get_weather(city: str) -> str:
    config = configparser.ConfigParser()
    c_path = os.path.join(os.path.dirname(__file__), '..', 'config.ini')
    config.read(c_path)
    api_key = config['keys']['api_key']
    geo_link = g_make_request(city, api_key)
    latitude = get_geo(geo_link, 'lat')
    longitude = get_geo(geo_link, 'lon')
    weather_link = w_make_request(latitude, longitude, api_key)
    connection_checker(weather_link)
    weather_all = requests.get(weather_link).json()
    weather_final = recompile(weather_all)
    return weather_final
