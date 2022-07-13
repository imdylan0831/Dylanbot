# Modules


import discord
import json
import os

from discord.ext import commands


# Configurations


with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
prefix = config.get('prefix')
url = "https://discord.com/api/v9/users/@me/guilds/"

Dylanbot = discord.Client()
Dylanbot = commands.Bot(
    command_prefix=prefix, 
    self_bot=True
)

async def on_ready():
    Dylanbot.remove_command('help')
    await Dylanbot.change_presence(activity=discord.Streaming(name="Dylanbot", url="https://twitch.tv/#"))

def Clear():
    os.system('cls')

def Startprint():
    print("Dylanbot is ready")

@Dylanbot.event
async def on_connect():
    Clear()
    Startprint()


# Commands


@Dylanbot.command()
async def massleave(ctx):
    await ctx.message.delete()
    for guild in Dylanbot.guilds:
        server = Dylanbot.get_guild(guild.id)
        await server.leave()

@Dylanbot.command()
async def massdelete(ctx):
    await ctx.message.delete()
    for guild in Dylanbot.guilds:
        await guild.delete()

@Dylanbot.command()
async def serverclear(ctx):
    await ctx.message.delete()
    try:
        for guild in Dylanbot.guilds:
            server = Dylanbot.get_guild(guild.id)
            await server.leave()
    except:
        for guild in Dylanbot.guilds:
            await guild.delete()

@Dylanbot.command()
async def massunfriend(ctx):
    await ctx.message.delete()
    for user in Dylanbot.user.friends:
        await user.remove_friend()

@Dylanbot.command()
async def massfarewell(ctx, message):
    await ctx.message.delete()
    for user in Dylanbot.user.friends:
        await user.send(message)
        await user.remove_friend()

@Dylanbot.command()
async def massgcleave(ctx):
    await ctx.message.delete()
    for channel in Dylanbot.private_channels:
        if isinstance(channel, discord.GroupChannel):
                await channel.leave()

Dylanbot.run(token, bot=False)