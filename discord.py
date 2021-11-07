import discord
import wikipedia
import random
import requests
from bs4 import BeautifulSoup
from discord.ext import commands
from keep_alive import keep_alive
import asyncio

client = commands.Bot(command_prefix='--')

quote_url = "https://www.appsious.com/quotes/random?topic=motivational-quotes"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}

#Commands
@client.command(name='quotes', help='Generates random quotes')
async def quotes(ctx):
    page = requests.get(quote_url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    quote = soup.find("div", {"class": "card-header bg-white p-lg-5 p-3 text-center border-0"}).getText()
    await ctx.send(quote)

@client.command(name='lyrics', help='Returns the lyrics of specified song')
async def lyrics(ctx, arg):
    lyric_url = "https://www.google.com/search?q="+arg+"+lyrics&hl=en"
    page = requests.get(lyric_url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    lyric1 = soup.find("div", jsname = "Vinbg").get_text(separator="\n")
    lyric2 = soup.find("div", jsname = "WbKHeb").get_text(separator="\n")
    await ctx.send(lyric1)
    await asyncio.sleep(3)
    await ctx.send(lyric2)

@client.command(name='wiki', help='Returns the results from wikipedia')
async def wiki(ctx, arg):
    results = wikipedia.summary(arg, sentences=2)
    await ctx.send('According to wikipedia: '+ results)

@client.command(name='say', help='Displays whatever you say or type, I guess')
async def say(ctx, arg):
    await ctx.send(arg)

@client.command(name='roast', help='Roasts your opponent')
async def roast(ctx, member: discord.Member):
  roasts = ['I’d give you a nasty look but you’ve already got one.',
            'Were you born this stupid or did you take lessons?',
            'I thought of you today. It reminded me to take out the trash.',
            'Your face makes onions cry.',
            'You look like a ‘before’ picture.',
            'Don’t be ashamed of who you are. That’s your parent’s job.',
            'You just might be why the middle finger was invented in the first place.',
            'The last time I saw something like you… I flushed.',
            'You’re the reason they put directions on shampoo.',
            'I’m busy right now. Can I ignore you another time?',
            'If I had a face like yours, I would sue my parents',
            'You are as useless as ‘ueue’ in ‘Queue’',
            'You are the reason God created the middle finger.',
            'I’d smack you, but that would be animal abuse.',
            'My middle finger gets a boner every time I see you.',
            'You are so ugly that when your mom dropped you off at school, she got a ticket for littering.',
            'You look like something I can draw with my left hand.',
            'If you had one more brain cell, it would be lonely']
  await ctx.send(f'{member.name}, {roasts[random.randrange(len(roasts))]}')

@client.command(name='ping', help='Returns the latency')
async def ping(ctx):
    await ctx.send(f'**Pong!**  Latency: {round(client.latency * 1000)}ms')

@client.command(name='hi', help='Probably compliments you')
async def hi(ctx):
  compliments = ['sexy', 'hot', 'beautiful', 'like a snack', 'tired', 'bomb', 'extra', 'like some weird dude from Florida']
  await ctx.send(f'Hello {ctx.message.author.name}, you look {compliments[random.randrange(len(compliments))]} today')

keep_alive()
client.run('sth-sth')
