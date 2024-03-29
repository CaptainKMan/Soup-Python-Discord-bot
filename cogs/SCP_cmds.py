import random
from discord.ext import commands

client = commands.Bot(command_prefix='*')

class SCP_cmds(commands.Cog):
    def __init__(self, client):
        self.client = client

    # SCP command
    @client.command()
    async def scp(self, ctx):
        scp = random.randint(1, 5000)
        if scp < (10):
            await ctx.send(f'SCP-000{scp}')
            await ctx.send(f'http://www.scp-wiki.net/scp-000{scp}')
        if scp < (100) and scp >= (10):
            await ctx.send(f'SCP-00{scp}')
            await ctx.send(f'http://www.scp-wiki.net/scp-00{scp}')
        if scp > (100) and scp < (1000):
            await ctx.send(f'SCP-0{scp}')
            await ctx.send(f'http://www.scp-wiki.net/scp-0{scp}')
        if scp >= (1000):
            await ctx.send(f'SCP-{scp}')
            await ctx.send(f'http://www.scp-wiki.net/scp-{scp}')

    # SCP link for specified SCP
    @client.command()
    async def scp_link(self, ctx, *, number):
        await ctx.send(f'SCP-{number}')
        await ctx.send(f'http://www.scp-wiki.net/scp-{number}')


def setup(client):
    client.add_cog(SCP_cmds(client))
