from pyrogram.types import InlineKeyboardButton

import config
from AbdoX import app

def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/QC_11"),
            InlineKeyboardButton(text="ɢʀᴏᴜᴘ", url=f"https://t.me/IUHHHP"), 
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضف البوت الي مجموعتك او قناتك⚡",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        
        [
            InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/QC_11"),
            InlineKeyboardButton(text="ɢʀᴏᴜᴘ", url=f"https://t.me/IUHHHP"), 
        ],
        [
            
            InlineKeyboardButton(text="sᴏᴜʀᴄᴇ sᴇʟᴠᴀ", url=f"https://t.me/QC_11") , 
        ],
    ]
    return buttons
