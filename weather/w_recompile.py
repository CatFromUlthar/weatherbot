def recompile(w: dict, name: str) -> str:
    city = name
    description = w["weather"][0]["description"].title()
    temp = w["main"]["temp"]
    feels_like = w["main"]["feels_like"]
    pressure = round(w['main']['pressure'] * 0.75006375541921, 2)
    humidity = w['main']['humidity']
    wind = w['wind']['speed']

    text = f'Погода в городе {city}:\n{description}, температура - {temp}°, ощущается как {feels_like}°\nДавление - \
{pressure} миллиметров р/с, влажность - {humidity}%\nСкорость ветра - {wind} м/с'
    return text
