from discord.ext import commands
import datetime
from datetime import timezone
import pytz
# define class
class time:
    def __init__(self, bot):
        self.bot = bot
        @commands.slash_command(name = 'time', description = 'Show date and time on specified timezone.')
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
# setup
def setup(bot):
    bot.add_cog(time(bot))