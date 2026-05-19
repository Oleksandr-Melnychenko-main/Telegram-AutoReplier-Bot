from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, filters
from services.ai_service import generate_ai_response

async def react_to_mention(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.effective_message or not update.effective_user:
        return

    bot_username = f"@{context.bot.username}"
    message_text = update.effective_message.text or update.effective_message.caption or ""

    if bot_username not in message_text:
        return
    
    cleaned_query = message_text.replace(bot_username, "").strip()
    ai_reply = generate_ai_response(cleaned_query)

    await update.effective_message.reply_text(ai_reply)

group_handlers = [
    MessageHandler(
        (filters.Entity("mention") | filters.CaptionEntity("mention")) & ~filters.COMMAND, 
        react_to_mention
    )
]
