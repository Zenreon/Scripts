import discord
import asyncio
import datetime 
from datetime, time import datetime
from discord.ext import commands
import os

client = discord.Client()

# joindate function, calls on datetime library for string strftime

@client.event
async def joindate(ctx, member: discord.Member):
    created_at = member.created_at.strftime('&b &d, &Y')
    try:
        await ctx.send(created_at)
    except:
        pass


# end joindate function
