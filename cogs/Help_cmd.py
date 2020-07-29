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
            title = 'Soup v2.0 Bot Commands',
            description = 'These are the commands:'

        )

        embed.set_author(name="Soups v2.0", url="https://raw.githubusercontent.com/CaptainKMan/Readme/master/README.md", icon_url="https://cdn.discordapp.com/avatars/733848929053180015/c3f5b24b94a47c8f079c65e740d92a0c.png?size=128")
        embed.add_field(name='Youtube', value="*youtube = sends the Soup Kitchen's youtube link", inline=False)
        embed.add_field(name='\u200b', value='\u200b')
        embed.add_field(name='8ball', value='*8ball = an 8ball', inline=False)
        embed.add_field(name='Help', value='*help = lists commands', inline=False)
        embed.add_field(name='Twitch', value="*twitch = sends the Soup Kitchen's Member's Twitch.tv links", inline=False)
        embed.add_field(name='R6 Random Operator', value='*aop = Random Attack Operator', inline=False)
        embed.add_field(name='R6 Random Operator', value='*dop = Random Defense Operator', inline=False)
        embed.add_field(name='Clear Command', value='*clear <number> = clears <number> amount of previous messages', inline=False)
        embed.add_field(name='The Ping Command', value='*ping = pong', inline=False)
        embed.add_field(name='Game Limitations', value='*gl = specifies challenges that you have to abide by for that match in R6 Siege', inline=False)
        embed.add_field(name='Rock, Paper, Scissors', value='*rock, paper, or scissors = I think you know what this does', inline=False)
        embed.add_field(name='SCP', value='*scp = sends a random SCP', inline=False)
        embed.add_field(name='SCP Link', value='*scp_link <number> = sends the wiki page for specified scp, i.e. *scp_link 001', inline=False)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Help_cmd(client))