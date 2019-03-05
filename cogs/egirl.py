import asyncio
import resources.config as conf
from discord.utils import get

class EgirlCog:
	def __init__(self, bot):
		self.bot = bot

	@asyncio.coroutine
	def on_message(self, message):
		if "E-Girl" in [role.name for role in message.author.roles]:
			yield from self.bot.add_reaction(message, "❤")

def setup(bot):
	bot.add_cog(EgirlCog(bot))			