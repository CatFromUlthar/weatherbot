from configs.config_reader import read_config
from openweather_api.geo_request import GeoParser
from openweather_api.weather_request import WeatherParser


def create_text(city: str) -> str:
    api_key = read_config('api_key')
    gp = GeoParser(city, api_key)
    gp.get_json()
    wp = WeatherParser(gp.geo_all, api_key)
    wp.get_json()
    wp.recompile()
    return wp.final_text