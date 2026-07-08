import requests

from config import (
    TG_TOKEN,
    CHAT_ID
)


def send_post(text):

    url = (
        f"https://api.telegram.org/"
        f"bot{TG_TOKEN}/sendMessage"
    )

    data = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": True
    }


    response = requests.post(
        url,
        data=data
    )


    print(response.json())

    return response.json()
