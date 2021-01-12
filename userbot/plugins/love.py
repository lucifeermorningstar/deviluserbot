"""Fun pligon...for HardcoreUserbot
\nCode by @Rambo_86
type `.love` and to see the fun.
"""
import random, re
from uniborg.util import admin_cmd
import asyncio
from telethon import events

@borg.on(admin_cmd(pattern="love ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("Pyase Ko Ek Katra Paani Kaafi hai")
        await asyncio.sleep(2)
        await event.edit("Ishq me char pall ke Zindegani Kaafi hai")
        await asyncio.sleep(2)
        await event.edit("Doobne ko Smandar me jaae kaha")
        await asyncio.sleep(2)
        await event.edit("Aapki Aankh se tapkta woh Paani kaafi hai")
        await asyncio.sleep(2)
        await event.edit("**Pyase Ko Ek Katra Pani Kafi Hai. Ishq Mein Char Pal Ki Zindgani Kafi Hai. Doobne Ko. Samander Mein Jayein Kahan. Aapki Aankh Se Tapka Voh Pani Kafi Hai.**")
