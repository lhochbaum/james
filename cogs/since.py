import asyncio
from discord.ext import commands
from datetime import datetime

class SinceCog:
	def __init__(self, bot):
		self.bot = bot

	@commands.command(pass_context=True)
	@asyncio.coroutine
	def since(self, ctx):
		yield from self.bot.say("Letzter Neustart: `{}`.".format(timestamp))

def setup(bot):
	bot.add_cog(SinceCog(bot))
	global timestamp
	timestamp = datetime.now().strftime("%d.%m.%Y %H:%M:%S")		