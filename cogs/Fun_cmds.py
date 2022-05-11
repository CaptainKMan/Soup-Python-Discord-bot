import random
from discord.ext import commands

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
                    'Ask me if I care',
                    'Dumb question ask another',
                    'Forget about it',  
                    'I do not have a clue',
                    'In your dreams',
                    'NOT IN A BILLION YEARS',
                    'Not a chance', 
                    'Obviously',
                    'Oh please',
                    'Sure',
                    'That is ridiculous',
                    'Well maybe',
                    'What do you think?',
                    'Whatever',
                    'Who cares?',
                    'Yeah and I am the pope',
                    'Yeah right',
                    'You wish',
                    'You have got to be kidding...',
                    'You are a cringe ass nanae baby for asking that stupid question',
                    'Were you abducted by aliens? Cause you should know the answer to that',
                    'It is in the mail',
                    'It is not my job to answer that question, its yours',
                    'I have a headache so I am not going to answer, ask again later',
                    'My fish died and I have crippling depression, so no',
                    'No hablo ingles',
                    'The voices told me To say that your question is "GEEEEEE"']
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