import json
import os
from datetime import datetime


FILE = "data/history.json"



def load_history():

    if not os.path.exists(FILE):
        return {}

    with open(
        FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)



def save_history(players):

    history = load_history()


    date = datetime.now().strftime(
        "%Y-%m-%d"
    )


    for p in players:

        if p["name"] not in history:

            history[p["name"]] = {}


        history[p["name"]][date] = p["trophies"]



    with open(
        FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            history,
            f,
            ensure_ascii=False,
            indent=4
        )



def get_week_grind():

    history = load_history()


    result = []


    for name,data in history.items():

        dates = sorted(data.keys())


        if len(dates) < 2:
            continue


        old = data[dates[-2]]

        new = data[dates[-1]]


        result.append({

            "name": name,

            "gain": new-old

        })


    result.sort(
        key=lambda x:x["gain"],
        reverse=True
    )


    return result[:10]
