#   AUTHOR: Jason Abrams
#   Statement: This is my third attempt at making a Discord bot for my friends.
#               Since, I have gotten more friends on my Discord server I can actually use a good bot
#               And since I know how to program slightly in python, I am using this to get my skills
#               Better in Python. If you download this project, you may use it. All I wish is to be
#               mentioned as the person that made this. Basically give credit where it is due

#imports
import discord
import os
import random

from discord import Game
from discord.ext.commands import Bot

#########################################
#    For information about this project, the Information class will be
#    responsible for it.
#########################################
from Python.Discord.info import Information as INFORMATION

File_Path = os.path.dirname(os.path.abspath(__file__))

BOT_PREFIX = '!'
TOKEN = INFORMATION.Get_Token()

client = Bot(command_prefix=BOT_PREFIX)

#Magic 8 Ball example
@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond")
async def eight_ball(message):
    possible_responses = [
                            'Most Likely',
                            'That is a resounding NO',
                            'Too hard to tell',
                            'It is quite possible',
                            'Definitely'
    ]
    print("in 8bLL")
    await message.channel.send("" + random.choice(possible_responses) + ", {0.author.mention}".format(message))
    
#Waluigi picture
@client.command(name='wah',
                description="Displays a picture of Waluigi.",
                brief="WALUIGI TIME")
async def wah(ctx):
    
    f =[]
    for( dirpath, dirnames, filenames ) in os.walk(os.path.join(File_Path, "waluigi")):
        f.extend(filenames)
        break;

    print(f)

    filename = File_Path + '\\waluigi\\' + random.choice(f)

    #COMMENT: Figure out how to iterate through a list of files in a directory and pick one at random.

    with open(filename, 'rb') as fp:
        await ctx.send(file=discord.File(fp))
        fp.close()


@client.command(name='length')
async def length(ctx):
    await ctx.send('Your message is {} characters long.'.format(len(ctx.message.content)))

#gets all of the message from user without quotes
@client.command(name='echo')
async def echo(ctx, *, message: str):
    await ctx.send(message)

#needs quotes from user to get more than immediate words
@client.command(name='echon')
async def echo(ctx, message: str):
    await ctx.send(message)

# DMs users
@client.command(name='tdm')
async def dm_me_test(message):
    msg = "Hello"
    user = client.get_user(message.author.id)
    await message.author.send(msg)
    await message.channel.send("I have sent you a DM, {0.author.mention}".format(message))

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    
    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)

    await client.process_commands(message)
  
    
    
    


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('--------')

client.run(TOKEN)
