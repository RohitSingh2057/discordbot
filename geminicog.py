import baseconfig
from discord.ext import commands
import google.generativeai as aibot

aibot.configure(api_key=baseconfig.gemini_sdk)
mssg_len=2000
error_mssg='There is an issue with your query, please try again'

class geminibot(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
        self.model=aibot.GenerativeModel('gemini-pro')

    @commands.Cog.listener()
    async def on_message(self,mssg):
        try:
            if mssg.content=='ping gemini':
                await mssg.channel.send('Gemini has been linked')
        except Exception as e:
            return error_mssg+str(e)