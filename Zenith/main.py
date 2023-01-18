#built through pycord
#dependencies: pycord pytz
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
from datetime import timezone
import pytz
from pytz import timezone
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

/time (timezone): displays current time to given timezone.

/uptime: displays Zenith's time since launch.

/insult (user): insults targeted user from a random list of insults.```"""
@bot.slash_command(description='shows the help menu.')
async def help(ctx):
        await ctx.respond(help_command)
#hello command
@bot.slash_command(name='hello', description='Say Hi!')
async def hello(ctx):
        await ctx.respond('Hello, ' +format(ctx.author.mention) +'!')
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
# math commands
@bot.slash_command(description="""Adds two numbers. Usage: mathadd <num1> <num2>""")
async def mathadd(ctx, x:float, y:float):	
	await ctx.respond(add(x, y))\
@bot.slash_command(description="""Divides two numbers. Usage: mathdiv <num1> <num2>.""")
async def mathdiv(ctx, x:float, y:float):
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
@bot.slash_command(description="""Subtracts two numbers. Usage: mathsub <num1> <num2>""")
async def mathsub(ctx, x:float, y:float):
        result = sub(x, y)
        await ctx.respond(result)
# time output command
@bot.slash_command(description='Show date and time on specified timezone.')
async def time(ctx, arg):       
        if (arg == "UTC" or arg == "utc"):
                UTC = pytz.utc
                datetime_utc = datetime.now(UTC)
                await ctx.respond(datetime_utc.strftime("Current UTC date and time:  "+"%Y/%m/%d %H:%M:%S"))
        elif (arg == "CST" or arg == "cst" or arg == 'CDT' or arg == 'cdt' or arg == 'Wisconsin' or arg == 'Illinois' or arg == 'Minnesota' or arg == 'Alabama' or arg == 'Arkansas' or arg == 'Iowa' or arg == 'Louisiana' or arg == 'Missouri' or arg == 'Mississippi' or arg == 'Oklahoma'):
                CST = timezone('US/Central')
                datetime_cst = datetime.now(CST)
                await ctx.respond(datetime_cst.strftime("Current time in "+arg+": "+"%Y/%m/%d %H:%M:%S"))
        elif (arg == "EST" or arg == "est" or arg == 'Connecticut' or arg == 'Delaware' or arg == 'Georgia' or arg == 'Maine' or arg == 'Maryland' or arg == 'Massachusetts' or arg == 'New Hampshire' or arg == 'New Jersey' or arg == 'New York' or arg == 'North Carolina' or arg == 'Ohio' or arg == 'Pennsylvania' or arg == 'Rhode Island' or arg == 'South Carolina' or arg == 'Vermont' or arg == 'Virginia' or arg == 'West Virginia'):
                EST = timezone('US/Eastern')
                datetime_est = datetime.now(EST)
                await ctx.respond(datetime_est.strftime("Current time in "+arg+": "+"%Y/%m/%d %H:%M:%S"))
        elif (arg == "MST" or arg == "mst" or arg == 'Arizona' or arg == 'Colorado' or arg == 'Montana' or arg == 'New Mexico' or arg == 'Utah' or arg == 'Wyoming'):
                MST = timezone('US/Mountain')
                datetime_mst = datetime.now(MST)
                await ctx.respond(datetime_mst.strftime("Current time in "+arg+": "+"%Y/%m/%d %H:%M:%S"))
        elif (arg == "PST" or arg == "pst" or arg == 'PDT' or arg == 'pdt' or arg == 'California' or arg == 'Nevada' or arg =='Washington'):
                PST = timezone('US/Pacific')
                datetime_pst = datetime.now(PST)
                await ctx.respond(datetime_pst.strftime("Current time in "+arg+": "+"%Y/%m/%d %H:%M:%S"))
        elif (arg == "HST" or arg == "hst" or arg == 'Hawaii'):
                HST = timezone('US/Hawaii')
                datetime_hst = datetime.now(HST)
                await ctx.respond(datetime_hst.strftime("Current time in "+arg+": "+"%Y/%m/%d %H:%M:%S"))
        elif (arg == 'AKST' or arg == 'AKDT' or arg == 'Alaska'):
                AKST = timezone('US/Alaska')
                datetime_akst = datetime.now(AKST)
                await ctx.respond(datetime_akst.strftime("Current time in "+arg+": "+"%Y/%m/%d %H:%M:%S"))
        elif (arg == "HAST" or arg == 'hast'):
                HAST = timezone('US/Aleutian')
                datetime_hast = datetime.now(HAST)
                await ctx.respond(datetime_hast.strftime("Current time in "+arg+": "+"%Y/%m/%d %H:%M:%S"))
# states in Eastern/Central
        elif (arg == 'Florida' or arg == 'Indiana' or arg == 'Kentucky' or arg == 'Michigan' or arg == 'Tennessee'):
                await ctx.respond(""+arg+" is in Eastern and Central timezones depending on location within the state.")
# states in Mountain/Pacific
        elif (arg == 'Idaho' or arg == 'Oregon'):
                await ctx.respond(""+arg+" is in Mountain and Pacific timezones depending on location within the state")
# states in Central/Mountain
        elif (arg == 'Kansas' or arg == 'Nebraska' or arg == 'North Dakota' or arg == 'South Dakota' or arg == 'Texas'):
                await ctx.respond(""+arg+" is in Central and Mountain timezones depending on location within the state.")
        else:
                await ctx.respond("Input error. Use any timezone in the US, or give an US state to gather its timezone. Case Sensitive.")
# uptime command
@bot.slash_command(name='uptime', description="""See Zenith's uptime""")
async def uptime(ctx):
        bottimenow = datetime.now()
        await ctx.respond(str(bottimenow - botstarttime))      
# insult command
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

bot.run('')
#test commit