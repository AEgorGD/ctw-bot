import os


BRAWL_TOKEN = os.getenv("BRAWL_TOKEN")

TG_TOKEN = os.getenv("TG_TOKEN")

CHAT_ID = os.getenv("CHAT_ID")

MESSAGE_ID = int(
    os.getenv("MESSAGE_ID", 0)
)
