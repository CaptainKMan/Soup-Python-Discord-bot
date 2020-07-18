import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '#')


@client.event
async def on_ready():
    print('Soups_v2.0 is ready!')

client.run('NzMzODQ4OTI5MDUzMTgwMDE1.XxJQcQ.03F4iDX4CW1AUgXaU_8E3RIQ-Oo')