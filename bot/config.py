import yaml

from os import getenv

PORT = int(getenv("PORT", "8000"))
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_ID = int(BOT_TOKEN.split(':', 1)[0])
OPENAI_API_KEY = getenv("OPENAI_API_KEY")
ALLOWED_CHATS = list(map(int, getenv("ALLOWED_CHATS", "").split(" ")))
DIALOGUE_TIMEOUT = int(getenv("TIMEOUT", "600"))
MONGODB_URI = getenv("MONGODB_URI")
MESSAGE_STREAMING = getenv("MESSAGE_STREAMING", True)

# chat_modes
with open("chat_modes.yml", 'r') as f:
    CHAT_MODES = yaml.safe_load(f)

# models
with open("models.yml", 'r') as f:
    MODELS = yaml.safe_load(f)