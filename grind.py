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


    today = datetime.now().strftime(
        "%Y-%m-%d"
    )


    for player in players:

        name = player["name"]


        if name not in history:

            history[name] = {}


        history[name][today] = player["trophies"]


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



def get_grind():

    history = load_history()

    result = []


    for name, dates in history.items():

        values = sorted(
            dates.keys()
        )


        if len(values) < 2:
            continue


        old = dates[values[-2]]

        new = dates[values[-1]]


        result.append({

            "name": name,

            "gain": new - old

        })


    result.sort(
        key=lambda x: x["gain"],
        reverse=True
    )


    return result[:10]
