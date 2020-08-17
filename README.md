# hcm-sizebot

##Overview

hcm-sizebot is a discord bot that when connected to a server allows users to be assigned a 
size (e.g. 6ft, 12ft, etc.) when requested by a command.

## Installation

### Choosing an Environment
Sizebot maintains state information using a configuration file on disk and therefore must 
have the ability to read and write from disk from one run to another. Therefore, some 
environments which will reset the disk image whenever the bot is restarted will lose any
assignments made since the last reset. This bot can be run by simply executing the sizebot.py
script (`python3 sizeboy.py`). However, most may find the best way to run this bot is to 
use the produced docker image which can be found in the docker repository.

### Connecting to Discord
To connect this bot to discord you will need to set it up a bot application in your discord
account. Instructions for doing so can be found at 
https://discordpy.readthedocs.io/en/latest/discord.html. The bot only needs permissions 
to send messages.
 
Once you have the bot secret from the connection process you will need to set/update the
SIZEBOT_TOKEN environmental variable with the secret so it can authenticate to discord.

