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
async def source(ctx):
	await ctx.message.channel.send("https://github.com/lhochbaum/james")

# remove the help command.
bot.remove_command("help")

# load cogs.
bot.load_extension("cogs.tlpd")
bot.load_extension("cogs.maimai")
bot.load_extension("cogs.egirl")
bot.load_extension("cogs.since")
bot.load_extension("cogs.praise")
bot.load_extension("cogs.doubt")
bot.load_extension("cogs.w2g")

# finally run the bot!
bot.run(conf.config_read()["token"])
