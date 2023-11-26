from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup


menu=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="     ",callback_data="no"),
            InlineKeyboardButton(text="  C  ",callback_data="C"),
            InlineKeyboardButton(text=" <=  ",callback_data="<="),
            InlineKeyboardButton(text="  /  ",callback_data="/"),
        ],
        [
            InlineKeyboardButton(text="7  ",callback_data="7"),
            InlineKeyboardButton(text="8  ",callback_data="8"),
            InlineKeyboardButton(text="9  ",callback_data="9"),
            InlineKeyboardButton(text="*  ",callback_data="*"),
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6"),
            InlineKeyboardButton(text="-", callback_data="-"),
        ],
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3"),
            InlineKeyboardButton(text="+", callback_data="+"),
        ],
        [
            InlineKeyboardButton(text=" ", callback_data="no"),
            InlineKeyboardButton(text="0", callback_data="0"),
            InlineKeyboardButton(text=",", callback_data="."),
            InlineKeyboardButton(text="=", callback_data="="),
        ],

    ],
)