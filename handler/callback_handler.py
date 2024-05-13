from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.dispatcher import FSMContext
from FSM import TakeQuestion, Mailing, AddSth
from config import get_bot_and_db
from blanks.dynamic_markups import (
    tasks_MCT_keyboard,
    tasks_dynamics_keyboard,
    tasks_electrical_circuits_keyboard,
    tasks_electrodynamics_electrodynamics_keyboard,
    tasks_electrostatics_keyboard,
    tasks_humidity_keyboard,
    tasks_hydrostatics_keyboard,
    tasks_magnetism_keyboard,
    tasks_oscillations_keyboard,
    tasks_section_keyboard,
    tasks_statics_keyboard,
    tasks_subsections_keyboard,
    tasks_thermal_processes_keyboard,
    tasks_thermodynamics_keyboard,
    take_tasks_sections,
    take_tasks_subsections,
)
from blanks.static_markups import (
    delete_messages,
    menu_keyboard,
    select_section_keyboard,
    select_subsection,
    task_quantum_mechanics_keyboard,
    task_roulette_keyboard,
    personal_account_keyboard,
    task_suboptics_keyboard,
    tasks_keyboard,
    video_courses_keyboard,
    free_roulettes,
    take_section_name_dict,
    take_section_dict,
    take_subsection_dict,
    take_section_name_dict_reverse,
    fast_access_dict_keyboard,
    fast_access_delete_messages_dict,
)
from blanks.admin_markups import (
    admin_panel_keyboard,
    admin_keyboard2,
    fast_access_dict_admin_keyboard,
    take_section_dict_admin,
    take_subsection_dict_admin,
)


