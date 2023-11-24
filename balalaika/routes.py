# Copyright (c) 2023-Present Shinshi Developers Team
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""Lavalink routes"""
from __future__ import annotations

from typing import Final, Sequence

from yarl import URL

__all__: Sequence[str] = (
    "LOCALHOST",
    "DEFAULT_PORT",
    "GET_PLAYERS",
    "GET_PLAYER",
    "UPDATE_PLAYER",
    "DESTROY_PLAYER",
    "UPDATE_SESSION",
    "TRACK_LOADING",
    "TRACK_DECODING",
    "TRACKS_DECODING",
    "INFO",
    "STATS",
    "VERSION",
    "ROUTEPLANNER",
    "UNMARK_FAILED_ADDRESS",
    "UNMARK_ALL_FAILED_ADDRESS"
)

LOCALHOST: Final[str] = "127.0.0.1"
DEFAULT_PORT: Final[int] = 2333

GET_PLAYERS: Final[URL] = URL("/sessions/{session_id}/players")
GET_PLAYER: Final[URL] = URL("/sessions/{session_id}/players/{guild_id}")
UPDATE_PLAYER: Final[URL] = URL("/sessions/{session_id}/players/{guild_id}?noReplace={no_replace}")
DESTROY_PLAYER: Final[URL] = URL("/sessions/{session_id}/players/{guild_id}")
UPDATE_SESSION: Final[URL] = URL("/sessions/{session_id}")
TRACK_LOADING: Final[URL] = URL("/loadtracks?identifier={identifier}")
TRACK_DECODING: Final[URL] = URL("/decodetrack?encodedTrack={encoded_track}")
TRACKS_DECODING: Final[URL] = URL("/decodetracks")

INFO: Final[URL] = URL("/info")
STATS: Final[URL] = URL("/stats")
VERSION: Final[URL] = URL("/version")

ROUTEPLANNER: Final[URL] = URL("/routeplanner/status")
UNMARK_FAILED_ADDRESS: Final[URL] = URL("/routeplanner/free/address")
UNMARK_ALL_FAILED_ADDRESS: Final[URL] = URL("/routeplanner/free/all")
