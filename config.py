from disnake.ext import commands
from disnake import Intents, ActivityType, Activity
import os

from db.db import UserBd, GuildDb
from db.models import Base
from environs import load_dotenv

load_dotenv()

# bot settings
TOKEN = os.getenv('BOT_TOKEN')

activity = Activity(name="https://github.com/NotBupyc/disnake-bot-template", type=ActivityType.watching)

prefixies = ['.']
bot = commands.Bot(
    command_prefix=prefixies, help_command=None, intents=Intents.all(), activity=activity, reload=True,
)

# DB
Base = Base
Users = UserBd()
Guilds = GuildDb()

BASE_DIR = os.path.dirname(__file__)
PATH_TO_DB = os.path.join(BASE_DIR, 'db.db')

# Cogs
COG_DIR = r'cogs'

OTHER_COGS = ["jishaku"]

