from telegram import Bot
from telegram.ext import Updater, CommandHandler

import os

BOT_TOKEN = os.environ.get('BOT_TOKEN')

def start(update, context):
    update.message.reply_text("Hello! Yeh ek anonymous chat bot hai!")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()
