from configs.config_reader import read_config
from aiogram import Bot, Dispatcher, types, executor
from weather.w_request_main import get_weather
from bot_translator import translate

token = read_config('bot_token')

bot = Bot(token=token, parse_mode='HTML')
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.answer('Я - бот, который делится погодой\nПришли мне название любого города, а я пришлю погоду')


@dp.message_handler(content_types=types.ContentType.TEXT)
async def weather_tell(message: types.Message):
    try:
        en_city = translate(message.text.capitalize())
        answer = (get_weather(en_city))
        await message.answer(answer)
    except IndexError:
        await message.answer('Такого города нет в нашей базе данных или вы ввели несуществующий город')
    except:
        await message.answer('Вы ввели некорректную информацию')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
