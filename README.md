Animal Bot Rewrite
===
Rewritten version of [Aresiel/Animal-Bot](https://github.com/Aresiel/Animal-Bot) to use slash commands in order to function with Discord's new changes.

## Self-hosting
The bot is not designed for self-hosting and might not be entirely convenient to self-host. Despite this, if you wish to try, follow the steps below.
1. Rename `empty.config.json` to `config.json` and provide the values inside. All values are obligatory, although tinkering allows you to change that.
2. Install the dependencies by running `npm install`
3. Register the slash commands by running `node deploy-commands.js`
4. Start the bot with `npm start`