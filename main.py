import asyncio
from aiogram import Bot, Dispatcher
from aiogram.utils.i18n import I18n
from middlewares import CustomI18nMiddleware
from config import settings
import constants
from routers import user_router

i18n = I18n(path=constants.LOCALES_PATH)

async def main():
    bot = Bot(token=settings.BOT_TOKEN)
    dp = Dispatcher()

    dp.message.middleware(CustomI18nMiddleware(i18n))

    dp.include_router(user_router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())