from discord.ext import commands
import asyncio

# emoji ID for :tlpdont:.
tlpdont = "<:tlpdont:551898126919663636>"

# if somebody talks about the TLPD, the bot will respond with :tlpdont:.
class TlpdCog:
	# initialize the cog.
	def __init__(self, bot):
		self.bot = bot

	# a user has sent a message.
	@asyncio.coroutine
	def on_message(self, message):
		# ignore own messages.
		if message.author == self.bot.user:
			return

		# lower the message so we can check for substrings easily.
		lowered = message.content.lower()

		# check for "tlpd" or "zeitverloren" in the message.
		if "tlpd" in lowered or "zeitverloren" in lowered:
			# send the emoji.
			yield from self.bot.send_message(destination=message.channel, content=tlpdont)

def setup(bot):
	bot.add_cog(TlpdCog(bot))		