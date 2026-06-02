from dotenv import load_dotenv
import os
import telebot
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


def connect_mongo(uri):
    client = MongoClient(uri, server_api=ServerApi('1'))
    return client['telegram'], client


def get_random_advice(collection):
    docs = list(collection.aggregate([{'$sample': {'size': 1}}]))
    if not docs:
        raise ValueError("'advices-personal' koleksiyonu boş")
    return docs[0]['advice']


def send_message(bot_token, chat_id, message):
    bot = telebot.TeleBot(bot_token)
    bot.send_message(chat_id, message)


def main():
    load_dotenv()

    missing = [k for k in ('BOT_TOKEN', 'CHAT_ID', 'URI') if not os.getenv(k)]
    if missing:
        raise RuntimeError(f"Eksik ortam değişkeni: {', '.join(missing)}")

    bot_token = os.getenv('BOT_TOKEN')
    chat_id = os.getenv('CHAT_ID')
    uri = os.getenv('URI')

    db, client = connect_mongo(uri)
    try:
        advice = get_random_advice(db['advices-personal'])
        send_message(bot_token, chat_id, advice)
        print('Nasihat gönderildi.')
    finally:
        client.close()


if __name__ == '__main__':
    main()
