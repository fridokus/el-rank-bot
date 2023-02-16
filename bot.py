#!/usr/bin/python3
import discord

TOKEN = open('.token.txt').read().split()[0]
intents = discord.Intents.all()
client = discord.Client(intents=intents)

bot = discord.ext.commands.Bot(command_prefix='!')

@bot.command()
async def rank(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)

@client.event
async def on_ready(): print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    u = str(message.author).split("#")[0]
    m = str(message.content)

    print(f'Message {m} by {u}')

    if message.author == client.user: return

    if m.lower() in ["tjena", "hej"]:
        await message.channel.send(f'Tjenixen, {u}')
    elif m.lower() == "bye":
        await message.channel.send(f'Bye {u}')
    if 'zoler' in m.lower():
        await message.add_reaction('🦊')
    if 'pontus' in m.lower():
        await message.add_reaction('🔢')

client.run(TOKEN)
