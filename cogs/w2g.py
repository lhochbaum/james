from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from discord.ext import commands
import asyncio

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--start-maximized")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--headless")
options.add_argument("--disable-gpu")

# get the chrome webdriver.
driver = webdriver.Chrome(chrome_options=options)

class W2gCog:
	def __init__(self, bot):
		self.bot = bot

	@commands.command(pass_context=True)
	@asyncio.coroutine
	def w2g(self, ctx, arg):
		# visit watch2gether.
		driver.get("https://watch2gether.com/")

		# click the button for creating a room.
		button = driver.find_element_by_id("create_room_button")
		button.click()

		# post the channel.
		url = driver.current_url
		yield from self.bot.say(url)

		# enter video URL in search bar and press enter.
		input = driver.find_element_by_id("search-bar-input")
		input.send_keys(arg)
		input.send_keys(Keys.ENTER)
		input.submit()

		# wait for results. TODO: check until it can find the results instead
		# of using a fixed delay.
		asyncio.sleep(3)

		# click the result.
		video = driver.find_element_by_class_name("w2g-item-content")
		video.click()

		asyncio.sleep(1.25)

		# pause the video.
		pause = driver.find_element_by_class_name("w2g-play-button")
		pause.click()

def setup(bot):
	bot.add_cog(W2gCog(bot))