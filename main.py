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


@bot.command(aliases = ["about"])
async def help(ctx):
    MyEmbed = discord.Embed(title = "Commands",
                            description = "These are the Commands that you can use for this bot. Once you are in a private message with the bot you can interact with it normally without issuing commands",
                            color = discord.Color.dark_purple())
    MyEmbed.add_field(name = "!ask", value = "To communicate with gemini, type your questions inside quoatations", inline = False)
    MyEmbed.add_field(name = "!pm", value = "To privately chat with the bot", inline = False)
    MyEmbed.add_field(name = "!sum", value = "To summarize website contents", inline = False)
    await ctx.send(embed = MyEmbed)


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
