from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import constants

async def get_start_keyboard() -> InlineKeyboardMarkup:
    Keyboard = [
        [
            InlineKeyboardButton(text = str(constants.CONTINUE_INLINE_BUTTON_TEXT), callback_data=constants.CONTINUE_INLINE_BUTTON_CALL)
        ]
    ]
    return InlineKeyboardMarkup(
        inline_keyboard = Keyboard
    )


async def get_agreement_keyboard() -> InlineKeyboardMarkup:
    Keyboard = [
        [
            InlineKeyboardButton(text = str(constants.TERMS_INLINE_BUTTON_TEXT), url = constants.TERMS_INLINE_BUTTON_URL),
            InlineKeyboardButton(text = str(constants.AGREE_INLINE_BUTTON_TEXT), callback_data = constants.AGREE_INLINE_BUTTON_CALLBACK),
            InlineKeyboardButton(text = str(constants.DISAGREE_INLINE_BUTTON_TEXT), callback_data = constants.DISAGREE_INLINE_BUTTON_CALLBACK)
        ]
    ]
    return InlineKeyboardMarkup(
        inline_keyboard = Keyboard
    )
