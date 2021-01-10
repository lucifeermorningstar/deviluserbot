"""Available Commands:
.permote
Credits to @TeleBotHelp

   TeleBot
"""

# Main Credits Goes to @T3b0N3
# He Worked Very Hard to do this, So Please Respect Him!!
from telethon import events

import asyncio

from userbot.utils import admin_cmd

@borg.on(admin_cmd("permote"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.9
    animation_ttl = range(0,36)
    #input_str = event.pattern_match.group(1)
   # if input_str == "nope":
    await event.edit("Promoting...... ")
    animation_chars = [
            "Promoted Successfully! Abh nacho sale"
         ]
            

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 40])
