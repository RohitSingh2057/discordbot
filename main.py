import discord
import baseconfig
from discord.ext import commands
import asyncio
from geminicog import geminibot

class Client(discord.Client):
    async def on_ready(self):
        print("Successfully logged on as {}".format(self.user))

intents = discord.Intents.all()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix="!",intents=intents,help_command=None)

@bot.event
async def on_ready():
    print("The bot is now online.")

@bot.command()
async def unloadGemini(ctx):
    await bot.remove_cog('GeminiBot')

@bot.command()
async def reloadGemini(ctx):
    await bot.add_cog(geminibot(bot))

async def startcogs():
    await bot.add_cog(geminibot(bot))

asyncio.run(startcogs())
bot.run(baseconfig.discord_sdk)