from discord.ext import commands

client = commands.Bot(command_prefix = '*')

class Soup_cmds(commands.Cog):
    def __init__(self, client):
        self.client = client


    #Send Youtube Link
    @client.command()
    async def youtube(self, ctx):
        await ctx.send('```https://www.youtube.com/channel/UC0KW9Y85cFkrZyPkWrNVRUQ```')

    #Twitch
    @client.command()
    async def twitch(self, ctx):
        await ctx.send('```https://www.twitch.com/dorito__soup```')
        await ctx.send('```https://www.twitch.com/daecu8603```')
        await ctx.send('```https://www.twitch.com/thejellysoup')


def setup(client):
    client.add_cog(Soup_cmds(client))