from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)

from main import update_club_post


ADMIN_ID = 123456789


async def update_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    if update.effective_user.id != ADMIN_ID:
        return


    await update.message.reply_text(
        "⏳ Обновляю..."
    )


    try:
        update_club_post()

        await update.message.reply_text(
            "✅ Пост обновлён"
        )

    except Exception as e:

        await update.message.reply_text(
            f"❌ Ошибка:\n{e}"
        )



app = Application.builder().token(
    "BOT_TOKEN"
).build()


app.add_handler(
    CommandHandler(
        "update",
        update_command
    )
)


app.run_polling()
