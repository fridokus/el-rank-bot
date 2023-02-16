#!/usr/bin/python3
import discord
from discord.ext import commands
from requests_html import HTMLSession

TOKEN = open('.token.txt').read().split()[0]
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name='rank')
async def rank(ctx, arg):
    if '#' in arg: user = arg.replace('#', '-')
    elif '-' in arg: user = arg
    else:
        ctx.send('Get the rank of a user using this format: PA#240')
    session = HTMLSession()
    r = session.get('https://slippi.gg/user/' + user)
    r.html.render()
    print(r)
    await ctx.send(arg)

@bot.command(name='add')
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)

@bot.event
async def on_ready(): print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    u = str(message.author).split("#")[0]
    m = str(message.content)

    print(f'Message {m} by {u}')

    if message.author == bot.user: return

    if m.lower() in ["tjena", "hej"]:
        await message.channel.send(f'Tjenixen, {u}')
    elif m.lower() == "bye":
        await message.channel.send(f'Bye {u}')
    if 'zoler' in m.lower():
        await message.add_reaction('🦊')
    if 'pontus' in m.lower():
        await message.add_reaction('🔢')

bot.run(TOKEN)
