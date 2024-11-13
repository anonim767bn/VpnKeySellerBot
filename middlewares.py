from aiogram.utils.i18n.middleware import I18nMiddleware
from aiogram.fsm.context import FSMContext
from db import get_user_language
from constants import AVALIABLE_LANGUAGES

class CustomI18nMiddleware(I18nMiddleware):
    async def get_supported_language(self, language: str):
        if language in AVALIABLE_LANGUAGES:
            print(f'language {language} in avaliable' )
            return language
        print(f'sorry, we replace your languge to {self.i18n.default_locale}')
        return self.i18n.default_locale

    async def get_locale(self, event, data):
        state: FSMContext = data.get('state')
        state_data = await state.get_data()
        user_state_language = state_data.get('language')
        if user_state_language:
            print(f'data from state {user_state_language}')
            return await self.get_supported_language(
                user_state_language
            )

        user_language_from_db = await get_user_language(str(event.from_user.id))
        if user_language_from_db:
            print(f'user language from db - {user_language_from_db}')
            await state.update_data(language=user_language_from_db)
            return user_language_from_db

        user_device_language = await self.get_supported_language(
            event.from_user.language_code
        )
        print(f'user device language {event.from_user.language_code}')
        await state.update_data(language=user_device_language)
        return user_device_language