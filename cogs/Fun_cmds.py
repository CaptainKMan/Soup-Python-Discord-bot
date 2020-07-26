import discord
import random
import os
import time
from itertools import cycle
from discord.ext import commands, tasks

client = commands.Bot(command_prefix = '*')

class Fun_cmds(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Magik 8Ball
    @client.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
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

    #random rock paper scissors
    @client.command(aliases=['rock', 'paper', 'scissors'])
    async def Rock_Paper_Scissors(self, ctx):
        rockps = ['Rock',
                'Paper',
                'Scissors']
        await ctx.send(f'{random.choice(rockps)}')

    #rigged RPS
        '''#rigged paper
        @client.command(aliases=['rock'])
        async def _paper(ctx):
            await ctx.send('Paper')

        #rigged scissors
        @client.command(aliases=['scissors'])
        async def _rock(ctx):
            await ctx.send('Rock')

        #rigged rock
        @client.command(aliases=['paper'])
        async def _scissors(ctx):
            await ctx.send('Scissors')'''




def setup(client):
    client.add_cog(Fun_cmds(client))