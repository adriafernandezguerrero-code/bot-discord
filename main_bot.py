import discord
from discord.ext import commands
from bot_logic import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hola(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def password(ctx, longitud):
    longitud = int(longitud)
    await ctx.send(f"Tu contraseña segura es:{gen_pass(longitud)}")

@bot.command()
async def moneda(ctx):
    await ctx.send(f"He lanzado la moneda y ha caido: {flip_coin()}")

@bot.command()
async def emoji(ctx):
    await ctx.send(f"Aqui tienes tu emoji: {gen_emoji()}") 

@bot.command()
async def como_estas(ctx):
    await ctx.send(f"Estoy muy papoi cansado de tanto responder papoi")

@bot.command()
async def adios(ctx):
    await ctx.send(f"\U0001f642")

@bot.command()
async def color(ctx):
    await ctx.send(f"He escogido un color y ese ha sido: {gen_color()}")

@bot.command()
async def numero(ctx):
    await ctx.send(f"He escogido un numero del 1 al 100 y ha sido el: {gen_number()}")

bot.run("TOKEN")
