import discord
import random
import os
import time
import asyncio
from itertools import cycle
from discord.ext import commands, tasks

client = commands.Bot(command_prefix = '*')
status = cycle(['DARK SOULS III', 'Can I interest you in everything? All of the time?','Rainbow Six: Quarantine', 'Elden Ring', """with Joseph's internet""", 'Breath of the Wild 2', 'with my feelings', 'with life itself', 'Bo Burnham: Welcome to the internet'])
client.remove_command('help')


#loads cogs
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

#unloads cogs
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

#filepath to cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

#background tasks
@tasks.loop(hours=168)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

# Sends ready message to console & Status
@client.event
async def on_ready():
    change_status.start()
    print('Soups_v2.0 is ready!')

#Sends join message to console
@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

#sends leave message to console
@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

#errors
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Missing arguements, please run the command again with required arguements')
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('bruh thats not even a commmand')

#command specific error message
'''@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please specify an amount of messages to delete.')'''


#Check Latencys
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')



#lets the bot run
client.run(os.environ.get('BOT_TOKEN'))