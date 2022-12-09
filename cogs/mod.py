import discord
import random
from discord import app_commands
from discord.ext import commands

class Mod(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Mod Cog loaded.")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, count: int):
        await ctx.channel.purge(limit = count)

    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member: discord.Member, reason):
        await ctx.guild.kick(member)

        embed = discord.Embed(title = "Success", color = discord.Color.blurple())
        embed.add_field(name="Kicked:", value=f"{member.mention} has been kicked from the server by {ctx.author.mention}.", inline=False)
        embed.add_field(name="Reason:", value=reason, inline=False)

        await ctx.send(embed)

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member: discord.Member, reason):
        await ctx.guild.ban(member)

        embed = discord.Embed(title = "Success", color = discord.Color.blurple())
        embed.add_field(name="Banned:", value=f"{member.mention} has been Banned from the server by {ctx.author.mention}.", inline=False)
        embed.add_field(name="Reason:", value=reason, inline=False)

        await ctx.send(embed)

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, userid):
        user = discord.Object(id = userid)
        await ctx.guild.unban(user)

        embed = discord.Embed(title = "Success", color = discord.Color.blurple())
        embed.add_field(name="Unbanned:", value=f"<@{userid}> has been Unbanned from the server by {ctx.author.mention}.", inline=False)

        await ctx.send(embed)


    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Error: Missing Required Arguments. You must pass in a whole number to run the clear command.")

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Error: Missing Required Arguments. You must pass in user ID or a @ mention with a reason.")

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Error: Missing Required Arguments. You must pass in user ID or a @ mention with a reason.")

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Error: Missing Required Arguments. You must pass in user ID or a @ mention with a reason.")

async def setup(bot):
    await bot.add_cog(Mod(bot))