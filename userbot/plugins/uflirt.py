""" Flirt...

    Command .rfilmy

    By Devil """



from telethon import events

import asyncio

import os

import sys

import random

from userbot.utils import admin_cmd
from userbot import CMD_HELP
from userbot.cmdhelp import CmdHelp



@borg.on(admin_cmd(pattern=r"uflirt$", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    await event.edit("Gonna tell you what's in my mind about you,my love....â¤ï¸")

    await asyncio.sleep(2)

    x=(random.randrange(1,25))

    if x==1:

        await event.edit(" You may fall from the sky,\n you may fall from a tree, \n but the best way to fallâ¦\n is in love with me. ")

    if x==2:

        await event.edit("Do you have a name or can I call you mine?")

    if x==3:

        await event.edit("You know youâre in love when you canât fall asleep because reality is finally better than your dreams.")

    if x==4:

        await event.edit("Guess what Iâm wearing? The smile you gave me!")

    if x==5:

        await event.edit("My friends bet I canât talk to the prettiest girl. Wanna use their money to buy drinks?")

    if x==6:

        await event.edit("You look familiar, didnât we take a class together? I couldâve sworn we had chemistry.")

    if x==7:

        await event.edit("Iâm no organ donor but Iâd be happy to give you my heart. ")    

    if x==8:

        await event.edit("When I look into your eyes, it is like a gateway into the world of which I want to be a part.")

    if x==9:

        await event.edit("Keep an eye out for elves with ropes and a blindfold! Why? Cause I asked Santa for you this Christmas")

    if x==10:

        await event.edit("Are you the ocean? Cuz baby I want to swim in you all day")

    if x==11:

        await event.edit("I just got dumped, and I think that you could make me feel better.")

    if x==12:

        await event.edit("Are you netflix? Because i could watch you for hours.")

    if x==13:

        await event.edit("When Iâm older, Iâll look back at all of my crowning memories, and Iâll think of the day my children were born, the day I got married, and the day that I met you.")

    if x==14:

        await event.edit("Wait, something is really wrong with my cell phone. Iâm not sure what happened but your number is not in it. May I have it again?")

    if x==15:

        await event.edit("I think your hand looks heavy. Would you like me to hold it for you?")

    if x==16:

        await event.edit("Damn, youâre so gorgeous you made me forget what my pick up line was.")

    if x==17:

        await event.edit("May I borrow your phone? \nGirl: Why? \nBoy: I want to call your mother and thank her for bringing you into this world.")

    if x==18:

        await event.edit("If being beautiful was a crime, youâd surely be guilty as charged.")

    if x==19:

        await event.edit("Are you lost? Because heavenâs a long way of here.")

    if x==20:

        await event.edit("Boy: I bet your feet are feeling tired now.\n Girl: Why?\n Boy: Because youâve been running through my mind day and night.")

    if x==21:

        await event.edit("Can I take a picture of you so I could show Santa what I want for Christmas?")

    if x==22:

        await event.edit("Can you recommend a bank where I can make a deposit? Because Iâm planning to save all my love for you.")

    if x==23:

        await event.edit("If a thousand painters worked for a thousand years, they could not create a work of art as beautiful as you.")

    if x==24:

        await event.edit("Do you believe in love at first sight or should I walk by again?")

    if x==25:

    	await event.edit("If I could rearrange the alphabet, I would put U and I together.")

    if x==26:

    	await event.edit("If I were a stop light, I would always turn red each time you pass by. In that way, I could stare at you longer.")

    if x==27:

        await event.edit("God has provided us with two ears, two eyes and two hands. But He only gave us one heart. He told me to find you and tell you that youâre the second one.")

    if x==28:

        await event.edit("Please donât go now. Else, I would have to go to the police station and report you to the cops. You just stole my heart.")

    if x==29:

        await event.edit("You know what Iâm going to do now? Iâll put a tear drop in the sea. When you find it, itâs the time Iâll stop loving you. Deal?")

    if x==30:

        await event.edit("Written and Created By: Idk! thank youðð»â¤")



CmdHelp("uflirt").add_command(
  'rfilmy', 'try and check'
) 
