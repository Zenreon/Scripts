# import libraries
from asyncio import sleep
import math
import discord
from discord.ext import commands
import os
import random
import asyncio
import datetime, time


# define bot prefix

bot = commands.Bot(command_prefix='>>')

# init message

@bot.event
async def on_ready():
        print('Logged in as Zenith')

# basic hello response

@bot.command(pass_context=True)
async def hello(ctx):
        await ctx.send('Hello, ' +format(ctx.author.mention) +'!')

# >>help output

@bot.command(pass_context=True)
async def commands(ctx):
        await ctx.send("""I'm Zenith, a bot made for small-case uses. Written in python3 by Zenreon#3279. 
**Prefix:** ``>>``
``
commands : Lists this text.
hello : Responds "Hello!"
mathadd num1 num2
mathsub num1 num2
mathmult num1 num2
mathdiv num1 num2 (num1/num2)
mathsqrt num1
mathrand num1 num2
uptime : Displays total uptime
time : Displays current CDT date and time``
        """)

# mentions new user join

@bot.command(pass_context=True)
async def joined(ctx, member: discord.Member):
        """Mentions new member"""
        await ctx.send('{0.name} joined in {0.joined_at}'.format(member))

# math functions for calculations

def add(n: float, n2: float):
	return n + n2

def sub(n: float, n2: float):
	return n - n2

def div(n: float, n2: float):
	return n / n2

def sqrt(n: float):
	return math.sqrt(n)

def mult(n: float, n2: float):
	return n * n2

def rand(n: int, n2: int):
        return random.randint(n, n2)
# end of math functions

# bot commands for math functions

@bot.command(pass_context=True)
async def mathadd(ctx, x: float, y: float):
	try:
		
		await ctx.send(add(x, y))

	except:
		pass

@bot.command(pass_context=True)
async def mathsub(ctx, x: float, y: float):
        try:
                result = sub(x, y)
                await ctx.send(result)
        
        except:
                pass

@bot.command(pass_context=True)
async def mathdiv(ctx, x: float, y:float):
        try:
                result = div(x, y)
                await ctx.send(result)
        
        except:
                pass

@bot.command(pass_context=True)
async def mathsqrt(ctx, x:float):
        try:
                result =  sqrt(x)
                await ctx.send(result)
        except:
                pass

@bot.command(pass_context=True)
async def mathmult(ctx, x:float, y:float):
        try:
                result = mult(x, y)
                await ctx.send(result)
        except:
                pass

@bot.command(pass_context=True)
async def mathrand(ctx, x:int, y:int):
        try:
                await ctx.send(x, y)
        except:
                pass

# end of math commands

# time output command

@bot.command(pass_context=True)
async def time(ctx):
        now = datetime.datetime.now()
        showtime = (now.strftime("Current CDT date and time: %Y-%m-%d, %H:%M:%S"))
        try:
                await ctx.send(showtime)
        except:
                pass

# end of time command

# uptime tracker and management commands begin

@bot.command(pass_context=True)
async def uptime(self, ctx):
        current_time = time.time()
        start_time = int(3)
        difference = int(round(current_time - start_time))
        text = str(datetime.timedelta(seconds=difference))
        embed = discord.Embed(colour=0xc8dc6c)
        embed.add_field(name='Uptime', value=text)
        embed.set_footer(text=Zenith)
        try:
                await ctx.send(embed=embed)
        except discord.HTTPException:
                await ctx.send("Current Uptime: " + text)

# end of uptime commands


#bot token

bot.run('ODg4NzgzMzUwOTcyNjg2NDI3.YUXt_w.NbSHbqHua142y7HZfV34lbgadOo')