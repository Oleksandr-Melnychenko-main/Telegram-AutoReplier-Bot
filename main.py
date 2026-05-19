import logging
from os import getenv
from sys import exit
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder

from handlers import all_handlers

load_dotenv()
TOKEN = getenv("TELEGRAM_BOT_TOKEN")
if not TOKEN: 
    print("No token has been found") #TODO: add logger here later
    exit(1)

#TODO: add logger things and db later
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     level=logging.INFO
# )


if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    for handler in all_handlers:
        application.add_handler(handler)

    print("Bot's running")
    application.run_polling()