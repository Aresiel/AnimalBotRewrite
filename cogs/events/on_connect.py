from discord.ext import commands
import animalBroker


def setup(bot):
    bot.add_cog(OnConnect(bot))


alreadyStartedRefreshLoop = False;


class OnConnect(commands.Cog, name="On Connect"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_connect(self):
        global alreadyStartedRefreshLoop
        if not alreadyStartedRefreshLoop:
            await animalBroker.startRefreshCycle()
            alreadyStartedRefreshLoop = True
