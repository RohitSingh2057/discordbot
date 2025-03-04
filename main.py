import discord

class Client(discord.Client):
    async def on_ready(self):
        print("Successfully logged on as {}".format(self.user))

intents=discord.Intents.default()
intents.message_content=True

client=Client(intents=intents)
client.run('')