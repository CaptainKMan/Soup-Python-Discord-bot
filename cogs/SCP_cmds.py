import discord
import random
import os
import time
from itertools import cycle
from discord.ext import commands, tasks

client = commands.Bot(command_prefix='*')
client.remove_command('help')

class SCP_cmds(commands.Cog):
    def __init__(self, client):
        self.client = client

    # SCP command
    '''@client.command()
    async def scp(self, ctx):
        scp = random.randint(1, 5000)
        if scp < (10):
            await ctx.send(f'SCP-000{scp}')
            await ctx.send(f'http://www.scp-wiki.net/scp-000{scp}')
        if scp > (10):
            await ctx.send(f'SCP-00{scp}')
            await ctx.send(f'http://www.scp-wiki.net/scp-00{scp}')
        if scp < (100) and scp >= (10):
            await ctx.send(f'SCP-00{scp}')
            await ctx.send(f'http://www.scp-wiki.net/scp-00{scp}')
        if scp > (100):
            await ctx.send(f'SCP-0{scp}')
            await ctx.send(f'http://www.scp-wiki.net/scp-0{scp}')'''

    # SCP link for specified SCP
    @client.command()
    async def scp_link(self, ctx, *, number):
        await ctx.send(f'SCP-{number}')
        await ctx.send(f'http://www.scp-wiki.net/scp-{number}')


def setup(client):
    client.add_cog(SCP_cmds(client))
