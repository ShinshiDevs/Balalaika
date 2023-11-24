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
"""Base node"""
from __future__ import annotations

import re
from typing import TYPE_CHECKING, Optional, Sequence, Final, List, Dict, Union
from logging import getLogger

from yarl import URL

from balalaika.routes import LOCALHOST, DEFAULT_PORT

if TYPE_CHECKING:
    from logging import Logger
    from asyncio import AbstractEventLoop, get_event_loop

    from hikari.voices import VoiceRegion

    from balalaika.emitter import Emitter
    from balalaika.player import Player
    from balalaika.ext.types import DiscordIDT, SEARCH_METHODS

__all__: Sequence[str] = ('Node')
_log: Logger = getLogger('balalaika.node')
_url_regex = re.compile(
    "https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"
)


class Node:
    def __init__(
            self,
            *,
            loop: Optional[AbstractEventLoop] = None,
            host: Optional[str] = LOCALHOST,
            port: int = DEFAULT_PORT,
            password: str,
            user_id: Optional[DiscordIDT],
            region: Optional[VoiceRegion],
            resume_key: Optional[str],
            resume_timeout: int = 180,
            shards_count: int = 1,
            ssl_connection: bool = False,
    ) -> None:
        self.host: Final[str] = host
        self.port: Final[int] = port
        self.password: Final[str] = password
        self.user_id: Optional[DiscordIDT] = user_id
        self.region: Optional[VoiceRegion] = region
        self.shards_count: Final[int] = shards_count
        self.ssl: Final[bool] = ssl_connection

        self.players: Dict[DiscordIDT, Player] = {}
        self.loop: AbstractEventLoop = loop or get_event_loop()
        self.event_manager: Emitter = Emitter(self.loop)
        self._websocket: Optional[Websocket] = None
        self._resume_key: Optional[str] = resume_key
        self._resume_timeout: Final[int] = resume_timeout
        self._voice_handlers: Dict[int, ConnectionInfo] = {}

        self.rest: Rest = Rest(
            host=self.host,
            port=self.port,
            password=self.password,
            ssl=self.ssl,
            region=self.region
        )
        self.stats: Optional[Stats] = None
        self.session_id: Optional[str] = None

    def set_event_loop(self, loop: AbstractEventLoop) -> None:
        """
        Set the event loop for the client requird set after call :meth:`connect`,

        Parameters
        ---------
        loop: :class:`asyncio.AbstractEventLoop`
            The event loop to use.
        """
        self.loop = loop
        self.event_manager._loop = loop

    def create_player(self, guild_id: DiscordIDT) -> Player:
        """
        Create a player for guild.

        Parameters
        ---------
        guild_id: :class:`DiscordIDT`
            The guild id for player.
        """
        player = Player(self, guild_id)
        self.players[guild_id] = player
        return player

    def destroy_player(self, guild_id: DiscordIDT) -> None:
        """
        Destroy a player for guild.

        Parameters
        ---------
        guild_id: :class:`DiscordIDT`
            The guild id for player.
        """
        del self.players[guild_id]

    def get_player(self, guild_id: DiscordIDT) -> Player:
        """
        Get player for guild.

        Parameters
        ---------
        guild_id: :class:`DiscordIDT`
            The guild id for player.
        """
        return self.players.get(guild_id)

    def change_player(self, guild_id: DiscordIDT, player: Player) -> Player:
        """
        Change player for guild id.

        Parameters
        ---------
        guild_id: :class:`DiscordIDT`
            The guild id for player.
        player: :class:`Player`
            The player to change.
        """
        self.players[guild_id] = player
        return player

    def search_tracks(self, method: SEARCH_METHODS, query: Union[str, URL]):