from dotenv import load_dotenv
import os
import telebot
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import random


def connect_mongo(uri):
    client = MongoClient(uri, server_api=ServerApi('1'))
    return client['telegram'], client


def get_random_document(collection):
    result = collection.find()
    data = list(result)
    return random.choice(data)


def set_message(document):
    return f"❤️‍🩹\n\n{document['title']}\n\n" \
           f"{document['advice']}\n\n🎈🤲🎉\n\n"


def send_message_to_personal(bot_token, chat_id, message):
    bot = telebot.TeleBot(bot_token)
    bot.send_message(chat_id, message)
    bot.stop_bot()


def main():
    load_dotenv()

    bot_token = os.getenv('BOT_TOKEN')
    chat_id = os.getenv('CHAT_ID')
    uri = os.getenv('URI')
    db, client = connect_mongo(uri)
    collection = db['advices-personal']
    random_document = get_random_document(collection)
    message = set_message(random_document)
    send_message_to_personal(bot_token, chat_id, message)
    client.close()


if __name__ == '__main__':
    main()
