from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import texts
import keyboards


async def start(message: Message, state: FSMContext):
    await message.answer(
        await texts.get_start_message(
            user = message.from_user.full_name
        ),
        reply_markup = await keyboards.get_start_keyboard()
    )