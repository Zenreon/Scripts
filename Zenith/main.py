# import libraries
from asyncio import sleep
import math
import discord
from discord.ext import commands
import os
import random
import asyncio
import datetime, time

# define bot prefix and edit help command categories
help_command = commands.DefaultHelpCommand(no_category = 'Commands')
bot = commands.Bot(command_prefix='>>', help_command=help_command)

# init message
@bot.event
async def on_ready():
        print('Logged in as Zenith')

# basic hello response
@bot.command(pass_context=True, brief='Say Hi!')
async def hello(ctx):
        await ctx.send('Hello, ' +format(ctx.author.mention) +'!')

# joindate command 
# TODO: make this work
@bot.command(pass_context=True, brief='See your joindate')
async def joindate(ctx):
        member = message.author
        date_format = "%a, %d %b %Y %I:%M %p"
        try:
                await ctx.send('User '+member+' created at %M %d %Y')
        except:
                pass

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

def rando(n: int, n2: int):
        return random.randint(n, n2)
# end of math functions

# bot commands for math functions
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
# time output command
@bot.command(pass_context=True)
async def time(ctx):
        now = datetime.datetime.now()
        showtime = (now.strftime("Current CDT date and time: %Y-%m-%d, %H:%M:%S"))
        try:
                await ctx.send(showtime)
        except:
                pass
# uptime command TODO: implement



# end of uptime command

# tauntself command
@bot.command(pass_context=True, brief='Get an insult thrown at you.')
async def tauntself(ctx):
        tauntlist = [
        'Fuck you, ' +format(ctx.author.mention)+'!', 
        'You smell like a sack of shit, '+format(ctx.author.mention)+'!',
        'Imagine being as big of a loser as '+format(ctx.author.mention)+'!',
        'There are nearly 10 million particles in the universe that we can observe, their mama took the ugly ones and put them into '+format(ctx.author.mention)+'.',] 
        try:
                await ctx.send(random.choice(tauntlist))
        except:
                pass
# insult command
@bot.command(pass_context=True, brief='Insult a specified user. Usage: insult <user>')
async def insult(ctx, arg):
        insultee = arg
        insultlist = [
        'Fuck you, '+insultee+'!', 
        'You smell like a sack of shit, '+insultee+'!',
        'Imagine being as big of a loser as '+insultee+'!',
        'There are nearly 10 million particles in the universe that we can observe, '+insultee+"""'s mama took the ugly ones and put them into one nerd"""]
        x = random.choice(insultlist)
        try:
                await ctx.send(x)
        except:
                pass
# bot token
bot.run('ODg4NzgzMzUwOTcyNjg2NDI3.YUXt_w.NbSHbqHua142y7HZfV34lbgadOo')
