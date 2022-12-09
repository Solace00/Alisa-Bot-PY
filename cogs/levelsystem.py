import discord
import json
import asyncio
import math
import random
from discord.ext import commands


class LevelSystem(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

       ## self.bot.loop.create_task(self.save())

        with open("user.json", "r") as f:
            self.users = json.load(f)

    
    def level_up(self, author_id):
        current_experience = self.user[author_id]["Experience"]
        current_level = self.user[author_id]["Level"]

        if current_experience >= math.ceil((6 * (current_level ** 4)) / 2.5):
            self.users[author_id]["Leve"] += 1
            return True
        else:
            return False


    async def save(self):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            with open("user.json", "w") as f:
                json.dump(self.users, f, indent = 4)

            await asyncio.sleep(15)

    @commands.Cog.listener()
    async def on_ready(self):
        print("LevelSystem Cog Loaded")


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == self.bot.user.id:
            return

        author_id = str(message.author.id)

        if not author_id in self.users:
            self.user[author_id] = {}
            self.user[author_id]["Level"] = 0
            self.user[author_id]["Experience"] = 0

        random_exp = random.randint(20, 40)
        self.user[author_id]["Experience"] += random_exp

        if self.level_up(author_id):

            level_embed = discord.Embed(title="Grats you leveled up")
            level_embed.add_field(name="Congrats", value=f"{message.author.mention} has just leveled up to level {self.users[author_id]['Level']}!")

            await message.channel.send(embed=level_embed)


    @commands.command(aliases = ["rank", "lvl", "r"])
    async def level(self, ctx, user:discord.User=None):
        if user is None:
            user = ctx.author
        elif user is not None:
            user = user

        level_card = discord.Embed(title= f"{user.name}'s level & Experience")
        level_card.add_field(name="Level:", value=self.users[str(user.id)]["Level"])
        level_card.add_field(name="Experience:", value=self.users[str(user.id)]["Experience"])

        await ctx.send(embed = level_card)

async def setup(bot):
    await bot.add_cog(LevelSystem(bot))
