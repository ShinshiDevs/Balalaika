from typing import Union, Literal

from yarl import URL
from hikari import Snowflake

DiscordIDT = Union[Snowflake, str, int]
URLT = Union[str, URL]

"""
ytsearch - YouTube searching
scsearch - SoundCloud searching
ytmsearch - YouTube Music searching

spsearch - Spotify searching (https://github.com/topi314/LavaSrc)
sprec - Spotify recommendations (https://github.com/topi314/LavaSrc)
amsearch - Apple Music searching (https://github.com/topi314/LavaSrc)
dzsearch - Deezer searching (https://github.com/topi314/LavaSrc)
dzisrc - Deezer ISRC (https://github.com/topi314/LavaSrc)
ymsearch - Yandex Music searching (https://github.com/topi314/LavaSrc)
"""
SEARCH_METHODS = Literal[
    "ytseacrch",
    "scsearch",
    "ytmsearch",
    "spsearch",
    "sprec",
    "amsearch",
    "dzsearch",
    "dzisrc",
    "ymsearch"
]
PlaylistT = Literal["album", "playlist", "artist", "recommendations"]
