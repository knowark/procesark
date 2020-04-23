from typing import List
from ..models import Process, Allocation, Trigger
from ..services import Scheduler, Executor
from ..repositories import (
    ProcessRepository, JobRepository, AllocationRepository,
    TriggerRepository)


class LaunchCoordinator:
    def __init__(self, process_repository: ProcessRepository,
                 job_repository: JobRepository,
                 allocation_repository: AllocationRepository,
                 trigger_repository: TriggerRepository,
                 scheduler: Scheduler,
                 executor: Executor) -> None:
        self.process_repository = process_repository
        self.job_repository = job_repository
        self.allocation_repository = allocation_repository
        self.trigger_repository = trigger_repository
        self.scheduler = scheduler
        self.executor = executor

    async def prepare(self) -> None:
        triggers = await self.trigger_repository.search([])
        await self.scheduler.schedule(triggers)
        await self.scheduler.subscribe(self.launch)
        await self.scheduler.start()

    async def launch(self, triggers: List[Trigger]) -> None:
        processes = await self.process_repository.search([('id', 'in', [
            trigger.process_id for trigger in triggers
        ])])
        await self.executor.execute(processes)
