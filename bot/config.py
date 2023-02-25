from os import getenv

telegram_token = getenv("BOT_TOKEN")
openai_api_key = getenv("OPENAI_API_KEY")
allowed_chats = list(map(int, getenv("ALLOWED_CHATS", "").split(" ")))
new_dialog_timeout = int(getenv("TIMEOUT", "600"))
mongodb_uri = getenv("DATABASE_URI")
