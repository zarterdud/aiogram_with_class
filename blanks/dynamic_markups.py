from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from handler.database import DataBase



def tasks_section_keyboard(id_user):
    db = DataBase("handler/database.sqlite")
    tasks_section_kb = InlineKeyboardMarkup()
    sections = db.take_files_from_ls(id_user)
    last = ""
    for i in range(len(sections)):
        if last != sections[i][3]:
            tasks_section_kb.add(
                InlineKeyboardButton(
                    text=sections[i][3], callback_data=f"task_{sections[i][3]}"
                )
            )
            last = sections[i][3]
    tasks_section_kb.add(InlineKeyboardButton("Назад", callback_data="open_tasks"))
    return tasks_section_kb


def task_mechanics_keyboard(size):
    task_mechanics_kb = InlineKeyboardMarkup()
    for i in range(1, size + 1):
        task_mechanics_kb.add(
            InlineKeyboardButton(
                f"Задача {i} - Механика", callback_data=f"open_task_section_mechanics {i}"
            )
        )
    task_mechanics_kb.add(InlineKeyboardButton("Назад", callback_data="tasks_section"))
    return task_mechanics_kb


def task_MKT_and_Termo_keyboard(size):
    task_MKT_and_Termo_kb = InlineKeyboardMarkup()
    for i in range(1, size + 1):
        task_MKT_and_Termo_kb.add(
            InlineKeyboardButton(
                f"Задача {i} - МКТ и Термо",
                callback_data=f"open_task_section_MCT_and_thermodynamics {i}",
            )
        )
    task_MKT_and_Termo_kb.add(
        InlineKeyboardButton("Назад", callback_data="tasks_section")
    )
    return task_MKT_and_Termo_kb


def task_electrodynamics_keyboard(size):
    task_electrodynamics_kb = InlineKeyboardMarkup()
    for i in range(1, size + 1):
        task_electrodynamics_kb.add(
            InlineKeyboardButton(
                f"Задача {i} - Электродинамика",
                callback_data=f"open_task_section_electrodynamics {i}",
            )
        )
    task_electrodynamics_kb.add(
        InlineKeyboardButton("Назад", callback_data="tasks_section")
    )
    return task_electrodynamics_kb


def tasks_subsections_keyboard(id_user):
    mechanics_kb = InlineKeyboardMarkup()
    db = DataBase("handler/database.sqlite")
    subsections = db.take_files_from_ls(id_user)
    last = []
    for i in range(len(subsections)):
        if subsections[i][4] not in last:
            mechanics_kb.add(
                InlineKeyboardButton(
                    text=subsections[i][4], callback_data=f"tasks_{subsections[i][4]}"
                )
            )
            last.append(subsections[i][4])
    mechanics_kb.add(InlineKeyboardButton("Назад", callback_data="open_tasks"))
    return mechanics_kb


def tasks_kinematics_keyboard(size):
    task_kinematics_kb = InlineKeyboardMarkup()
    for i in range(1, size + 1):
        task_kinematics_kb.add(
            InlineKeyboardButton(
                f"Задача {i} - Кинематика", callback_data=f"open_task_kinematics {i}"
            )
        )
    task_kinematics_kb.add(InlineKeyboardButton("Назад", callback_data="tasks_section"))
    return task_kinematics_kb


def tasks_dynamics_keyboard(size):
    tasks_dynamics_kb = InlineKeyboardMarkup()
    for i in range(1, size + 1):
        tasks_dynamics_kb.add(
            InlineKeyboardButton(
                f"Задача {i} - Динамика", callback_data=f"open_task_dynamics {i}"
            )
        )
    tasks_dynamics_kb.add(InlineKeyboardButton("Назад", callback_data="tasks_section"))
    return tasks_dynamics_kb


def tasks_statics_keyboard(size):
    tasks_statics_kb = InlineKeyboardMarkup()
    for i in range(1, size + 1):
        tasks_statics_kb.add(
            InlineKeyboardButton(
                f"Задача {i} - Статика", callback_data=f"open_task_statics {i}"
            )
        )
    tasks_statics_kb.add(InlineKeyboardButton("Назад", callback_data="tasks_section"))
    return tasks_statics_kb


def tasks_hydrostatics_keyboard(size):
    tasks_hydrostatics_kb = InlineKeyboardMarkup()
    for i in range(1, size + 1):
        tasks_hydrostatics_kb.add(
            InlineKeyboardButton(
                f"Задача {i} - Гидростатика",
                callback_data=f"open_task_hydrostatics {i}",
            )
        )
    tasks_hydrostatics_kb.add(
        InlineKeyboardButton("Назад", callback_data="tasks_section")
    )
    return tasks_hydrostatics_kb


def tasks_oscillations_keyboard(size):
    tasks_oscillations_kb = InlineKeyboardMarkup()
    for i in range(1, size + 1):
        tasks_oscillations_kb.add(
            InlineKeyboardButton(
                f"Задача {i} - Колебания", callback_data=f"open_task_oscillations {i}"
            )
        )
    tasks_oscillations_kb.add(
        InlineKeyboardButton("Назад", callback_data="tasks_section")
    )
    return tasks_oscillations_kb


