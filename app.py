import discord
from discord.ext import commands
import json

with open('./config/config.json') as json_file:
    json_data = json.load(json_file)

    token = json_data["bot_token"]
    token_beta = json_data["bot_token_beta"]
    prefix = json_data["default_prefix"]
    ver = json_data["ver"]

client = commands.Bot(command_prefix=prefix)
bot = discord.Client()

beta = True
if beta == True:
    token_release = token_beta
else:
    token_release = token


@bot.event
async def on_ready():
    print("version : v%s" % ver)


bot.run(token_beta)