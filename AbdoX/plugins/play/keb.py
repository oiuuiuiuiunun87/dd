import asyncio
from pyrogram import Client, filters
from random import choice
from pyrogram import filters
from config import BANNED_USERS
from AbdoX import (Apple, Resso, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, Message, ChatJoinRequest


@app.on_message(filters.regex("^/selva"), group=39)
async def cpanel(_, message: Message):             
        text = "اهلا بك بك عزيزي العضو اليك كيب الاعضاء⚡"
        kep = ReplyKeyboardMarkup([
["مطور السورس"],
["السورس","المطور"],
["مبرمج السورس"],
["انميي","متحركة"],
["كتابات"],
["لو خيروك"],
["اقتباس","نقشبندي"],
["سوال","اقتباس"],
["استوريهات"],
["تلاوات","عبدالباسط"],
["صور بنات","صور ولاد"],
["❎ ¦ حذف الكيبورد"]], resize_keyboard=True)
        await message.reply(
              text=text,
               reply_markup=kep,quote=True)

@app.on_message(filters.command(["❎ ¦ حذف الكيبورد"], ""))
async def upbkgt(client: Client, message: Message):
    await message.reply_text(
        text="""❎ ¦ تم حذف الكيبورد بنجاح""",
        reply_markup=ReplyKeyboardRemove()
    )

@app.on_message(filters.command(["❎ ¦ حذف الكيبورد"], ""))
async def upbkgt(client: Client, message: Message):
    await message.reply_text(
        text="""❎ ¦ تم حذف الكيبورد بنجاح""",
        reply_markup=ReplyKeyboardRemove()
    )

@app.on_message(filters.regex("يـوتيوب"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://d.top4top.io/p_32475f9ct1.jpg",
        caption=f"""يتم استخدام هذا الامر لعرض تحميل من اليوتيوب\nاستخدم الامر بهذا الشكل `تنزيل`  او  `يوتيوب`  كمثل تنزيل سوره الرحمن اضغط علي الامر لنسخ والاستخدا """,
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("sᴏᴜʀᴄᴇ sᴇʟᴠᴀ", url=f"https://t.me/QC_11"),
            ]
         ]
     )
        )
