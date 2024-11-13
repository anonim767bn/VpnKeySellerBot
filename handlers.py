from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.utils.i18n import gettext as _

async def start(message: Message, state: FSMContext):
    await message.answer(
        _("hello, {name}!").format(name=message.from_user.full_name)
    )