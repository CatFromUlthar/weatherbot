def w_make_request(lat: float, lon: float, appid: str) -> str:
    weather_link = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={appid}&units=metric&lang=ru'
    return weather_link
