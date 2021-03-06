from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

You can use me to generate pyrogram and telethon string session. Use the below buttons to know more!
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(" Generating Session ", callback_data="generate")],
        [InlineKeyboardButton(text=" Back ", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("๐ฅ Generating Session ๐ฅ", callback_data="generate")]
    ]

    support_button = [
        [InlineKeyboardButton("๐ Support ๐", url="https://t.me/Baapjiiiiiiiiii")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("๐ฅ Generating Session ๐ฅ", callback_data="generate")],
        [InlineKeyboardButton("๐จโ๐ป Repo subscribe ๐ฅ and come to get repo โฃ๏ธ ๐จโ๐ป", url="https://youtube.com/channel/UCE5jPA5zAKw37gM7tptdJew")],
        [
            InlineKeyboardButton("How to Use โ", callback_data="help"),
            InlineKeyboardButton(" About", callback_data="about")
        ],
        [InlineKeyboardButton("๐ฎ๐ณ Owner ๐ฎ๐ณ", url="t.me/legit_adder_01")],
    ]

    # Help Message
    HELP = """
ยป Click the below button or use /generate command to start generating session!
ยป Click the required button; [Pyrogram/Telethon]
ยป Enter the required variables when asked.
"""

    # About Message
    ABOUT = """
๐จโ๐ป **About Me** 

A telegram bot to generate pyrogram and telethon string session...

[Pyrogram](docs.pyrogram.org)
[Telethon](docs.telethon.org)

Language : [Python](www.python.org)
            **Regarding ~ **@legit_adder_01
"""
