import random
from discord.ext import commands
from discord.ext.commands import Bot
from discord_slash import SlashContext, SlashCommand, cog_ext
import helpers
import json
import discord
import animalBroker


def slash_command_factory(animal: str):
    async def _cmd(ctx: SlashContext):
        embed = discord.Embed(
            title=animal.capitalize() + "!"
        ).set_image(url=animalBroker.randomAnimal(animal))
        await ctx.send(embed=embed)

    return _cmd


class Animals(commands.Cog, name="Animals"):
    def __init__(self, bot: Bot):
        self.bot = bot

        for animal in animalBroker.animals.keys():
            helpers.info(f"Adding '{animal}' command")
            bot.slash.add_slash_command(cmd=slash_command_factory(animal), name=animal, description=f"A picture of a {animal}!", guild_ids=[432264604702343179])

    """
    @cog_ext.cog_slash(name="cat", description="A cute picture of a cute cat!", guild_ids=[432264604702343179])
    async def cat(self, ctx: SlashContext):
        image = animalBroker.randomCat()
        embed = discord.Embed(
            title="Cat!"
        ).set_image(url=image)
        await ctx.send(embed=embed)
        """


def setup(bot):
    bot.add_cog(Animals(bot))
