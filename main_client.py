import discord
from bot_logic import *

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('/hello'):
        await message.channel.send("Papoi!")
    elif message.content.startswith('/saludo'):
        await message.channel.send("estoy muy papoi cansado de tanto responder papoi")
    elif message.content.startswith('/password'):
        await message.channel.send(gen_pass(12))
    elif message.content.startswith('/flip'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('/emoji'):
        await message.channel.send(gen_emoji())
    elif message.content.startswith('/color'):
        await message.channel.send(gen_color())
    elif message.content.startswith('/number'):
        await message.channel.send(gen_number())    
    elif message.content.startswith('/bye'):
        await message.channel.send("\U0001f642")
    else:
        await message.channel.send(message.content)

client.run("TOKEN")
