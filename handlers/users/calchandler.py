from aiogram import types
import requests

from keyboards.default.keymenu import obhavo
from keyboards.inline.calckeyboard import menu
from loader import dp,bot






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
#
#
# # ob havo
@dp.message_handler(commands="ob-havo")
@dp.message_handler(commands="Location")
async def select_menu(message:types.Message):
    await message.answer("Manzilingizni yuboring",reply_markup=obhavo)


import requests
#
# WEATHER_API_KEY = "12c82a0790e84ec8ae6154829232611"
#
# @dp.message_handler(content_types=types.ContentTypes.LOCATION)
# async def handle_location(message: types.Message):
#     latitude = message.location.latitude
#     longitude = message.location.longitude
#
#     # WeatherAPI ga so'rov tuzish
#     api_url = f"https://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={latitude},{longitude}&aqi=yes"
#     response = requests.get(api_url)
#
#     if response.status_code == 200:
#         weather_data = response.json()
#         # Endi  weather_data obyektida foydalanuvchi joylashuvi bo'yicha hozirgi ob-havo ma'lumotlarini topasiz
#         # Shu ma'lumotlarni foydalanuvchiga yuboring yoki kerakli vazifalarni bajarishni davom ettirishingiz mumkin
#         await message.answer(f"Ob-havo ma'lumotlari: {weather_data}")
#     else:
#         await message.answer("Ob-havo ma'lumotlarini olishda xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
#



WEATHER_API_KEY = "12c82a0790e84ec8ae6154829232611"

@dp.message_handler(content_types=types.ContentTypes.LOCATION)
async def handle_location(message: types.Message):
    latitude = message.location.latitude
    longitude = message.location.longitude

    # WeatherAPI ga so'rov tuzish
    api_url = f"https://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={latitude},{longitude}&aqi=yes"
    response = requests.get(api_url)

    if response.status_code == 200:
        weather_data = response.json()
        location_info = weather_data.get("location", {})
        current_info = weather_data.get("current", {})

        #  xabar tuzish
        text = (
            f"Assalomu alaykum! Hozirgi ob-havo ma'lumotlari:\n\n"
            f"Joy: {location_info.get('name', '')}, {location_info.get('region', '')}, {location_info.get('country', '')}\n"
            f"Latitude: {location_info.get('lat', '')}, Longitude: {location_info.get('lon', '')}\n"
            f"Temperature: {current_info.get('temp_c', '')}°C, Condition: {current_info.get('condition', {}).get('text', '')}\n"
            f"Wind: {current_info.get('wind_kph', '')} kph, Humidity: {current_info.get('humidity', '')}%\n"
            f"Air Quality: CO {current_info.get('air_quality', {}).get('co', '')}, NO2 {current_info.get('air_quality', {}).get('no2', '')}\n"
            f"Ozone: {current_info.get('air_quality', {}).get('o3', '')}, SO2: {current_info.get('air_quality', {}).get('so2', '')}\n"
        )

        await message.answer(text)
    else:
        await message.answer("Ob-havo ma'lumotlarini olishda xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")


























