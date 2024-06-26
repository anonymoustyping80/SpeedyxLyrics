# Copyright ©️ 2023 anonymoustyping80. All Rights Reserved
# You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [❍⏤‌•Јαу___❍‌ᴘ𓆪༆✨](https://github.com/anonymoustyping80/SpeedyxLyrics)

# Read GNU General Public License v3.0: https://github.com/anonymoustyping80/SpeedyxLyrics/blob/mai/LICENSE
# Don't forget to follow github.com/anonymoustyping80 because I am doing these things for free and open source
# Star, fork, enjoy!

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345678))
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    TOKEN = os.environ.get("TOKEN")
