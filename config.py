from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", 19275563""))
API_HASH = getenv("API_HASH", "332213ccd9f10bd2924e4824172e791e")
BOT_TOKEN = getenv("BOT_TOKEN", "5834312062:AAGgwcjbP5bkphbyeKeIgBkdHJhJrsaW4co")
BOT_NAME = getenv("BOT_NAME","-●⏤͟͟͞͞ ꜱᴘᴏᴛɪꜰʏ ✗ ᴍᴜsɪᴄ🕊️⃝🫧")
BOT_USERNAME = getenv("BOT_USERNAME", "spotify_Xtream_bot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Raj_Oop")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "ALL_EXAM_QUIZ_GROUP_NEW")
CHANNEL_UPDATES = getenv("CHANNEL_UPDATES", "Spotifyupdatebots")

START_IMG = getenv("START_IMG", "https://te.legra.ph/file/cb2763a4fd9af49b26cb0.jpg")
PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/262e434f76a5f2e414178.jpg")
SESSION_NAME = getenv("SESSION_NAME", "BQBoqqauYEUp9emSz2726pOlMTWmtl_mTV6C-v8_rB6mt36AWlSMPe_hKjTcZZgnJzVHBSowIgZ7kMak3ueDWdKWS1Ps5ZyLu6eHZR8_7FYsuxr8SP-QW3PUyi9hgo2ClI4Y7oeESZ3VPqpZ2ahzYMMmZ5u6_x4j3mZ0ylIXwPCun1EzJWtFWpWfoyq5E1swwDLCltyTwJCkZjvF8yZYomlf1dCdT5g-sbRJj_EqV_FckX_xQUMPmGkQM1Tcy30ndJCJ4e7Myl3kV-ilmJvbQayNYRc-xYQhQoCymi9WbjFxbj2TwEg8IebeILwkri_LOTeNW06sTYHN2c4-qwx7aqpwAAAAAU7bqnUA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !  .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5617986165").split()))
