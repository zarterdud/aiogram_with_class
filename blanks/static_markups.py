from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from handler.database import DataBase
db = DataBase("handler/database.sqlite")


def start_keyboard():
    start_kb = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton("Меню", callback_data="menu")]]
    )
    return start_kb


def menu_keyboard():
    menu_kb = InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [InlineKeyboardButton("Рулетка задач", callback_data="task_roulette")],
            [InlineKeyboardButton("Личный аккаунт", callback_data="personal_account")],
            [
                InlineKeyboardButton(
                    "Репетиторство", url="https://webk.telegram.org/#@Tredikt"
                )
            ],
            [
                InlineKeyboardButton(
                    "Полноценные видеокурсы", callback_data="video_courses"
                )
            ],
        ],
    )
    return menu_kb


def select_subsection():
    select_subsection_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    "Выбрать раздел", callback_data="select_section_call"
                )
            ],
            [
                InlineKeyboardButton(
                    "Выбрать подраздел", callback_data="select_subsection_call"
                )
            ],
            [
                InlineKeyboardButton(
                    "Бесплатный курс по 18-20 задачам", callback_data="course"
                )
            ],
            [InlineKeyboardButton("Назад", callback_data="menu")],
        ]
    )
    return select_subsection_kb


def select_section_keyboard():
    task_roulette_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("Механика", callback_data="sub_mechanics")],
            [
                InlineKeyboardButton(
                    "МКТ и Термодинамика", callback_data="sub_MCT_and_thermodynamics"
                )
            ],
            [
                InlineKeyboardButton(
                    "Электродинамика", callback_data="sub_electrodynamics"
                )
            ],
            [InlineKeyboardButton("Оптика", callback_data="sub_optics")],
            [
                InlineKeyboardButton(
                    "Квантовая механика", callback_data="sub_quantum_mechanics"
                )
            ],
            [InlineKeyboardButton("Назад", callback_data="task_roulette")],
        ]
    )
    return task_roulette_kb


def task_roulette_keyboard():
    task_roulette_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("Механика", callback_data="mechanics")],
            [
                InlineKeyboardButton(
                    "МКТ и Термодинамика", callback_data="MCT_and_thermodynamics"
                )
            ],
            [InlineKeyboardButton("Электродинамика", callback_data="electrodynamics")],
            [InlineKeyboardButton("Оптика", callback_data="optics")],
            [
                InlineKeyboardButton(
                    "Квантовая механика", callback_data="quantummechanics"
                )
            ],
            [InlineKeyboardButton("Назад", callback_data="task_roulette")],
        ]
    )
    return task_roulette_kb


def mechanics_keyboard():
    mechanics_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("Кинематика", callback_data="kinematics")],
            [InlineKeyboardButton("Динамика", callback_data="dynamics")],
            [InlineKeyboardButton("Статика", callback_data="statics")],
            [InlineKeyboardButton("Гидростатика", callback_data="hydrostatics")],
            [InlineKeyboardButton("Колебания", callback_data="oscillations")],
            [InlineKeyboardButton("Назад", callback_data="select_subsection_call")],
        ]
    )
    return mechanics_kb


def MCT_and_thermodynamics_keyboard():
    MCT_and_thermodynamics_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("МКТ", callback_data="MCT")],
            [InlineKeyboardButton("Термодинамика", callback_data="thermodynamics")],
            [InlineKeyboardButton("Влажность", callback_data="humidity")],
            [
                InlineKeyboardButton(
                    "Тепловые процессы", callback_data="thermal_processes"
                )
            ],
            [InlineKeyboardButton("Назад", callback_data="select_subsection_call")],
        ]
    )
    return MCT_and_thermodynamics_kb


def electrodynamics_keyboard():
    electrodynamics_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    "Электродинамика", callback_data="electrodynamics_electrodynamics"
                )
            ],
            [InlineKeyboardButton("Электростатика", callback_data="electrostatics")],
            [
                InlineKeyboardButton(
                    "Электрические цепи", callback_data="electrical_circuits"
                )
            ],
            [InlineKeyboardButton("Магнетизм", callback_data="magnetism")],
            [InlineKeyboardButton("Назад", callback_data="select_subsection_call")],
        ]
    )
    return electrodynamics_kb


def optics_keyboard():
    optics_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("Назад", callback_data="select_subsection_call")]
        ]
    )
    return optics_kb


def quantum_mechanics():
    quantum_mechanics_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("Назад", callback_data="select_subsection_call")]
        ]
    )
    return quantum_mechanics_kb


def personal_account_keyboard(tg_id):
    count = db.know_count_messages(tg_id)
    personal_account_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(f"Задать вопрос ({count})", callback_data="ask_a_question")],
            [InlineKeyboardButton("Открыть задачи", callback_data="open_tasks")],
            [InlineKeyboardButton("Назад", callback_data="menu")],
        ]
    )
    return personal_account_kb


