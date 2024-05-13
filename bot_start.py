from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from main import MyBot
from handler.database import DataBase
from config import TOKEN, db_name


bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=MemoryStorage())
db = DataBase(db_name)

my_bot = MyBot(bot=bot, dp=dp, db=db)
my_bot.run()
