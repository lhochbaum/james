import asyncio
from discord.ext import commands
from datetime import datetime

# implements the !since command which displays the date of the last restart.
class SinceCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	# handler for the !since command.
	@commands.command(pass_context=True)
	async def since(self, ctx):
		await ctx.message.channel.send("Letzter Neustart: `{}`.".format(timestamp))

def setup(bot):
	bot.add_cog(SinceCog(bot))

	# create a timestamp for the current time, which will be sent on command.
	global timestamp
	timestamp = datetime.now().strftime("%d.%m.%Y %H:%M:%S")		