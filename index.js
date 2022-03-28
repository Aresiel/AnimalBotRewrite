const { Client, Intents, MessageEmbed } = require('discord.js')
const config = require('./config.json')
const fetch = require("node-fetch")

const client = new Client({ intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES] });

// Top.gg stats autoposter
const { AutoPoster } = require('topgg-autoposter')
const autoposter = AutoPoster(config.topGGToken, client)

client.once('ready', () => {
    console.log(`${client.user.username} is ready!`)

    // Client activity
    let activityObject = { activities: [{ type: 'WATCHING', name: "for /animal-bot-info" }], status: "online" }
    setInterval(() => {
        client.user.setPresence(activityObject)
    }, 1000*60*60)
    client.user.setPresence(activityObject)
})

/*
    TEMPORARY DURING MIGRATION
    While the bot migrates to slash commands, the old help commands will inform users of the migration.
 */
client.on("messageCreate", message => {
    if(message.content.toLowerCase().startsWith("a!help")){
        const embed = new MessageEmbed()
            .setTitle("Migrated to slash commands")
            .setDescription("**IF YOU CAN'T USE THE BOT, KICK IT AND INVITE IT AGAIN USING [THIS LINK](https://discord.com/api/oauth2/authorize?client_id=511117189835653150&permissions=52288&scope=applications.commands%20bot). IF THAT DOESN'T WORK, CONTACT ME @Aresiel#0666 FOR SUPPORT.**\nThe bot has migrated to slash commands, please type / in order to see the commands. (:")
        message.channel.send({embeds: [embed]})
    }
})

client.on('interactionCreate', async interaction => {
    if(!interaction.isCommand()) return;

    const  { commandName } = interaction;

    if(commandName === "animal-bot-info"){

        const embed = new MessageEmbed()
            .setColor(3421755)
            .setThumbnail(client.user.avatarURL())
            .setTitle("Bot Info")
            .setDescription("A small bot for seeing pictures of animals.")
            .addFields(
                { "name": "How to use", "value": "I have several slash commands available by typing a / and then selecting the one you wish to use in the menu." },
                { name: "Contact me", "value": "You can contact my creator via discord, his username and tag is Aresiel#0666" },
                { name: "Privacy policy", "value": "You can read my privacy policy [here](https://github.com/Aresiel/contact-me/blob/main/privacy%20policy%20no%20data.md)." }
            )
            .setTimestamp()

        interaction.reply({ embeds: [embed] })

    } else {
        await interaction.reply({ embeds: [randomAnimalEmbed(commandName)] })
    }
})

function imageEmbed(title, url){
    const embed = new MessageEmbed()
        .setColor(3421755)
        .setURL(url)
        .setImage(url)
        .setTitle(title)
    return embed
}

function randomAnimal(animal){
    return images[animal][Math.floor(Math.random()*images[animal].length)]
}

function randomAnimalEmbed(animal){
    return imageEmbed(animal.charAt(0).toUpperCase() + animal.slice(1), randomAnimal(animal))
}

let images = {
    "cat": [],
    "dog": [],
    "fox": [],
    "koala": [],
    "horse": [],
    "wolf": [],
    "panda": [],
    "otter": []
}

function updateImages(){
    // Pixabay animals
    ["koala", "horse", "wolf", "panda", "otter"].forEach(animal => {
        fetch(`https://pixabay.com/api/?key=${config.pixabayKey}&q=${animal}&per_page=100&safesearch=true`)
            .then(res => res.json())
            .then(json => {
                json['hits'].forEach(hit => {
                    images[animal].push(hit['largeImageURL'])
                })
            })
        console.log("Updated " + animal)
    })

    // Cat
    fetch('https://api.thecatapi.com/v1/images/search')
        .then(res => res.json())
        .then(json => {
            images['cat'].push(json[0].url)
        })
    console.log("Updated cat")

    // Dog
    fetch('https://api.thedogapi.com/v1/images/search')
        .then(res => res.json())
        .then(json => {
            images['dog'].push(json[0].url)
        })
    console.log("Updated dog")

    // Fox
    fetch('https://randomfox.ca/floof/')
        .then(res => res.json())
        .then(json => {
            images['fox'].push(json.image)
        })
    console.log("Updated fox")
}

setInterval(updateImages, 1000*60*15) // Update every 15 minutes
updateImages()
updateImages()
updateImages()
updateImages()
updateImages()

client.login(config.token)