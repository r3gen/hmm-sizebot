# Work with Python 3.6
import random
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

def read_token():
    import os
    return os.environ["SIZEBOT_TOKEN"]
    '''
        with open("token.txt", "r") as f:
            lines = f.readlines()
            return lines[0].strip()
    '''

TOKEN = read_token()

sizes = dict()

@bot.command()
async def sizeme(ctx):
    size = get_size()
    user = '{0.author.mention}'.format(ctx.message)
    # server = '{0.server.id}'.format(ctx.message)
    msg = user + ' is ' + size + " tall."
    await ctx.send(msg)
    sizes[user] = size
    
@bot.command()
async def showsizes(ctx):
    msg = "All sizes:\n"
    for user in sizes.keys():
        msg += user + ": " + sizes[user] + "\n"
    await ctx.send(msg)
    
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    
def get_stats():
    return null
    
def get_size():
    size = {
        1: "1 mm",
        2: "1 cm",
        3: "1 inch",
        4: "3 inch",
        5: "6 inch",
        6: "1 foot",
        7: "3 foot",
        8: "6 foot",
        9: "12 foot",
        10: "50 foot",
        11: "100 foot",
        12: "200 foot",
        13: "400 foot",
        14: "500 foot",
        15: "600 foot",
        16: "800 foot",
        17: "1000 foot",
        18: "2000 foot",
        19: "3000 foot",
        20: "5000 foot"
    }
    return size.get(random.randint(1,20),"No size for you")

bot.run(TOKEN)
