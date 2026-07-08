from datetime import datetime

from brawl import get_club_members

from grind import (
    save_history,
    get_week_grind
)

from telegram_bot import update_post



def make_post(players):


    total = sum(
        p["trophies"]
        for p in players
    )


    player_text = ""


    for i,p in enumerate(players,1):

        player_text += (
            f"{i} {p['name']} "
            f"– {p['trophies']} 🏆\n"
        )


    grind = get_week_grind()


    grind_text = ""


    medals = [
        "🥇",
        "🥈",
        "🥉"
    ]


    for i,p in enumerate(grind):

        if i < 3:

            place = medals[i]

        else:

            place = f"{i+1}."


        grind_text += (
            f"{place} {p['name']}: "
            f"+{p['gain']}\n"
        )



    text = f"""

<b>Вся инфа по клубу CT-W</b>


<b>1. Руководство</b>

Президент - AFGT | VoxX

Вице - AEGD и QLS | Phoenix


<b>2. Участники</b>

<blockquote expandable>
{player_text}
</blockquote>


<b>Общее количество игроков:</b> {len(players)}

<b>Общие кубки клуба:</b> {total:,} 🏆



<b>3. Топ по гринду кубков</b>

<blockquote expandable>
{grind_text}
</blockquote>


<b>4. Важное</b>


<a href="https://telegra.ph/Pravila-CT-FAMILY-03-20-2">
Правила чата
</a>


📌 Правила замен в клубе


Обычно при замене нового игрока освобождается 30-е место. Однако если среди последних участников есть игрок, который набрал значительно меньше трофеев или приносит клубу меньше пользы, то заменён может быть именно он.


Главная цель — постепенно усиливать состав клуба.


<i>Информация на {datetime.now().strftime('%d.%m.%Y')}</i>

"""


    return text



players = get_club_members()


save_history(players)


post = make_post(players)


update_post(post)
