from ..models import Process, Job, Allocation, Trigger, Run
from .repository import Repository
from .memory_repository import MemoryRepository


class AllocationRepository(Repository[Allocation]):
    """Allocation Repository"""


class MemoryAllocationRepository(
        MemoryRepository, AllocationRepository):
    """Memory Allocation Repository"""


class JobRepository(Repository[Job]):
    """Job Repository"""


class MemoryJobRepository(
        MemoryRepository, JobRepository):
    """Memory Job Repository"""


class ProcessRepository(Repository[Process]):
    """Process Repository"""


class MemoryProcessRepository(
        MemoryRepository, ProcessRepository):
    """Memory Process Repository"""


class RunRepository(Repository[Run]):
    """Run Repository"""


class MemoryRunRepository(
        MemoryRepository, RunRepository):
    """Memory Run Repository"""


class TriggerRepository(Repository[Trigger]):
    """Trigger Repository"""


class MemoryTriggerRepository(
        MemoryRepository, TriggerRepository):
    """Memory Trigger Repository"""
