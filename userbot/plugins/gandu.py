import asyncio

from userbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp


@bot.on(admin_cmd(pattern=r"gandu$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"gandu$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 5
    animation_ttl = range(0, 21)
    animation_chars = [
        "`abe gandu,Ruk abhi teri gand marta hu lodu`",
        "`Dekh sale Teri gand me dal diya lund`",
        "`now twisting my lund in your gand`",
        "`Your Gand Fat giye Successfully`",
        "`es Gandu Ka Gand Fat gye a`",
        "`Gandu Asking again to taste my DICK🍌`",
        "`Requested accepted😻💋, Ready to taste my DICK🍌`",
        "`Getting again with fati hoi gand ready to fuck 👀`",
        "`You Gandu Is Ready To Fuck`",
        "`Fucking Your 😈😈\n\n\nYour  Ass Get Red\nTrying new SEX position to make u Squirt\n\nAlmost Done. 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Fucking Your 😈😈\n\n\nYour Gand Get White\nu squirted like a shower💧💦👅\n\nAlmost Done..\n\nFucked Percentage... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Fucking Your 😈😈\n\n\nYour gand Get Red\nDoing Extreme SEX with u👄\n\nAlmost Done...\n\nFucked Percentage... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Fucking Your 😈😈\n\n\nYour gand Get Red\nWarming ur Ass🍑 to Fuck!🍑🍑\n\nAlmost Done....\n\nFucked Percentage... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Fucking Your 😈😈\n\n\nYour ASS🍑 Get Red\nInserted my Penis🍌 in ur ASS🍑\n\nAlmost Done.....\n\nFucked Percentage... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Fucking Your 😈😈\n\n\nYour ASS🍑 Get Red\ndoing extreme sex with u\n\nAlmost Done......\n\nFucked Percentage... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Fucking Your 😈😈\n\n\nYour Boobs🤚😘 are Awesome\nPressing u tight Nipples🤚👀\n\nAlmost Done.......\n\nFucked Percentage... 84%\n███████████████████▒▒▒▒▒▒ `",
        "`Fucking Your 😈😈\n\n\nYour Gand Get Horny\nDoing Gandsex with you👄💋\n\nAlmost Done........\n\nFucked Percentage... 89%\n██████████████████████▒▒▒ `",
        "`Fucking Your 😈😈\n\n\nYour Boobs🤚😘 are Awesome\nI am getting ready to cum in ur Mouth👄\n\nAlmost Done.......\n\nFucked Percentage... 90%\n██████████████████████▒▒▒ `",
        "`Fucking Your 😈😈\n\n\nYour  Boobs🤚😘 are Awesome\nFinally, I have cummed in ur Mouth👅👄\n\nAlmost Done.......\n\nFucked Percentage... 96%\n████████████████████████▒ `",
        "`Fucking Your 😈😈\n\n\nYour ur Gand is Awesome\nyou is Licking my Dick🍌 in the Awesome Way✊🤛🤛👅👄\n\nAlmost Done.......\n\nFucked Percentage... 100%\n█████████████████████████ `",
        "`Fucking Your 😈😈\n\n\nYour  ASS🍑 Get Red\nCummed On ur Mouth👅👄\n\nYou got Pleasure\n\nResult: Now I Have 1 More SEX Partner 👍👍 abh ja ki kise aur se chuda gandu`",
    ]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 21])


CmdHelp("Gandu").add_command(
  "gandu", None, "Uhhhh... Try it and see"
)