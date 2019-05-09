#This is a welcome bot for AikoSena created by Diego Rojas on April 4th, 2019
import discord
print(discord.__version__)
from discord.ext import commands
import asyncio
from itertools import cycle
import time

T = 'NTYzNzczMjcxODM3OTAwODIw.XKeqFA.-0E-qIgkhG9mDsCKMRbAAQkPEmc'

welBot = commands.Bot(command_prefix = '!')

#activates bot
@welBot.event
async def on_ready():
    await welBot.change_presence(game=discord.Game(name='with your feelings >:D'))
    print("UmaruBot has connected successfully!")

#Welcome Bot
@welBot.event
async def on_member_join(member):
    channel = member.server.get_channel("542992242709626911")
    await welBot.send_message(channel, f"Welcome to Aiko's Corner {member.mention}! I purple you :purple_heart: Be sure to check out the #read-me-first channel and pinned messages!")
    await welBot.send_message(member, "Hello there :purple_heart: my name is UmaruBot and welcome to Aiko's Corner! Hope you enjoy your stay! I was created by Diego_mz3 using Python 3.6 :)")

#

#LIST OF COMMANDS-------------------------------------------------------------------------------------------------------

@welBot.event
async def on_message(message):
    author = message.author
    channel = message.channel
    if message.content.startswith('!hi'):
        await welBot.send_message(channel, f'Hello there {author.mention} :) How is your day going? :purple_heart:' )
    await welBot.process_commands(message)

@welBot.command()
async def umaru():
    await welBot.say('Hello World, my name is Umaru. How may I be of service?')

@welBot.command()
async def lol():
    await welBot.say('HAHAHAHAHAHAHAHA')

@welBot.command()
async def botinfo():
    await welBot.say('Umaru Bot. Created by the hands of Diego_mz3, designed for Aiko on April 4th, 2019.')

@welBot.command()
async def ping():
    await welBot.say('Pong!')

@welBot.command()
async def purple():
    await welBot.say('I Purple You! :purple_heart:')

@welBot.command()
async def maker():
    await welBot.say(':100: Ban Maker! :100:')

@welBot.command()
async def three():
    await welBot.say('NOOOOT WHOLESOMEEEE')

@welBot.command(pass_context=True)
async def aiko(ctx):
    channel = ctx.message.channel
    embed = discord.Embed(
        title = ''
    )
    embed.set_image(url='https://cdn.discordapp.com/attachments/542992242709626911/567193210296860678/Screenshot_237.jpg')
    await welBot.send_message(channel, embed=embed)

@welBot.command()
async def Aiko():
    await welBot.say('FLAT IS JUSTICE!!!!!!!!!!!!!!')

@welBot.command()
async def huh():
    await welBot.say('NANI THE F*CK?!?!?!?!?!?')

@welBot.command()
async def deleted():
    await welBot.say(':anger: :anger: :anger: STOB IT!! :anger: :anger: :anger:')

@welBot.command()
async def warning():
    await welBot.say('WeEwOo this content is not wholesome. Tread carefully now! :purple_heart:')

@welBot.command()
async def birthday():
    await welBot.say(':birthday: Happy Birthday from Aiko and friends to you! :birthday:')

@welBot.command()
async def stream():
    await welBot.say(' https://www.twitch.tv/psycho_aiko AIKO IS STREAMING GO GO GO!')

@welBot.command()
async def diego():
    await welBot.say('GO DIEGO GO!!!')

@welBot.command()
async def bye():
    await welBot.say('Bai! Come back soon :purple_heart:')

@welBot.command()
async def xp():
    await welBot.say('EXPOSED')

@welBot.command()
async def corner():
    await welBot.say('Aiko is sulking...')

@welBot.command()
async def ding():
    await welBot.say('Dong!')

@welBot.command(pass_context=True)
async def doggo(ctx):
    channel = ctx.message.channel
    embed = discord.Embed(
        title = 'Link is such a handsome boy'
    )
    embed.set_image(url='https://media.discordapp.net/attachments/550926149455446016/566676638155276533/IMG_20190412_235621.jpg?width=1192&height=671')
    await welBot.send_message(channel, embed=embed)

@welBot.command()
async def gm():
    await welBot.say('Hello World, UmaruBot is activated :)')

@welBot.command()
async def gn():
    await welBot.say('Goodnight Server, UmaruBot Deactivated :( see you soon!')

@welBot.command()
async def freake():
    await welBot.say('Freake for LIFE O.o')

@welBot.command()
async def happy():
    await welBot.say('I am happy for YOU :purple_heart:')

@welBot.command()
async def sad():
    await welBot.say(':( We are here for you :purple_heart:')

@welBot.command()
async def pog():
    await welBot.say('POOOGGERSSS!!')

@welBot.command()
async def bui():
    await welBot.say('Aww I LOVE Bui :purple_heart:')

@welBot.command()
async def hype():
    await welBot.say('HYPE HYPE HYPE HYPE HYPE HYPE')

@welBot.command()
async def brb():
    await welBot.say('UmaruBot will be deactivated for a short amount of time :c')

@welBot.command(pass_context=True)
async def deth(ctx):
    channel = ctx.message.channel
    embed = discord.Embed(
        title = 'FOR THE MOTHERLAND!!!!'
    )
    embed.set_image(url='https://media.tenor.com/images/e71dec17746af9d0e3555fbbb9c580f0/raw')
    await welBot.send_message(channel, embed=embed)

@welBot.command(pass_context=True)
async def yuki(ctx):
    channel = ctx.message.channel
    embed = discord.Embed(
        title = 'YUKIII'
    )
    embed.set_image(url='https://cdn.discordapp.com/attachments/543258687699943424/565791287002005514/IMG_20190410_235053.jpg')
    await welBot.send_message(channel, embed=embed)

@welBot.command(pass_context=True)
async def yoshie(ctx):
    channel = ctx.message.channel
    embed = discord.Embed(
        title = 'Insert Yoshi Noises Here'
    )
    embed.set_image(url='https://i.kym-cdn.com/photos/images/newsfeed/000/910/691/71e.jpg')
    await welBot.send_message(channel, embed=embed)

@welBot.command(pass_context=True)
async def aikorun(ctx):
    channel = ctx.message.channel
    embed = discord.Embed(
        title = 'GET AWAY WHILE YOU CAN'
    )
    embed.set_image(url='https://cdn.discordapp.com/attachments/543258687699943424/559275843696984064/image0.jpg')
    await welBot.send_message(channel, embed=embed)



#END COMMAND LIST-------------------------------------------------------------------------------------------------------

welBot.run(T)









#await channel.send(f"Welcome to the {member.guild.name} discord server!, {member.mention}")
#await welBot.send_message(member, "Welcome to Aiko's Corner! I hope you enjoy your stay, i purple you <3")

#@welBot.event
#async def on_member_join(member):
    #channel = discord.utils.get(member.guild.channels, name='general')
    #await channel.send(f"Welcome to the server {member.mention}! This bot was created by Diego_mz3 using Python, ")





