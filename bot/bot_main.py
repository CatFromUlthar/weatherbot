import configparser
import os
from aiogram import Bot, Dispatcher, types, executor
from weather.w_request_main import get_weather
from aiogram.utils.exceptions import BotBlocked, ToMuchMessages, UserDeactivated, CantTalkWithBots
from translate import Translator

config = configparser.ConfigParser()
c_path = os.path.join(os.path.dirname(__file__), '..', 'config.ini')
config.read(c_path)
token = config['keys']['bot_token']

bot = Bot(token=token, parse_mode='HTML')
dp = Dispatcher(bot)

to_en = Translator(to_lang='en')


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.answer('Я - бот, который делится погодой\nПришли мне название любого города, а я пришлю погоду')


@dp.message_handler(content_types=types.ContentType.TEXT)
async def weather_tell(message: types.Message):
    answer = to_en.translate(get_weather(message.text))
    print(answer)
    print(message.text)
    await message.answer(answer)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