def tasks_keyboard():
    tasks_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("Разделы", callback_data="tasks_section")],
            [InlineKeyboardButton("Подразделы", callback_data="tasks_subsection")],
            [InlineKeyboardButton("Назад", callback_data="personal_account")],
        ]
    )
    return tasks_kb


def task_suboptics_keyboard():
    tasks_electrical_circuits_kb = InlineKeyboardMarkup()
    tasks_electrical_circuits_kb.add(
        InlineKeyboardButton("Назад", callback_data="tasks_section")
    )
    return tasks_electrical_circuits_kb


def task_quantum_mechanics_keyboard():
    tasks_electrical_circuits_kb = InlineKeyboardMarkup()
    tasks_electrical_circuits_kb.add(
        InlineKeyboardButton("Назад", callback_data="tasks_section")
    )
    return tasks_electrical_circuits_kb


def free_roulettes():
    rullets = 0
    if rullets > 0:
        free_roulettes_kb = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton("Использовать", callback_data="None")],
                [InlineKeyboardButton("Назад", callback_data="personal_account")],
            ]
        )
        return free_roulettes_kb
    else:
        free_roulettes_kb = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton("Ввести промокод", callback_data="None")],
                [InlineKeyboardButton("Назад", callback_data="personal_account")],
            ]
        )
        return free_roulettes_kb


def video_courses_keyboard():
    video_courses_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("Вконтакте", url="https://vk.com")],
            [InlineKeyboardButton("Степик", url="https://stepik.org")],
            [InlineKeyboardButton("Назад", callback_data="menu")],
        ]
    )
    return video_courses_kb


def question_keyboard():
    question_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("Назад", callback_data="personal_account")]
        ]
    )
    return question_kb


def delete_messages(call):
    delete = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Назад", callback_data=call)
    )
    return delete


fast_access_delete_messages_dict = {
    "kinematics": delete_messages("back_delete_kinematics"),
    "dynamics": delete_messages("back_delete_dynamics"),
    "statics": delete_messages("back_delete_statics"),
    "hydrostatics": delete_messages("back_delete_hydrostatics"),
    "oscillations": delete_messages("back_delete_oscillations"),
    "MCT": delete_messages("back_delete_MCT"),
    "thermodynamics": delete_messages("back_delete_thermodynamics"),
    "humidity": delete_messages("back_delete_humidity"),
    "thermal_processes": delete_messages("back_delete_thermal_processes"),
    "electrodynamics_electrodynamics": delete_messages("back_delete_electrodynamics_electrodynamics"),
    "electrostatics": delete_messages("back_delete_electrostatics"),
    "electrical_circuits": delete_messages("back_delete_electrical_circuits"),
    "magnetism": delete_messages("back_delete_magnetism"),
}

fast_access_dict_keyboard = {
    "mechanics": mechanics_keyboard(),
    "MCT_and_thermodynamics": MCT_and_thermodynamics_keyboard(),
    "electrodynamics": electrodynamics_keyboard(),
    "optics": optics_keyboard(),
    "quantum_mechanics": quantum_mechanics(),
}


take_section_name_dict = {
    "mechanics": "Механика",
    "MCT_and_thermodynamics": "МКТ и Термодинамика",
    "electrodynamics": "Электродинамика",
    "optics": "Оптика",
    "quantum_mechanics": "Квантовая механика",
}


take_section_name_dict_reverse = {
    "Механика": "mechanics",
    "МКТ и Термодинамика": "MCT_and_thermodynamics",
    "Электродинамика": "electrodynamics",
    "Оптика": "optics",
    "Квантовая механика": "quantum_mechanics",
}


take_section_dict = {
    "kinematics": "Механика",
    "dynamics": "Механика",
    "statics": "Механика",
    "hydrostatics": "Механика",
    "oscillations": "Механика",
    "MCT": "МКТ и Термодинамика",
    "thermodynamics": "МКТ и Термодинамика",
    "humidity": "МКТ и Термодинамика",
    "thermalprocesses": "МКТ и Термодинамика",
    "electrodynamicselectrodynamics": "Электродинамика",
    "electrostatics": "Электродинамика",
    "electricalcircuits": "Электродинамика",
    "magnetism": "Электродинамика",
}


take_subsection_dict = {
    "kinematics": "Кинематика",
    "dynamics": "Динамика",
    "statics": "Статика",
    "hydrostatics": "Гидростатика",
    "oscillations": "Колебания",
    "MCT": "МКТ",
    "thermodynamics": "Термодинамика",
    "humidity": "Влажность",
    "thermalprocesses": "Тепловые процессы",
    "electrodynamicselectrodynamics": "Электродинамика",
    "electrostatics": "Электростатика",
    "electricalcircuits": "Электрические цепи",
    "magnetism": "Магнетизм",
}
