from aiogram.types import ReplyKeyboardMarkup,KeyboardButton



obhavo=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Location",request_location=True),
        ],
    ],
    resize_keyboard=True
)