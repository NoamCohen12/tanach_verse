import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

from core.finder import VerseFinder

load_dotenv()

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
assert BOT_TOKEN, "BOT TOKEN not found"

finder = VerseFinder()  # נטען פעם אחת


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.message.text.strip()

    if len(name) < 2:
        await update.message.reply_text("כתוב שם בעברית (לפחות 2 אותיות)")
        return

    results = finder.find(name)

    if not results:
        await update.message.reply_text("לא מצאתי פסוקים מתאימים 😕")
        return

    lines = []
    for index, v in enumerate(results,start=1):
        line = f'{index}.{v["book"]} {v["chapter"]}:{v["verse"]}\n{v["text"]}'
        lines.append(line)

    header = f"מצאתי {len(lines)} פסוקים מתאימים:\n"
    reply = header + "\n\n".join(lines)

    await update.message.reply_text(reply)


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("🤖 הבוט רץ...")
    app.run_polling()


if __name__ == "__main__":
    main()
