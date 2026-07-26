import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

# Твой личный токен от BotFather
API_TOKEN = '8861147643:AAG35lLBDhxRhzE3BjEL05Y4ACG8TE9xx_4'

# Создаем объекты бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Команда /start
@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}! Я твой первый бот на Python! 🚀")

# Ответ на любое текстовое сообщение
@dp.message()
async def echo_message(message: types.Message):
    await message.answer("Я тебя понял! Ты учишься программировать, молодец! 👍")

# Функция запуска
async def main():
    print("Бот успешно запущен и ждет сообщений...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
