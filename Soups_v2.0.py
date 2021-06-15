import discord
import random
import os
import time
import asyncio
from itertools import cycle
from discord.ext import commands, tasks

client = commands.Bot(command_prefix = '*')

client.remove_command('help')

#limit Teseting CMDs to me ( Captain_KMan#8603 <id: 357663989418688513> )
@client.event
async def on_message(message):
    if type(message.author) == discord.user.ClientUser:357663989418688513
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.event
async def on_message(message):
    if type(message.author) == discord.user.ClientUser:357663989418688513
async def no(ctx):
    await ctx.send('Currently only <@357663989418688513> has access')



@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

# Sends ready message to console & Status
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Rainbow Six: Siege'))
    print('Soups_v2.0 is ready!')

#Sends join message to console
@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

#sends leave message to console
@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

#Check Latencys
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


client.run(os.environ.get['BOT_TOKEN'])