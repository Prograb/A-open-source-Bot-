import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='YOUR PREFIX')
                   
                   
@bot.command()
  async def hello(ctx):
        await ctx.send('Hello this is a bot with open source code')
                       
                       
                       
                   @bot.command()
                       async def Ping(ctx):
                       await ctx.send('Pong')
                  
                bot.run('your token bot')
