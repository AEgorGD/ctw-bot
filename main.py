from datetime import datetime

from brawl import get_club_players

from grind import (
    save_history,
    get_grind
)

from telegram_bot import update_post



def create_post(players):


    total_trophies = sum(
        p["trophies"]
        for p in players
    )


    players_text = ""


    for i, player in enumerate(players, 1):

        players_text += (
            f"{i} {player['name']} "
            f"– {player['trophies']} 🏆\n"
        )


    grind = get_grind()


    grind_text = ""


    medals = [
        "🥇",
        "🥈",
        "🥉"
    ]


    for i, player in enumerate(grind):

        if i < 3:

            place = medals[i]

        else:

            place = f"{i+1}."


        grind_text += (
            f"{place} {player['name']}: "
            f"+{player['gain']}\n"
        )


    text = f"""
<b>Вся инфа по клубу CT-W</b>


<b>1. Руководство</b>

Президент - AFGT | VoxX

Вице - AEGD и QLS | Phoenix


<b>2. Участники</b>

<blockquote expandable>
{players_text}
</blockquote>


<b>Общие кубки клуба:</b>
{total_trophies:,} 🏆


<b>3. Топ по гринду кубков</b>

<blockquote expandable>
{grind_text}
</blockquote>


<b>4. Важное</b>


<a href="https://telegra.ph/Pravila-CT-FAMILY-03-20-2">
Правила чата
</a>


📌 Правила замен в клубе


Главная цель — постепенно усиливать состав клуба.


<i>Информация на {datetime.now().strftime('%d.%m.%Y')}</i>
"""


    return text



def update_club_post():

    players = get_club_players()


    save_history(players)


    post = create_post(players)


    result = update_post(post)


    print(result)



if __name__ == "__main__":

    update_club_post()
