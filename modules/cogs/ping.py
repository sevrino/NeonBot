import discord
from discord.commands import slash_command
from discord.ext import commands

class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="ping", description="지연율을 확인합니다.")
    async def ping(self, ctx):
        embed = discord.Embed(colour=0x5C7EBB)
        embed.add_field(name="PING", value=f"{round(self.bot.latency*1000)}ms"  )
        embed.set_footer(
            text="Copyright (c) 2019-2021 sevrino All rights reserved.")
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(ping(bot))