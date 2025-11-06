import os
from os import getenv

API_ID = int(os.environ.get("API_ID", "27433400"))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("API_HASH", "1a286620de5ffe0a7d9b57e604293555")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

OWNER_ID = int(os.environ.get("OWNER_ID", "6201066540"))  # Your Telegram user ID
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "27433400 6201066540").split()))  # Space-separated user IDs

MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://niravpatel180503_db_user:vjWNaWhRk0gMSNyQ@cluster0.26bfgmf.mongodb.net/?appName=Cluster0")##your mongo url eg: withmongodb+srv://xxxxxxx:xxxxxxx@clusterX.xxxx.mongodb.net/?retryWrites=true&w=majority
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1003182485007"))  # Telegram channel ID (with -100 prefix)

PREMIUM_LOGS = os.environ.get("PREMIUM_LOGS", "")  # Optional here you'll get all logs
