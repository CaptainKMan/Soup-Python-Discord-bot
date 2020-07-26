import discord
import random
import os
import time
from itertools import cycle
from discord.ext import commands, tasks

client = commands.Bot(command_prefix = '*')

client.remove_command('help')

#limit Teseting CMDs to Me (Captain_KMan#8603)
"""if ctx.author.id == 357663989418688513:"""

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

#Check Latencys
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

#Send Youtube Link
@client.command()
async def youtube(ctx):
    await ctx.send('```https://www.youtube.com/channel/UC0KW9Y85cFkrZyPkWrNVRUQ```')

#Twitch
@client.command()
async def twitch(ctx):
    await ctx.send('```https://www.twitch.com/dorito__soup```')
    await ctx.send('```https://www.twitch.com/daecu8603```')
    await ctx.send('```https://www.twitch.com/thejellysoup')

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

#random defense op 
@client.command(aliases=['dop'])
async def Defense_random_operator(ctx):
    defense_ops = ['Mute',
                 'Smoke',
                 'Pulse',
                 'Castle',
                 'Doc',
                 'Rook',
                 'Bandit',
                 'Jager',
                 'KapKan',
                 'Techanka',
                 'Frost',
                 'Valk',
                 'Cav',
                 'Echo',
                 'Mira',
                 'Lesion',
                 'Ela',
                 'Vigil',
                 'Maestro',
                 'Alibi',
                 'Clash',
                 'Kaid',
                 'Mozzie',  
                 'Warden',
                 'Goyo da Boyo',
                 'Melusi',
                 'Oryx', 
                 'Wamai',
                 'Random',
                 'Recruit (M870)',
                 'Recruit (MP5K)']
    await ctx.send(f'You should go: {random.choice(defense_ops)}')

#random Offense op 
@client.command(aliases=['aop'])
async def Attack_random_operator(ctx):
    Attack_ops = ['Ace',
                 'Iana',
                 'Kali',
                 'Amaru',
                 'Kokk',
                 'Gridlock',
                 'Nomad',
                 'Maverick',
                 'Lion',
                 'Finka',
                 'Dokkaebi',
                 'Zofia',
                 'Ying',
                 'Jackal',
                 'Hibana',
                 'Capitao',
                 'Blackbeard',
                 'Buck',
                 'Sledge',
                 'Thatcher',
                 'Ash',
                 'Thermite',
                 'Montagne',  
                 'Twitch',
                 'Blitz',
                 'IQ',
                 'Fuze', 
                 'Glaz',
                 'Random',
                 'Recruit (LMG)',
                 'Recruit (DMR)',
                 'Recruit (AR)']
    await ctx.send(f'You should go: {random.choice(Attack_ops)}')

#random game things
@client.command(aliases=['gl'])
async def Game_Limitations(ctx):
    limitors = ['can not ADS',
                'can play normally',
                'can only play in prone position',
                'can only play in crouching position',
                'can only sprint and can not ads',
                'can only use gadgets',
                'can only use secondary',
                'are not to use gadgets',
                'are not aloud to use audio, no sound allowed. That includes discord sounds. In other words mute your PC',
                'have to listen to this while you play, on repeat, on 100% volume. https://www.youtube.com/watch?v=6-5F3jt_WWs',
                'are not allowed to lean',
                'are not allowed to lean or crouch',
                'change your primary weapons firing mode once',
                'can not ads or lean',
                'are not allowed to reload your primary weapon',
                'have to tk as many people as possible without getting banned',
                'have to tk the party leader at the beginning of every round for 1 match']
    await ctx.send(f'You {random.choice(limitors)}.')

#random rock paper scissors
@client.command(aliases=['rock', 'paper', 'scissors'])
async def Rock_Paper_Scissors(ctx):
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

#clear command
@client.command()
async def clear(ctx, amount=1, check=1):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(':white_check_mark:')
    time.sleep(5)
    await ctx.channel.purge(limit=check)

#SCP command
@client.command()
async def scp(ctx):
    scp = random.randint(1,5000)
    if scp <= (10):
        await ctx.send(f'SCP-00{scp}')
        await ctx.send(f'http://www.scp-wiki.net/scp-00{scp}')
    if scp <= (100) and scp >= (10):
        await ctx.send(f'SCP-0{scp}')
        await ctx.send(f'http://www.scp-wiki.net/scp-0{scp}')
    if scp >= (100):
        await ctx.send(f'SCP-{scp}')
        await ctx.send(f'http://www.scp-wiki.net/scp-{scp}')

#SCP link
@client.command(aliases=['scp link'])
async def scp_link(ctx, *, number):
    if number <= (10):
        await ctx.send(f'SCP-00{number}')
        await ctx.send(f'http://www.scp-wiki.net/scp-00{number}')
    if number <= (100) and number >= (10):
        await ctx.send(f'SCP-0{number}')
        await ctx.send(f'http://www.scp-wiki.net/scp-0{number}')
    if number >= (100):
        await ctx.send(f'SCP-{number}')
        await ctx.send(f'http://www.scp-wiki.net/scp-{number}')

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