import discord
import os
import asyncio
import json
from discord_components import ComponentsBot
from discord.ext import commands, tasks
from itertools import cycle

with open('config.json', 'r') as f:
    data = json.load(f)
token = data['tokens']['bot token']

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix = "A!", intents = intents, help_command=None)


bot_status = cycle(["Prefix for Bot A!", "Type in A!help", "Developed by: Solace#7058 & Yato#6441"])

@tasks.loop(seconds=20)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(bot_status)))

@bot.event
async def on_ready():
    print("am online cutie.")
    change_status.start()

##@bot.event
##async def on_command_error(ctx, error):
##    if isinstance(error, commands.MissingRequiredArgument):
##        await ctx.send("Error: Missing Required Arguments. Are you sure you provided __all__ required arguments")

async def load():
    for filename in os.listdir('cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

################### HELP ##########################################

@bot.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title = "help", description = "help commands duh", color = 0x000000)

    em.add_field(name = "Roleplay", value = "baka, bite, blush, clap, confused, cry cuddle, dance, destroy, dodge, facepalm, fbi, fight, hug, kill, kiss, laugh, lick, mad, nom, nosebleed, pat, peek, poke, pout, protect, punch, run, salute, scream, shocked, shrug, slap, sleepy, smile, stare, tickle, triggered, wave, wiggle, wink, yeet")
    em.add_field(name = "Information", value = "Avatar, Stats, serverinfo, userinfo")
    em.add_field(name = "Music", value = "play, pause, resume, stop [STILL IN TEST]")
    em.add_field(name = "Fun", value = "rps, toss, 8ball, roll")
    em.add_field(name = "Mod", value="Clear, Kick, Ban, Unban  [BUGGY EMBED]")

    await ctx.send(embed = em)

#####################################################################


async def main():
    await load ()
    await bot.start(token)

asyncio.run(main())