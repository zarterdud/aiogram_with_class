from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def admin_panel_keyboard():
    admin_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("Добавить материалы", callback_data="add_materies")],
            [
                InlineKeyboardButton(
                    "Рассылка пользователям", callback_data="Mailing_to_users"
                )
            ],
            [InlineKeyboardButton("выйти", callback_data="menu")],
        ]
    )
    return admin_kb


def admin_keyboard2():
    admin_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("Механика", callback_data="mechanics_admin")],
            [
                InlineKeyboardButton(
                    "МКТ и Термодинамика", callback_data="MCTandthermodynamics_admin"
                )
            ],
            [
                InlineKeyboardButton(
                    "Электродинамика", callback_data="electrodynamics_admin"
                )
            ],
            [InlineKeyboardButton("Оптика", callback_data="optics_admin")],
            [
                InlineKeyboardButton(
                    "Квантовая механика", callback_data="quantummechanics_admin"
                )
            ],
            [InlineKeyboardButton("Назад", callback_data="admin_keyboard")],
        ]
    )
    return admin_kb


def mechanics_keyboard_admin():
    mechanics_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("Кинематика", callback_data="kinematics_admin")],
            [InlineKeyboardButton("Динамика", callback_data="dynamics_admin")],
            [InlineKeyboardButton("Статика", callback_data="statics_admin")],
            [InlineKeyboardButton("Гидростатика", callback_data="hydrostatics_admin")],
            [InlineKeyboardButton("Колебания", callback_data="oscillations_admin")],
            [InlineKeyboardButton("Назад", callback_data="add_materies")],
        ]
    )
    return mechanics_kb


def MCTandthermodynamics_keyboard_admin():
    MCT_and_thermodynamics_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("МКТ", callback_data="MCT_admin")],
            [
                InlineKeyboardButton(
                    "Термодинамика", callback_data="thermodynamics_admin"
                )
            ],
            [InlineKeyboardButton("Влажность", callback_data="humidity_admin")],
            [
                InlineKeyboardButton(
                    "Тепловые процессы", callback_data="thermalprocesses_admin"
                )
            ],
            [InlineKeyboardButton("Назад", callback_data="add_materies")],
        ]
    )
    return MCT_and_thermodynamics_kb


def electrodynamics_keyboard_admin():
    electrodynamics_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    "Электродинамика",
                    callback_data="electrodynamicselectrodynamics_admin",
                )
            ],
            [
                InlineKeyboardButton(
                    "Электростатика", callback_data="electrostatics_admin"
                )
            ],
            [
                InlineKeyboardButton(
                    "Электрические цепи", callback_data="electricalcircuits_admin"
                )
            ],
            [InlineKeyboardButton("Магнетизм", callback_data="magnetism_admin")],
            [InlineKeyboardButton("Назад", callback_data="add_materies")],
        ]
    )
    return electrodynamics_kb


def optics_keyboard_admin():
    optics_kb = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton("Назад", callback_data="add_materies")]]
    )
    return optics_kb


def quantum_mechanics_admin():
    quantum_mechanics_kb = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton("Назад", callback_data="add_materies")]]
    )
    return quantum_mechanics_kb


fast_access_dict_admin_keyboard = {
    "mechanics": mechanics_keyboard_admin(),
    "MCTandthermodynamics": MCTandthermodynamics_keyboard_admin(),
    "electrodynamics": electrodynamics_keyboard_admin(),
    "optics": optics_keyboard_admin(),
    "quantummechanics": quantum_mechanics_admin(),
}


take_section_dict_admin = {
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


take_subsection_dict_admin = {
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
