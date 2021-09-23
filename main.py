import discord
import requests
import time
from datetime import datetime
from dotenv import load_dotenv
import os
import random as r
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
    
            if command[0].lower() == "datetime": #current date time 
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                await message.channel.send(dt_string)

            if command[0].lower() == "random": #random number gen
                    randomnum = r.randint(command[1])
                    numint = "The random number you chose from the numbers: ", command[1], "are", randomnumber
                    await message.channel.send()
                        await message.channel.send("Sorry, please format your response like this: "
                    + "\n <number>, <number>")
                
            if command[0].lower() == "help":
                await message.channel.send("**Commands** /n"
                + "help <command> - Specific help for a command")
                
            #end of code


                

client.run(TOKEN)




