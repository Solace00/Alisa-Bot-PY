import discord 
import os
import asyncio 
import youtube_dl
from discord import app_commands
from discord.ext import commands
voice_clients= {}
yt_dl_opts={
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
        'restrictfilenames': True,
        'noplaylist': True,
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'logtostderr': False,
        'quiet': True,
        'no_warnings': True,
        'default_search': 'auto',
        'source_address': '0.0.0.0'}
ytdl = youtube_dl.YoutubeDL(yt_dl_opts)
f_opts = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn'}
class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print("Music Cog loaded.")
    @commands.command()
    async def play(self,ctx):
                voice_client= await ctx.message.author.voice.channel.connect()
                voice_clients[voice_client.guild.id]= voice_client
                url = ctx.message.content.split()[1]
                loop = asyncio.get_event_loop()
                data = await loop.run_in_executor(None,lambda : ytdl.extract_info(url,download=False))
                song = data['url']
                player = discord.FFmpegPCMAudio(song,**f_opts)
                voice_clients[ctx.message.guild.id].play(player)
    @commands.command()
    async def pause(self,ctx):
        voice_clients[ctx.message.guild.id].pause()
    @commands.command()
    async def stop(self,ctx):
        voice_clients[ctx.message.guild.id].stop()
        await voice_clients[ctx.message.guild.id].disconnect()
    @commands.command()
    async def resume(self,ctx):
        voice_clients[ctx.message.guild.id].resume()
async def setup(bot):
    await bot.add_cog(Music(bot))
        
