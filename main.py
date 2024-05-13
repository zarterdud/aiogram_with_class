from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from FSM import Mailing, TakeQuestion, AddSth
from handler.database import DataBase
from aiogram import types
from handler.callback_handler import callback_handler
from blanks.admin_markups import admin_panel_keyboard
from blanks.static_markups import (
    start_keyboard,
    question_keyboard,
)
from aiogram.dispatcher.filters import IsReplyFilter
from admins_functions.admin_start import admin_start_panel
import random


class MyBot:
    def __init__(self, bot: Bot, dp: Dispatcher, db: DataBase):
        self.bot = bot
        self.dp = dp
        self.db = db

    async def start(self, message: Message):
        tg_id = self.db.users_id()
        id_user = message.from_user.id
        if id_user not in tg_id:
            user_full_name = message.from_user.full_name
            username = message.from_user.username
            self.db.user_in_db(
                id_user,
                user_full_name,
                username,
            )
            section = random.choice(
                ["Механика", "Электродинамика", "МКТ и Термодинамика"]
            )
            add = self.db.take_from_section(id_user, section)
            for doc in add:
                self.db.add_in_ls(
                    message.from_user.id,
                    doc[0],
                    doc[1],
                    doc[2],
                    section,
                    doc[3],
                )
            await message.answer(
                "Приветствуем в нашем боте! Вам выданы бесплатные курсы. Перейдите в личный кабинет чтобы их активировать!",
                reply_markup=start_keyboard(),
            )
            self.db.give_count_messages(id_user)
        else:
            await message.answer(
                "Приветствуем в нашем боте!",
                reply_markup=start_keyboard(),
            )

    async def question(self, message: Message, state: FSMContext):
        tg_username_asked = message.from_user.username
        user_message = await self.bot.send_message(
            chat_id=1283802964,
            text=f"Вам вопрос от @{tg_username_asked}: \n" + message.text,
        )
        user_message
        tg_id_user = message.from_user.id
        tg_question_id = user_message.message_id
        tg_question = message.text
        await message.reply("Вопрос отправлен!", reply_markup=question_keyboard())
        self.db.add_user(tg_id_user, tg_question_id, tg_question)
        self.db.take_away_count_messages(tg_id_user)
        await state.finish()

    async def is_ivan(self, message: Message):
        message_id = message.reply_to_message.message_id
        chat_id, question = self.db.take_tg_id_and_question(message_id)
        await self.bot.send_message(
            chat_id=chat_id,
            text=f'Ответ на вопрос: "{question}" \n' + message.text,
        )

    async def add_task(self, message: Message, state: FSMContext):
        async with state.proxy() as data:
            document_id = message.document.file_id
            data["add_task_id"] = document_id
        await message.answer(text="Пришлите файл чтоб добавить теорию")
        await AddSth.next()

    async def add_theory(self, message: Message, state: FSMContext):
        async with state.proxy() as data:
            document_id = message.document.file_id
            data["add_theory_id"] = document_id
        await message.answer(text="Пришлите файл для его сохранения")
        await AddSth.next()

    async def add_file(self, message: Message, state: FSMContext):
        async with state.proxy() as data:
            document_id = message.document.file_id
            data["add_file_id"] = document_id
        await message.answer(text="Все сохранено!")
        await message.answer(text="Панель задач", reply_markup=admin_panel_keyboard())
        section = data["add_section"]
        subsection = data["add_subsection"]
        task_id = data["add_task_id"]
        theory_id = data["add_theory_id"]
        file_id = data["add_file_id"]
        self.db.add_full_task(
            section,
            subsection,
            task_id,
            theory_id,
            file_id,
        )
        await state.finish()

    async def take_mailing(self, message: Message, state: FSMContext):
        tg_ids = self.db.take_id_users()
        for tg_id in tg_ids:
            tg_id = tg_id[0]
            from_chat_id = message.from_user.id
            message_id = message.message_id
            await self.bot.copy_message(
                from_chat_id=from_chat_id,
                chat_id=tg_id,
                message_id=message_id,
            )
        await message.answer(text="Сообщения отправлены!")
        await message.answer(text="Панель задач", reply_markup=admin_panel_keyboard())
        await state.finish()

    def register_handlers(self):
        self.dp.register_message_handler(callback=self.start, commands=["start"])
        self.dp.register_message_handler(callback=admin_start_panel, commands=["admin"])
        self.dp.register_message_handler(
            self.is_ivan,
            IsReplyFilter(is_reply=True),
            state="*",
        )
        self.dp.register_message_handler(
            callback=self.question, state=TakeQuestion.question
        )
        self.dp.register_message_handler(
            callback=self.add_task,
            state=AddSth.add_task_id,
            content_types=types.ContentType.DOCUMENT,
        )
        self.dp.register_message_handler(
            callback=self.add_theory,
            state=AddSth.add_theory_id,
            content_types=types.ContentType.DOCUMENT,
        )
        self.dp.register_message_handler(
            callback=self.add_file,
            state=AddSth.add_file_id,
            content_types=types.ContentType.DOCUMENT,
        )
        self.dp.register_message_handler(
            callback=self.take_mailing, state=Mailing.question, content_types=["any"]
        )
        self.dp.register_callback_query_handler(callback=callback_handler, state="*")

    def run(self):
        self.register_handlers()
        executor.start_polling(dispatcher=self.dp, skip_updates=True)
