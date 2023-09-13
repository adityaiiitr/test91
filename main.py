import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from dotenv import load_dotenv
load_dotenv()
import os
# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Define your bot's token here
TOKEN = os.getenv('BOT_TOKEN')

# Create an Updater
updater = Updater(token=TOKEN, use_context=True)

# Define a command handler
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your echo bot.')

# Define an echo message handler
def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

# Create dispatchers and handlers
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

import os
# Start the bot
if __name__ == '__main__':
    # updater.start_polling()
    WEBHOOK_URL=os.getenv('WEBHOOK_URL_PATH')
    # Set up the webhook
    updater.start_webhook(
        listen='0.0.0.0',
        port=8443,
        url_path=TOKEN,
        webhook_url=f'{WEBHOOK_URL}/{TOKEN}'
    )
    updater.idle()
