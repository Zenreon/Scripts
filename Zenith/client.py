import discord
import asyncio
from discord.ext import commands
import os

client = discord.Client()

# joindate function

@client.event
async def joindate(ctx, member: discord.Member):
    created_at = member.created_at.strftime('&b &d, &Y')
    try:
        await ctx.send(created_at)
    except:
        pass


# end joindate function