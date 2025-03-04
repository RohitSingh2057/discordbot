import discord
import baseconfig
from discord.ext import commands

class Client(discord.Client):
    async def on_ready(self):
        print("Successfully logged on as {}".format(self.user))

intents=discord.Intents.default()
intents.message_content=True
bot=commands.Bot(command_prefix='!',intents=intents,help_command=None)

@bot.event
async def on_ready():
    print('The bot is now online.')

client=Client(intents=intents)
client.run(baseconfig.discord_sdk)