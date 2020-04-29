from typing import List
from ..models import Process, Allocation, Trigger
from ..utilities import RecordList
from ..repositories import (
    ProcessRepository, JobRepository,
    AllocationRepository, TriggerRepository)


class StageCoordinator:
    def __init__(self, process_repository: ProcessRepository,
                 job_repository: JobRepository,
                 allocation_repository: AllocationRepository,
                 trigger_repository: TriggerRepository) -> None:
        self.process_repository = process_repository
        self.job_repository = job_repository
        self.allocation_repository = allocation_repository
        self.trigger_repository = trigger_repository

    async def set_processes(self, process_records: RecordList) -> None:
        await self.process_repository.add([
            Process(**record) for record in process_records])

    async def set_triggers(self, trigger_records: RecordList) -> None:
        process_set = {
            item.id for item in
            await self.process_repository.search([('id', 'in', [
                record["process_id"] for record in trigger_records])])}
        await self.trigger_repository.add([
            Trigger(**record) for record in trigger_records
            if record['process_id'] in process_set])

    async def allocate(self, allocation_records: RecordList) -> None:
        process_set = {
            item.id for item in
            await self.process_repository.search([('id', 'in', [
                record["process_id"] for record in allocation_records])])}
        job_set = {
            item.id for item in
            await self.job_repository.search([('id', 'in', [
                record["job_id"] for record in allocation_records])])}

        await self.allocation_repository.add([
            Allocation(**record) for record in allocation_records
            if record['process_id'] in process_set
            and record['job_id'] in job_set])

    async def delete_processes(self, process_ids: List[str]) -> None:
        processes = await self.process_repository.search(
            [('id', 'in', process_ids)])
        await self.process_repository.remove(processes)
