import praw, asyncio, urllib.request, random, discord
import resources.config as conf
from discord.ext import commands

# get clientID and client secret from our config.
client_id = conf.config_read()["clientId"]
client_secret = conf.config_read()["clientSecret"]

# initialize reddit.
user_agent = "JamesBot v1.0 (github.com/lhochbaum)"
subreddit = "ich_iel"
reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)

# implements the !maimai command which posts a random image of r/ich_iel inside the 
# specified maimai channel.
class MaimaiCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(pass_context=True)
	async def maimai(self, ctx):
		channel = ctx.message.channel

		# check for the meme channel.
		if not channel.name == "maimais":
			return

		# download a random meme.
		maimai = random_maimai()
		file = download(maimai["image"])

		# send the file.
		await channel.send(file=discord.File(file))

def setup(bot):
	bot.add_cog(MaimaiCog(bot))

# we are getting a single trending post and returning title and its image.
def random_maimai():
	post = reddit.subreddit(subreddit).random()
	return { "title": post.title, "image": post.url }

# downloads the file and returns the path.
def download(url):
	filename = "images/{}".format(url.split("/")[-1])

	urllib.request.urlretrieve(url, filename)
	return filename