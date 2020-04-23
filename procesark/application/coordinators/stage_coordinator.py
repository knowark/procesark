from ..models import Process, Allocation
from ..utilities import RecordList
from ..repositories import (
    ProcessRepository, JobRepository, AllocationRepository)


class StageCoordinator:
    def __init__(self, process_repository: ProcessRepository,
                 job_repository: JobRepository,
                 allocation_repository: AllocationRepository) -> None:
        self.process_repository = process_repository
        self.job_repository = job_repository
        self.allocation_repository = allocation_repository

    async def set_processes(self, process_records: RecordList) -> None:
        await self.process_repository.add([
            Process(**record) for record in process_records])

    async def allocate(self, allocation_records: RecordList) -> None:
        process_ids = [record["process_id"] for record in allocation_records]
        job_ids = [record["job_id"] for record in allocation_records]
        process_set = {
            item.id for item in
            await self.process_repository.search([('id', 'in', process_ids)])}
        job_set = {
            item.id for item in
            await self.job_repository.search([('id', 'in', job_ids)])}

        await self.allocation_repository.add([
            Allocation(**record) for record in allocation_records
            if record['process_id'] in process_set
            and record['job_id'] in job_set])
