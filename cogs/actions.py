import discord
import random
from discord import app_commands
from discord.ext import commands

class Action(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Actions Cog loaded.")

#Hugs

    @commands.command()
    async def hug(self, ctx, user: discord.User = None, *, Notes=None):
        hugGifs = ["https://media.giphy.com/media/GMFUrC8E8aWoo/giphy.gif", 
        "https://media.giphy.com/media/wSY4wcrHnB0CA/giphy.gif", "https://media.giphy.com/media/lrr9rHuoJOE0w/giphy.gif", 
        "https://media.giphy.com/media/ZQN9jsRWp1M76/giphy.gif", "https://media.giphy.com/media/fLv2F5rMY2YWk/giphy.gif", 
        "https://media.giphy.com/media/vVA8U5NnXpMXK/giphy.gif", "https://media.giphy.com/media/DjczAlIcyK1Co/giphy.gif", 
        "https://media.giphy.com/media/sUIZWMnfd4Mb6/giphy.gif", "https://c.tenor.com/xIuXbMtA38sAAAAd/toilet-bound-hanakokun.gif",
        "https://c.tenor.com/pcULC09CfkgAAAAC/hug-anime.gif", "https://c.tenor.com/vkiqyZJWJ4wAAAAC/hug-cat.gif", 
        "https://c.tenor.com/rQ2QQQ9Wu_MAAAAC/anime-cute.gif", "https://c.tenor.com/1fXGbo7KvNUAAAAC/hug-anime.gif", 
        "https://c.tenor.com/oQPT1dxDIVQAAAAC/anime-hug.gif", 
        "https://cdn.myanimelist.net/s/common/uploaded_files/1461073447-335af6bf0909c799149e1596b7170475.gif"]

        if not user:
            em = discord.Embed(description=f"{ctx.message.author.mention} hugs", color = 0x000000)
            em.set_image(url=f"{random.choice(hugGifs)}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.message.author.mention} hugs {user.mention}", color = 0x000000)
        embed.set_image(url=f"{random.choice(hugGifs)}")

        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.message.author.mention} hugs {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{random.choice(hugGifs)}")
            await ctx.send(embed=embedZ)

async def setup(bot):
    await bot.add_cog(Action(bot))