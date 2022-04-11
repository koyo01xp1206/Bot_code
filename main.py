import discord
import os
import requests
import json
import random

client = discord.Client()

sad_words = ["sad","depressed","unhappy","angry","miserable","depressing"]
starter_encouragements = ["Cheer up",
                         "Hang in there",
                         "You are a great person / bot!"]

def get_quote():
  response = requests.get("http://zenquotes.io/api/random")
  #this returns a random quote from the link
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  #q stands for quote and a stands for author
  return(quote)

@client.event  #this is how you register an event
#these function names below are directly taken from the discord.py library
async def on_ready():  #called when bot starts being used.
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):  
#occurs when message is received, but we write if statement to make sure that the message is not by the bot.
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith("$inspire"):
      quote = get_quote()
      await message.channel.send(quote)

    if any(word in message for word in sad_words):
      await message.channel.send(random.choice(starter_encouragements))
    # if message.content.startswith("$hello"):
    #     #to return a message to the discord, use await
    #     await message.channel.send("Hello!")

      
#We need this following line to run the bot
client.run(os.getenv("TOKEN"))
