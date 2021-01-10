# Made By @MarioDevs Keep Credits If You Are Goanna Kang This Lol

# And Thanks To The Creator Of Autopic This Script Was Made from Snippets From That Script

# Usage .avengersdp Im Not Responsible For Any Ban caused By This

import asyncio
import os
import random
import re
import urllib

import requests
from telethon.tl import functions

from userbot.utils import admin_cmd

COLLECTION_STRING = [
    "indian-actress-wallpapers",
    "latest-bollywood-actress-wallpapers-2018-hd",
    "bollywood-actress-wallpaper",
    "hd-wallpapers-of-bollywood-actress",
    "new-bollywood-actress-wallpaper-2018",
]


async def animepp():

    os.system("rm -rf donot.jpg")

    rnd = random.randint(0, len(COLLECTION_STRING) - 1)

    pack = COLLECTION_STRING[rnd]

    pc = requests.get("http://getwallpapers.com/collection/" + pack).text

    f = re.compile("/\w+/full.+.jpg")

    f = f.findall(pc)

    fy = "http://getwallpapers.com" + random.choice(f)

    print(fy)

    if not os.path.exists("f.ttf"):

        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf",
            "f.ttf",
        )

    urllib.request.urlretrieve(fy, "donottouch.jpg")


@borg.on(admin_cmd(pattern="dp ?(.*)"))
async def main(event):

    await event.edit("**Starting Auto set Actress Profile Pic... in 15 seconds\n\nDone !!! Check Your DP **")

    while True:

        await animepp()

        file = await event.client.upload_file("donottouch.jpg")

        await event.client(functions.photos.UploadProfilePhotoRequest(file))

        os.system("rm -rf donottouch.jpg")

        await asyncio.sleep(15)  # Edit this to your required needs
