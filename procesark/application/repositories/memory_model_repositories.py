from .repository import Repository
from .memory_repository import MemoryRepository


class AllocationRepository(Repository):
    """Allocation Repository"""


class MemoryAllocationRepository(
        MemoryRepository, AllocationRepository):
    """Memory Allocation Repository"""


class JobRepository(Repository):
    """Job Repository"""


class MemoryJobRepository(
        MemoryRepository, JobRepository):
    """Memory Job Repository"""


class ProcessRepository(Repository):
    """Process Repository"""


class MemoryProcessRepository(
        MemoryRepository, ProcessRepository):
    """Memory Process Repository"""


class RunRepository(Repository):
    """Run Repository"""


class MemoryRunRepository(
        MemoryRepository, RunRepository):
    """Memory Run Repository"""


class TriggerRepository(Repository):
    """Trigger Repository"""


class MemoryTriggerRepository(
        MemoryRepository, TriggerRepository):
    """Memory Trigger Repository"""