def tasks_MCT_keyboard(size):
    tasks_MCT_kb = InlineKeyboardMarkup()
    for i in range(1, size + 1):
        tasks_MCT_kb.add(
            InlineKeyboardButton(
                f"Задача {i} - МКТ", callback_data=f"open_task_MCT {i}"
            )
        )
    tasks_MCT_kb.add(InlineKeyboardButton("Назад", callback_data="tasks_section"))
    return tasks_MCT_kb


def tasks_thermodynamics_keyboard(size):
    tasks_thermodynamics_kb = InlineKeyboardMarkup()
    for i in range(1, size + 1):
        tasks_thermodynamics_kb.add(
            InlineKeyboardButton(
                f"Задача {i} - Термодинамика",
                callback_data=f"open_task_thermodynamics {i}",
            )
        )
    tasks_thermodynamics_kb.add(
        InlineKeyboardButton("Назад", callback_data="tasks_section")
    )
    return tasks_thermodynamics_kb


def tasks_humidity_keyboard(size):
    tasks_humidity_kb = InlineKeyboardMarkup()
    for i in range(1, size + 1):
        tasks_humidity_kb.add(
            InlineKeyboardButton(
                f"Задача {i} - Влажность", callback_data=f"open_task_humidity {i}"
            )
        )
    tasks_humidity_kb.add(InlineKeyboardButton("Назад", callback_data="tasks_section"))
    return tasks_humidity_kb


def tasks_electrodynamics_electrodynamics_keyboard(size):
    tasks_electrodynamics_electrodynamics_kb = InlineKeyboardMarkup()
    for i in range(1, size + 1):
        tasks_electrodynamics_electrodynamics_kb.add(
            InlineKeyboardButton(
                f"Задача {i} - Электродинамика",
                callback_data=f"open_task_electrodynamics_electrodynamics {i}",
            )
        )
    tasks_electrodynamics_electrodynamics_kb.add(
        InlineKeyboardButton("Назад", callback_data="tasks_section")
    )
    return tasks_electrodynamics_electrodynamics_kb


def tasks_electrostatics_keyboard(size):
    tasks_electrostatics_kb = InlineKeyboardMarkup()
    for i in range(1, size + 1):
        tasks_electrostatics_kb.add(
            InlineKeyboardButton(
                f"Задача {i} - Электростатика",
                callback_data=f"open_task_electrostatics {i}",
            )
        )
    tasks_electrostatics_kb.add(
        InlineKeyboardButton("Назад", callback_data="tasks_section")
    )
    return tasks_electrostatics_kb


def tasks_electrical_circuits_keyboard(size):
    tasks_electrical_circuits_kb = InlineKeyboardMarkup()
    for i in range(1, size + 1):
        tasks_electrical_circuits_kb.add(
            InlineKeyboardButton(
                f"Задача {i} -Электро цепи ",
                callback_data=f"open_task_electrical_circuits {i}",
            )
        )
    tasks_electrical_circuits_kb.add(
        InlineKeyboardButton("Назад", callback_data="tasks_section")
    )
    return tasks_electrical_circuits_kb


def tasks_magnetism_keyboard(size):
    tasks_electrical_circuits_kb = InlineKeyboardMarkup()
    for i in range(1, size + 1):
        tasks_electrical_circuits_kb.add(
            InlineKeyboardButton(
                f"Задача {i} - Магнетизм", callback_data=f"open_task_magnetism {i}"
            )
        )
    tasks_electrical_circuits_kb.add(
        InlineKeyboardButton("Назад", callback_data="tasks_section")
    )
    return tasks_electrical_circuits_kb


def tasks_thermal_processes_keyboard(size):
    tasks_thermal_processes_kb = InlineKeyboardMarkup()
    for i in range(1, size + 1):
        tasks_thermal_processes_kb.add(
            InlineKeyboardButton(
                f"Задача {i} - Тепловые процессы",
                callback_data=f"open_task_thermal_processes {i}",
            )
        )
    tasks_thermal_processes_kb.add(
        InlineKeyboardButton("Назад", callback_data="tasks_section")
    )
    return tasks_thermal_processes_kb



def take_tasks_sections(name, len):
    take_tasks_dict = {
        "Механика": task_mechanics_keyboard(len),
        "МКТ и Термодинамика": task_MKT_and_Termo_keyboard(len),
        "Электродинамика": task_electrodynamics_keyboard(len),
    }
    return take_tasks_dict[name]


def take_tasks_subsections(name, len):
    take_tasks_dict = {
        "Кинематика": tasks_kinematics_keyboard(len),
        "Динамика": tasks_dynamics_keyboard(len),
        "Статика": tasks_statics_keyboard(len),
        "Гидростатика": tasks_hydrostatics_keyboard(len),
        "Колебания": tasks_oscillations_keyboard(len),
        "МКТ": tasks_MCT_keyboard(len),
        "Термодинамика": tasks_thermodynamics_keyboard(len),
        "Влажность": tasks_humidity_keyboard(len),
        "Тепловые процессы": tasks_thermal_processes_keyboard(len),
        "Электродинамика": tasks_electrodynamics_electrodynamics_keyboard(len),
        "Электростатика": tasks_electrostatics_keyboard(len),
        "Электрические цепи": tasks_electrical_circuits_keyboard(len),
        "Магнетизм": tasks_magnetism_keyboard(len),
    }
    return take_tasks_dict[name]
