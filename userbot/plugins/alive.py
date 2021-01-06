from userbot import *
from userbot.utils import *
from userbot.cmdhelp import CmdHelp
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "DevilUserBot User"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

kraken = bot.uid

PM_IMG = " https://telegra.ph/file/c2bbdc0f85074429fd928.jpg "
pm_caption = "➥ **DEVIL USERBOT IS:** `ONLINE`\n\n"
pm_caption += "➥ **SYSTEMS STATS**\n"
pm_caption += "➥ **Telethon Version:** `1.15.0` \n"
pm_caption += "➥ **Python:** `3.7.4` \n"
pm_caption += f"➥ **Owner** : "[Click here](𝚑𝚝𝚝𝚙𝚜://t.me/lucifeermorningstar)" \n"
pm_caption += "➥ **Database Status:**  `ALL GOOD`\n"
pm_caption += "➥ **Current Branch** : `master`\n"
pm_caption += f"➥ **Version** : `D.0`\n"
pm_caption += f"➥ **My Boss** : {DEFAULTUSER} \n"
pm_caption += "➥ **Heroku Database** : `WORKING PROPERLY`\n\n"
pm_caption += "➥ **License** : [GNU General Public License v3.0](github.com/lucifeermorningstar/deviluserbot/blob/master/LICENSE)\n"
pm_caption += "➥ **Copyright** : By [lucifeermorningstar@Github](GitHub.com/lucifeermorningstar)\n"
pm_caption += "➥ **Check Stats By Doing** `.stat`. \n\n"
pm_caption += "[🇮🇳 Deploy DevilUserbot 🇮🇳](https://telegra.ph/file/c2bbdc0f85074429fd928.jpg)"


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
