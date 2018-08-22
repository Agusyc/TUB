# -*- coding: utf-8 -*-
from telethon import TelegramClient, sync
import handlers

import logging
logging.basicConfig(level=logging.ERROR)

# You must include your API_ID, API_HASH and SESSION_NAME in their respective files. You can get them on my.telegram.org.
api_id = int(open("api_id", "r").read())
api_hash = open("api_hash", "r").read().rstrip()
session_name = open("session_name", "r").read().rstrip()

client = TelegramClient(session_name, api_id, api_hash)

# This connects the client to the Telegram Account
client.start()

# Calls the register function, to add all the event handlers
handlers.register(client)

client.run_until_disconnected()
