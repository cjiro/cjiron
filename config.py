## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AQAZjTo9pYDyWYSg2bXdWFWheHFeEMdrQenOlO023rUrLoF02B2RAj71v7lHZadFEbmQPjQlvsPkIiauX2MVt5rau6sq7qAfWNR6NbVSbJC4e39bMqqKJHzebRjVRjergHLk5ADIXjc_cFXYjCb0xm1c6ZjYSpcMkcPnZ_3S2GlOt--g-ChQ9gsX993NestEMtU3OlZ31KCUn6CHLAxL_vMC4NAZMEs8dkgy8y21T-zjHC24waVib_Hql6tGetdSfqLha5FwovNn1pHbCGZJyVXwL9TA5O8MAHiC5TJ1hg6Nt0gg7fPn7bbYTbiOr5i1EHZeaDp_m9yznmS6xJdH7_IfAAAAAUZJEVMA")
BOT_TOKEN = getenv("BOT_TOKEN", "5479438535:AAH6oMvsTQ6dvIFMewO6AUTGyxvcPbhYEWE")
BOT_NAME = getenv("BOT_NAME", ". ხ᥆ƚ 𑜀ᥙ᥉Ꭵᥴ . ")
API_ID = int(getenv("API_ID", "13935880"))
API_HASH = getenv("API_HASH", "67115ac8482957c18715b456c0b58d4b")
OWNER_NAME = getenv("OWNER_NAME", "abs")
OWNER_USERNAME = getenv("OWNER_USERNAME", "dd3ddi")
ALIVE_NAME = getenv("ALIVE_NAME", "abs")
BOT_USERNAME = getenv("BOT_USERNAME", "XIIGBOT")
OWNER_ID = getenv("OWNER_ID", "5238519413")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Paaane")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Q73QQ")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Q73QQ")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/7713b9828bced85d9b46e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
