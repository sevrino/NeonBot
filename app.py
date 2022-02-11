import discord
from discord.ext import commands
import json
import os

with open('./config/config.json') as json_file:
    json_data = json.load(json_file)
    token = json_data["bot_token"]
    token_beta = json_data["bot_token_beta"]
    prefix = json_data["default_prefix"]
    ver = json_data["ver"]

client = commands.Bot(command_prefix=prefix)
bot = discord.Bot()

beta = True
if beta == True:
    token_release = token_beta
else:
    token_release = token

@bot.event
async def on_ready():
    print("version : v%s" % ver)
    game = discord.Game("%s도움말" % prefix + " | " + "v.%s" % ver)
    await client.change_presence(status=discord.Status.online, activity=game)


for folder in os.listdir("modules"):
    if os.path.exists(os.path.join("modules", folder, "cog.py")):
        client.load_extension(f"modules.{folder}.cog")

bot.run(token_release)