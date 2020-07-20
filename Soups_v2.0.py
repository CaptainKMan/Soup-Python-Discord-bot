import discord
import random
import os
import time
from itertools import cycle
from discord.ext import commands, tasks

client = commands.Bot(command_prefix = '#')

#Use this to only allow Captain_KMan#4631 to test new cmds
"""def test_cmds():
    return ctx.author.id == 357663989418688513"""

#This is what you use to implement the check
"""@commands.check(test_cmds)"""


# Sends ready message to console & Status
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Rainbow Six: Siege'))
    print('Soups_v2.0 is ready!')

#Sends join message to console
@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

#sends leave message to console
@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

def test_cmds():
    return ctx.author.id == 357663989418688513

#Check Latencys
@client.command()
@commands.check(test_cmds)
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

#Send Youtube Link
@client.command()
async def youtube(ctx):
    await ctx.send('```https://www.youtube.com/channel/UC0KW9Y85cFkrZyPkWrNVRUQ```')

#Magik 8Ball
@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['As I see it, yes.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 'Don’t count on it.',
                 'It is certain.',
                 'It is decidedly so.',
                 'Most likely.',
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Outlook good.',
                 'Reply hazy, try again.',
                 'Signs point to yes.',
                 'Very doubtful.',
                 'Without a doubt.',
                 'Yes.',
                 'Yes – definitely.',
                 'You may rely on it.',
                 'Ask Me If I Care',
                 'Dumb Question Ask Another',
                 'Forget About It',  
                 'I do not Get A Clue',
                 'In Your Dreams',
                 'NOT IN A BILLION YEARS',
                 'Not A Chance', 
                 'Obviously',
                 'Oh Please',
                 'Sure',
                 'That is Ridiculous',
                 'Well Maybe',
                 'What Do You Think?',
                 'Whatever',
                 'Who Cares?',
                 'Yeah And I am The Pope',
                 'Yeah Right',
                 'You Wish',
                 'You have Got To Be Kidding...',
                 'You are a Cringe Nanae Baby for Asking That Stupid Question',
                 'Were you Abducted By Aliens? Cause You Should Know the Answer to That',
                 'It is In The Mail',
                 'It is Not My Job to Answer That Question, its Yours',
                 'I have Got a Headache so I am not Going to answer, Ask again Later',
                 'My Fish Died and I have Crippling Depression, so NO',
                 'No Hablo Ingleses',
                 'The Voices Told Me To say That Your Question is "GEEEEEE"']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

#clear command
@client.command()
async def clear(ctx, amount=1, check=1):
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

client.run(os.environ['BOT_TOKEN'])