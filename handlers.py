from aiogram.types import Message, CallbackQuery
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


async def agreement_message(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text(
        await texts.get_agreement_message(),
        reply_markup = await keyboards.get_agreement_keyboard()
    )