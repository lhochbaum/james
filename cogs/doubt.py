import asyncio
from discord.ext import commands

class DoubtCog:
	def __init__(self, bot):
		self.bot = bot

	@commands.command(pass_context=True)
	@asyncio.coroutine
	def doubt(self, ctx):
		msg = yield from self.bot.say("Reagiere mit \"🤔\", um anzuzweifeln.")
		yield from self.bot.add_reaction(msg, "🤔")
		
def setup(bot):
	bot.add_cog(DoubtCog(bot))		