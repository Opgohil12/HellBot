import asyncio
from telethon import events
from userbot.utils import admin_cmd, sudo_cmd
from userbot import ALIVE_NAME, hellversion
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Hell User"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

kraken = bot.uid

PM_IMG = "https://telegra.ph/mp4-11-24"
pm_caption = "__**🔥🔥ÒP ɨs օռʟɨռɛ🔥🔥**__\n\n"

pm_caption += f"               __↼🄼🄰🅂🅃🄴🅁⇀__\n**『[{DEFAULTUSER}](tg://user?id={kraken})』**\n\n"

pm_caption += "🛡️TELETHON🛡️ : `1.15.0` \n"

pm_caption += f"😈Òpẞø†😈       : `{hellversion}`\n"

pm_caption += f"⚜️Sudo⚜️            : `{sudou}`\n"
pm_caption += "Currently Alive, my peru master! ψ(｀∇´)ψ"
pm_caption += "MY Details iz" 
pm_caption += "I aM A Ro BOT OP"
pm_caption += "Telethon version: 6.9.0"
pm_caption += "MY GoD iZ @Gujjuopgohil"
pm_caption += "Python: 3.7.3"

pm_caption += "Bot created by: SnapDragon, @opgohil"

pm_caption += "My peru owner: @GUJJUOPGOHIL"
pm_caption += f"I Talk To YöU 😠"
pm_caption += "Bol kya kam he Bhadve (‘_’)"


#@command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
