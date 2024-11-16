from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
import texts
import keyboards
from db import is_user_exist, register_user


async def start(message: Message, state: FSMContext):
    await state.clear()
    if not await is_user_exist(message.from_user.id):
        await message.answer(
            await texts.get_start_message(
                user = message.from_user.full_name
            ),
            reply_markup = await keyboards.get_start_keyboard()
        )
    else:
        # TODO
        pass



async def agreement_message(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text(
        await texts.get_agreement_message(),
        reply_markup = await keyboards.get_agreement_keyboard()
    )


async def agree_with_terms(call: CallbackQuery, state: FSMContext):
    await register_user(call.from_user.id, call.from_user.language_code or 'en')
    await call.message.edit_text(
        await texts.get_agree_with_terms_message(),
        reply_markup = await keyboards.get_agree_with_terms_keyboard()
    )


async def disagree_with_terms(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text(
        await texts.get_disagree_with_terms_message(),
        reply_markup = await keyboards.get_disagree_with_terms_keyboard()
    )

async def start_again(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text(
        await texts.get_start_again_message(
            user = call.from_user.full_name
        ),
        reply_markup = await keyboards.get_start_keyboard()
    )


async def personal_account(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text(
        await texts.get_personal_account_message(),
        reply_markup = await keyboards.get_personal_account_keyboard()
    )