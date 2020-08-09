# Work with Python 3.6

import random
from configparser import ConfigParser
from datetime import datetime
from os import path

from discord import Permissions, Embed, Colour
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

config_filename = 'hcm_sizebot.ini'

size = [
        "1 mm",
        "1 cm",
        "1 inch",
        "3 inch",
        "6 inch",
        "1 foot",
        "3 foot",
        "6 foot",
        "12 foot",
        "50 foot",
        "100 foot",
        "200 foot",
        "400 foot",
        "500 foot",
        "600 foot",
        "800 foot",
        "1000 foot",
        "2000 foot",
        "3000 foot",
        "5000 foot"
    ]

def load_config():
    bot_config = ConfigParser()
    if path.exists(config_filename):
        bot_config.read(config_filename)
        reset_config(bot_config)
    else:
        bot_config['Default'] = {
            "reset_hour": '5',
            "last_reset": datetime.now().isoformat()
        }
        save_config(bot_config)

    return bot_config


def save_config(bot_config):
    with open(config_filename, 'w') as config_file:
        bot_config.write(config_file)


def reset_config(bot_config, server_id=None):
    if server_id is not None:
        if not bot_config.has_section(server_id):
            bot_config.add_section(server_id)

    last_date = datetime.fromisoformat(bot_config["Default"]["last_reset"])
    if last_date.date() < datetime.now().date():
        for section in bot_config.sections():
            if section != "Default":
                bot_config.remove_section(section)
                bot_config.add_section(section)
        bot_config["Default"]["last_reset"] = datetime.now().isoformat()
        save_config(bot_config)


def read_token():
    import os
    return os.environ["SIZEBOT_TOKEN"]
    '''with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()
    '''


TOKEN = read_token()

config = load_config()


@bot.command()
async def sizeme(ctx):
    reset_config(config)
    user_id = "{}".format(ctx.author.id)
    server = "{}".format(ctx.guild.id)
    if config.has_option(server, user_id):
        size = config[server][user_id]
    else:
        size = get_size()
    msg = '{0.author.mention} is '.format(ctx.message) + size + " tall."
    await ctx.send(msg)
    # sizes[user] = size
    if not config.has_section(server):
        config.add_section(server)
    config[server][user_id] = size
    save_config(config)


@bot.command()
async def showsizes(ctx):
    server = str(ctx.guild.id)
    reset_config(config, server)

    user_list = {}
    if not config.has_section(server):
        await ctx.send("SERVER NOT FOUND... but this should be impossible")
        return
    for user in config.options(server):
        user_list[user] = config[server][user]

    sorted_list = sorted(user_list, key=lambda x: size.index(user_list[x]), reverse=True)

    embed_msg = Embed(
        title="All Sizes",
        description="Server member sizes.",
        colour=Colour.blue()
    )

    for user_id in sorted_list:
        member = await ctx.guild.fetch_member(user_id)
        embed_msg.add_field(name=member.display_name, value=user_list[user_id], inline=False)
    await ctx.send(embed=embed_msg)


@bot.command()
@commands.has_permissions(manage_roles=True)
async def sizeuser(ctx, arg=None):
    server_id = str(ctx.guild.id)
    if arg is None:
        await ctx.send("You must specify a user's ID with this command. For example:\n"
                       "`!sizeuser 000000000000000000`\nFor a list of user IDs: !listmembers")
        return

    member = await ctx.guild.fetch_member(arg)
    if member is None:
        await ctx.send("Member {} not found. Trying `!listmembers` to find the user'd ID.".format(arg))
        return

    user_id = str(member.id)
    reset_config(config)
    if config.has_option(server_id, user_id):
        user_size = config[server_id][user_id]
    else:
        user_size = get_size()
    msg = '{} is {} tall.'.format(member.mention, user_size)
    await ctx.send(msg)
    if not config.has_section(server_id):
        config.add_section(server_id)
    config[server_id][user_id] = user_size
    save_config(config)


@bot.command()
@commands.has_permissions(manage_roles=True)
async def listmembers(ctx):
    embed_msg = Embed(
        title="User ID List",
        description="A list of server members and their discord user IDs.",
        colour=Colour.blue()
    )
    for member in ctx.guild.members:
        embed_msg.add_field(name=member.display_name, value=member.id, inline=False)
    await ctx.send(embed=embed_msg)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


def get_size():
    return size[random.randint(1, len(size))]


bot.run(TOKEN)
