#!/usr/bin/python3
import discord
from discord.ext import commands
from requests_html import AsyncHTMLSession

TOKEN = open('.token.txt').read().split()[0]
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name='rating')
async def rating(ctx, arg):
    if '#' in arg: user = arg.replace('#', '-')
    elif '-' in arg: user = arg
    else:
        ctx.send('Get the rating of a user using this format: PA#240')
    user = user.lower()
    asession = AsyncHTMLSession()
    r = await asession.get('https://slippi.gg/user/' + user)
    await r.html.arender(timeout=20000)
    rating = float(r.html.find('.css-1rxv754', first=True).text.split(' ')[0])
    ret = user + ' has ' + str(rating) + ' rating. '
    if   rating >= 2800: ret += 'This guy/girl might be the G.O.A.T 🐐'
    elif rating >= 2600: ret += 'This guy is a god ⛪️'
    elif rating >= 2400: ret += 'Better than the best GnW in the world 🏴'
    elif rating >= 2300: ret += 'Shoot for the moon 🌚'
    elif rating >= 2200: ret += 'Don\'t wanna run into this BEAST 🦁'
    elif rating >= 2150: ret += 'This is higher than Pontus will ever get 📈'
    elif rating >= 2100: ret += 'Whoa Daddy! 🧔'
    elif rating >= 2050: ret += 'I guess you play Fox 🦊'
    elif rating >= 2000: ret += 'Diamond BOYS 💎'
    elif rating >= 1900: ret += 'Respectable 🙏'
    elif rating >= 1800: ret += 'Pump the numbers 💹'
    elif rating >= 1700: ret += 'Not bad 🐘'
    elif rating >= 1600: ret += 'Give this guy/girl a gold medal 🥇'
    elif rating >= 1500: ret += 'Git gud 🐅'
    elif rating >= 1400: ret += 'Need more practice against Falco 🐦️'
    elif rating >= 1350: ret += 'Great things start small 🪦'
    elif rating >= 1300: ret += 'You are a hard worker and a beautiful human being 👶'
    elif rating >= 1200: ret += 'Do you know how to wavedash? 🌊'
    elif rating >= 1100: ret += 'Do you know how to CC? 💀'
    elif rating >= 1000: ret += 'Do you know how to L-cancel? 🍂'
    elif rating >=  900: ret += 'Do you know how to short-hop? 🐇'
    elif rating >=  800: ret += 'Do you know how to fast-fall? 🌠'
    elif rating >=  780: ret += 'Super Smash Brothers Melee for the Nintendo Gamecube 🧊'
    elif rating >=  700: ret += 'Your rating is about as low as the lowest I\'ve seen 🍃 But don\'t give up!'
    else               : ret += 'You must have a girl-/boyfriend and I hope you have found meaning in life'
    await ctx.send(ret)

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
