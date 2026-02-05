import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, CallbackQueryHandler, ContextTypes, filters

from core.finder import VerseFinder

MODE_EDGES = "edges"
MODE_CONTAINS = "contains"
MODE_CHANGE = "change_mode"

load_dotenv()

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
assert BOT_TOKEN, "BOT TOKEN not found"

finder = VerseFinder()  # נטען פעם אחת

MAX_LEN = 4000  # קצת פחות מ-4096 בשביל ביטחון


async def send_long_message(message, text: str):
    current = ""

    for line in text.split("\n"):
        # +1 בשביל ה־\n
        if len(current) + len(line) + 1 > MAX_LEN:
            await message.reply_text(current)
            current = line
        else:
            if current:
                current += "\n" + line
            else:
                current = line

    if current:
        await message.reply_text(current)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # ⬅️ בדיקה: האם זו הפעם הראשונה
    if not context.user_data.get("intro_shown"):
        intro = (
            "ברוך הבא 👋\n\n"
            "אפשר לחפש פסוקים בשתי דרכים:\n\n"
            "לפי האות הראשונה והאחרונה של השם 🔤\n"
            "פסוק שמכיל את השם עצמו 🔎\n\n"
            "בחר איך תרצה לחפש:"
        )

        keyboard = [
            [InlineKeyboardButton("אות ראשונה ואחרונה 🔤", callback_data="mode_edges")],
            [InlineKeyboardButton("מכיל את השם 🔎", callback_data="mode_contains")],
        ]

        await update.message.reply_text(
            intro,
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

        context.user_data["intro_shown"] = True
        return

    mode = context.user_data.get("mode")
    if not mode:
        await update.message.reply_text("בחר קודם סוג חיפוש 👆")
        return

    name = update.message.text.strip()
    if len(name) < 2:
        await update.message.reply_text("כתוב שם בעברית (לפחות 2 אותיות)")
        return

    if mode == MODE_EDGES:
        results = finder.find(name)

    elif mode == MODE_CONTAINS:
        results = finder.find_contains(name)

    if not results:
        if mode == MODE_CONTAINS:
            await update.message.reply_text(
                "לא מצאתי פסוקים מתאימים 😕\n\n"
                "טיפ: לפעמים כדאי לנסות להסיר אותיות ניקוד כמו י/ו אם השם שלך מכיל אותם.\n"
                "לדוגמה: נועם -> נעם"
            )
        else:
            await update.message.reply_text("לא מצאתי פסוקים מתאימים 😕")
        return

    lines = []
    for index, v in enumerate(results, start=1):
        line = f'{index}.{v["book"]} {v["chapter"]}:{v["verse"]}\n{v["text"]}'
        lines.append(line)

    header = f"מצאתי {len(lines)} פסוקים מתאימים:\n"
    reply = header + "\n\n".join(lines)

    keyboard = [
        [InlineKeyboardButton("החלף סוג חיפוש 🔄", callback_data=MODE_CHANGE)]
    ]

    await send_long_message(update.message, reply)
    await update.message.reply_text(
        "רוצה להחליף דרך חיפוש?",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def on_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "mode_edges":
        context.user_data["mode"] = MODE_EDGES
        await query.message.reply_text(
            "נבחר חיפוש לפי אות ראשונה ואחרונה 🔤\n"
            "עכשיו שלח שם בעברית"
        )

    elif query.data == "mode_contains":
        context.user_data["mode"] = MODE_CONTAINS
        await query.message.reply_text(
            "נבחר חיפוש פסוק שמכיל את השם 🔎\n"
            "עכשיו שלח שם בעברית"
        )

    elif query.data == MODE_CHANGE:
        # מאפסים מצב
        context.user_data.pop("mode", None)

        intro = (
            "אפשר להחליף דרך חיפוש 👇\n\n"
            "לפי האות הראשונה והאחרונה של השם 🔤\n"
            "פסוק שמכיל את השם עצמו 🔎\n\n"
            "בחר איך תרצה לחפש:"
        )

        keyboard = [
            [InlineKeyboardButton("אות ראשונה ואחרונה 🔤", callback_data="mode_edges")],
            [InlineKeyboardButton("מכיל את השם 🔎", callback_data="mode_contains")],
        ]

        await query.message.reply_text(
            intro,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(CallbackQueryHandler(on_button))
    print("🤖 הבוט רץ...")
    app.run_polling()


if __name__ == "__main__":
    main()
