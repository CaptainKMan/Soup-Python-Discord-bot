import discord
import random
import os
import time
from itertools import cycle
from discord.ext import commands, tasks

client = commands.Bot(command_prefix = '*')
client.remove_command('help')

class Help_cmd(commands.Cog):
    def __init__(self, client):
        self.client = client

    #clear command
    @client.command()
    async def help(self, ctx):
        author = ctx.message.author

        embed = discord.Embed(
            color = discord.Color.blue()

        )

        embed.title(name='Soup v2.1 Bot Commands', url=('https://raw.githubusercontent.com/CaptainKMan/Readme/master/README.md'))
        embed.description('These are the commands')
        embed.add_field(name='The Ping Command', value='```*ping = pong```', inline=False)
        embed.thumbnail('https://cdn.discordapp.com/avatars/733848929053180015/c3f5b24b94a47c8f079c65e740d92a0c.png?size=128')

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Help_cmd(client))