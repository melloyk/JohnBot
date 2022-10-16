import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('JOHN_TOKEN')
GUILD = os.getenv('GUILD')

intents = discord.Intents.all()
intents.presences = False

client = discord.Client(intents=intents)

@client.event
async def on_ready():
	guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
	print(
		f'{client.user} is connected to the following guild:\n'
		f'{guild.name} (id: {guild.id})'
	)
	
	members = '\n - '.join([member.name for member in guild.members])
	print(f'Guild Members:\n - {members}')

client.run(TOKEN)
