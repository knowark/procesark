from abc import ABC, abstractmethod
from typing import Callable, Awaitable, List, Any
from ..models import Trigger


Callback = Callable[[Trigger], Awaitable[Any]]


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
    def __init__(self) -> None:
        self.triggers = set()
        self.subscribers = set()
        self.active = False

    async def schedule(self, triggers: List[Trigger]) -> None:
        self.triggers.update(triggers)

    async def subscribe(self, callback: Callback) -> None:
        self.subscribers.add(callback)

    async def start(self) -> None:
        pass

    async def stop(self) -> None:
        pass
