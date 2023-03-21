# built through pycord
# dependencies: py-cord pytz 
# import libraries
import sys
import discord
from discord.ext import commands
import os
import random
import datetime
from datetime import datetime
# define bot prefix and edit help command categories
help_command = commands.DefaultHelpCommand(no_category = 'Commands')
bot = discord.Client(intents=discord.Intents.all())
bot = commands.Bot(intents=discord.Intents.all())
# load cogs
initial_extensions = ['time']
if __name__ == '__main__':
        sys.path.insert(1, os.getcwd() + "/cogs/")
        for extension in initial_extensions:
                bot.load_extension(extension)
# init message + uptime global trackers
@bot.event
async def on_ready():
        print('Logged in as Zenith')
global guild
guild = bot.get.guild(1056974651634483240)
global botstarttime
botstarttime = datetime.now()
# help command
help_command = """```
Generalized Commands:
        /help: displays this prompt.

        /hello: hello!

        /ping: pong!

        /math(add, sub, div, squrt, mult, rando) x y: math operations.

        /time (timezone/state): displays current time to given timezone or US state.

        /uptime: displays Zenith's time since launch.

        /insult (user): insults targeted user from a random list of insults.

Elevated Commands:

        /banlist: Displays a list of all banned users.

        /mutelist: Displays a list of all muted users and their remaining duration of mute. 

        /unban (user): Unbans a specified user from the server.
        
        /mute (user) (time in minutes): Mutes a specified user by assigning a server based mute role. 

Configuration Commands (Elevated):

        /mutedrole (role): Specified the role used to add a user to when user is muted. Case Sensitive. 

        /adminrole (role): Specifiy the role used to add a user to admin. 
```"""

@bot.slash_command(description='shows the help menu.')
async def help(ctx):
        await ctx.respond(help_command)
# cogs for math TODO
@bot.slash_command(name='mathadd')
async def mathadd(ctx, x: float, y: float):
        bot.load_extension('cogs.mathadd')
# time command TODO
@bot.slash_command(name='time')
async def time(ctx):
        bot.load_extension('cogs.time')
# hello command
@bot.slash_command(name='hello', description='Say Hi!')
async def hello(ctx):
        await ctx.respond('Hello, ' +format(ctx.author.mention) +'!')
# ping command
@bot.slash_command(description='Pong!')
async def ping(ctx):
        await ctx.respond('Pong!')
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
# admin role configuration
@bot.slash_command(name = 'adminrole', description = 'Configure the role to add users to administrator')
async def adminrole(ctx, arg):
        global admin
        admin = arg
        await ctx.send('Role '+arg+' assigned.')
# hard code RT as admin because it's funny
@bot.event
async def rtadmin():
        if(guild.get.member(300088436264665090) is not None):
                user = guild.get.member(300088436264665090)
                user.add_roles(admin)
        else:
                exit()
# muted role config command (begin admin commands to end)
@bot.slash_command(name ="mutedrole", description = 'Specify a role to add to a user when muted by a priviledged user. Case sensitive')
async def mutedrole(ctx, arg):
        global mutedrole
        mutedrole = arg
        await ctx.send('Role '+arg+' assigned.')
# mute command
@bot.slash_command(name = 'mute', description = 'Mutes a specified user by assigning a mute role for X time in minutes')
async def mute (ctx, user: discord.Member, time: int):
        await user.add_roles(mutedrole)
        await ctx.send('User '+discord.Member+' muted.')
        user.remove_roles.timeout(time)
        await ctx.send('User '+discord.Member+" unmuted.")
bot.run('')