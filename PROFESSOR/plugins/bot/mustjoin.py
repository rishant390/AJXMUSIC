import random 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from PROFESSOR import app

MISHI = [
    "https://files.catbox.moe/ly6x23.jpg",
    "https://files.catbox.moe/ly6x23.jpg",
    "https://files.catbox.moe/ly6x23.jpg",
    "https://files.catbox.moe/ly6x23.jpg",
    "https://files.catbox.moe/ly6x23.jpg",
    "https://files.catbox.moe/ly6x23.jpg",
    "https://files.catbox.moe/ly6x23.jpg",
    "https://files.catbox.moe/ly6x23.jpg"
    "https://files.catbox.moe/ly6x23.jpg",
    "https://files.catbox.moe/ly6x23.jpg",
    "https://files.catbox.moe/ly6x23.jpg",
    "https://files.catbox.moe/ly6x23.jpg",
    "https://files.catbox.moe/ly6x23.jpg",
    "https://files.catbox.moe/ly6x23.jpg",
    "https://files.catbox.moe/ly6x23.jpg",
    "https://files.catbox.moe/ly6x23.jpg",
    "https://files.catbox.moe/ly6x23.jpg",
    "https://files.catbox.moe/ly6x23.jpg",
]

#--------------------------

MUST_JOIN = ksd_bot_network""
#------------------------
@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(app: Client, msg: Message):
    if not MUST_JOIN:
        return
    try:
        try:
            await app.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await app.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(random.choice(MISHI), caption=f"❅ ʜᴇʏ ᴛʜᴇʀᴇ, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ᴜʜʜ !\n\n❅ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴜsᴇ ʜᴜɴᴛᴇʀ ʙᴏᴛ, ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴀɴᴅ ʏᴏᴜ ᴊᴏɪɴᴇᴅ, ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴀʟʟ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs ",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ", url="https://t.me/KSD_BOT_NETWORK"),
                                InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url=link),
                            ]
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"๏ ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ ᴀs ᴀɴ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴇ ᴍᴜsᴛ_ᴊᴏɪɴ ᴄʜᴀᴛ ๏: {MUST_JOIN} !")
      
