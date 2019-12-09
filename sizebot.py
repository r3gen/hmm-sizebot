# Work with Python 3.6
import datetime, time
import random
import discord
from discord.ext import commands
from configparser import ConfigParser
from os import path

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


@bot.command()
async def sizeme(ctx):
    msg = '{0.author.mention} is '.format(ctx.message) + get_size() + " tall."
    await ctx.send(msg)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


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


def load_config():
    filename = 'hcm_sizebot.ini'
    config = ConfigParser()
    if path.exists(filename):
        config.read(filename)
        if config["Default"]["last_reset"].date() < datetime.now().date():
            for section in config.sections():
                if section is not "Default":
                    config.remove_section(section)
            config["Default"]["last_reset"] = datetime.now()
            save_config(config, filename)
    else:
        config['Default'] = {
            "reset_hour": '5',
            "last_reset": datetime.now()
        }
        save_config(config, filename)

    return config


def save_config(config, filename):
    with open(filename, 'w') as config_file:
        config.write(config_file)


bot.run(TOKEN)
