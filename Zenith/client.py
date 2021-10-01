import discord
import asyncio
import datetime 
from datetime import time
from discord.ext import commands
import os

client = discord.Client()

# joindate function, calls on datetime library for string strftime

@client.command()
async def joindate(ctx, member: discord.member):
    date_format = "%a, %d %b %Y %I:%M %p"
    created_at = member.created_at.strftime("%b %d, %Y")
    try:
        await ctx.send('User created at %M %d %y')
    except:
        pass
        
# end joindate function
