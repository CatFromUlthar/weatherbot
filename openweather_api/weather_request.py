import requests
from connection_handlers.connection import connection_checker


class WeatherParser:
    def __init__(self, geo_all: list, appid: str) -> None:
        self.geo_all = geo_all
        self.appid = appid

    def get_json(self) -> dict:
        lat = self.geo_all[0]['lat']
        lon = self.geo_all[0]['lon']
        link = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={self.appid}&units=metric&lang=ru'
        resp = requests.get(link)
        connection_checker(resp)
        weather_all = resp.json()
        return weather_all

    def recompile(self) -> str:
        weather_all = self.get_json()
        name = self.geo_all[0]['local_names']['ru']
        description = weather_all["weather"][0]["description"].capitalize()
        temp = weather_all["main"]["temp"]
        feels_like = weather_all["main"]["feels_like"]
        pressure = round(weather_all['main']['pressure'] * 0.75006375541921, 2)
        humidity = weather_all['main']['humidity']
        wind = weather_all['wind']['speed']
        final_text = f'Погода в городе {name}:\n{description}, температура: {temp}°, ощущается как \
{feels_like}°\nДавление - {pressure} миллиметров р/с, влажность - {humidity}%\nСкорость ветра - {wind} м/с'
        return final_text
