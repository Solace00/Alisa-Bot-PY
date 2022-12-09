import discord
import os
import asyncio
import json
from discord import app_commands
from discord.ext import commands

with open('config.json', 'r') as f:
    data = json.load(f)
token = data['tokens']['bot token']

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix = "!", intents = intents, help_command=None)


@bot.event
async def on_ready():
    print("am online cutie.")


async def load():
    for filename in os.listdir('cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')


################### HELP ##########################################

@bot.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title = "help", description = "help commands duh", color = 0x000000)

    em.add_field(name = "Roleplay", value = "baka, bite, blush, clap, confused, cry cuddle, dance, destroy, dodge, facepalm, fbi, fight, hug, kill, kiss, laugh, lick, mad, nom, nosebleed, pat, peek, poke, pout, protect, punch, run, salute, scream, shocked, shrug, slap, sleepy, smile, stare, tickle, triggered, wave, wiggle, wink, yeet")
    em.add_field(name = "Information", value = "Avatar, Stats, serverinfo")
    ##em.add_field(name = "Music", value = "Join, Summon, leave, volume, play, now_playing, pause, resume, skip, stop, queue, shuffle, remove, loop")
    em.add_field(name = "Fun", value = "rps, toss")

    await ctx.send(embed = em)

#####################################################################


async def main():
    await load ()
    await bot.start(token)

asyncio.run(main())