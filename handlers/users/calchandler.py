from aiogram import types

from keyboards.inline.calckeyboard import menu
from loader import dp,bot

# value=""
# old_value=""
#
# @dp.message_handler(commands="calc")
# async def select_message(message:types.Message):
#     global value
#     if value=="":
#         await message.answer("0",reply_markup=menu)
#     else:
#         await message.answer(value,reply_markup=menu)
#
#
#
# @dp.callback_query_handler(lambda call:True)
# async def self_calc(query:types.CallbackQuery):
#     global value,old_value
#     data=query.data
#
#     if data=="no":
#         pass
#     elif data=="C":
#         value=""
#
#     elif data=="=":
#         try:
#             value=str(eval(value))
#         except:
#             value="Xatolik"
#
#     else:
#         value+=data
#
#     if value !=old_value:
#         if value==" ":
#             await bot.edit_message_text(chat_id=query.message.chat.id,message_id=query.message.message_id,text="0",reply_markup=menu)
#         else:
#             await bot.edit_message_text(chat_id=query.message.chat.id,message_id=query.message.message_id,text=value,reply_markup=menu)
#     old_value=value

value = ""

@dp.message_handler(commands="calc")
async def select_message(message: types.Message):
    global value
    await message.answer(value or "0", reply_markup=menu)

@dp.callback_query_handler(lambda call: True)
async def self_calc(query: types.CallbackQuery):
    global value
    data = query.data

    if data == "C":
        value = ""
    elif data == "=":
        try:
            value = str(eval(value))
        except:
            value = "Xatolik"
    elif data != "no":
        value += data

    if value != query.message.text:
        await bot.edit_message_text(
            chat_id=query.message.chat.id,
            message_id=query.message.message_id,
            text=value or "0",
            reply_markup=menu
        )


