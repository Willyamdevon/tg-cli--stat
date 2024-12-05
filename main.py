from telethon import TelegramClient, sync
from dotenv import load_dotenv
import os

load_dotenv()
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
SESSION_NAME = os.getenv('SESSION_NAME')
USER_TO_SEND = os.getenv('USER_TO_SEND')

def create_client():
    client = TelegramClient(SESSION_NAME, API_ID, API_HASH)
    client.start()
    return client

if __name__ == "__main__":
    client = create_client()
    # print(client.get_me().stringify())
    client.send_message(USER_TO_SEND, 'Hello! Talking to you from Telethon')