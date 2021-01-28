"""Check if userbot awake or not . 



"""

#make by @LEGENDX22 don't kang this plugin

# if you kang then keep credits

#cReDiTs -LEGENDX22⚡⚡

import os

import time

import asyncio

from telethon import events

from telethon.tl.types import ChannelParticipantsAdmins

from userbot import ALIVE_NAME, StartTime, CMD_HELP

from userbot.utils import admin_cmd

from telethon import version

from math import ceil

import json

import random

import re

from telethon import events, errors, custom

import io

from platform import python_version, uname



ALIVE_PIC = Config.ALIVE_PIC

if ALIVE_PIC is None:

  ALIVE_PIC = "https://telegra.ph/file/0e36b02061064b7229e3b.jpg"





DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "DEVIL USER"



global ghanti

        

#make by LEGEND X bht mehnat lag gayi yrr but banhi gaya ð           

#@command(outgoing=True, pattern="^.awake$")

@borg.on(admin_cmd(pattern=r"awake"))

async def amireallyalive(awake):

   """ For .awake command, check if the bot is running.  """

   tag = borg.uid

   ALIVE_MESSAGE= " ⚡⚡ DEVIL BOT 🔥  IS ON 🔥 FIRE 🔥 \n\n"

   ALIVE_MESSAGE += "🔥🔥 SYSTEM STATUS🔥🔥\n"

   ALIVE_MESSAGE += "🔥🔥TELETHON VERSION🔥🔥 : 6.0.9\n"

   ALIVE_MESSAGE += "🔥🔥 DEVIL VERSION🔥🔥 :   1.0.9\n"

   ALIVE_MESSAGE += f"🔥🔥 SYSTEM🔥🔥 : DATABASE OK\n"

   ALIVE_MESSAGE += f"🔥 MY BOSS 🔥: {DEFAULTUSER}\n"

   ALIVE_MESSAGE += "🔥🔥MADE BY🔥🔥 : [DEVIL](t.me/luciifeermorningstar) \n\n"

   ALIVE_MESSAGE += "⚡⚡Deploy DEVILBOT⚡⚡ : [REPO](https://github.com/lucifeermorningstar/deviluserbot)\n"   

   await awake.delete() 

   await borg.send_file(awake.chat_id, ALIVE_PIC,caption=ALIVE_MESSAGE)


#make by LEGENDX22
