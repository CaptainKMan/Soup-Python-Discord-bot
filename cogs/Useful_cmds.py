import discord
import random
import os
import time
from itertools import cycle
from discord.ext import commands, tasks


client = commands.Bot(command_prefix = '*')
client.remove_command('help')

class Useful_cmds(commands.Cog):
    def __init__(self, client):
        self.client = client

    #first command
    '''@client.command()'''
    





def setup(client):
    client.add_cog(Useful_cmds(client))