import praw
import asyncio
import resources.config as conf
from discord.ext import commands
import urllib.request

# get clientID and client secret from our config.
client_id = conf.config_read()["clientId"]
client_secret = conf.config_read()["clientSecret"]

# get the meme channel.
maimai_channel = conf.config_read()["maimaiChannel"]

# initialize reddit.
user_agent = "JamesBot v1.0 (github.com/lhochbaum)"
subreddit = "ich_iel"
reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)

class MaimaiCog:
	def __init__(self, bot):
		self.bot = bot

	@commands.command(pass_context=True)
	@asyncio.coroutine
	def maimai(self, ctx):
		channel = ctx.message.channel

		# check for the meme channel.
		if not channel.id == conf.config_read()["maimaiChannel"]:
			return

		# download a random meme.
		maimai = random_maimai()
		file = download(maimai["image"])

		# send the file.
		yield from self.bot.send_file(destination=ctx.message.channel, fp=file, content=maimai["title"])

def setup(bot):
	bot.add_cog(MaimaiCog(bot))

# we are getting a single trending post and returning title and its image.
def random_maimai():
	for submission in reddit.subreddit(subreddit).hot(limit=1):
		return { "title": submission.title, "image": submission.url }

# downloads the file and returns the path.
def download(url):
	filename = "images/{}".format(url.split("/")[-1])

	urllib.request.urlretrieve(url, filename)
	return filename