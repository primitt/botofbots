import discord
import requests
import time
from datetime import datetime
from dotenv import load_dotenv
import os
import random
import json
TOKEN = os.getenv('TOKEN')
client = discord.Client()

# datetime object containing current date and time
@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
    
        if message.content.startswith("svms"):
            command = message.content.strip("svms ").split(" ")
    
            if command[0].lower() == "datetime":    
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                await message.channel.send(dt_string)

            if command[0].lower() == "random"
                random.randint("")

client.run(TOKEN)




