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

        embed.set_author(name='Help')
        embed.add_field(name='ping', value='pong')

        await ctx.send(author, embed=embed)


def setup(client):
    client.add_cog(Help_cmd(client))