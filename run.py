from mcstatus import MinecraftServer
import discord
from discord.ext import commands

server = MinecraftServer.lookup("127.0.0.1:25565")
bot = commands.Bot(command_prefix='@')

@bot.command()
async def 誰在玩(ctx):
    s = ''
    for p in server.status().players.sample:
        s += p.name + '\r\n'
    await ctx.send(content=s)

bot.run('<your OAuth 2.0 token here>')

input()