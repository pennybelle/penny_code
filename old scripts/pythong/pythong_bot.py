
import discord
import asyncio

TOKEN = 'MTA4MTQwMjA4NTY2NjQ3MTk5OA.G5T9tj.MLnBIM_FDGhqTDkq0AM42_0vrLn89HYdcxSJQA'
client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'{client.user} has connected!')

client.run(TOKEN)
