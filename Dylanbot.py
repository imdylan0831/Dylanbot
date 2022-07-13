import discord
import json

from discord.ext import commands

with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
prefix = config.get('prefix')

Dylanbot = discord.Client()
Dylanbot = commands.Bot(
    command_prefix=prefix, 
    self_bot=True
)

async def on_ready():
    Dylanbot.remove_command('help')
    await Dylanbot.change_presence(activity=discord.Streaming(name="Dylanbot", url="https://twitch.tv/#"))

Dylanbot.run(token, bot=False)