from telegram import Update
from telegram.ext import ContextTypes, CommandHandler


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return
    
    await update.message.reply_text(
        "Bot has been started. Information, this bot passes, can be seen by other people if free API key is used"
        )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return
    
    await update.message.reply_text("To make the bot reply just teg him in a message")


common_handlers = [
    CommandHandler("start", start),
    CommandHandler("help", help_command),
]
