import os
from telegram.ext import Updater, CommandHandler, JobQueue
import logging
import time
from dotenv import load_dotenv

import requests


url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&category=blast-ecosystem&order=volume_desc&per_page=100&page=1&sparkline=false&locale=en"

response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # List to store formatted token data
    formatted_data = []

    # Iterate through each token data dictionary
    for token_data in data:
        token_name = token_data.get('name', 'N/A')
        token_price = token_data.get('current_price', 'N/A')
        total_volume = token_data.get('total_volume', 'N/A')
        all_time_high = token_data.get('ath', 'N/A')

        # Append token data to formatted_data list
        formatted_data.append({
            'name': token_name,
            'price': token_price,
            'total_volume': total_volume,
            'all_time_high': all_time_high
        })


# Load environment variables from .env file
load_dotenv()
# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

logger = logging.getLogger(__name__)

# Define the function to send hi hello message
def send_hi_hello(context: JobQueue):
    chat_id = os.environ.get("CHANNEL_NAME")
    context.bot.send_message(chat_id=chat_id, text=formatted_data)

# Define the start command
def start(update, context):
    update.message.reply_text('Hi! I will send "Hi, hello!" to the channel every 30 minutes.')

# Define the main function
def main():
    bot_token = os.environ.get("BOT_TOKEN")
    if not bot_token:
        print("Error: BOT_TOKEN environment variable is not set.")
        return

    # Create the Updater and pass it your bot's token.
    updater = Updater(bot_token, use_context=True)
    
    # Get the job queue
    job_queue = updater.job_queue

    # Schedule the job to send hi hello message every 30 minutes
    job_queue.run_repeating(send_hi_hello, interval=100, first=1)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
