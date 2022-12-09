import discord
import random
import aiohttp
import asyncio
import json
from discord import app_commands
from discord.ext import commands

with open('config.json','r') as f:
    data = json.load(f)


kawaii_token = data['tokens']['kawaii_token']

class Roleplay(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Roleplay Cog loaded.")

#Hugs

    @commands.command(aliases=["Hug", "HUG"])
    async def hug(self, ctx, user: discord.User = None, *, Notes=None):
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://kawaii.red/api/gif/hug/token={kawaii_token}') as r:
                js = await r.json()
                ur=str(js["response"])

        if not user:
            em = discord.Embed(description=f"{ctx.author.mention} aww you are that alone... here a hug for you", color = 0x000000)
            em.set_image(url=f"{ur}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.author.mention} hugs {user.mention}", color = 0x000000)
        embed.set_image(url=f"{ur}")
        
        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.author.mention} hugs {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{ur}")
            await ctx.send(embed=embedZ)


#Kiss

    @commands.command(aliases=["Kiss", "KISS"])
    async def kiss(self, ctx, user: discord.User = None, *, Notes=None):
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://kawaii.red/api/gif/kiss/token={kawaii_token}') as r:
                js = await r.json()
                ur=str(js["response"])

        if not user:
            em = discord.Embed(description=f"{ctx.author.mention} aww you are that alone... here a kiss for you", color = 0x000000)
            em.set_image(url=f"{ur}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.author.mention} kisses {user.mention}", color = 0x000000)
        embed.set_image(url=f"{ur}")
        
        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.author.mention} kisses {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{ur}")
            await ctx.send(embed=embedZ)      


#Cuddle

    @commands.command(aliases=["Cuddle", "CUDDLE"])
    async def cuddle(self, ctx, user: discord.User = None, *, Notes=None):
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://kawaii.red/api/gif/cuddle/token={kawaii_token}') as r:
                js = await r.json()
                ur=str(js["response"])

        if not user:
            em = discord.Embed(description=f"{ctx.author.mention} aww you are that alone... here a cuddle for you", color = 0x000000)
            em.set_image(url=f"{ur}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.author.mention} cuddles {user.mention}", color = 0x000000)
        embed.set_image(url=f"{ur}")
        
        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.author.mention} cuddles {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{ur}")
            await ctx.send(embed=embedZ)


#Poke

    @commands.command(aliases=["Poke", "POKE"])
    async def poke(self, ctx, user: discord.User = None, *, Notes=None):
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://kawaii.red/api/gif/poke/token={kawaii_token}') as r:
                js = await r.json()
                ur=str(js["response"])

        if not user:
            em = discord.Embed(description=f"{ctx.author.mention} pokes you", color = 0x000000)
            em.set_image(url=f"{ur}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.author.mention} pokes {user.mention}", color = 0x000000)
        embed.set_image(url=f"{ur}")
        
        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.author.mention} pokes {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{ur}")
            await ctx.send(embed=embedZ)


#Pout

    @commands.command(aliases=["Pout", "POUT"])
    async def pout(self, ctx, user: discord.User = None, *, Notes=None):
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://kawaii.red/api/gif/pout/token={kawaii_token}') as r:
                js = await r.json()
                ur=str(js["response"])

        if not user:
            em = discord.Embed(description=f"{ctx.author.mention} pouts", color = 0x000000)
            em.set_image(url=f"{ur}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.author.mention} pouts at {user.mention}", color = 0x000000)
        embed.set_image(url=f"{ur}")
        
        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.author.mention} pouts at {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{ur}")
            await ctx.send(embed=embedZ)


#Bite


    @commands.command(aliases=["Bite", "BITE"])
    async def bite(self, ctx, user: discord.User = None, *, Notes=None):
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://kawaii.red/api/gif/bite/token={kawaii_token}') as r:
                js = await r.json()
                ur=str(js["response"])

        if not user:
            em = discord.Embed(description=f"{ctx.author.mention} bites you", color = 0x000000)
            em.set_image(url=f"{ur}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.author.mention} bites {user.mention}", color = 0x000000)
        embed.set_image(url=f"{ur}")
        
        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.author.mention} bites {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{ur}")
            await ctx.send(embed=embedZ)


#Wave

    @commands.command(aliases=["Wave", "WAVE"])
    async def wave(self, ctx, user: discord.User = None, *, Notes=None):
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://kawaii.red/api/gif/wave/token={kawaii_token}') as r:
                js = await r.json()
                ur=str(js["response"])

        if not user:
            em = discord.Embed(description=f"{ctx.author.mention} waves at you", color = 0x000000)
            em.set_image(url=f"{ur}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.author.mention} waves at {user.mention}", color = 0x000000)
        embed.set_image(url=f"{ur}")
        
        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.author.mention} waves at {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{ur}")
            await ctx.send(embed=embedZ)


#Baka

    @commands.command(aliases=["Baka", "BAKA"])
    async def baka(self, ctx, user: discord.User = None, *, Notes=None):
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://kawaii.red/api/gif/baka/token={kawaii_token}') as r:
                js = await r.json()
                ur=str(js["response"])

        if not user:
            em = discord.Embed(description=f"{ctx.author.mention} calls you baka", color = 0x000000)
            em.set_image(url=f"{ur}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.author.mention} calls {user.mention} baka", color = 0x000000)
        embed.set_image(url=f"{ur}")
        
        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.author.mention} calls {user.mention} baka, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{ur}")
            await ctx.send(embed=embedZ)   


