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

    #clear command
    @client.command()
    async def clear(self, ctx, amount=1, check=1):
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(':white_check_mark:')
        time.sleep(5)
        await ctx.channel.purge(limit=check)






#Kick/Ban/Unban
    #Kick command
    """@client.command()
    async def kick(ctx, member : discord.Member, *, reason=None, check=1):
        await member.kick(reason=reason)
        time.sleep(5)
        await ctx.channel.purge(limit=check)"""

    #Ban Command
    """@client.command()
    async def ban(ctx, member : discord.Member, *, reason=None, check=1):
        await member.ban(reason=reason)
        time.sleep(5)
        await ctx.channel.purge(limit=check)"""

    #Unban Command
    """@client.command()
    async def unban(ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.member_discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)"""

def setup(client):
    client.add_cog(SCP_cmds(client))