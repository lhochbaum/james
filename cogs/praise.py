import asyncio

# if a user praises the bot by saying "guter bot", it will
# respond with "Danke <user>".
class PraiseCog:
	def __init__(self, bot):
		self.bot = bot

	# listens for messages and checks if they praise the bot.	
	@asyncio.coroutine
	def on_message(self, message):
		if message.content.lower() == "guter bot":
			yield from self.bot.send_message(destination=message.channel, content="{} danke".format(message.author.mention))

def setup(bot):
	bot.add_cog(PraiseCog(bot))			