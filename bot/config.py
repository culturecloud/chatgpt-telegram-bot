from os import getenv

BOT_TOKEN = getenv("BOT_TOKEN")
OPENAI_API_KEY = getenv("OPENAI_API_KEY")
ALLOWED_CHATS = list(map(int, getenv("ALLOWED_CHATS", "").split(" ")))
DIALOGUE_TIMEOUT = int(getenv("TIMEOUT", "600"))
MONGODB_URI = getenv("MONGODB_URI")
