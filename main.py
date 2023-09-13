import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from dotenv import load_dotenv
load_dotenv()
import os 
# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Define a function to handle messages
def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def main() -> None:
    # Replace 'YOUR_BOT_TOKEN' and 'YOUR_WEBHOOK_URL' with your actual bot token and webhook URL.
    bot_token = os.getenv('BOT_TOKEN')
    webhook_url = os.getenv('WEBHOOK_URL')

    # Create the Updater with the bot token
    updater = Updater(token=bot_token, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register a message handler
    message_handler = MessageHandler(Filters.text & ~Filters.command, echo)
    dispatcher.add_handler(message_handler)

    # Set up the webhook
    updater.start_webhook(listen="0.0.0.0", port=8443, url_path=bot_token)
    updater.bot.setWebhook(f"{webhook_url}/{bot_token}")

    # Start the Bot
    updater.idle()

if __name__ == '__main__':
    main()
