import random
from discord.ext import commands
import math

class math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
# functions for math cmd
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
def rando(n: float, n2: float):
            return math.random(n, n2)
# math commands
@commands.slash_command(description="""Adds two numbers. Usage: mathadd <num1> <num2>""")
async def mathadd(ctx, x:float, y:float):	
	        await ctx.respond(add(x, y))
@commands.slash_command(description="""Divides two numbers. Usage: mathdiv <num1> <num2>.""")
async def mathdiv(ctx, x:float, y:float):
                result = div(x, y)
                await ctx.respond(result)
@commands.slash_command(description="""Takes the square root of any float. Usage: mathsqrt <num1>""")
async def mathsqrt(ctx, x:float):
                result =  sqrt(x)
                await ctx.respond(result)
@commands.slash_command(description="""Multiplies two numbers. Usage: mathmult <num1> <num2>""")
async def mathmult(ctx, x:float, y:float):
                result = mult(x, y)
                await ctx.respond(result)
@commands.slash_command(description="""Random value between two numbers. Usage: mathrando <num1> <num2>""")
async def mathrando(ctx, x:float, y:float):
                result = rando(x, y)
                await ctx.respond(x, y)
@commands.slash_command(description="""Subtracts two numbers. Usage: mathsub <num1> <num2>""")
async def mathsub(ctx, x:float, y:float):
                result = sub(x, y)
                await ctx.respond(result)

# setup
def setup(bot):
    bot.add_cog(math(bot))