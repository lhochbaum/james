import asyncio
import resources.config as conf
from discord.utils import get
from discord.ext import commands

class EgirlCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_message(self, message):
		if "E-Girl" in [role.name for role in message.author.roles]:
			await message.add_reaction("❤")

def setup(bot):
	bot.add_cog(EgirlCog(bot))			