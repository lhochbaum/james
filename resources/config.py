import json

config_name = "conf.json"

# initializes the config.
def config_load():
	with open(config_name) as file:
		global config
		config = json.load(file)

	print("successfully loaded configuration")

# returns the config dict.
def config_read():
        return config