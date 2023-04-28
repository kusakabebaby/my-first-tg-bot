

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=token)
dp=Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def startcom(message:types.Message):
    await message.reply("привет")

@dp.message_handler()
async def first(message:types.Message):
 
    if "привет" in message.text.lower():
        await bot.send_message(message.from_user.id,"привет!")
    elif "как дела" in message.text.lower():
        await bot.send_message(message.from_user.id,"у меня все отлично! а как твои дела?")
    elif "меня зовут" in message.text.lower():
        await bot.send_message(message.from_user.id, f"нет, ты меня обманываешь! тебя зовут {message.from_user.username}")
    else:
        await bot.send_message(message.from_user.id,"прости, но я тебя не понимаю(")
executor.start_polling(dp)
