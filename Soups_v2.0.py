import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '#')

@client.event
async def on_ready():
    print('Soups_v2.0 is ready!')

# Don't need or want this
"""@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')"""

#Check Latency
@client.command()
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
                 'You may rely on it.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

#A Test of the word detector
@client.event
async def on_message(message):
    if client.user.id != message.author.id:
        if 'fruck' in message.content:
            await client.send_message(message.channel, 'SWORE DETECTOR HAS DETECTED THE USE OF THE FR-WORD')

    await client.process_commands(message)






client.run('NzMzODQ4OTI5MDUzMTgwMDE1.XxJQcQ.03F4iDX4CW1AUgXaU_8E3RIQ-Oo')