#Blush


    @commands.command(aliases=["Blush", "BLUSH"])
    async def blush(self, ctx, user: discord.User = None, *, Notes=None):
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://kawaii.red/api/gif/blush/token={kawaii_token}') as r:
                js = await r.json()
                ur=str(js["response"])

        if not user:
            em = discord.Embed(description=f"{ctx.author.mention} blushes at you", color = 0x000000)
            em.set_image(url=f"{ur}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.author.mention} blushes at {user.mention}", color = 0x000000)
        embed.set_image(url=f"{ur}")
        
        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.author.mention} blushes at {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{ur}")
            await ctx.send(embed=embedZ)   


#Cry

    @commands.command(aliases=["Cry", "CRY"])
    async def cry(self, ctx, user: discord.User = None, *, Notes=None):
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://kawaii.red/api/gif/cry/token={kawaii_token}') as r:
                js = await r.json()
                ur=str(js["response"])

        if not user:
            em = discord.Embed(description=f"{ctx.author.mention} is crying", color = 0x000000)
            em.set_image(url=f"{ur}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{user.mention} made {ctx.author.mention} cry", color = 0x000000)
        embed.set_image(url=f"{ur}")
        
        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{user.mention} made {ctx.author.mention} cry, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{ur}")
            await ctx.send(embed=embedZ)   


#Dance

    @commands.command(aliases=["Dance", "DANCE"])
    async def dance(self, ctx, user: discord.User = None, *, Notes=None):
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://kawaii.red/api/gif/dance/token={kawaii_token}') as r:
                js = await r.json()
                ur=str(js["response"])

        if not user:
            em = discord.Embed(description=f"{ctx.author.mention} dances", color = 0x000000)
            em.set_image(url=f"{ur}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.author.mention} dances for {user.mention}", color = 0x000000)
        embed.set_image(url=f"{ur}")
        
        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.author.mention} dances for {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{ur}")
            await ctx.send(embed=embedZ)


#Lick


    @commands.command(aliases=["Lick", "LICK"])
    async def lick(self, ctx, user: discord.User = None, *, Notes=None):
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://kawaii.red/api/gif/lick/token={kawaii_token}') as r:
                js = await r.json()
                ur=str(js["response"])

        if not user:
            em = discord.Embed(description=f"{ctx.author.mention} lickes you", color = 0x000000)
            em.set_image(url=f"{ur}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.author.mention} lickes {user.mention}", color = 0x000000)
        embed.set_image(url=f"{ur}")
        
        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.author.mention} lickes {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{ur}")
            await ctx.send(embed=embedZ)


#Nom

    @commands.command(aliases=["Nom", "NOM"])
    async def nom(self, ctx, user: discord.User = None, *, Notes=None):
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://kawaii.red/api/gif/nom/token={kawaii_token}') as r:
                js = await r.json()
                ur=str(js["response"])

        if not user:
            em = discord.Embed(description=f"{ctx.author.mention} nomes", color = 0x000000)
            em.set_image(url=f"{ur}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.author.mention} nomes on {user.mention}", color = 0x000000)
        embed.set_image(url=f"{ur}")
        
        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.author.mention} nomes on {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{ur}")
            await ctx.send(embed=embedZ)


#pat

    @commands.command(aliases=["Pat", "PAT"])
    async def pat(self, ctx, user: discord.User = None, *, Notes=None):
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://kawaii.red/api/gif/pat/token={kawaii_token}') as r:
                js = await r.json()
                ur=str(js["response"])

        if not user:
            em = discord.Embed(description=f"{ctx.author.mention} pats you", color = 0x000000)
            em.set_image(url=f"{ur}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.author.mention} pats {user.mention}", color = 0x000000)
        embed.set_image(url=f"{ur}")
        
        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.author.mention} pats {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{ur}")
            await ctx.send(embed=embedZ)


#Slap


    @commands.command(aliases=["Slap", "SLAP"])
    async def slap(self, ctx, user: discord.User = None, *, Notes=None):
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://kawaii.red/api/gif/slap/token={kawaii_token}') as r:
                js = await r.json()
                ur=str(js["response"])

        if not user:
            em = discord.Embed(description=f"{ctx.author.mention} slaps you", color = 0x000000)
            em.set_image(url=f"{ur}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.author.mention} slaps {user.mention}", color = 0x000000)
        embed.set_image(url=f"{ur}")
        
        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.author.mention} slaps {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{ur}")
            await ctx.send(embed=embedZ)


#Punch

    @commands.command(aliases=["Punch", "PUNCH"])
    async def punch(self, ctx, user: discord.User = None, *, Notes=None):
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://kawaii.red/api/gif/punch/token={kawaii_token}') as r:
                js = await r.json()
                ur=str(js["response"])

        if not user:
            em = discord.Embed(description=f"{ctx.author.mention} punches you", color = 0x000000)
            em.set_image(url=f"{ur}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.author.mention} punches {user.mention}", color = 0x000000)
        embed.set_image(url=f"{ur}")
        
        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.author.mention} punches {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{ur}")
            await ctx.send(embed=embedZ)

#Run

    @commands.command(aliases=["Run", "RUN"])
    async def run(self, ctx, user: discord.User = None, *, Notes=None):
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://kawaii.red/api/gif/run/token={kawaii_token}') as r:
                js = await r.json()
                ur=str(js["response"])

        if not user:
            em = discord.Embed(description=f"{ctx.author.mention} runs from you", color = 0x000000)
            em.set_image(url=f"{ur}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.author.mention} runs from {user.mention}", color = 0x000000)
        embed.set_image(url=f"{ur}")
        
        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.author.mention} runs from {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{ur}")
            await ctx.send(embed=embedZ)

#Kill

    @commands.command(aliases=["Kill", "KILL"])
    async def kill(self, ctx, user: discord.User = None, *, Notes=None):
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://kawaii.red/api/gif/kill/token={kawaii_token}') as r:
                js = await r.json()
                ur=str(js["response"])

        if not user:
            em = discord.Embed(description=f"{ctx.author.mention} kills you", color = 0x000000)
            em.set_image(url=f"{ur}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.author.mention} kills {user.mention}", color = 0x000000)
        embed.set_image(url=f"{ur}")
        
        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.author.mention} kills {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{ur}")
            await ctx.send(embed=embedZ)


#Clap


    @commands.command(aliases=["Clap", "CLAP"])
    async def clap(self, ctx, user: discord.User = None, *, Notes=None):
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://kawaii.red/api/gif/clap/token={kawaii_token}') as r:
                js = await r.json()
                ur=str(js["response"])

        if not user:
            em = discord.Embed(description=f"{ctx.author.mention} claps for you", color = 0x000000)
            em.set_image(url=f"{ur}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.author.mention} claps for {user.mention}", color = 0x000000)
        embed.set_image(url=f"{ur}")
        
        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.author.mention} claps for {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{ur}")
            await ctx.send(embed=embedZ)

#Confused

    @commands.command(aliases=["Confused", "CONFUSED"])
    async def confused(self, ctx, user: discord.User = None, *, Notes=None):
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://kawaii.red/api/gif/confused/token={kawaii_token}') as r:
                js = await r.json()
                ur=str(js["response"])

        if not user:
            em = discord.Embed(description=f"{ctx.author.mention} is confused", color = 0x000000)
            em.set_image(url=f"{ur}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.author.mention} is confused at {user.mention}", color = 0x000000)
        embed.set_image(url=f"{ur}")
        
        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.author.mention} is confused at {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{ur}")
            await ctx.send(embed=embedZ)


#Destroy

    @commands.command(aliases=["Destroy", "DESTROY"])
    async def destroy(self, ctx, user: discord.User = None, *, Notes=None):
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://kawaii.red/api/gif/destroy/token={kawaii_token}') as r:
                js = await r.json()
                ur=str(js["response"])

        if not user:
            em = discord.Embed(description=f"{ctx.author.mention} is destroyed", color = 0x000000)
            em.set_image(url=f"{ur}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.author.mention} was destroyed by {user.mention}", color = 0x000000)
        embed.set_image(url=f"{ur}")
        
        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.author.mention} was destroyed by {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{ur}")
            await ctx.send(embed=embedZ)


#Dodge

    @commands.command(aliases=["Dodge", "DODGE"])
    async def dodge(self, ctx, user: discord.User = None, *, Notes=None):
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://kawaii.red/api/gif/dodge/token={kawaii_token}') as r:
                js = await r.json()
                ur=str(js["response"])

        if not user:
            em = discord.Embed(description=f"{ctx.author.mention} dodges you", color = 0x000000)
            em.set_image(url=f"{ur}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.author.mention} dodges {user.mention}", color = 0x000000)
        embed.set_image(url=f"{ur}")
        
        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.author.mention} dodges {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{ur}")
            await ctx.send(embed=embedZ)


#Facepalm

    @commands.command(aliases=["Facepalm", "FACEPALM", "FP", "Fp", "fp"])
    async def facepalm(self, ctx, user: discord.User = None, *, Notes=None):
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://kawaii.red/api/gif/facepalm/token={kawaii_token}') as r:
                js = await r.json()
                ur=str(js["response"])

        if not user:
            em = discord.Embed(description=f"{ctx.author.mention} facepalms at you", color = 0x000000)
            em.set_image(url=f"{ur}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.author.mention} facepalms at {user.mention}", color = 0x000000)
        embed.set_image(url=f"{ur}")
        
        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.author.mention} facepalms at {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{ur}")
            await ctx.send(embed=embedZ)


#fbi

    @commands.command(aliases=["Fbi", "FBI"])
    async def fbi(self, ctx, user: discord.User = None, *, Notes=None):
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://kawaii.red/api/gif/fbi/token={kawaii_token}') as r:
                js = await r.json()
                ur=str(js["response"])

        if not user:
            em = discord.Embed(description=f"{ctx.author.mention} was raided by fbi", color = 0x000000)
            em.set_image(url=f"{ur}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.author.mention} raids {user.mention} with fbi", color = 0x000000)
        embed.set_image(url=f"{ur}")
        
        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.author.mention} raids {user.mention} with fbi, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{ur}")
            await ctx.send(embed=embedZ)


