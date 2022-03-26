const { SlashCommandBuilder } = require('@discordjs/builders');
const { REST } = require('@discordjs/rest');
const { Routes } = require('discord-api-types/v9');
const { clientId, guildId, token } = require('./config.json');

const commands = [
    new SlashCommandBuilder().setName('cat').setDescription('A cute little cat!'),
    new SlashCommandBuilder().setName('dog').setDescription('Man\'s best friend!'),
    new SlashCommandBuilder().setName('fox').setDescription('Mix between a cat and dog.'),
    new SlashCommandBuilder().setName('koala').setDescription('Like a huge terrifying bear, but without the huge and terrifying parts.'),
    new SlashCommandBuilder().setName('horse').setDescription('How else are you supposed to get anywhere? Oh wait, cars.'),
    new SlashCommandBuilder().setName('wolf').setDescription('Big woof.'),
    new SlashCommandBuilder().setName('panda').setDescription('All pandas aren\'t black and white.'),
    new SlashCommandBuilder().setName('otter').setDescription('A cute otter.'),
    new SlashCommandBuilder().setName('animal-bot-info').setDescription('Contact info, privacy policy, etc.'),
].map(command => command.toJSON());

const rest = new REST({ version: '9' }).setToken(token);

rest.put(Routes.applicationCommands(clientId), { body: commands })
    .then(() => console.log('Successfully registered application commands.'))
    .catch(console.error);
