import asyncio
from discord.ext import commands

class DoubtCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(pass_context=True)
	async def doubt(self, ctx):
		msg = await ctx.message.channel.send("Reagiere mit \"🤔\", um anzuzweifeln.")
		await msg.add_reaction("🤔")
		
def setup(bot):
	bot.add_cog(DoubtCog(bot))		