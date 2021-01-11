"""Fun pligon...for DevilUserbot
\nCode by @Sensei_nex
type .ga and .gaa to see the fun.
"""
import random, re
from uniborg.util import admin_cmd
import asyncio
from telethon import events

@borg.on(admin_cmd(pattern="ga ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("Abey O aatishbaji lodu")
        await asyncio.sleep(0.7)
        await event.edit("kaan khol ke sun lein")
        await asyncio.sleep(1)
        await event.edit("Baap ke samne Bakchodi nhi")
        await asyncio.sleep(0.8)
        await event.edit("Aur tera Baap Kaun h janta h na")
        await asyncio.sleep(0.9)
        await event.edit("Nhi janta to jaan le")
        await asyncio.sleep(1)
        await event.edit("Mai hu tera baap")
        await asyncio.sleep(0.8)
        await event.edit("Naam Sensei")
        await asyncio.sleep(0.7)
        await event.edit("**Sensei PAPA**")
        await asyncio.sleep(1)
        await event.edit("Abb Nikal yaha se madarchod")

@borg.on(events.NewMessage(pattern=r"\.gaa", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Jaaa jakaar APNI maa se poochna `")
    await asyncio.sleep(0.9)
    await event.edit("WHO IS YOUR FATHER ?")
    await asyncio.sleep(0.9)
    await event.edit("Pta h teri maa kya bolegi")
    await asyncio.sleep(0.9)
    await asyncio.edit("vo khegi LODEE BETA ye koi poochne Ki baat hai")
    await asyncio.sleep(0.9)
    await asyncio.edit("tera baap sensei hai aur vhi rhega")