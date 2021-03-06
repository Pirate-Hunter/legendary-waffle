import os
from telethon import TelegramClient

DEFAULT_TIMEOUT = 60

api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')
bot_token = os.environ.get('BOT_TOKEN')
timeout = os.environ.get('TIMEOUT')

if timeout == None:
    timeout = DEFAULT_TIMEOUT

timeout = int(timeout)


bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)