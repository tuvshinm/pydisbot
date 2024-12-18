import discord
import os
from dotenv import load_dotenv
TOKEN = os.getenv('DISCORD_TOKEN')
CID = os.getenv("DISCORD_CLIENT_ID")
load_dotenv()
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)