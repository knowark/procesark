from abc import ABC, abstractmethod
from ..utilities import RecordList, QueryDomain
from ..repositories import (
    AllocationRepository, JobRepository, ProcessRepository,
    RunRepository, TriggerRepository)


class ProcesarkInformer(ABC):
    @abstractmethod
    async def search(self,
                     model: str,
                     domain: QueryDomain = None,
                     limit: int = 0,
                     offset: int = 0) -> RecordList:
        """Returns a list of <<model>> dictionaries matching the domain"""

    @abstractmethod
    async def count(self,
                    model: str,
                    domain: QueryDomain = None) -> int:
        """Returns a the <<model>> records count"""


class StandardProcesarkInformer(ProcesarkInformer):
    def __init__(
            self, process_repository: ProcessRepository,
            job_repository: JobRepository,
            allocation_repository: AllocationRepository,
            trigger_repository: TriggerRepository,
            run_repository: RunRepository
    ) -> None:
        self.process_repository = process_repository
        self.job_repository = job_repository
        self.allocation_repository = allocation_repository
        self.trigger_repository = trigger_repository
        self.run_repository = run_repository

    async def search(self,
                     model: str,
                     domain: QueryDomain = None,
                     limit: int = 1000,
                     offset: int = 0) -> RecordList:
        repository = getattr(self, f'{model}_repository')
        return [vars(entity) for entity in
                await repository.search(
                    domain or [], limit=limit, offset=offset)]

    async def count(self,
                    model: str,
                    domain: QueryDomain = None) -> int:
        repository = getattr(self, f'{model}_repository')
        return await repository.count(domain or [])
