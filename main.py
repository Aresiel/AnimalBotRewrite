from discord.ext import commands
from discord_slash import SlashCommand
from colorama import init, deinit

import animalBroker
import config
import helpers

init()  # Colorama Initialisation

bot = commands.AutoShardedBot(
    command_prefix=config.prefix,
    case_insensitive=True,
    owner_id=config.owner,
    description=config.description
)

bot.slash = SlashCommand(bot, sync_commands=True, sync_on_cog_reload=True)

for extension in config.extensions:
    try:
        helpers.info(f'Loading {extension}')
        bot.load_extension(extension)
        helpers.info(f'Loaded')
        print()
    except Exception as exception:
        helpers.warn(f'Failed to load {extension} - {exception}')

bot.run(config.token)
deinit()