async def callback_handler(call: CallbackQuery, state: FSMContext):
    bot, db = get_bot_and_db()
    callback = call.data
    tg_id = call.from_user.id
    if callback == "menu":
        await call.message.edit_text(text="Меню", reply_markup=menu_keyboard())

    elif callback == "add_materies":
        await call.message.edit_text(
            text="Выберите раздел", reply_markup=admin_keyboard2()
        )
    elif callback == "admin_keyboard":
        await state.finish()
        await call.message.edit_text(
            text="Панель задач", reply_markup=admin_panel_keyboard()
        )
    elif callback.endswith("admin"):
        callback_sec = callback.split("_")[0]
        if callback_sec in [
            "mechanics",
            "MCTandthermodynamics",
            "electrodynamics",
            "optics",
            "quantummechanics",
        ]:
            await call.message.edit_text(
                text="Выберите подраздел",
                reply_markup=fast_access_dict_admin_keyboard[callback_sec],
            )
        elif callback_sec in take_subsection_dict_admin.keys():
            section = take_section_dict_admin[callback_sec]
            subsection = take_subsection_dict_admin[callback_sec]
            await AddSth.add_task_id.set()
            async with state.proxy() as data:
                data["add_section"] = section
                data["add_subsection"] = subsection
            await call.message.edit_text(
                text="Пришлите файл чтоб добавить задачу",
            )
    elif callback == "Mailing_to_users":
        await Mailing.question.set()
        await call.message.answer(
            text="Напишите текст рассылки",
            reply_markup=InlineKeyboardMarkup().add(
                InlineKeyboardButton("Назад", callback_data="admin_keyboard")
            ),
        )

    elif callback == "task_roulette":
        await call.message.edit_text(
            text="Рулетка задач", reply_markup=select_subsection()
        )
    elif callback == "select_section_call":
        await call.message.edit_text(
            text="Выберите раздел для получения 5 задач",
            reply_markup=select_section_keyboard(),
        )
    elif callback.startswith("sub"):
        section = take_section_name_dict[callback[4:]]
        documents = db.take_from_section(tg_id, section)
        if documents == []:
            await call.message.edit_text(
                "Вы получили все задачи!",
                reply_markup=InlineKeyboardMarkup().add(
                    InlineKeyboardButton("Назад", callback_data="select_section_call")
                ),
            )
        else:
            for doc in documents:
                db.add_in_ls(
                    call.from_user.id, doc[0], doc[1], doc[2], "Механика", doc[3]
                )
            await call.message.edit_text(
                text="Задачи добавлены в Личный кабинет!",
                reply_markup=InlineKeyboardMarkup().add(
                    InlineKeyboardButton("Назад", callback_data="select_section_call")
                ),
            )
    elif callback == "select_subsection_call":
        await call.message.edit_text(
            text="Выбрать раздел", reply_markup=task_roulette_keyboard()
        )
    elif callback == "personal_account":
        await call.message.edit_text(
            text="Личный кабинет", reply_markup=personal_account_keyboard(tg_id)
        )
    elif callback == "video_courses":
        await call.message.edit_text(
            text="Видеокрусы", reply_markup=video_courses_keyboard()
        )
    elif callback in take_section_name_dict.keys():
        text = take_section_name_dict[callback]
        reply_markup = fast_access_dict_keyboard[callback]
        await call.message.edit_text(text=text, reply_markup=reply_markup)
    elif callback == "tasks":
        await call.message.edit_text(
            text="Рулетка задач", reply_markup=select_subsection()
        )
    elif callback == "free_roulettes_call":
        await call.message.edit_text(
            text="Бесплатные рулетки", reply_markup=free_roulettes()
        )
    elif callback == "ask_a_question":
        await TakeQuestion.question.set()
        await call.message.edit_text(
            text="Напишите вопрос", reply_markup=InlineKeyboardMarkup()
        )

    elif callback in take_subsection_dict.keys():
        subsection = take_subsection_dict[callback]
        callback_data = take_section_name_dict_reverse[take_section_dict[callback]]
        documents = db.take_from_subsection(tg_id, subsection)
        if documents == []:
            await call.message.edit_text(
                "Вы получили все задачи!",
                reply_markup=InlineKeyboardMarkup().add(
                    InlineKeyboardButton("Назад", callback_data=callback_data)
                ),
            )
        else:
            section = take_section_dict[callback]
            for doc in documents:
                db.add_in_ls(
                    call.from_user.id,
                    doc[0],
                    doc[1],
                    doc[2],
                    section,
                    subsection,
                )
            await call.message.edit_text(
                text="Задачи добавлены в Личный кабинет!",
                reply_markup=InlineKeyboardMarkup().add(
                    InlineKeyboardButton("Назад", callback_data=callback_data)
                ),
            )

    elif callback == "open_tasks":
        await call.message.edit_text(
            text="Выберите задачу", reply_markup=tasks_keyboard()
        )

    elif callback == "tasks_section":
        await call.message.edit_text(
            text="Выберите задачу",
            reply_markup=tasks_section_keyboard(call.from_user.id),
        )
    elif callback == "task_optics":
        await call.message.answer(text="В разработке")

    elif callback == "task_quantum_mechanics":
        await call.message.answer(text="В разработке")

    elif callback == "task_suboptics":
        await call.message.edit_text(
            text="В разработке",
            reply_markup=task_suboptics_keyboard(),
        )

    elif callback == "task_quantum_submechanics":
        await call.message.edit_text(
            text="В разработке",
            reply_markup=task_quantum_mechanics_keyboard(),
        )

    elif callback.startswith("task_"):
        chat_id = call.message.chat.id
        message_id = call.message.message_id
        user_id = call.from_user.id
        section = callback[5:]
        await bot.delete_message(chat_id, message_id)
        tasks = db.take_files_from_ls(user_id, section=section)
        if len(tasks) == 0:
            await call.message.answer(text="Нет задач в этой теме")
        else:
            reply_markup = take_tasks_sections(section, len(tasks))
            await call.message.answer(text="Выберите задачу", reply_markup=reply_markup)

    elif callback.startswith("open_task_section_"):
        chat_id = call.message.chat.id
        message_id = call.message.message_id
        section = take_section_name_dict[callback[18:-2]]
        user_id = call.from_user.id
        await bot.delete_message(chat_id, message_id)
        tasks = db.take_files_from_ls(user_id, section=section)
        num = int(callback.split(" ")[-1])
        await call.message.answer(text=f"Задача номер {num}")
        task_name = {0: "Задача", 1: "Теория", 2: "Файл"}
        for i in range(3):
            await call.message.answer(text=task_name[i])
            await bot.send_document(chat_id=chat_id, document=tasks[num - 1][i])
        await call.message.answer(
            text="Назад", reply_markup=delete_messages("back_delete_mechanics")
        )

    elif callback == "tasks_subsection":
        await call.message.edit_text(
            text="Выберите подраздел",
            reply_markup=tasks_subsections_keyboard(call.from_user.id),
        )

    elif callback.startswith("tasks_"):
        chat_id = call.message.chat.id
        message_id = call.message.message_id
        user_id = call.from_user.id
        subsection = callback[6:]
        await bot.delete_message(chat_id, message_id)
        tasks = db.take_files_from_ls(user_id, subsection=subsection)
        if len(tasks) == 0:
            await call.message.answer(text="Нет задач в этой теме")
        else:
            reply_markup = take_tasks_subsections(subsection, len(tasks))
            await call.message.answer(
                text="Выберите задачу",
                reply_markup=reply_markup,
            )
    elif callback.startswith("open_task_"):
        chat_id = call.message.chat.id
        message_id = call.message.message_id
        user_id = call.from_user.id
        section = take_subsection_dict[callback[10:-2]]
        await bot.delete_message(chat_id, message_id)
        tasks = db.take_files_from_ls(user_id, subsection=section)
        num = int(callback.split(" ")[-1])
        await call.message.answer(text=f"Задача номер {num}")
        task_name = {0: "Задача", 1: "Теория", 2: "Файл"}
        for i in range(3):
            await call.message.answer(text=task_name[i])
            await bot.send_document(chat_id=chat_id, document=tasks[num - 1][i])
        reply_markup = fast_access_delete_messages_dict[callback[10:-2]]
        await call.message.answer(text="Назад", reply_markup=reply_markup)

    elif "back_delete" in callback:
        chat_id = call.message.chat.id
        for i in range(8):
            await bot.delete_message(chat_id, call.message.message_id - i)
        await call.message.answer(
            text="Личный кабинет",
            reply_markup=personal_account_keyboard(tg_id),
        )
