import asyncio
from discord.ext import commands

# if a user praises the bot by saying "guter bot", it will
# respond with "Danke <user>".
class PraiseCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	# listens for messages and checks if they praise the bot.
	@commands.Cog.listener()
	async def on_message(self, message):
		if message.content.lower() == "guter bot":
			await message.channel.send("{} danke".format(message.author.mention))

def setup(bot):
	bot.add_cog(PraiseCog(bot))			