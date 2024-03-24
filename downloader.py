import discord
import aiohttp
import os

TOKEN = 'Replace with ur token'

intents = discord.Intents.default()
intents.messages = True # Enable message events

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}!')
        channel = self.get_channel(Channel_ID_Here)
        if channel:
            await self.download_attachments(channel)

    async def download_attachments(self, channel):
        messages = []
        async for message in channel.history(limit=message limit_here):
            messages.append(message)
        
        for message in messages:
            if message.attachments:
                for attachment in message.attachments:
                    await self.download_file(attachment.url, attachment.filename)

    async def download_file(self, url, filename):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    with open(os.path.join('downloads', filename), 'wb') as f:
                        f.write(await response.read())
                    print(f'Downloaded {filename}')

client = MyClient(intents=intents)
client.run(TOKEN)
