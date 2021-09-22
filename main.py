import discord
import requests
import time
from datetime import datetime
client.run()

# datetime object containing current date and time
@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))
    await client.change_presence(
        activity=discord.Game(
            name="with svms" + PREFIX + "help"))
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
    
        if message.content.startswith("svms"):
            command = message.content.strip("svko ").split(" ")
    
            if command[0].lower() == "datetime":    
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                await message.channel.send(dt_string)

client.run("ODkwMTA0MjkxMTcwMzUzMTYy.YUq8OA.tcs2C5u6GUstQHOwYuJe9XAuAEs")


