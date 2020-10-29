import discord
import re
import os

global sparkles
sparkles = []

client = discord.Client(everyone=False, here=False, roles=False)
BOT_TOKEN = os.environ.get('BOT_TOKEN')


@client.event
async def on_message(message):
    global sparkles
    if message.author == client.user:
        return
    if message.content == "sparkle on":
        sparkles.append(message.channel.id)
        await message.add_reaction('👍')
    elif message.content == "sparkle off":
        sparkles.remove(message.channel.id)
        await message.add_reaction('👍')
    if sparkles and message.channel.id in sparkles and message.content != 'sparkle on':
        string = ":sparkles: " + re.sub('\s', ' :sparkles: ', message.content) + " :sparkles:"
        string = re.sub('@', ' ', string)
        if len(string) > 2000:
            await message.channel.send("That message is too long by " + str(len(string) - 2000) + " characters!")
        await message.channel.send(string)
    if message.content.lower() == 'ahlie':
        await message.channel.send(":sparkles: TRUE :sparkles:")
    if message.content.lower() == 'good morning':
        await message.channel.send(":sparkles: Good morning! :sparkles:")
    if 'sparkle' in message.content and message.content != 'sparkle on' and not sparkles:
        # make message content into string
        string = message.content
        # remove the initial sparkle
        string = string.replace('sparkle ', '')
        string = string.replace('sparkle', '')
        # replace space characters with sparkles
        string = re.sub('\s', ' :sparkles: ', string)
        # prefix and append a sparkle
        string = ":sparkles: " + string + " :sparkles:"
        if len(string) > 2000:
            await message.channel.send("That message is too long by " + str(len(string) - 2000) + " characters!")
        await message.channel.send(string)


client.run(BOT_TOKEN)
# invite link: https://discord.com/oauth2/authorize?client_id=760945753379176498&scope=bot