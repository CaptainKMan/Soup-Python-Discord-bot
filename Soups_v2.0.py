import discord
import os
import logging
from itertools import cycle
from discord.ext import commands, tasks
from discord.ext.commands import errors

# handles logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)



client = commands.Bot(command_prefix = '*')
status = cycle(['DARK SOULS III', 'Can I interest you in everything? All of the time?','Rainbow Six: Quarantine', 'Elden Ring', """with Joseph's internet""", 'Breath of the Wild 2', 'with my feelings', 'with life itself', 'Bo Burnham: Welcome to the internet'])

#class CustomHelpCommand(commands.HelpCommand):
#
#    def __init__(self):
#        super().__init__() 

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

#on joining a guild writes down prefix for that guild (doesnt work with heroku)
"""
@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    
    prefixes[str(guild.id)] = '*'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
"""

#on leaving guild deletes prefix entry (doesnt work with heroku)
"""
@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    
    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
"""

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
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('Unsufficient perms')

#Check Latencys
@client.command()
@commands.is_owner()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

#command specific error message
@ping.error
async def clear_error(ctx, error):
    if isinstance(error, errors.NotOwner):
        await ctx.send('This is only available to the bot owner.')

#lets the bot run
client.run(os.environ.get('BOT_TOKEN'))