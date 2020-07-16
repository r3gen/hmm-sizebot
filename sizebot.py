# Work with Python 3.6
import datetime, time
import random
import discord
from discord.ext import commands
from configparser import ConfigParser
from os import path

bot = commands.Bot(command_prefix='!')

config_filename = 'hcm_sizebot.ini'


def load_config():
    bot_config = ConfigParser()
    if path.exists(filename):
        bot_config.read(filename)
        if bot_config["Default"]["last_reset"].date() < datetime.now().date():
            for section in config.sections():
                if section is not "Default":
                    bot_config.remove_section(section)
            bot_config["Default"]["last_reset"] = datetime.now()
            save_config(bot_config)
    else:
        config['Default'] = {
            "reset_hour": '5',
            "last_reset": datetime.now()
        }
        save_config(config)

    return bot_config


def save_config(bot_config):
    with open(config_filename, 'w') as config_file:
        bot_config.write(config_file)


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

config = load_config()


@bot.command()
async def sizeme(ctx):
    user = '{0.author.display_name}'.format(ctx.message)
    server = '{0.server.id}'.format(ctx.message)
    if config.has_option(server, user):
        size = config[server][user]
    else:
        size = get_size()
    msg = '{0.author.mention} is '.format(ctx.message) + size + " tall."
    await ctx.send(msg)
    sizes[user] = size
    if not config.has_section(server):
        config.add_section(server)
    config[server][user] = size
    save_config(config)


@bot.command()
async def showsizes(ctx):
    server = '{0.server.id}'.format(ctx.message)
    msg = "All sizes:\n"
    for user in config.options(server):
        msg += user + ": " + config[server][user] + "\n"
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
