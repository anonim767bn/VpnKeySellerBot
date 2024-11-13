from aiogram.utils.i18n import gettext as _

async def get_start_message(user: str):
    return _(
        "👋 <b>Hello, {user}!</b>\n\n"
        "Here you can buy a <b>VPN</b> subscription 🛡️\n"
        "Tap the button below this message to continue ⬇️"
    ).format(user=user)