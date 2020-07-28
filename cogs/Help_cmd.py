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

            color = 0x0099ff,
            title = 'Soup v2.1 Bot Commands',
            description = 'These are the commands:'

        )
        
        embed.add_field(name="The Ping Command", value="*ping = pong", inline=False)
        embed.add_field(name="Youtube", value="*youtube = sends the Soup Kitchen's youtube link", inline=False)
        embed.add_field(name="8ball", value="*8ball = an 8ball", inline=False)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Help_cmd(client))