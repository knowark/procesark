from abc import ABC, abstractmethod
from typing import List, Any
from ..models import Process


class Executor(ABC):
    @abstractmethod
    async def execute(self, processes: List[Process]) -> None:
        "Execute method to be implemented."

    @abstractmethod
    async def invoke(self, processes: List[Process]) -> List[Any]:
        "Invoke method to be implemented."


class MemoryExecutor(Executor):
    def __init__(self, result=None) -> None:
        self.executed = None
        self.invoked = None
        self.result = result or {}

    async def execute(self, processes: List[Process]) -> None:
        self.executed = processes

    async def invoke(self, processes: List[Process]) -> List[Any]:
        self.invoked = processes
        return [self.result for _ in self.invoked]
