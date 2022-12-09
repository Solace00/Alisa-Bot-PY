import discord
import random
from discord import app_commands
from discord.ext import commands
from time import sleep as delay
from typing import Optional

class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Fun Cog loaded.")

    #Avatar

    @commands.command(aliases=["pfp", "av"])
    async def avatar(self, ctx, member: discord.Member=None):
        if not member:
            member = ctx.author
        embed = discord.Embed(title=f"Avatar Link!", url=str(member.avatar.url), color=discord.Color.teal())
        embed.set_image(url=str(member.avatar.url))
        await ctx.send(embed=embed) ##, mention_author=False

    #8ball

    @commands.command(aliases=["8ball", "8b"])
    async def eightball(self, ctx, *, question):
        response = ["It is certain.", "It is decidedly so.", "without a doubt", "Yes, Definitely.",
        "you may rely on it.", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Reply haze, try again",
        "Better not tell you now", "cannot predict now.", "Don't count on it.", "My reply is a no.", "Very doubtful"]
        await ctx.send(f':8ball: Question: {question}\n :8ball: Answer: {random.choice(response)}')

    #ROCK PAPER SCISSOR
    @commands.command()
    async def rps(self, ctx, player: Optional[str]):
        H = ["ROCK", "PAPER", "SCISSOR"]
        bot_ = random.choice(H)
        user = player.upper()
        if user == "ROCK" or user == "PAPER" or user == "SCISSOR" or user == "SCISSORS":
            await ctx.send(
                f"{ctx.message.author.mention} : ``{user}``    vs    {self.bot.user.mention} : ``{bot_}``"
            )
            if user == bot_:
                await ctx.send("lol its a tie")
            elif (
                (user == "ROCK" and bot_ == "SCISSOR")
                or (user == "PAPER" and bot_ == "ROCK")
                or ((user == "SCISSOR" or user == "SCISSORS") and bot_ == "PAPER")
            ):
                await ctx.send("you win")
            else:
                await ctx.send("bot wins")
        else:
            await ctx.send("You baka pick\n``rock``  or  ``paper``  or  ``scissor``?")
    

    #COIN TOSS

    @commands.command()
    async def toss(self, ctx, side=""):
        side = side.lower()
        possibilities = ["heads", "tails"]
        head = ["h", "heads", "head"]
        tail = ["t", "tails", "tail"]
        await ctx.send("tossing coin . . .")
        delay(0.5)
        tossed = random.choice(possibilities)
        await ctx.send(f"Its **{tossed}**")

        if side != "":
            if side in head:
                side = "heads"
            elif side in tail:
                side = "tails"

            if side == tossed:
                await ctx.send("You won")
            else:
                await ctx.send("You lost")

    # ROLL DIE
    
    @commands.command()
    async def roll(self, ctx):
        await ctx.send("rolling dice . . .")
        delay(0.5)
        await ctx.send(f"rolled a **{random.choice(range(1,7))}**")

async def setup(bot):
    await bot.add_cog(Fun(bot))