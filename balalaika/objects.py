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
"""Balalaika base objects"""
from __future__ import annotations

from typing import Sequence, Optional

import attrs

from balalaika.ext.types import URLT, PlaylistT

__all__: Sequence[str] = ('BalalaikaObject')


class BalalaikaObject:
    """Base object"""


@attrs.define(kw_only=True, weakref_slot=False)
class Artist(BalalaikaObject):
    name: Optional[str] = attrs.field(factory=str)
    artist_url: Optional[URLT] = attrs.field(factory=URLT)
    artist_artwork_url: Optional[URLT] = attrs.field(factory=URLT)


@attrs.define(kw_only=True, weakref_slot=False)
class Album(BalalaikaObject):
    name: Optional[str] = attrs.field(factory=str)
    album_url: Optional[URLT] = attrs.field(factory=URLT)
    album_artwork_url: Optional[URLT] = attrs.field(factory=URLT)


@attrs.define(kw_only=True, weakref_slot=False)
class Playlist(BalalaikaObject):
    type: PlaylistT = attrs.field(factory=PlaylistT)
    url: Optional[URLT] = attrs.field(factory=URLT)
    artwork_url: Optional[URLT] = attrs.field(factory=URLT)
    author: Optional[str] = attrs.field(factory=str)
    total_tracks: Optional[int] = attrs.field(factory=int)


@attrs.define(kw_only=True, weakref_slot=False)
class Track(BalalaikaObject):
    label: Optional[str] = attrs.field(factory=str)
    identifier: Optional[str] = attrs.field(factory=str)
    artist: Optional[Artist] = attrs.field(factory=Artist)
    album: Optional[Album] = attrs.field(factory=Album)
    playlist: Optional[Playlist] = attrs.field(factory=Playlist)
    preview_url: Optional[URLT] = attrs.define(factory=URLT)
