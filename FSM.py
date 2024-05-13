from aiogram.dispatcher.filters.state import StatesGroup, State


class TakeQuestion(StatesGroup):
    question = State()

class AddSth(StatesGroup):
    add_section = State()
    add_subsection = State()
    add_task_id = State()
    add_theory_id = State()
    add_file_id = State()

class Mailing(StatesGroup):
    question = State()
