import baseconfig
from discord.ext import commands
import google.generativeai as genai


genai.configure(api_key=baseconfig.gemini_sdk)
mssg_len=2000
error_mssg='There is an issue with your query, please try again '


class geminibot(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
        self.model=genai.GenerativeModel('gemini-1.5-pro')


    @commands.Cog.listener()
    async def on_message(self,mssg):
        try:
            if mssg.content=='ping gemini':
                await mssg.channel.send('Gemini has been linked')
            elif 'Direct Message' in str(mssg.channel) and not mssg.author.bot:
                response = self.gemini_generate_content(mssg.content)
                dmchannel = await mssg.author.create_dm()
                await dmchannel.send(response.text)
        except Exception as e:
            return error_mssg+str(e)
   
    @commands.command()
    async def pm(self,ctx):
        dmchannel = await ctx.author.create_dm()
        await dmchannel.send('What would you like to know?')


    @commands.command()
    async def ask(self,ctx,question):
        try:
            response = self.gemini_generate_content(question)
            await ctx.send(response)
        except Exception as e:
            await ctx.send(error_mssg + str(e))


    def gemini_generate_content(self,content):
        try:
            response = self.model.generate_content(content, stream=True)
            text = ""
            for chunk in response:
                if chunk.text:
                    text += chunk.text
            return text
        except Exception as e:
            return error_mssg + str(e)
