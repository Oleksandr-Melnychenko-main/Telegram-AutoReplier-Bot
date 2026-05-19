from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return
    
    await update.message.reply_text("Hello! I am a modular bot.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return
    
    await update.message.reply_text("Here are my commands: /start, /help")

# Pack them up into a list, just like registering a list of listeners
common_handlers = [
    CommandHandler("start", start),
    CommandHandler("help", help_command),
]