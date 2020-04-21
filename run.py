# encoding: utf-8
import os
from mcstatus import MinecraftServer
import discord
from discord.ext import commands

MC_SERVER_ENDPOINT = '127.0.0.1:25565'
MC_BOT_OAUTH20_TOKEN = os.getenv('MC_BOT_OAUTH20_TOKEN')
if MC_BOT_OAUTH20_TOKEN is None:
    exit(-1)

server = MinecraftServer.lookup(MC_SERVER_ENDPOINT)
bot = commands.Bot(command_prefix='@')

@bot.event
async def on_ready():
    print('init completed.')
    print('mention: '+bot.user.mention)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return 
    # print('>'+message.content+'<')
    if message.content in [ bot.user.mention, f'<@!{bot.user.id}>']:
        try:
            players = server.status().players.sample
            print(players)
            if players == None:
                await message.channel.send(content='現在沒人在玩唷 uwu)/')
            else:
                s = '正在玩的人有: \r\n'
                for p in server.status().players.sample:
                    s += p.name + '\r\n'
                await message.channel.send(content=s)
        
        except:
            await message.channel.send(content='伺服器可能沒開 \\(qwq')
    #if message.content == bot.user.name:
    #    await message.channel.send('???')

#@bot.command()
#async def 誰在玩(ctx):
#    try:
#        s = ''
#        for p in server.status().players.sample:
#            s += p.name + '\r\n'
    
#        if len(s) == 0:
#            await ctx.send(content='現在沒人在玩唷 uwu)/')
#        else:
#            await ctx.send(content=s)
#    except:
#        await ctx.send(content='伺服器可能沒開 \(qwq')
    

bot.run(MC_BOT_OAUTH20_TOKEN)