from pytest import fixture
from procesark.application.models import Process, Job, Allocation
from procesark.application.utilities import QueryParser
from procesark.application.repositories import (
    MemoryProcessRepository, MemoryJobRepository, MemoryAllocationRepository)
from procesark.application.coordinators import StageCoordinator


@fixture
def process_repository(tenant_provider, auth_provider):
    process_repository = MemoryProcessRepository(
        QueryParser(), tenant_provider, auth_provider)
    process_repository.load({'default': {
        '001': Process(id='001', name='Sync Inventory Transactions'),
        '002': Process(id='002', name='Send Promotion Emails')
    }})
    return process_repository


@fixture
def job_repository(tenant_provider, auth_provider):
    job_repository = MemoryJobRepository(
        QueryParser(), tenant_provider, auth_provider)
    job_repository.load({'default': {
        '001': Job(id='001', name='Download Transactions'),
        '002': Job(id='002', name='Transform Transactions'),
        '003': Job(id='003', name='Load Transactions'),
        '004': Job(id='004', name='Design Promotion Email'),
        '005': Job(id='005', name='Send Email')
    }})
    return job_repository


@fixture
def allocation_repository(tenant_provider, auth_provider):
    allocation_repository = MemoryAllocationRepository(
        QueryParser(), tenant_provider, auth_provider)
    return allocation_repository


@fixture
def stage_coordinator(process_repository, job_repository,
                      allocation_repository):
    return StageCoordinator(
        process_repository, job_repository, allocation_repository)


def test_stage_coordinator_instantiation(
        stage_coordinator: StageCoordinator) -> None:
    assert hasattr(stage_coordinator, 'allocate')


async def test_stage_coordinator_allocate(stage_coordinator):
    allocation_dicts = [
        {'id': '001', 'process_id': '001', 'job_id': '001', 'sequence': 1},
        {'id': '002', 'process_id': '001', 'job_id': '002', 'sequence': 2},
        {'id': '003', 'process_id': '001', 'job_id': '003', 'sequence': 3},
        {'id': '004', 'process_id': '001', 'job_id': '005', 'sequence': 4}
    ]

    await stage_coordinator.allocate(allocation_dicts)

    allocations = stage_coordinator.allocation_repository.data['default']

    assert len(allocations) == 4
    for record in allocation_dicts:
        assert record['id'] in allocations


async def test_stage_coordinator_set_processes(stage_coordinator):
    process_dicts = [
        {'id': '003', 'name': 'Update System Dependencies'},
        {'id': '004', 'name': 'Deploy Website'},
    ]

    await stage_coordinator.set_processes(process_dicts)

    processes = stage_coordinator.process_repository.data['default']

    assert len(processes) == 4
    for record in process_dicts:
        assert record['id'] in processes
