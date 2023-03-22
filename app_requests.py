import asyncio
import time
import requests
from pyrogram import Client , filters
from pyrogram.types import Message, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
import os
from pyrogram.errors import ChatAdminRequired, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
#from json import loads,dumps
from pyrogram.types import ForceReply
from pyrogram.handlers import MessageHandler

api_id = 9910861
api_hash = "86e927460a8998ba6d84e9c13acfda95"
bot_token = "5897771276:AAHjxn9_D-ar3lHXxfEJAqjdwAdTp01Lw30"
bot = Client("bot",api_id=api_id,api_hash=api_hash,bot_token=bot_token)

@bot.on_message(filters.command('url') & filters.private & filters.incoming)
async def add(bot, message):
    send = message.reply
    username = message.from_user.username
    await send("Iniciando")
    username = f"alejandropo"
    password = "1234567m"
    data = {'username': username, 'password': password, 'rememberusername': 1} 
    url = "https://eduvirtual.uho.edu.cu/login/index.php"
    s = requests.get(url, data=data)
    print(s.text)
    r = requests.Session.post(url=url, data=data)
    print(r.tetx)

bot.start()
bot.send_message(5416296262,'**BoT Iniciado**')
bot.loop.run_forever()
