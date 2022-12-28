#built through pycord 
#import libraries
from asyncio import sleep
import math
import discord
from discord import default_permissions
from discord.ext import commands
import os
import random
import asyncio
import datetime, time
from datetime import datetime
from datetime import timedelta
#define bot prefix and edit help command categories
help_command = commands.DefaultHelpCommand(no_category = 'Commands')
bot = discord.Client(intents=discord.Intents.all())
bot = commands.Bot(intents=discord.Intents.all())
#init message + uptime global trackers
@bot.event
async def on_ready():
        print('Logged in as Zenith')
global botstarttime
botstarttime = datetime.now()
#help command
help_command = """```
/help: displays this prompt.

/hello: hello!

/ping: pong!

/math(add, sub, div, squrt, mult, rando) x y: math operations.

/time (timezone/state/country): shows local time to specified location.

/uptime: displays Zenith's time since launch.

/insult (user): insults targeted user from a random list of insults.```"""
@bot.slash_command(description='shows the help menu.')
async def help(ctx):
        await ctx.respond(help_command)
#hello command
@bot.slash_command(name='hello', description='Say Hi!')
async def hello(ctx):
        await ctx.respond('Hello, ' +format(ctx.author.mention) +'!')
#joindate command TODO

#ping command
@bot.slash_command(description='Pong!')
async def ping(ctx):
        await ctx.respond('Pong!')
#math functions 
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
def rando(n: int, n2: int):
        return random.randint(n, n2)
#math commands
@bot.slash_command(description="""Adds two numbers. Usage: mathadd <num1> <num2>""")
async def mathadd(ctx, x: float, y: float):	
	await ctx.respond(add(x, y))\
@bot.slash_command(description="""Subtracts two numbers. Usage: mathsub <num1> <num2>""")
async def mathsub(ctx, x: float, y: float):
        result = sub(x, y)
        await ctx.respond(result)
@bot.slash_command(description="""Divides two numbers. Usage: mathdiv <num1> <num2>.""")
async def mathdiv(ctx, x: float, y:float):
        result = div(x, y)
        await ctx.respond(result)
@bot.slash_command(description="""Takes the square root of any float. Usage: mathsqrt <num1>""")
async def mathsqrt(ctx, x:float):
        result =  sqrt(x)
        await ctx.respond(result)
@bot.slash_command(description="""Multiplies two numbers. Usage: mathmult <num1> <num2>""")
async def mathmult(ctx, x:float, y:float):
        result = mult(x, y)
        await ctx.respond(result)
@bot.slash_command(description="""Random value between two numbers. Usage: mathrando <num1> <num2>""")
async def mathrando(ctx, x:float, y:float):
        result = rando(x, y)
        await ctx.respond(x, y)
#time output command
@bot.slash_command(name='time', description='show CDT date and time.')
async def time(ctx):
        now = datetime.now()
        showtime = (now.strftime("Current CDT date and time: %Y-%m-%d, %H:%M:%S"))
        await ctx.respond(showtime)
#uptime command
@bot.slash_command(name='uptime', description="""See Zenith's uptime""")
async def uptime(ctx):
        bottimenow = datetime.now()
        await ctx.respond(str(bottimenow - botstarttime))      
#insult command
@bot.slash_command(name='insult', description='Insult a specified user. Usage: insult <user>')
async def insult(ctx, arg):
        insultee = arg
        insultlist = [
        'Fuck you, '+insultee+'!', 
        'You smell like a sack of shit, '+insultee+'!',
        'Imagine being as big of a loser as '+insultee+'!',
        'There are nearly 10 million particles in the universe that we can observe, '+insultee+"""'s mama took the ugly ones and put them into one nerd!"""]
        x = random.choice(insultlist)
        await ctx.respond(x)

<<<<<<< HEAD
bot.run('ODg4NzgzMzUwOTcyNjg2NDI3.GJZ2Q4.ErXUSgpmfspsj3i_zDmTU9LGyWJe7dZD8uAdW4')
=======
bot.run('')
>>>>>>> 7f1071a2bc444f924f13e261920a2515ca0ef517
