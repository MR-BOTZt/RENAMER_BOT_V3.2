import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6205069553:AAFBeXmGWF3yVLMK1NxWSYWF2E4a-2bMdmQ")

API_ID = int(os.environ.get("API_ID", "1664585"))

API_HASH = os.environ.get("API_HASH", "52872e45fd30ae002caca0deb789d77b")

STRING = os.environ.get("STRING", "")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
