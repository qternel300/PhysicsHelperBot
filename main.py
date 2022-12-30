from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from os import getenv

load_dotenv()

HELP_COMMAND = """
<b>/start</b> - <i>начало работы</i>
<b>/help</b> - <i>начало работы</i>
<b>/картинка</b> - <i>начало работы</i>
"""

async def on_startup(_):
    print('Я запустился!')
TOKEN_API = getenv('TOKEN_API')
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=HELP_COMMAND, parse_mode='HTML')
    await message.delete()



if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