#fight

    @commands.command(aliases=["Fight", "FIGHT"])
    async def fight(self, ctx, user: discord.User = None, *, Notes=None):
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://kawaii.red/api/gif/fight/token={kawaii_token}') as r:
                js = await r.json()
                ur=str(js["response"])

        if not user:
            em = discord.Embed(description=f"{ctx.author.mention} is fighting with themselve", color = 0x000000)
            em.set_image(url=f"{ur}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.author.mention} is fighting with {user.mention}", color = 0x000000)
        embed.set_image(url=f"{ur}")
        
        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.author.mention} is fighting with {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{ur}")
            await ctx.send(embed=embedZ)


#laugh

    @commands.command(aliases=["Laugh", "LAUGH"])
    async def laugh(self, ctx, user: discord.User = None, *, Notes=None):
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://kawaii.red/api/gif/laugh/token={kawaii_token}') as r:
                js = await r.json()
                ur=str(js["response"])

        if not user:
            em = discord.Embed(description=f"{ctx.author.mention} is laughing at you", color = 0x000000)
            em.set_image(url=f"{ur}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.author.mention} is laughing at {user.mention}", color = 0x000000)
        embed.set_image(url=f"{ur}")
        
        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.author.mention} is laughing at {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{ur}")
            await ctx.send(embed=embedZ)


#mad

    @commands.command(aliases=["Mad", "MAD"])
    async def mad(self, ctx, user: discord.User = None, *, Notes=None):
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://kawaii.red/api/gif/mad/token={kawaii_token}') as r:
                js = await r.json()
                ur=str(js["response"])

        if not user:
            em = discord.Embed(description=f"{ctx.author.mention} is mad at you", color = 0x000000)
            em.set_image(url=f"{ur}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.author.mention} is mad at {user.mention}", color = 0x000000)
        embed.set_image(url=f"{ur}")
        
        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.author.mention} is mad at {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{ur}")
            await ctx.send(embed=embedZ)


#nosebleed

    @commands.command(aliases=["Nosebleed", "NOSEBLEED"])
    async def nosebleed(self, ctx, user: discord.User = None, *, Notes=None):
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://kawaii.red/api/gif/nosebleed/token={kawaii_token}') as r:
                js = await r.json()
                ur=str(js["response"])

        if not user:
            em = discord.Embed(description=f"{ctx.author.mention} is having nosebleed", color = 0x000000)
            em.set_image(url=f"{ur}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.author.mention} is having nosebleed for {user.mention}", color = 0x000000)
        embed.set_image(url=f"{ur}")
        
        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.author.mention} is having nosebleed for {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{ur}")
            await ctx.send(embed=embedZ)


#peek

    @commands.command(aliases=["Peek", "PEEK"])
    async def peek(self, ctx, user: discord.User = None, *, Notes=None):
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://kawaii.red/api/gif/peek/token={kawaii_token}') as r:
                js = await r.json()
                ur=str(js["response"])

        if not user:
            em = discord.Embed(description=f"{ctx.author.mention} is peeking at you", color = 0x000000)
            em.set_image(url=f"{ur}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.author.mention} is peeking at {user.mention}", color = 0x000000)
        embed.set_image(url=f"{ur}")
        
        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.author.mention} is peeking at {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{ur}")
            await ctx.send(embed=embedZ)



#protect

    @commands.command(aliases=["Protect", "PROTECT"])
    async def protect(self, ctx, user: discord.User = None, *, Notes=None):
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://kawaii.red/api/gif/protect/token={kawaii_token}') as r:
                js = await r.json()
                ur=str(js["response"])

        if not user:
            em = discord.Embed(description=f"{ctx.author.mention} is protecting you", color = 0x000000)
            em.set_image(url=f"{ur}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.author.mention} is protecting {user.mention}", color = 0x000000)
        embed.set_image(url=f"{ur}")
        
        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.author.mention} is protecting {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{ur}")
            await ctx.send(embed=embedZ)


#salute

    @commands.command(aliases=["Salute", "SALUTE"])
    async def salute(self, ctx, user: discord.User = None, *, Notes=None):
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://kawaii.red/api/gif/salute/token={kawaii_token}') as r:
                js = await r.json()
                ur=str(js["response"])

        if not user:
            em = discord.Embed(description=f"{ctx.author.mention} is giving you a salute", color = 0x000000)
            em.set_image(url=f"{ur}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.author.mention} is saluting at {user.mention}", color = 0x000000)
        embed.set_image(url=f"{ur}")
        
        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.author.mention} is saluting at {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{ur}")
            await ctx.send(embed=embedZ)


#Scream

    @commands.command(aliases=["Scream", "SCREAM"])
    async def scream(self, ctx, user: discord.User = None, *, Notes=None):
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://kawaii.red/api/gif/scream/token={kawaii_token}') as r:
                js = await r.json()
                ur=str(js["response"])

        if not user:
            em = discord.Embed(description=f"{ctx.author.mention} is screaming at you", color = 0x000000)
            em.set_image(url=f"{ur}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.author.mention} is screaming at {user.mention}", color = 0x000000)
        embed.set_image(url=f"{ur}")
        
        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.author.mention} is screaming at {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{ur}")
            await ctx.send(embed=embedZ)


#Shocked

    @commands.command(aliases=["Shocked", "SHOCKED"])
    async def shocked(self, ctx, user: discord.User = None, *, Notes=None):
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://kawaii.red/api/gif/shocked/token={kawaii_token}') as r:
                js = await r.json()
                ur=str(js["response"])

        if not user:
            em = discord.Embed(description=f"{ctx.author.mention} is shocked at you", color = 0x000000)
            em.set_image(url=f"{ur}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.author.mention} is shocked at {user.mention}", color = 0x000000)
        embed.set_image(url=f"{ur}")
        
        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.author.mention} is shocked at {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{ur}")
            await ctx.send(embed=embedZ)


#shrug

    @commands.command(aliases=["Shrug", "SHRUG"])
    async def shrug(self, ctx, user: discord.User = None, *, Notes=None):
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://kawaii.red/api/gif/shrug/token={kawaii_token}') as r:
                js = await r.json()
                ur=str(js["response"])

        if not user:
            em = discord.Embed(description=f"{ctx.author.mention} is shrugging at you", color = 0x000000)
            em.set_image(url=f"{ur}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.author.mention} is shrugging at {user.mention}", color = 0x000000)
        embed.set_image(url=f"{ur}")
        
        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.author.mention} is shrugging at {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{ur}")
            await ctx.send(embed=embedZ)


#sleepy

    @commands.command(aliases=["Sleepy", "SLEEPY"])
    async def sleepy(self, ctx, user: discord.User = None, *, Notes=None):
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://kawaii.red/api/gif/sleepy/token={kawaii_token}') as r:
                js = await r.json()
                ur=str(js["response"])

        if not user:
            em = discord.Embed(description=f"{ctx.author.mention} is sleepy", color = 0x000000)
            em.set_image(url=f"{ur}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.author.mention} is sleepy", color = 0x000000)
        embed.set_image(url=f"{ur}")
        
        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.author.mention} is sleepy, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{ur}")
            await ctx.send(embed=embedZ)


