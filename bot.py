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


@dp.message(Command('start'))
async def cmd_start(message: Message):
    user = message.from_user
    user_id = user.id
    if not User.check_if_user_exists(user_id=user_id):
        first_name = user.first_name
        last_name = user.last_name
        username = user.username
        lang_code = user.language_code
        User(first_name=first_name, last_name=last_name, 
                    username=username, user_id=user_id, 
                    lang_code=lang_code, ip=generate_random_ip_address())

    await message.answer('Дай денег')


@dp.message(F.text == 'Добрый день')
@dp.message(F.text == 'Здравствуйте')
async def send_ip(message: Message):
    user = message.from_user
    user_config = User.create_from_file(user.id)
    await message.answer(user_config.ip)
    await message.answer(f'Ты надоел вызываю ментов, {user.first_name}!')
    await message.answer('За тобой выехали')


@dp.message(F.text)
async def send_random_insult(message):
    insult = choice(insults)
    await message.answer(insult)


async def main():
    await dp.start_polling(bot)

asyncio.run(main())
