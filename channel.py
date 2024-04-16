import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Telegram bot token
bot_token = os.getenv("BOT_TOKEN")

# Function to get the chat ID of the channel
def get_channel_chat_id(bot_token):
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
    response = requests.get(url)
    data = response.json()
    return data
    # if data["ok"]:
    #     # Check if there are any updates
    #     if data["result"]:
    #         # Get the chat ID of the first message
    #         chat_id = data["result"][0]["message"]["chat"]["id"]
    #         return chat_id
    #     else:
    #         print("No messages received by the bot yet.")
    #         return None
    # else:
    #     print("Error:", data.get("description"))
    #     return None

def main():
    chat_id = get_channel_chat_id(bot_token)
    if chat_id:
        print("Chat ID:", chat_id)
        print("You can set this chat ID as the value of CHANNEL_NAME environment variable.")
    else:
        print("Failed to retrieve chat ID.")

if __name__ == "__main__":
    main()
