from telegram import Update
from telegram.ext import ContextTypes, CommandHandler


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return
    
    await update.message.reply_text(
        "Проснувся. Нагадую, що інфу, яку передає цей бот за допомогою пайтон модуля google.genai можуть бачити сторонні (хоч і анонімізовану)"
        )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return
    
    await update.message.reply_text("Щоб цей бот вам відповів просто тегніть його у повідомленні")


common_handlers = [
    CommandHandler("start", start),
    CommandHandler("help", help_command),
]
