import discord
import random
from discord import app_commands
from discord.ext import commands

class Info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Info Cog loaded.")

    #Stats

    @commands.command()
    async def stats(self,ctx):
        emb = discord.Embed(title="**STATS**",color=0xFF0000)
        emb.add_field(name="Total Servers",value=str(len(self.bot.guilds)),inline=False)
        emb.add_field(name="Latency(s)",value=str(round(self.bot.latency,3)),inline=False)
        emb.add_field(name=f"{ctx.guild} members",value=f'{ctx.guild.member_count}',inline=False)
        await ctx.send(embed=emb)

    #ServerStats

    @commands.command(pass_context=True)
    async def serverinfo(self,ctx):
        embed = discord.Embed(
            title = str(ctx.guild.name) + " Server Information",
            color = 0x000000
        )
        embed.set_thumbnail(url=str(ctx.guild.icon_url))
        embed.add_field(name="Owner", value=str(ctx.guild.owner), inline=True)      #FIX OWNER PART
        embed.add_field(name="Server ID", value=str(ctx.guild.id), inline=True)
        embed.add_field(name="Region", value=str(ctx.guild.region), inline=True)
        embed.add_field(name="Member Count", value=str(ctx.guild.member_count), inline=True)
        await ctx.send(embed=embed)

    #UserINfo

    @commands.command()
    async def userinfo(self,ctx, member: discord.Member):
        embed = discord.Embed(color=0x000000, timestamp=ctx.message.created_at)

        embed.set_author(name=f"User Info - {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"REquested by {ctx.author}", icon_url=ctx.author.avatar_url)

        embed.add_field(name="ID:", value=member.id)
        embed.add_field(name="Guild name:", value=member.display_name)

        embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %#d, %B %Y, %I:%M %p UTC"))
        embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %#d, %B %Y, %I:%M %p UTC"))

async def setup(bot):
    await bot.add_cog(Info(bot))