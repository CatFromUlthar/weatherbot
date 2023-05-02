def g_make_request(city_name: str, appid: str) -> str:
    geo_link = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={appid}'
    return geo_link
