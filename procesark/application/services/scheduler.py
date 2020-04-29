import asyncio
from typing import Optional
from abc import ABC, abstractmethod
from asyncio.futures import Future
from contextlib import suppress
from datetime import datetime, timedelta, timezone
from typing import Set, Callable, Awaitable, List, Any
from ..models import Trigger
from ..utilities import cronable


Callback = Callable[[List[Trigger]], Awaitable[Any]]


class Scheduler(ABC):
    @abstractmethod
    async def schedule(self, triggers: List[Trigger]) -> None:
        "Schedule method to be implemented."

    @abstractmethod
    async def subscribe(self, callback: Callback) -> None:
        "Subscribe method to be implemented."

    @abstractmethod
    async def start(self) -> None:
        "Start method to be implemented."

    @abstractmethod
    async def stop(self) -> None:
        "Start method to be implemented."


class StandardScheduler(Scheduler):
    def __init__(self, tick: int = 1) -> None:
        self.triggers: Set[Trigger] = set()
        self.subscribers: Set[Callback] = set()
        self.active = False
        self.tick = max(tick, 1)
        self._task: Optional[Future] = None

    async def schedule(self, triggers: List[Trigger]) -> None:
        self.triggers.update(triggers)

    async def subscribe(self, callback: Callback) -> None:
        self.subscribers.add(callback)

    async def start(self) -> None:
        if not self.active:
            self.active = True
            self._task = asyncio.ensure_future(self._run())

    async def stop(self) -> None:
        if self.active and self._task is not None:
            self.active = False
            self._task.cancel()
            with suppress(asyncio.CancelledError):
                await self._task

    async def _run(self) -> None:
        while True:
            now = datetime.now(timezone.utc)
            target = now.replace(microsecond=0) + timedelta(seconds=self.tick)
            delay = (target - now).total_seconds()
            await asyncio.sleep(delay)
            await self._notify(target)

    async def _notify(self, target: datetime):
        active_triggers = [trigger for trigger in self.triggers
                           if cronable(trigger.pattern, target)]
        if self.subscribers and active_triggers:
            await asyncio.gather(*[subscriber(active_triggers)
                                   for subscriber in self.subscribers])
