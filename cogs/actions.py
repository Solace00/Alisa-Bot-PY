import discord
import random
import giphy_client
from giphy_client.rest import ApiException
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
        
        api_key="EFYlbleRxNekO5wTwwxmLxLf7y5NAQ9t"
        api_instance = giphy_client.DefaultApi()
        
        api_response=api_instance.gifs_search_get(api_key,q="anime hug",limit=30,rating='g')
        hugGifs = list(api_response.data)
        giff=random.choice(hugGifs)
        ur=giff.images.original.url

        if not user:
            em = discord.Embed(description=f"{ctx.message.author.mention} aww, are you that alone. here a hugs just for you", color = 0x000000)
            em.set_image(url=f"{ur}")
            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.message.author.mention} hugs {user.mention}", color = 0x000000)
        embed.set_image(url=f"{ur}")

        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.message.author.mention} hugs {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{ur}")
            await ctx.send(embed=embedZ)


#Kiss

    @commands.command()
    async def kiss(self, ctx, user: discord.User = None, *, Notes=None):
        
        api_key="EFYlbleRxNekO5wTwwxmLxLf7y5NAQ9t"
        api_instance = giphy_client.DefaultApi()
        
        api_response=api_instance.gifs_search_get(api_key,q="anime kiss",limit=30,rating='g')
        kissGifs = list(api_response.data)
        giff=random.choice(kissGifs)
        ur=giff.images.original.url

        if not user:
            em = discord.Embed(description=f"{ctx.message.author.mention} aww, are you that alone. here a kiss just for you", color = 0x000000)
            em.set_image(url=f"{ur}")
            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.message.author.mention} kisses {user.mention}", color = 0x000000)
        embed.set_image(url=f"{ur}")

        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.message.author.mention} kisses {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{ur}")
            await ctx.send(embed=embedZ)


#Cuddle

#Gotta find a solution for it


#Poke



#Wave




#Bite





#Tease




#Harass or Bully




#Blush




#Cry




#Dance




#Lick





#Nom




#pat




#Slap





#Punch



#Greet





#Kill




#

async def setup(bot):
    await bot.add_cog(Action(bot))