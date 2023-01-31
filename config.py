from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", None)
BOT_NAME = getenv("BOT_NAME","frawn bot")
BOT_USERNAME = getenv("BOT_USERNAME", "devfrawnbot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "F_php")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "devahmedfr")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://telegra.ph/file/c8e0655948fe4135758f1.jpg")
PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/c8e0655948fe4135758f1.jpg")
SESSION_NAME = getenv("SESSION_NAME", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5656828413").split()))
