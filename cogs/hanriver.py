from discord.ext import commands
import discord
import json
import requests as r

bot = discord.Bot()

@bot.slash_command(name='한강', description='한강 수온을 확인합니다.')
class hanriver(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def hanriver(self, ctx):
        api = "https://api.hangang.msub.kr"

        with open("./config/hanriver.json", "wb") as file:
            response = r.get(api)
            file.write(response.content)

        with open("./config/hanriver.json", "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            temp = data["temp"]
            refresh_time = data["time"]

        embed = discord.Embed(colour=0x5C7EBB)
        embed.add_field(name="한강 수온",
                        value="현재 한강 수온은 %s도 입니다." % temp)
        embed.set_footer(text="새로고침 시간 : %s" % refresh_time)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(hanriver(bot))