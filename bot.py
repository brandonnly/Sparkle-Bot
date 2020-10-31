"""
Main bot functions

invite link: https://discord.com/oauth2/authorize?client_id=760945753379176498&scope=bot
"""

import discord
from datetime import datetime
from discord.ext import commands, tasks
import re
import os

global sparkles
global mudae_reminder
sparkles = []
mudae_reminder = []

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = discord.ext.commands.Bot('sparkle ', allowed_mentions=discord.AllowedMentions.none())


@bot.event
async def on_message(message):
    # stops bot from looping itself
    if message.author == bot.user:
        return

    # sparkles message if sparkle on
    elif message.channel.id in sparkles and message.content.lower() != 'sparkle off':
        # subs out spaces for sparkles and attaches sparkles to the front and back
        string = ":sparkles: " + re.sub(r'\s+', ' :sparkles: ', message.content) + " :sparkles:"
        if len(string) > 2000:
            for chunk in [string[i:i+2000] for i in range(0, len(string), 2000)]:
                await message.channel.send(chunk)
        await message.channel.send(string)

    # sparkles individual words
    elif 'sparkle' in message.content.lower():
        string = message.content.lower().split(' ')
        for x in range(len(string)):
            if string[x+1] == 'message' or string[x+1] == 'on' or string[x+1] == 'off' or string[x+1] == 'help' or string[x+1] == 'mudae':
                break
            elif string[x] == 'sparkle':
                string[x+1] = ":sparkles: " + string[x+1] + " :sparkles:"
                string.pop(x)
                break
        if string[1] == 'message' or string[1] == 'on' or string[1] == 'off' or string[1] == 'help' or string[1] == 'mudae':
            pass
        else:
            string = ' '.join(string)
            await message.channel.send(string)

    # ahlie response
    elif 'ahlie' in message.content.lower():
        await message.channel.send(":sparkles: TRUE :sparkles:")

    # good morning response
    elif 'good morning' in message.content.lower():
        await message.channel.send(":sparkles: Good morning! :sparkles:")

    # allows the bot to process all the commands below
    await bot.process_commands(message)


@bot.command()
async def on(ctx):
    """
    Enables the sparkling of all messages in this channel
    """
    sparkles.append(ctx.channel.id)
    await ctx.message.add_reaction('👍')


@bot.command()
async def off(ctx):
    """
    Disables the sparkling of all messages in this channel
    """
    sparkles.remove(ctx.channel.id)
    await ctx.message.add_reaction('👍')


@bot.command()
async def message(ctx, *, arg):
    """
    Sparkles this message only
    """
    string = ":sparkles: " + re.sub(r'\s+', ' :sparkles: ', ctx.message.content) + " :sparkles:"
    if len(string) > 2000:
        for chunk in [string[i:i + 2000] for i in range(0, len(string), 2000)]:
            await ctx.send(chunk[21:len(chunk)])
    await ctx.send(string[37:len(string)])


@bot.command()
async def mudae(ctx):
    """
    Toggles mudae roll reminder in the current channel
    """
    if ctx.channel.id not in mudae_reminder:
        mudae_reminder.append(ctx.channel.id)
        await ctx.send("I'll send reminders to roll in this channel.")
    else:
        mudae_reminder.remove(ctx.channel.id)
        await ctx.send("I'll stop sending reminders to roll in this channel.")


@tasks.loop(seconds=55.0)
async def roll_reminder():
    if datetime.now().minute == 30:
        for c in mudae_reminder:
            channel = bot.get_channel(c)
            await channel.send('✨ time ✨ to ✨ roll! ✨')

roll_reminder.start()


bot.run(BOT_TOKEN)
