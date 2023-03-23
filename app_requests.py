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
from bs4 import BeautifulSoup
import json
from requests import Session
from bs4 import BeautifulSoup as s
import openai
api_id = 9910861
api_hash = "86e927460a8998ba6d84e9c13acfda95"
bot_token = "5999344767:AAErW_Ejrlhv4X-GocxLdXxdRX__JNenVyc"
bot = Client("bot",api_id=api_id,api_hash=api_hash,bot_token=bot_token)
openai.api_key = bot_token

def generate_text(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = response.choices[0].text
    return message

@bot.on_message(filters.command('url') & filters.private & filters.incoming)
async def add(bot, message):
    send = message.reply
    username = message.from_user.username
    await send("Iniciando")
    session = requests.Session()
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0'}
    url = f"https://santiago.uo.edu.cu/index.php/stgo/login/signIn"
  #  resp = session.get(url, headers=header)
  #  soup = s(resp.text,'html.parser')
  #  ltoken = soup.find("input", attrs={"name": "logintoken"})['value']
  #  await send(ltoken)
    data = {
           # "anchor": "",
           # "logintoken": ltoken,
            "username": "stvz02",
            "password": "stvz02**",
        #    "rememberusername": 1,
        }
    resp2 = session.post(url, headers=header, data=data)
    print(resp2.text)
    if 'válidos' in resp2.text:
        await send('Datos Erróneos')
        return
    else:
        soup2 = s(resp2.text,'html.parser')
        await send('Login ok')
        url1 = f"https://santiago.uo.edu.cu/index.php/stgo/user/profile"
        resp3 = session.post(url1, headers=header)
        print(resp3.text)
        await send("Estás en el perfil")

@bot.on_message(filters.command('kk') & filters.private & filters.incoming)
async def add(bot, message):
    session = requests.Session()
    https://santiago.uo.edu.cu/index.php/stgo/login/signIn

@bot.on_message(filters.text)
def chat(client, message):
    send = message.reply
    username = message.from_user.username
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0'}
    session = requests.Session()
    response = session.get('https://santiago.uo.edu.cu/index.php/stgo/login/signIn')
    soup = BeautifulSoup(response.text, 'html.parser')
    csrf_token = soup.find('input', {'name': 'csrf_token'}).get('value')
    await send("csrf_token")
#3. Inicia sesión con tus credenciales y el token CSRF:
    username = 'stvz02'
    password = 'stvz02**'

    data = {
        'csrf_token': csrf_token,
        'username': username,
        'password': password,
        'submit': 'Iniciar sesión'
    }
    response = session.post('https://santiago.uo.edu.cu/index.php/stgo/login/signIn', headers=header, data=data)
    if 'Cerrar sesión' in response.text:
        print('Inicio de sesión exitoso!')
        await send("error")
    else:
        print('Error al iniciar sesión.')
        await send("ok")

bot.start()
bot.send_message(5416296262,'**BoT Iniciado**')
bot.loop.run_forever()
