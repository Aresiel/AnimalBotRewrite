import discord
from discord.ext import commands


def setup(bot):
    bot.add_cog(OnConnect(bot))


alreadyStartedRefreshLoop = False;


class OnConnect(commands.Cog, name="On Ready"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("test")
        await self.bot.change_presence(activity=discord.Game("/info"))
