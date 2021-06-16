import discord
import random
import os
import time
import json
from itertools import cycle
from discord.ext import commands, tasks
from discord.ext.commands import cooldown, BucketType

client = commands.Bot(command_prefix = '*')

class Admin_cmds(commands.Cog):
    def __init__(self, client):
        self.client = client

    #clear command
    @client.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=1, check=1):
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(':white_check_mark:')
        time.sleep(5)
        await ctx.channel.purge(limit=check)
    

    #Change prefix command (doesnt work with heroku)
"""
    @client.command()
    @commands.has_permissions(administrator=True)
    async def chgprefix(ctx, prefix):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)
    
        prefixes[str(ctx.guild.id)] = prefix

        with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)
        
        await ctx.send(f'Prefix changed to {prefix}')
"""


def setup(client):
    client.add_cog(Admin_cmds(client))