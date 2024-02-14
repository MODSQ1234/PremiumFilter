class script(object):
    START_TXT = """<b>היי {} אני בוט משחקים תכתבו לי את המשחק/אפלקציה הפרוצה שאתם רוצים ואני ישלח לכם אותו👇</b>"""

    HELP_TXT = """<b>Hᴇʏ {} Fʀɪᴇɴᴅ Hᴇʀᴇ Yᴏᴜʀ Bᴜᴛᴛᴏɴs 👇</b>"""

    PRIVATEBOT_TXT = """<b>Tʜᴀɴᴋs Fᴏʀ Aᴅᴅɪɴɢ Mᴇ

- ›› Mᴜsᴛ Aᴅᴅ Mᴇ Aᴅᴍɪɴ Tᴏ Wᴏʀᴋ Oɴ Tʜɪs Gʀᴏᴜᴘ

- ›› Cʜᴀɴɢᴇ Sᴇᴛᴛɪɴɢ Fᴏʀ Uʀ Gʀᴏᴜᴘ Cʟɪᴄᴋ 👉 /connect

- ›› I Wɪʟʟ Pʀᴏᴠɪᴅᴇ Mᴏᴠɪᴇs/Sᴇʀɪᴇs Dᴏɴ'ᴛ Wᴏʀʀʏ

- ›› Eɴᴊᴏʏ !! Mᴏʀᴇ Iɴғᴏ Usᴇ Uɴᴅᴇʀ Bᴜᴛᴛᴏɴs</b>
"""

    MODS_TXT = """I Hᴀᴠᴇ Mᴀɴʏ Fᴇᴀᴛᴜʀᴇs"""

    PONGD_TXT = """Cʜᴇᴄᴋ Mʏ Pɪɴɢ Bʏ Cʟɪᴄᴋɪɴɢ 👉 /ping"""
    
    PONG_TXT = """Cʜᴇᴄᴋ Mʏ Pɪɴɢ Bʏ Cʟɪᴄᴋɪɴɢ 👉 /ping"""

    ABOUT_TXT = """<b>🤖 השם שלי : בוט סרטים : <a href=https://t.me/Movietext83>בוט סרטים חדשני</a>
👨‍💻 מתכנת : <a href=https://t.me/Sharathitsisme>sʜᴀʀᴀᴛʜ</a>
📝 שפה : ᴘʏʀᴏɢʀᴀᴍ
📚 ꜰʀᴀᴍᴇᴡᴏʀᴋ : ᴘʏᴛʜᴏɴ 3
📡 אוחסן : ғʀᴇᴇ ʜᴏsᴛɪɴɢ
📢 sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ : <a href=https://t.me/TamilanMoviesChat>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>
🌟 לקנייה קוד כזה : <a href=@Mods1234>שלחו לי הודעה</a></b>"""

    SOURCES_TXT = """למה אתם מחכים שלחו לי הודעה

- 100﹪ הקוד נכתב על ידי <a href=@Mods1234</a>

- & Rᴇᴩᴏ Lɪɴᴋ 👇 Hᴇʀᴇ"""

    SOURCE_TXT = """Tʜɪs Is Aɴ Oᴩᴇɴ-Sᴏᴜʀᴄᴇ Pʀᴏᴊᴇᴄᴛ Bʏ @Mods1234</b>

- 100﹪ Cᴏᴅᴇᴅ Bʏ <a href=@Mods1234</a></b>

- 👇 Hᴇʀᴇ"""

    FONT_TXT = """I Cᴀɴ Gᴇɴᴇʀᴀᴛᴇ Aᴛᴛʀᴀᴄᴛɪᴠᴇ Fᴏɴᴛs Fᴏʀ Yᴏᴜʀ Tᴇxᴛ Sᴇɴᴅ Lɪᴋᴇ Tʜɪs 👇

ᴇɢ :- /font hi da"""

    CARBON_TXT = """/carbon ﹛ ʏᴏᴜʀ ᴛᴇxᴛ ﹜

ᴇɢ :- /carbon hi"""

    SHARE_TXT = """/share ﹛ ʏᴏᴜʀ ᴛᴇxᴛ ﹜

ᴇɢ :- /share hi da"""

    VIDEO_TXT ="""Dᴏᴡɴʟᴏᴀᴅ Aɴʏ Yᴏᴜᴛᴜʙᴇ Vɪᴅᴇᴏ Fʀᴏᴍ Tʜᴇ Vɪᴅᴇᴏ Lɪɴᴋ

• Hᴏᴡ Tᴏ Usᴇ
• Tʏᴘᴇ /video 𝘈𝘯𝘥 (YᴏᴜTᴜʙᴇ Vɪᴅᴇᴏ Lɪɴᴋ)
• Exᴀᴍᴘʟᴇ:
• /video https://youtu.be/kB9TkCscX0"""

    TELE_TXT = """▫️Hᴇʟᴘ: ▪️ Tᴇʟᴇɢʀᴀᴘʜ ▪️
     Tᴇʟᴇɢʀᴀᴘʜ Lɪɴᴋ Gᴇɴᴇʀᴀᴛᴏʀ
    Usᴀɢᴇ
    🤧 /telegraph - Sᴇɴᴅ Mᴇ Pʜᴏᴛᴏ Oʀ Vɪᴅᴇᴏ Uɴᴅᴇʀ (5ᴍʙ)"""

    MANUELFILTER_TXT = """<b>Hᴏᴡ Tᴏ Dᴏᴡɴʟᴏᴀᴅ Mᴏᴠɪᴇs / Sᴇʀɪᴇs Usɪɴɢ Tʜɪs Bᴏᴛ</b> 😌 🔋

<b>Fɪʀsᴛ Jᴏɪɴ Tʜɪs Gʀᴏᴜᴩ » https://t.me/Movietext83</b>

<b>Sᴇɴᴅ Yᴏᴜ Wᴀɴᴛ Mᴏᴠɪᴇs Oʀ Sᴇʀɪᴇs Nᴀᴍᴇ Wɪᴛʜ Cᴏʀʀᴇᴄᴛ Sᴩᴇʟʟɪɴɢ</b>

<b>Aɴᴅ Bᴏᴛ Wɪʟʟ Sᴇɴᴅ Yᴏᴜ Asᴋᴇᴅ Fɪʟᴇ</b>

<b>Hᴏᴡ Tᴏ Oᴩᴇɴ Bᴏᴛ Sᴇɴᴅᴇᴅ Fɪʟᴇ Lɪɴᴋ. » <a href=https://t.me/Movietext83/13>ᴛᴜᴛᴏʀɪᴀʟ</a>.﹤/b>"""

    CONTACT_TXT = """<b>
<b>»» ° Oɴʟʏ Cᴏɴᴛᴀᴄᴛ Fᴏʀ Pᴀɪᴅ Wᴏʀᴋs / Pʀᴏʙʟᴇᴍ / Dᴏᴜʙᴛ / Cᴏʟʟᴀʙ / Hᴇʟᴩ °</b>

<b>»» Iғ U Cᴏɴᴛᴀᴄᴛ Mᴇ Sᴇᴇ Bᴇʟᴏᴡ Bᴜᴛᴛᴏɴs 😙</b>
"""

    STATUS_TXT = """<b><u>Cᴜʀʀᴇɴᴛ Dᴀᴛᴀʙᴀsᴇ Sᴛᴀᴛᴜs</b></u>
    
<b>📑 ғɪʟᴇs sᴀᴠᴇᴅ: <code>{}</code>
👩🏻‍💻 ᴜsᴇʀs: <code>{}</code>
👥 ɢʀᴏᴜᴘs: <code>{}</code>
🗂️ ᴏᴄᴄᴜᴘɪᴇᴅ: <code>{}</code>
🗄️ ғʀᴇᴇ sᴛᴏʀᴀɢᴇ: <code>{}</code></b>
"""
    LOG_TEXT_G = """<b> #NewGroup
👥 ɢʀᴏᴜᴘ 👥 = {}(<code>{}</code>)
😇 ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀs 😇 = <code>{}</code>
💌 ᴀᴅᴅᴇᴅ ʙʏ 💌 - {} </b>
"""
    LOG_TEXT_P = """<b> #NewUser
ɪᴅ ♥️- <code>{}</code>
ɴᴀᴍᴇ 💥- {} </b>
"""
