import requests
from config import BRAWL_TOKEN, CLUB_TAG


HEADERS = {
    "Authorization": f"Bearer {BRAWL_TOKEN}"
}


def get_club_members():

    url = (
        "https://api.brawlstars.com/v1/clubs/"
        f"{CLUB_TAG.replace('#','%23')}"
    )


    response = requests.get(
        url,
        headers=HEADERS
    )

    data = response.json()


    players = []


    for member in data["members"]:

        tag = member["tag"]

        player_url = (
            "https://api.brawlstars.com/v1/players/"
            f"{tag.replace('#','%23')}"
        )


        player = requests.get(
            player_url,
            headers=HEADERS
        ).json()


        players.append({

            "name": player["name"],

            "tag": tag,

            "trophies": player["trophies"]

        })


    players.sort(
        key=lambda x: x["trophies"],
        reverse=True
    )


    return players
