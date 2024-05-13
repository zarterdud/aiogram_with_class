from aiogram import Bot
from handler.database import DataBase

TOKEN = "6714704690:AAGusdRE_2A8n77Lr8h-UBl6t6_KQcEZFKc"
db_name = "database.sqlite"
admins = [1077886176, 1283802964]
mechanics_admin = [
    "kinematics_admin",
    "dynamics_admin",
    "statics_admin",
    "hydrostatics_admin",
    "oscillations_admin",
]
MCT_and_thermodynamics_admin = [
    "MCT_admin",
    "thermodynamics_admin",
    "humidity_admin",
    "thermal_processes_admin",
]
electrodynamics_admin = [
    "electrodynamics_electrodynamics_admin",
    "electrostatics_admin",
    "electrical_circuits_admin",
    "magnetism_admin",
]


def get_bot_and_db():
    bot = Bot(TOKEN)
    db = DataBase(db_name)
    return bot, db
