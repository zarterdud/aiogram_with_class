from aiogram.types import Message
from blanks.admin_markups import admin_panel_keyboard
from config import admins


async def admin_start_panel(message: Message):
        if message.from_user.id in admins:
            await message.answer(text="Панель задач", reply_markup=admin_panel_keyboard())
