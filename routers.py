from aiogram import Router
from aiogram.filters import Command, CommandStart, StateFilter
import handlers

user_router = Router()

user_router.message.register(handlers.start, CommandStart())
