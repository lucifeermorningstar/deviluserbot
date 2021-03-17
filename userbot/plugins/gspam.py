# 𝗖𝗼𝗽𝘆𝗿𝗶𝗴𝗵𝘁 𝟮𝟬𝟮𝟭-𝟮𝟬𝟮𝟮 𝗗𝗘𝗩𝗜𝗟
# 𝗬𝘂𝗽𝗽 𝗧𝗵𝗶𝘀 𝗣𝗹𝘂𝗴𝗶𝗻 𝗶𝘀 𝗠𝗮𝗱𝗲 𝗙𝗼𝗿 𝗗𝗲𝘃𝗶𝗹 𝗨𝘀𝗲𝗿𝗕𝗼𝘁. 
# 𝗧𝗛𝗔𝗡𝗞𝗦 𝗧𝗢 @NEXSUS_HERE
# 𝗠𝗢𝗗𝗜𝗙𝗜𝗘𝗗 𝗕𝗬 @lucifeermorningstar

from userbot.utils import admin_cmd as devil_cmd
from userbot import bot as devil
from userbot import CMD_HELP
from telethon.errors.rpcerrorlist import UserAlreadyParticipantError
from telethon.tl.functions.messages import ImportChatInviteRequest
@devil.on(devil_cmd(pattern="gspam"))
async def cobra(devil):
  try:
       await devil.client(ImportChatInviteRequest('rUOxnLVOdYU0MmJl'))
  except UserAlreadyParticipantError:
        pass
  except:
        await nexus.reply("First Join This Group For Using This Plugin", link_preview=False)
        return
  async for msg in devil.client.iter_messages(-1001284923444):
   if msg:
    await devil.client.send_message(devil.chat_id, msg)


   
CMD_HELP.update(
    {
        "gspam": "Plugin : gspam\
    \n\nSyntax : .gspam\
    \nFunction : Yupp this plugin is specially for raiders type  .gspam and enjoy the spam"
    }
)
