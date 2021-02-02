from userbot import *
from userbot.utils import *
from userbot.cmdhelp import CmdHelp
from userbot.uniborgConfig import Config
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "DevilUserBot User"

PM_IMG = Config.ALIVE_PIC

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

kraken = bot.uid

pm_caption = "__**🔥🔥𝙳𝚎𝚟𝚒𝚕 υѕєявσт ιѕ ση ƒιяє🔥🔥**__\n\n"

pm_caption += (
    f"               __↼🄼🄰🅂🅃🄴🅁⇀__\n**『[{DEFAULTUSER}](tg://user?id={kraken})』**\n\n"
)

pm_caption += "†êlê†hðñ Vêr§ïðñ: `1.15.0` \n"

pm_caption += "ꉣꌦ꓄꒻ꄲꋊ ꒦ꏂꋪꇙ꒐ꄲꋊ:      `3.7.4` \n"

pm_caption += f"ĐɆVłⱠ฿Ø₮ VɆⱤ₴łØ₦:  __**D.0**__\n"

pm_caption += f"sᴜᴅᴏ            : `{sudou}`\n"

pm_caption += "ꇙ꒤ꉣꉣꄲꋪ꓄ ꍌꋪꄲ꒤ꉣ  : [ᴊᴏɪɴ](https://t.me/deviluserbot)\n"

pm_caption += "𝙲𝚛𝚎𝚊𝚝𝚘𝚛    : [Click Here](https://t.me/lucifeermorningstar)\n\n"

pm_caption += "    [✨REPO✨](https://github.com/lucifeermorningstar/deviluserbot) 🔹 [📜License📜](https://github.com/lucifeermorningstar/deviluserbot/blob/master/LICENSE)"



@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()

CmdHelp("alive").add_command(
  'alive', None, 'Check weather the bot is alive or not'
).add_command(
  'devil', None, 'Check weather yhe bit is alive or not. In your custom Alive Pic and Alive Msg if in Heroku Vars'
).add()
