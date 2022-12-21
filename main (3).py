import os
import discord
import random
from datetime import datetime
from variables import responses

TOKEN = os.environ['DISCORD_BOT_TOKEN']

intents = discord.Intents.default()
intents.message_content = True



client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  username = str(message.author).split("#")[0]
  user_message = str(message.content)
  channel = str(message.channel.name)
  print(f"{username}: {user_message}: ({channel})")
  if message.author == client.user:
    return

##########################################################################


  
  if " " in message.content:
      ai_resp = random.choice(responses)
      await message.channel.send(f"{ai_resp}")
      return

client.run(TOKEN)