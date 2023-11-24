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
"""Emitter of websocket events"""
from __future__ import annotations

from collections import deque
from typing import TYPE_CHECKING, Sequence, Final, Union, Callable, Any
from logging import getLogger

if TYPE_CHECKING:
    from asyncio import AbstractEventLoop, iscoroutinefunction
    from logging import Logger

    from balalaika.events import BaseEvent

__all__: Sequence[str] = ("Emitter")
_log: Logger = getLogger("balalaika.emitter")


class Emitter:
    """Manager of websockets' events

    Parameters
    ---------
    loop: :class:`AbstractEventLoop`
        asyncio event loop
    """
    def __init__(self: Emitter, loop: AbstractEventLoop) -> None:
        self._loop: AbstractEventLoop = loop
        self.listeners: deque = deque()

    def subscibe(self: Emitter, event: Union[str, BaseEvent], callback: Callable) -> None:
        try:
            event: str = event if isinstance(event, str) else event.__name__
            self.listeners.append(
                {"event": event, "callback": callback}
            )
        except Exception as error:
            _log.error(f"Error was occurred while emitting a event.\n{error}")
        else:
            _log.debug(f"Emitted {event} websocket event")

    def unsubscibe(self: Emitter, event: Union[str, BaseEvent], callback: Callable) -> None:
        try:
            event: str = event if isinstance(event, str) else event.__name__
            for listener in self.listeners:
                if listener["event"] == event and listener["callback"] == callback:
                    self.listeners.remove(listener)
        except Exception as error:
            _log.error(f"Error was occurred while emitting a event.\n{error}")
        else:
            _log.debug(f"Removed {event} websocket event")

    def emit(self: Emitter, event: Union[str, Any], data: Any) -> None:
        event_name: Final[str] = event if isinstance(event, str) else event.__name__
        events: Final[list] = list(filter(lambda listener: listener["event"] == event_name, self.listeners))

        for event in events:
            _log.debug(f"Dispatch {event} for {len(events)} listeners")
            if iscoroutinefunction(event["callback"]):
                self._loop.create_task(event["callback"](data))
            else:
                _log.error("Callback must be coroutine")
