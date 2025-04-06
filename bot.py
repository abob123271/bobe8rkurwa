from aiogram import Bot, Dispatcher, F
from aiogram.filters.command import Command
from aiogram.types import Message

from dotenv import dotenv_values
from random import choice
import asyncio

from utils import generate_random_ip_address
from users.users import User

insults = [
    'Слышь, лопух, дай бабла',
    'Чертила, ты мне денег дашь, нет?',
    'Я тебе лицо снесу, утырок',
]

config = dotenv_values()

bot = Bot(token=config["TOKEN"])
dp = Dispatcher()

ip_address = generate_random_ip_address()

@dp.message(Command('start'))
async def cmd_start(message: Message):
    user = message.from_user
    first_name = user.first_name
    last_name = user.last_name
    username = user.username
    user_id = user.id
    lang_code = user.language_code
    user_config = User(first_name=first_name, last_name=last_name, 
                username=username, user_id=user_id, 
                lang_code=lang_code, ip=generate_random_ip_address())

    await message.answer('Дай денег')


@dp.message(F.text == 'Добрый день')
@dp.message(F.text == 'Здравствуйте')
async def send_ip(message):
    await message.answer(ip_address)
    await message.answer('За тобой выехали')


@dp.message(F.text)
async def send_random_insult(message):
    insult = choice(insults)
    await message.answer(insult)


async def main():
    await dp.start_polling(bot)

asyncio.run(main())
