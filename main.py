from aiogram import Bot, Dispatcher, executor, types
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN_API = os.getenv('TOKEN_API')



bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(text=message.text) # ответить на сообщение text

if __name__ == '__main__':
    executor.start_polling(dp) # старт бота