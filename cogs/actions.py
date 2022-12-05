import discord
import aiohttp
import asyncio
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
        
        kawaii_token ="288311787072389120.wddZbVkXYndQaUNlFo9H"
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://kawaii.red/api/gif/hug/token={kawaii_token}') as r:
                js = await r.json()
                ur=str(js["response"])
        if not user:
            em = discord.Embed(description=f"{ctx.message.author.mention} aww you are that alone... here a hug for you ", color = 0x000000)
            em.set_image(url=f"{ur}")
            if Notes is None:
                await ctx.send(embed=em)
            return
        embed = discord.Embed(description=f"{ctx.message.author.mention} hugs  {user.mention}", color = 0x000000)
        embed.set_image(url=f"{ur}")
        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.message.author.mention} hugs  {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{ur}")
            await ctx.send(embed=embedZ)
            
       

async def setup(bot):
    await bot.add_cog(Action(bot))