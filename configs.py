# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", "977080"))
	API_HASH = os.environ.get("API_HASH", "0c20c4265501492a1513f91755acd42b")
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "6394289671:AAFLSJCS8F0OIp2td3zXVgnmsa66KRnNuVg")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "thunder_files_bot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001637400311"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "399726799"))
	DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://abcd:abcd@cluster0.zglig1z.mongodb.net/?retryWrites=true&w=majority")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1001637400311")
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is Permanent Files Store Bot!
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [Files Store Bot](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** [Heroku](https://heroku.com)

🧑🏻‍💻 **Developer:** @ded_eye
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** @ded_eye

remember that developer will Delete Adult Contents from Database. So better don't Store Those Kind of Things.
"""
	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nThis is Permanent **File Store Bot**.

Send me any file I will give you a permanent Sharable Link. I Support Channel Also! Check **About Bot** Button.
"""
