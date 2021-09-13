from os import path, getenv
from dotenv import load_dotenv

if path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
BOT_TOKEN = getenv("BOT_TOKEN", None)
API_ID = int(getenv("API_ID", "2107384"))
API_HASH = getenv("API_HASH", "43ed88f662a3fcdaf787fef864fb37fa")
SESSION_NAME = getenv("SESSION_NAME", None)
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
ADMIN = list(map(int, getenv("ADMIN").split()))
DB_URL = getenv("DB_URL", "mongodb+srv://s1com:s1com@cluster0.wrrwz.mongodb.net/Cluster0?retryWrites=true&w=majority")
DB_NAME = getenv("DB_NAME", "my")
BOT_USERNAME = getenv("BOT_USERNAME", "YuiVidioPlayer_bot")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
