import discord
import os
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix = "!", intents = intents, help_command=None)

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
                bot.load_extension(f'cogs.{filename[:-3]}')

################### HELP ##############################
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

bot.run("TOKEN")