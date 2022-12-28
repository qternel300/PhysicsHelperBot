from aiogram import Bot, Dispatcher, executor, types


TOKEN_API = '5887818155:AAGXj_UKxkRaFp_UcqmAQg3AKd02WYU_9fo'



bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(text=message.text) # ответить на сообщение text

if __name__ == '__main__':
    executor.start_polling(dp) # старт бота