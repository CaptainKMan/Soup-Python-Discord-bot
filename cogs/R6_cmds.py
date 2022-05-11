import random
from discord.ext import commands

client = commands.Bot(command_prefix='*')

class R6_cmds(commands.Cog):
    def __init__(self, client):
        self.client = client

    # random defense op
    @client.command(aliases=['dop'])
    async def Defense_random_operator(self, ctx):
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

    # random Offense op
    @client.command(aliases=['aop'])
    async def Attack_random_operator(self, ctx):
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

    # random game things
    @client.command(aliases=['gl'])
    async def Game_Limitations(self, ctx):
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
                    'have to listen to this while you play, on repeat, on 100% volume. https://www.youtube.com/watch?v=ebqHjxhycVA',
                    'are not allowed to lean',
                    'are not allowed to lean or crouch',
                    'change your primary weapons firing mode once',
                    'can not ads or lean',
                    'are not allowed to reload your primary weapon',
                    'have to tk as many people as possible without getting banned',
                    'have to tk the party leader at the beginning of every round for 1 match']
        await ctx.send(f'You {random.choice(limitors)}.')


def setup(client):
    client.add_cog(R6_cmds(client))
