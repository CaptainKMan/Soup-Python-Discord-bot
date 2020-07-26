import discord
import random
import os
import time
from itertools import cycle
from discord.ext import commands, tasks

client = commands.Bot(command_prefix = '*')

class SCP_cmds(commands.Cog):
    def __init__(self, client):
        self.client = client


  #Check Latencys
@client.command()
async def ping(self, ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

#clear command
@client.command()
async def clear(self, ctx, amount=1, check=1):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(':white_check_mark:')
    time.sleep(5)
    await ctx.channel.purge(limit=check)



def setup(client):
    client.add_cog(SCP_cmds(client))