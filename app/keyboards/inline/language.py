from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from loader import _, bot, dp


def get_markup():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=_("English"), callback_data="lang_en")],
            [InlineKeyboardButton(text=_("Spanish"), callback_data="lang_es")],
            [InlineKeyboardButton(text=_("French"), callback_data="lang_fr")],
            [InlineKeyboardButton(text=_("Italian"), callback_data="lang_it")],
            [InlineKeyboardButton(text=_("German"), callback_data="lang_de")],
            [InlineKeyboardButton(text=_("Polish"), callback_data="lang_pl")],
            [InlineKeyboardButton(text=_("Russian"), callback_data="lang_ru")],
            [InlineKeyboardButton(text=_("Ukraine"), callback_data="lang_uk")],
            [InlineKeyboardButton(text=_("Arabic"), callback_data="lang_ar")],
            [InlineKeyboardButton(text=_("Hindi"), callback_data="lang_hi")],
            [InlineKeyboardButton(text=_("Other"), callback_data="lang_en")],
            
        ]
    )
