import requests


class WeatherParser:
    def __init__(self, geo_all: list, appid: str) -> None:
        self.geo_all = geo_all
        self.appid = appid
        self.link = None
        self.weather_all = None
        self.final_text = None

    def get_json(self) -> None:
        lat = self.geo_all[0]['lat']
        lon = self.geo_all[0]['lon']
        self.link = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={self.appid}&units=metric&lang=ru'
        self.weather_all = requests.get(self.link).json()

    def recompile(self) -> None:
        name = self.geo_all[0]['local_names']['ru']
        description = self.weather_all["weather"][0]["description"].title()
        temp = self.weather_all["main"]["temp"]
        feels_like = self.weather_all["main"]["feels_like"]
        pressure = round(self.weather_all['main']['pressure'] * 0.75006375541921, 2)
        humidity = self.weather_all['main']['humidity']
        wind = self.weather_all['wind']['speed']
        self.final_text = f'Погода в городе {name}:\n{description}, температура: {temp}°, ощущается как \
{feels_like}°\nДавление - {pressure} миллиметров р/с, влажность - {humidity}%\nСкорость ветра - {wind} м/с'
