import discord
import asyncio
import json
from discord.ext import commands
import resources.config as conf

conf.config_load()

# set description for the bot.
description = """Ein mechanischer Kerl, welcher ein paar zusätzliche
Hilfsfunktionen implementiert.
"""

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
bot.load_extension("cogs.maimai")
bot.load_extension("cogs.egirl")
bot.load_extension("cogs.since")
bot.load_extension("cogs.praise")

# finally run the bot!
bot.run(conf.config_read()["token"])
