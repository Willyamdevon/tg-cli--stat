from telethon import TelegramClient
from dotenv import load_dotenv
import os
import asyncio
import logging


load_dotenv()

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y—%m—%d %H:%M:%S",
)

API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
SESSION_NAME = os.getenv('SESSION_NAME')
USER_TO_SEND = os.getenv('USER_TO_SEND')

EXCEPTIONS = ["что", "для", "чтобы", "ага", "еще", "ещё", "вот", "это", "уже", "там", "как", "так", "будет", "меня", "мне", "если", "тут", "тоже", "есть", "про", "типо", "было", "когда", "нас", "только", "или", "нет", "его", "тебе", "они"]
def create_client():
    return TelegramClient(SESSION_NAME, API_ID, API_HASH)

async def get_messages(client, chat_username):
    await client.start()
    try:
        messages = await client.get_messages(chat_username, limit=None)
        for message in messages:
            print(f"Sender ID: {message.sender_id}, Message: {message.text}")
    except Exception as e:
        print(f"An error occurred: {e}")

async def stats(client, chat_username):
    logging.info("Starting stats")
    await client.start()
    res = {}
    cnt = 0
    try:
        messages = await client.get_messages(chat_username, limit=None)
        logging.info("Get all messages")
        for message in messages:
            cnt += 1
            if not isinstance(message.text, str):
                continue
            words = message.text.split()
            for word in words:
                if len(word) <3 or word in EXCEPTIONS:
                    continue
                if word not in res:
                    res[word] = 1
                    continue
                res[word] += 1
            print(cnt)
        top_10_items = sorted(res.items(), key=lambda item: item[1], reverse=True)[:10]

        top_10 = {key: value for key, value in top_10_items}
        return top_10

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    client = create_client()
    res = asyncio.run(stats(client, USER_TO_SEND))
    print(res)