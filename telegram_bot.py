import requests
from config import TG_TOKEN, CHAT_ID, MESSAGE_ID



def update_post(text):


    url = (
        "https://api.telegram.org/"
        f"bot{TG_TOKEN}/editMessageText"
    )


    data = {

        "chat_id": CHAT_ID,

        "message_id": MESSAGE_ID,

        "text": text,

        "parse_mode": "HTML",

        "disable_web_page_preview": True

    }


    requests.post(
        url,
        data=data
    )
