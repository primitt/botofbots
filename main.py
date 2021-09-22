import discord
import requests
import time
from datetime import datetime

# datetime object containing current date and time
@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))
    await client.change_presence(
        activity=discord.Game(
            name="with svms" + PREFIX + "help"))
client.run()
# Time and date

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("svms"):
        command = message.content.strip("svko ").split(" ")
    
        if command[0].lower() == "datetime"
        
    now = datetime.now()
 
    print("now =", now)

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    await.message.channel.send(dt_string)
