import asyncio
import re

from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import ChatActions
from aiogram.dispatcher import FSMContext

from keyboards.inline.choise_buttons import menu_, similar_movie_keyboard
from loader import _, bot, dp
from message_output.message_output import MessageText
from tmdb_v3_api import get_api_for_context
from database.db import DBCommands


db = DBCommands()
async def get_lang(user_id):
    user = await db.get_user(user_id)
    if user:
        return user.language


# ================ SIMILAR ============================================================================================


@dp.callback_query_handler(Text(startswith="similar"))
async def movie_like_this(callback: types.CallbackQuery,state: FSMContext):
    """

    :param callback:
    :return: similar movies by move_id
    """
    try:
        message = callback.message.text

        movie_id = (re.findall(r"#️⃣ ID: .(\d+)", message))[-1]

        tmdb_with_language = await get_api_for_context(callback.message.chat.id)

        user_language = await get_lang(callback.from_user.id)

        # Use the fetched language or provide a default if it's None
        if user_language:
            language = user_language
        else:
            language = "EN"  

        movie_list = tmdb_with_language.movie.recommendations(movie_id)
        first = int(callback["data"].replace("similar_", ""))

        message = MessageText(movie_list[first])

        if message.movie_image is None:
            poster = "https://image.tmdb.org/t/p/original"
        else:
            poster = "https://image.tmdb.org/t/p/original" + message.movie_image

        # For "typing" message in top console
        await bot.send_chat_action(callback.message.chat.id, ChatActions.TYPING)
        await asyncio.sleep(1)

        await callback.message.edit_text(
            _("{message} {poster}").format(message=message.message, poster=poster)
        )
        await callback.message.edit_reply_markup(
            reply_markup=similar_movie_keyboard(
                first, len(movie_list), message.original_title, message.movie_id,language
            )
        )
    except IndexError:
        await callback.message.reply(_("Sorry. No Results"), reply_markup=menu_())


# =====================================================================================================================
