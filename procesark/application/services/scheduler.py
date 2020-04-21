from abc import ABC, abstractmethod
from typing import Callable, Awaitable, List, Any
from ..models import Trigger


Callback = Callable[[Trigger], Awaitable[Any]]


class Scheduler(ABC):
    @abstractmethod
    async def schedule(self, triggers: List[Trigger]) -> None:
        "Schedule method to be implemented."

    @abstractmethod
    async def subscribe(self, Callback: Callback) -> None:
        "Subscribe method to be implemented."


class StandardScheduler(Scheduler):
    def __init__(self) -> None:
        self.triggers = []

    async def schedule(self, triggers: List[Trigger]) -> None:
        self.triggers = triggers

    async def subscribe(self, Callback: Callback) -> None:
        "Subscribe method to be implemented."
