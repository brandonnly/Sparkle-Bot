"""
Main bot functions

invite link: https://discord.com/oauth2/authorize?client_id=760945753379176498&scope=bot
"""

import discord
from discord.ext import commands
import re
import os

global sparkles
sparkles = []

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = discord.ext.commands.Bot('sparkle ', allowed_mentions=discord.AllowedMentions.none())


@bot.event
async def on_message(message):
    if message.channel.id in sparkles and message.content.lower() != 'sparkle off':
        # subs out spakles for sparkles and attaches sparkles to the front and back
        string = ":sparkles: " + re.sub('\s', ' :sparkles: ', message.content) + " :sparkles:"
        if len(string) > 2000:
            await message.channel.send("That message is too long by " + str(len(string) - 2000) + " characters!")
        await message.channel.send(string)

    if 'ahlie' in message.content.lower():
        await message.channel.send(":sparkles: TRUE :sparkles:")

    if 'good morning' in message.content.lower():
        await message.channel.send(":sparkles: Good morning! :sparkles:")

    # allows the bot to process all the commands below
    await bot.process_commands(message)


@bot.command()
async def on(ctx):
    sparkles.append(ctx.channel.id)
    await ctx.message.add_reaction('👍')


@bot.command()
async def off(ctx):
    sparkles.remove(ctx.channel.id)
    await ctx.message.add_reaction('👍')


bot.run(BOT_TOKEN)
