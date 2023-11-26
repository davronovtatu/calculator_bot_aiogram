from aiogram import types

from keyboards.inline.calckeyboard import menu
from loader import dp


value = ""

@dp.message_handler(commands="start")
async def select_message(message: types.Message):
    global value
    await message.answer(value or "0", reply_markup=menu)
