import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('JOHN_TOKEN')

intents = discord.Intents.all()
intents.members = False
intents.presences = False

client = discord.Client(intents=intents)

@client.event
async def on_ready():
	for guild in client.guilds:
		print(f'{client.user} is connected to the following guild:\n')
		print(f'{guild.name}(id: {guild.id})')

		members = '\n - '.join([member.name for member in guild.members])
    	print(f'Guild Members:\n - {members}')

	print(f'{client.user} has connected to Discord!')

client.run(TOKEN)
