from discord.ext import commands
import helpers
from nanoid import generate
import re

def setup(bot):
    bot.add_cog(ErrorHandler(bot))


class ErrorHandler(commands.Cog, name="Error Handler"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, err):

        if isinstance(err, commands.CommandNotFound):
            return

        if isinstance(err, commands.NotOwner):
            return await ctx.send("Only the owner can use this command")

        if isinstance(err, commands.CheckFailure) or isinstance(err, commands.CheckAnyFailure):
            return await ctx.send("Unable to use command")

        if re.search(".+ (jsk|jishaku)", str(err)):
            return await ctx.send(err)

        err_id = generate(size=10)
        helpers.error(f'[{err_id}] {err}')
        return await ctx.send(f'Unknown error occurred. If this problem persists, contact the developers. [{err_id}]')
