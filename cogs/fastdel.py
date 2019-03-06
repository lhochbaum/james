import asyncio
from discord.ext import commands
import resources.config as conf

# implements fast deletion mode.
# during fast deletion mode, the bot will react with "❌" to every message sent.
# users who are allowed to manage messages can quickly delete those messages by
# clicking on the reaction.
class FastDelCog:
	# determines whether fast deletion is turned on or off.
	active = False

	def __init__(self, bot):
		self.bot = bot

	# handler for the !fastdel command.
	@commands.command(pass_context=True)
	@asyncio.coroutine
	def fastdel(self, ctx):
		if not ctx.message.author.server_permissions.manage_messages:
			return

		# invert the active flag.
		self.active = not self.active
		yield from self.bot.say("Schnelles Löschen {}!".format("aktiv" if self.active else "deaktiviert"))

	# listens for messages and reacts to them if active is true.
	@asyncio.coroutine
	def on_message(self, message):
		# fast deletion will only work for messages by users who are not permitted to
		# manage channels.
		if not message.author.server_permissions.manage_messages:
			yield from self.bot.add_reaction(message, "❌")

	# handles clicking on reactions.
	@asyncio.coroutine
	def on_reaction_add(self, reaction, user):
		# stop if fast deletion is disabled or the reaction comes from the bot.
		if not self.active or user == self.bot.user:
			return

		# delete message if permitted.
		if user.server_permissions.manage_messages and reaction.emoji == "❌":
			yield from self.bot.delete_message(reaction.message)

def setup(bot):
	bot.add_cog(FastDelCog(bot))	