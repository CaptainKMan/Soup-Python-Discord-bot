import discord
import random
import os
import time

from discord.ext import commands


class Ban_kick_unban(commands.cog):

    def __init__(self, client):
        self.client = client

#kick command 
    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None, check=1):
        await member.kick(reason=reason)
        time.sleep(5)
        await ctx.channel.purge(limit=check)

#Ban Command
    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason=None, check=1):
        await member.ban(reason=reason)
        time.sleep(5)
        await ctx.channel.purge(limit=check)

#Unban Command
    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.member_discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)     

def setup(client):
    client.add_cog(Ban_kick_unban(client))
