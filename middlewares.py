from aiogram.utils.i18n.middleware import I18nMiddleware
from aiogram.fsm.context import FSMContext
from db import get_user_language
from states import LanguageState
from constants import AVALIABLE_LANGUAGES

class CustomI18nMiddleware(I18nMiddleware):
    async def get_locale(self, event, data):
        state: FSMContext = data.get('state')
        if state:
            current_state = await state.get_state()
            if current_state == LanguageState.language.state:
                state_data = await state.get_data()
                user_language = state_data.get('language')
                if user_language:
                    return user_language
        user_language_from_db = await get_user_language(str(event.from_user.id))
        if user_language_from_db:
            await state.set_state(LanguageState.language.state)
            await state.update_data(language=user_language_from_db)
            return user_language_from_db

        if event.from_user.language_code in AVALIABLE_LANGUAGES:
            user_device_language = event.from_user.language_code
        else:
            user_device_language = self.i18n.default_locale
        await state.set_state(LanguageState.language.state)
        await state.update_data(language=user_device_language)
        return user_device_language