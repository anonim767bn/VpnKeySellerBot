from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import constants

async def get_start_keyboard() -> ReplyKeyboardMarkup:
    Keyboard = [
        [
            InlineKeyboardButton(text = str(constants.CONTINUE_INLINE_BUTTON_TEXT), callback_data=constants.CONTINUE_INLINE_BUTTON_CALL)
        ]
    ]
    return InlineKeyboardMarkup(
        inline_keyboard = Keyboard
    )