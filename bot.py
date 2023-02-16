#!/usr/bin/python3
import os

import discord

TOKEN = open('.token.txt').read().split()[0]
print(TOKEN)
intents = discord.Intents.all()
print(intents)
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    user_message = str(message.content)

    print(f'Message {user_message} by {username}')

    if message.author == client.user: return

    if user_message.lower() == "hello" or user_message.lower() == "hi":
        await message.channel.send(f'Hello {username}')
        return
    elif user_message.lower() == "bye":
        await message.channel.send(f'Bye {username}')

client.run(TOKEN)
