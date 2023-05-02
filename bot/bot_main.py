import configparser
import os
from aiogram import Bot, Dispatcher, types, executor
from weather.w_request_main import get_weather
from aiogram.utils.exceptions import BotBlocked, ToMuchMessages, UserDeactivated, CantTalkWithBots
from deep_translator import GoogleTranslator

config = configparser.ConfigParser()
c_path = os.path.join(os.path.dirname(__file__), '..', 'config.ini')
config.read(c_path)
token = config['keys']['bot_token']

bot = Bot(token=token, parse_mode='HTML')
dp = Dispatcher(bot)

to_en = GoogleTranslator(source='auto', target='en')


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.answer('Я - бот, который делится погодой\nПришли мне название любого города, а я пришлю погоду')


@dp.message_handler(content_types=types.ContentType.TEXT)
async def weather_tell(message: types.Message):
    if message.text.isdigit():
        await message.answer('Вы ввели не название города')
    en_city = to_en.translate(message.text)
    try:
        answer = (get_weather(en_city))
        await message.answer(answer)
    except IndexError:
        await message.answer('Вы ввели несуществующий город')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
