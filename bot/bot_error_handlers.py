from bot_main import dp
from aiogram.utils.exceptions import ToMuchMessages, TelegramAPIError, MessageTextIsEmpty, MessageIsTooLong


@dp.errors_handler(exception=TelegramAPIError)
async def handle_telegram_api_error(update):
    await update.message.answer("Произошла ошибка при отправке сообщения. Попробуйте позже.")


@dp.errors_handler(exception=MessageTextIsEmpty)
async def handle_empty_message(update):
    await update.message.answer("Вы не ввели текст сообщения. Пожалуйста, введите текст.")


@dp.errors_handler(exception=ToMuchMessages)
async def handle_to_many_messages(update):
    await update.message.answer("Слишком много сообщений. Попробуйте позже.")


@dp.errors_handler(exception=MessageIsTooLong)
async def handle_too_long_message(update):
    await update.message.answer("Сообщение слишком длинное")
