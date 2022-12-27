#sdependencies: discord.py
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
bot = commands.Bot(intents=discord.Intents.all(), command_prefix='>>', help_command=help_command)
#init message + uptime global trackers
@bot.event
async def on_ready():
        print('Logged in as Zenith')
global botstarttime
botstarttime = datetime.now()
#slash help command
@bot.slash_command(name='help', description='shows the help menu.', guild_id=888782260852113438)
async def help(ctx):
        await ctx.respond(help_command)
#basic hello response
@bot.slash_command(name='hello', description='Say Hi!')
async def hello(ctx):
        await ctx.respond('Hello, ' +format(ctx.author.mention) +'!')
#joindate command TODO

#ping command for checking responses
@bot.slash_command(name='ping', description='Pong!')
async def ping(ctx):
        await ctx.respond('Pong!')
#math functions for calculations
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
#bot commands for math functions
@bot.command(pass_context=True, brief="""Adds two numbers. Usage: mathadd <num1> <num2>""")
async def mathadd(ctx, x: float, y: float):
	try:
		
		await ctx.send(add(x, y))

	except:
		pass
@bot.command(pass_context=True, brief="""Subtracts two numbers. Usage: mathsub <num1> <num2>""")
async def mathsub(ctx, x: float, y: float):
        try:
                result = sub(x, y)
                await ctx.send(result)
        
        except:
                pass
@bot.command(pass_context=True, brief="""Divides two numbers. Usage: mathdiv <num1> <num2>.""")
async def mathdiv(ctx, x: float, y:float):
        try:
                result = div(x, y)
                await ctx.send(result)
        
        except:
                pass
@bot.command(pass_context=True, brief="""Takes the square root of any float. Usage: mathsqrt <num1>""")
async def mathsqrt(ctx, x:float):
        try:
                result =  sqrt(x)
                await ctx.send(result)
        except:
                pass
@bot.command(pass_context=True, brief="""Multiplies two numbers. Usage: mathmult <num1> <num2>""")
async def mathmult(ctx, x:float, y:float):
        try:
                result = mult(x, y)
                await ctx.send(result)
        except:
                pass
@bot.command(pass_context=True, brief="""Random value between two numbers. Usage: mathrando <num1> <num2>""")
async def mathrando(ctx, x:float, y:float):
        try:
                result = rando(x, y)
                await ctx.send(x, y)
        except:
                pass
#time output command
@bot.slash_command(name='time', description='show CDT date and time.')
async def time(ctx):
        now = datetime.now()
        showtime = (now.strftime("Current CDT date and time: %Y-%m-%d, %H:%M:%S"))
        try:
                await ctx.respond(showtime)
        except:
                pass
#uptime command
@bot.slash_command(name='uptime', description="""See Zenith's uptime""")
async def uptime(ctx):
        bottimenow = datetime.now()
        await ctx.respond(str(bottimenow - botstarttime))      
#taunt command
@bot.slash_command(name='taunt', description='Get an insult thrown at you.')
async def taunt(ctx):
        tauntlist = [
        'Fuck you, ' +format(ctx.author.mention)+'!', 
        'You smell like a sack of shit, '+format(ctx.author.mention)+'!',
        'Imagine being as big of a loser as '+format(ctx.author.mention)+'!',
        'There are nearly 10 million particles in the universe that we can observe, their mama took the ugly ones and put them into '+format(ctx.author.mention)+'.',] 
        try:
                await ctx.respond(random.choice(tauntlist))
        except:
                pass
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
        try:
                await ctx.respond(x)
        except:
                pass

bot.run('')
