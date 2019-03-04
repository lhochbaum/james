import discord
import asyncio
import json
from discord.ext import commands

# set description for the bot.
description = """Ein mechanischer Kerl, welcher ein paar zusätzliche
Hilfsfunktionen implementiert.
""" 

# read credentials from creds.json.
with open("creds.json") as file:
	creds = json.load(file)

# set up the command bot.
bot = commands.Bot(command_prefix='!', description=description)

# small command printing the repo URL.
@bot.command()
@asyncio.coroutine
def source():
	yield from bot.say("https://github.com/lhochbaum/james")

# remove the help command.
bot.remove_command("help")

# load cogs.
bot.load_extension("cogs.tlpd")

# finally run the bot!
bot.run(creds["token"])