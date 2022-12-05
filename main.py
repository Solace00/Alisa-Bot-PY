import discord
import os
import random
import json
import asyncio
from discord import app_commands
from discord.ext import commands
with open('tokens.json', 'r') as f:
  data = json.load(f)
token=data['tokens']['bot token']
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

    em.add_field(name = "Actions", value = "hug, kiss, cuddle, poke, tease, harass, blush, cry, dance, lick, nom, pat, wave, slap, greet, kill")
    em.add_field(name = "Information", value = "Avatar, Stats, serverinfo")
    em.add_field(name = "Music", value = "Join, Summon, leave, volume, play, now_playing, pause, resume, skip, stop, queue, shuffle, remove, loop")
    em.add_field(name = "Fun", value = "rps, toss")

    await ctx.send(embed = em)

#####################################################################


async def main():
    await load ()
    await bot.start(token)
    

asyncio.run(main())