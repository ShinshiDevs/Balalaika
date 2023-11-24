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
"""Balalaika exceptions"""
from __future__ import annotations

from typing import Sequence, Any, Optional

__all__: Sequence[str] = (
    "AuthorizationFailed",
    "InvalidLavalinkVersion",
    "BadLavalinkResponse",
    "LavalinkUndefinedTracks",
    "QueueIsEmpty",
    "InvalidChannelStateError",
    "InvalidChannelPermissions"
)


class BalalaikaException(Exception):
    """Base balalaika exception."""


class AuthorizationFailed(BalalaikaException):
    """An exception occurs when authorisation via password fails."""


class InvalidLavalinkVersion(BalalaikaException):
    """An exception occurs when the Balalaika version is not compatible with the Lavalink version."""


class BadLavalinkResponse(BalalaikaException):
    """An exception occurs when Balalaika receives an incomprehensible response from Lavalink.

    Attributes
    ----------
    status_code: :class:`Optional[int]`
        The received status code from Lavalink.
        Should be None.
    """
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args)
        self.status_code: Optional[int] = kwargs.get('status_code')


class LavalinkUndefinedTracks(BalalaikaException):
    """An exception occurs when there are no tracks found."""


class QueueIsEmpty(BalalaikaException):
    """The exception occurs when they want to get something from an empty queue."""


class InvalidChannelStateError(BalalaikaException):
    """An exception occurs when there is a client state conflict when trying to connect
    to :class:`hikari.channels.GuildVoiceChannel`"""


class InvalidChannelPermissions(InvalidChannelStateError):
    """An exception occurs when a client cannot connect to a channel because of permissions

    It can also occur when the channel is full.
    """
