import discord
import random
import os
import time
from itertools import cycle
from discord.ext import commands, tasks
from discord.ext.commands import cooldown, BucketType

client = commands.Bot(command_prefix = '*')
client.remove_command('help')

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





def setup(client):
    client.add_cog(Admin_cmds(client))