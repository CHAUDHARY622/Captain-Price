class script(object):
    START_TXT = """🤖ඔයාට අවශ්‍ය වෙන Film එකක් හෝ Tv Series එකක් ගන්න පුළුවන් මේකෙන් 📥 නම Send කරන්න විතරයි තියෙන්නේ🔥😉"""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """🔘 Just Send Series Name and Season OR Use Inline Search Button.
    
[Dont Use words Like Season/Episode/Series](https://t.me/MovieHubOfficialSL)

♻️ If any series is Not Available, Then Request it at
@MovieHubOfficialSL

✨ **My Name :**  [🔥𝐌𝐨𝐯𝐢𝐞𝐇𝐮𝐛 𝐅𝐢𝐥𝐭𝐞𝐫𝐬🔥](t.me/MHOFilter_bot)
👨‍💻 **Developer :** [𝚂𝚎𝚗𝚞 𝙶𝚊𝚖𝚎𝚛 𝙱𝚘𝚢](https://github.com/SenuGamerBoy)
🍀 Data Base : Mango DB
📝 **Language :** [Python3](https://python.org)
🧰 **Framework :** [Pyrogram](https://pyrogram.org)
📡 **Server :** [heroku](https://heroku.com)
🌹 **Build Status :** 𝚅2.5
"""
    SOURCE_TXT = """MMa</a>"""
    MANUELFILTER_TXT = """Coming Soon"""
    BUTTON_TXT = """Help: <b>Buttons</b>
    
- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>

1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>

<code>[Button Text](buttonurl:https://t.me/MHOFilter_bot)</code>

<b>Alert buttons:</b>

<code>[Button Text](buttonalert:This is an alert message)</code>"""
    
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>
    
<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    
    CONNECTION_TXT = """Help: <b>Connections</b>
    
- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>

1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM
<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    
    EXTRAMOD_TXT = """
<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>"""
    ADMIN_TXT = """
Coming Soon"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
