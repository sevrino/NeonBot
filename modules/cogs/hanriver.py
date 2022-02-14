from discord.ext import commands
import discord
import json
import requests as r

class hanriver(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="한강")
    async def hanriver(self, ctx):
        api = "https://api.hangang.msub.kr"

        with open("./config/hanriver.json", "wb") as file:
            response = r.get(api)
            file.write(response.content)

        with open("./config/hanriver.json", "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            temp = data["temp"]
            refresh_time = data["time"]

        embed = discord.Embed(colour=0x000000)
        embed.add_field(name="한강 수온",
                        value="현재 한강 수온은 %s도 입니다." % temp)
        embed.set_footer(text="새로고침 시간 : %s" % refresh_time + "\n자살예방상담전화 : 1393")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(hanriver(bot))