#smile

    @commands.command(aliases=["Smile", "SMILE"])
    async def smile(self, ctx, user: discord.User = None, *, Notes=None):
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://kawaii.red/api/gif/smile/token={kawaii_token}') as r:
                js = await r.json()
                ur=str(js["response"])

        if not user:
            em = discord.Embed(description=f"{ctx.author.mention} is smiling at you", color = 0x000000)
            em.set_image(url=f"{ur}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.author.mention} is smiling at {user.mention}", color = 0x000000)
        embed.set_image(url=f"{ur}")
        
        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.author.mention} is smiling at {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{ur}")
            await ctx.send(embed=embedZ)


#stare

    @commands.command(aliases=["Stare", "STARE"])
    async def stare(self, ctx, user: discord.User = None, *, Notes=None):
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://kawaii.red/api/gif/stare/token={kawaii_token}') as r:
                js = await r.json()
                ur=str(js["response"])

        if not user:
            em = discord.Embed(description=f"{ctx.author.mention} is staring at you", color = 0x000000)
            em.set_image(url=f"{ur}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.author.mention} is staring at {user.mention}", color = 0x000000)
        embed.set_image(url=f"{ur}")
        
        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.author.mention} is staring at {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{ur}")
            await ctx.send(embed=embedZ)


#tickle

    @commands.command(aliases=["Tickle", "TICKLE"])
    async def tickle(self, ctx, user: discord.User = None, *, Notes=None):
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://kawaii.red/api/gif/tickle/token={kawaii_token}') as r:
                js = await r.json()
                ur=str(js["response"])

        if not user:
            em = discord.Embed(description=f"{ctx.author.mention} is tickling at you", color = 0x000000)
            em.set_image(url=f"{ur}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.author.mention} is tickling {user.mention}", color = 0x000000)
        embed.set_image(url=f"{ur}")
        
        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.author.mention} is ticklng {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{ur}")
            await ctx.send(embed=embedZ)


#triggered

    @commands.command(aliases=["Triggered", "TRIGGERED"])
    async def triggered(self, ctx, user: discord.User = None, *, Notes=None):
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://kawaii.red/api/gif/triggered/token={kawaii_token}') as r:
                js = await r.json()
                ur=str(js["response"])

        if not user:
            em = discord.Embed(description=f"{ctx.author.mention} is triggered at you", color = 0x000000)
            em.set_image(url=f"{ur}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.author.mention} is triggered at {user.mention}", color = 0x000000)
        embed.set_image(url=f"{ur}")
        
        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.author.mention} is triggered at {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{ur}")
            await ctx.send(embed=embedZ)


#wink

    @commands.command(aliases=["Wink", "WINK"])
    async def wink(self, ctx, user: discord.User = None, *, Notes=None):
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://kawaii.red/api/gif/wink/token={kawaii_token}') as r:
                js = await r.json()
                ur=str(js["response"])

        if not user:
            em = discord.Embed(description=f"{ctx.author.mention} is winking at you", color = 0x000000)
            em.set_image(url=f"{ur}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.author.mention} is winking at {user.mention}", color = 0x000000)
        embed.set_image(url=f"{ur}")
        
        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.author.mention} is winking at {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{ur}")
            await ctx.send(embed=embedZ)


#wiggle

    @commands.command(aliases=["Wiggle", "WIGGLE"])
    async def wiggle(self, ctx, user: discord.User = None, *, Notes=None):
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://kawaii.red/api/gif/wiggle/token={kawaii_token}') as r:
                js = await r.json()
                ur=str(js["response"])

        if not user:
            em = discord.Embed(description=f"{ctx.author.mention} is wiggling at you", color = 0x000000)
            em.set_image(url=f"{ur}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.author.mention} is wiggling at {user.mention}", color = 0x000000)
        embed.set_image(url=f"{ur}")
        
        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.author.mention} is wiggling at {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{ur}")
            await ctx.send(embed=embedZ)



#Yeet

    @commands.command(aliases=["Yeet", "YEET"])
    async def yeet(self, ctx, user: discord.User = None, *, Notes=None):
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://kawaii.red/api/gif/yeet/token={kawaii_token}') as r:
                js = await r.json()
                ur=str(js["response"])

        if not user:
            em = discord.Embed(description=f"{ctx.author.mention} is yeeting you", color = 0x000000)
            em.set_image(url=f"{ur}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.author.mention} is yeeting {user.mention}", color = 0x000000)
        embed.set_image(url=f"{ur}")
        
        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.author.mention} is yeeting {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{ur}")
            await ctx.send(embed=embedZ)


async def setup(bot):
    await bot.add_cog(Roleplay(bot))