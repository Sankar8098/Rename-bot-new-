#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
import re
from os import environ
import os

id_pattern = re.compile(r'^.\d+$')


API_ID = os.environ.get("API_ID", "23990433")
API_HASH = os.environ.get("API_HASH", "e6c4b6ee1933711bc4da9d7d17e1eb20")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5992501587:AAHG9qI4VZn9EBawIdCM91ORC1nQuEN4VZc")
ADMIN = int(os.environ.get("ADMIN", '5821871362'))
FSUB_UPDATES = os.environ.get("FSUB_CHANNEL", "SK_MoviesOffl")
FSUB_GROUP = os.environ.get("FSUB_GROUP", "SK_MoviesOffl")
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://sankar:sankar@sankar.lldcdsx.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
CAPTION = os.environ.get("CAPTION", "")
group = environ.get('GROUP', '-1002197729525')
GROUP = int(group) if group and id_pattern.search(group) else None
#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
SUNRISES_PIC= "https://graph.org/file/bd91761f6e938e2e6d23a.jpg"  # Replace with your Telegraph link
AUTH_USERS = int(os.environ.get("AUTH_USERS", '5821871362'))
WEBHOOK = bool(os.environ.get("WEBHOOK", True))
PORT = int(os.environ.get("PORT", "8080"))
LOG_CHANNEL_ID = os.environ.get("LOG_CHANNEL_ID", -1001870015374)
