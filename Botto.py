#   AUTHOR: Jason Abrams
#   Statement: This is my third attempt at making a Discord bot for my friends.
#               Since, I have gotten more friends on my Discord server I can actually use a good bot
#               And since I know how to program slightly in python, I am using this to get my skills
#               Better in Python. If you download this project, you may use it. All I wish is to be
#               mentioned as the person that made this. Basically give credit where it is due


#imports
__name__ = "__main__"
import json
import os
import random
import sys

import discord
from discord import Game
from discord.ext.commands import Bot

#########################################
#    For information about this project, the Information class will be
#    responsible for it.
#########################################
from my_info import Information
from Internet_Calls import API_Calls

INFO = Information()
API_CALLS = API_Calls()

File_Path = os.path.dirname(os.path.abspath(__file__))

BOT_PREFIX = '!'
TOKEN = INFO.Get_Token()

client = Bot(command_prefix=BOT_PREFIX)
##################################################################################

#Chooses a file at random from a folder
def Choose_File(folder_name: str):
    if(folder_name == None or folder_name == ""):
        return None

    try:
        f =[]
        for( dirpath, dirnames, filenames ) in os.walk(os.path.join(File_Path, folder_name)):
            f.extend(filenames)
            break;

        filename = File_Path + '\\' + folder_name + '\\' + random.choice(f)
        return filename
    except FileExistsError or FileNotFoundError:
        print("incorrect folder name")
        return None
    except IndexError:
        print("Index Error, most likely folder wasn't found")
        return None


##################################################################################

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
    
    #Gets all files in the Waluigi folder and then chooses one at random

    filename = Choose_File("waluigi")
    if(filename == None):
        filename = File_Path + '\\For_Broken\\dr evil sorry.jpg'
        await ctx.send("```Sorry, it looks like I can't find a file. Please notify someone.```{0}".format(":frowning2:"))

    with open(filename, 'rb') as fp:
        await ctx.send(file=discord.File(fp))
        fp.close()


#Dr Doofenshmirtz giphy
@client.command(name='doof',
                description="Shows Dr. Doofenshmirtz or Perry the Platypus from a URL from GIPIHY",
                brief="Perry or Doofenshmirtz")
async def doof(message):
    doof_url = API_CALLS.Giphy_API_Call("doofenshmirtz phineas and ferb", "10")
    if( doof_url == None):
        doof_url = Choose_File("For_Broken")
        with open(doof_url, 'rb') as fp:
            await message.channel.send(file=discord.File(fp))
    else:
        await message.channel.send("``` BEHOLD, it is the giphy-inator\n ```URL: {0}".format(doof_url))

#X-blade Kingdom Hearts
@client.command(name='x',
                aliases=('chi', 'kai', 'keyblade'))
async def key_blade(message):
    await message.channel.send("Not Yet Implemented!")

#Rolf from Ed, Edd n' Eddy
@client.command(name='rolf')
async def rolf(message):
    await message.channel.send("Not Yet Implemented!")



'''
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
'''

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
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("Awakening the Powers in me"))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('--------')

client.run(TOKEN)
