import asyncio

class PraiseCog:
	def __init__(self, bot):
		self.bot = bot

	@asyncio.coroutine
	def on_message(self, message):
		if message.content.lower() == "guter bot":
			yield from self.bot.send_message(destination=message.channel, content="{} danke".format(message.author.mention))

def setup(bot):
	bot.add_cog(PraiseCog(bot))			