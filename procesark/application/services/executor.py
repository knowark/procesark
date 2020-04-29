from abc import ABC, abstractmethod
from typing import List, Optional, Any
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
        self.executed: Optional[List[Process]] = None
        self.invoked: Optional[List[Process]] = None
        self.result = result or {}

    async def execute(self, processes: List[Process]) -> None:
        self.executed = processes

    async def invoke(self, processes: List[Process]) -> List[Any]:
        self.invoked = processes
        return [self.result for _ in self.invoked]
