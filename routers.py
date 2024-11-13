from aiogram import Router, F
from aiogram.filters import Command, CommandStart, StateFilter
import handlers
import constants

user_router = Router()

user_router.message.register(handlers.start, CommandStart())
user_router.callback_query.register(handlers.agreement_message, F.data == constants.CONTINUE_INLINE_BUTTON_CALL)
