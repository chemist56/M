# https://t.me/ultroid_official



import os
import logging
from logging.handlers import RotatingFileHandler




TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7876087766:AAEB0UCeiCn-147d0lm196ydFezSlCvcbts")
APP_ID = int(os.environ.get("APP_ID", "23336308"))
API_HASH = os.environ.get("API_HASH", "884c5a2f4583f875d9d021b222e1d752")


OWNER = os.environ.get("OWNER", "UsernamesNothing") #Owner username
OWNER_ID = int(os.environ.get("OWNER_ID", "5324831370")) #Owner user id
DB_URL = os.environ.get("DB_URL", "mongodb+srv://david:Nath@cluster0.dv0ma.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "cluster0")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002318835253")) #database id 
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002457281221"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002217845978"))
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "-1002110905372"))
FORCE_SUB_CHANNEL4 = int(os.environ.get("FORCE_SUB_CHANNEL4", "-1001522888236"))


SECONDS = int(os.getenv("SECONDS", "200")) # auto delete in seconds



PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))




START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")

try:
    ADMINS=[6831947029]
    for x in (os.environ.get("ADMINS", "5324831370 6831947029").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")


FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot !"

ADMINS.append(OWNER_ID)
ADMINS.append(5324831370)

LOG_FILE_NAME = "uxblogs.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   





# https://t.me/ultroid_official
