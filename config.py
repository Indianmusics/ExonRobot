from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "22069537"))
API_HASH = getenv("API_HASH", "cd11171a4e13d4efe0fbb6b69ac0eb6f")
BOT_TOKEN = getenv("BOT_TOKEN", "5636806554:AAETH-YcIKUKdg-v6YnmuBYV2mxNPynr2ZM")
BOT_NAME = getenv("BOT_NAME","Nancy Music")
BOT_USERNAME = getenv("BOT_USERNAME", "Nancy_XtreamBot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "StarXAssistance")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "gumnaam_aashiq_sayar")
CHANNEL_UPDATES = getenv("CHANNEL_UPDATES", "help_bot_technology")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/cb2763a4fd9af49b26cb0.jpg")
PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/262e434f76a5f2e414178.jpg")
SESSION_NAME = getenv("SESSION_NAME", "BQAGS7gJBx0VI8S1zWrGCz5qvcP7OpUClUagm8h2VYAss-oRNQvKz1OZHzX6bdobWKvCai2OiCHzJjiXDxoFTnDCFpi4CET97hFvv9euMNf4v6XtE2s2cf3irvXlDQ-6CF3jMrwrACqzKji_fvyAv35Rnm1Di-5knbtXDHEOpEVcyUMP1H11rEc3cEUdJtlGca9bFDhvkJ-_labsRy9dG02_SOGf9Qsj8TPlypt7anxAxtHGjOYCXdS3OBttQfdRjJ1CfeFzwqfdauMnblM3Kyr-CJAvXjZ_PZvxd5RCKE9XP8-cUodKFoCHDbdyj2QW1KLxvliN4zka1D67m5lEn-LzAAAAATd3YX0A")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5225537917").split()))
