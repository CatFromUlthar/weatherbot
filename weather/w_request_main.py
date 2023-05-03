import requests
from weather.w_request_forming import w_make_request
from weather.w_recompile import recompile
from geocoding.g_request_forming import g_make_request
from geocoding.g_request_main import get_json, get_geo
from connection_handlers.connection import connection_checker
from configs.config_reader import read_config


def get_weather(city: str) -> str:
    api_key = read_config('api_key')
    geo_link = g_make_request(city, api_key)
    geo_all = get_json(geo_link)
    latitude = get_geo(geo_all, 'lat')
    longitude = get_geo(geo_all, 'lon')
    name = get_geo(geo_all, 'local_names')
    weather_link = w_make_request(latitude, longitude, api_key)
    connection_checker(weather_link)
    weather_all = requests.get(weather_link).json()
    weather_final = recompile(weather_all, name)
    return weather_final
