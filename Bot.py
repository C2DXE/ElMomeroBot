import os
import discord
from discord.ext import commands
import random













path = os.getenv('PATH')

token = "MTE2Nzg4NzAxMzMyODk5ODU2MA.Gp7hPb.Ax6OqlN5dRfFtzzmLrGL5MJDkMS3Jge40mO46w"


with open('pollo.jpg', 'rb') as f:
    picture = discord.File(f)



intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def pollo(ctx):
    await ctx.send(f'pollo')
    await ctx.send('https://www.ocu.org/-/media/ocu/images/themes/alimentacion/alimentos/tips/pollo%20guia%20para%20elegir%20y%20conservar/456844_thumbnail.jpg?rev=0e3d5afb-0096-4cbb-8cb9-681c40b3931b&mw=480&hash=F7F9EF56A9B5E525765639B30D670AC4')



bot.run("MTE2Nzg4NzAxMzMyODk5ODU2MA.Gp7hPb.Ax6OqlN5dRfFtzzmLrGL5MJDkMS3Jge40mO46w")
