from pytest import fixture
from procesark.application.models import (
    Process, Job, Allocation, Trigger, Run)
from procesark.application.utilities import (
    QueryParser, StandardTenantProvider, Tenant,
    StandardAuthProvider, User, QueryDomain)
from procesark.application.repositories import (
    MemoryProcessRepository, MemoryJobRepository,
    MemoryAllocationRepository, MemoryTriggerRepository,
    MemoryRunRepository)
from procesark.application.informers import (
    ProcesarkInformer, StandardProcesarkInformer)


@fixture
def parser():
    return QueryParser()


@fixture
def auth_provider():
    auth_provider = StandardAuthProvider()
    auth_provider.setup(User(id='001', name='johndoe'))
    return auth_provider


@fixture
def tenant_provider():
    tenant_provider = StandardTenantProvider()
    tenant_provider.setup(Tenant(name="Default"))
    return tenant_provider


@fixture
def process_repository(tenant_provider, auth_provider, parser):
    process_repository = MemoryProcessRepository(
        parser, tenant_provider, auth_provider)
    process_repository.load({
        'default': {
            '001': Process(**{'id': '001', 'name': "Daily Backups"}),
            '002': Process(**{'id': '002', 'name': 'Datawarehouse Sync'})
        }
    })
    return process_repository


@fixture
def job_repository(tenant_provider, auth_provider, parser):
    job_repository = MemoryJobRepository(
        parser, tenant_provider, auth_provider)
    job_repository.load({
        'default': {
            '001': Job(**{'id': '001', 'name': 'Download Data'}),
            '002': Job(**{'id': '002', 'name': 'Normalize Records'})
        }
    })
    return job_repository


@fixture
def allocation_repository(tenant_provider, auth_provider, parser):
    allocation_repository = MemoryAllocationRepository(
        parser, tenant_provider, auth_provider)
    allocation_repository.load({
        'default': {
            '001': Allocation(**{'id': '001', 'process_id': '001',
                                 'job_id': '001'}),
            '002': Allocation(**{'id': '002', 'process_id': '001',
                                 'job_id': '002'})
        }
    })
    return allocation_repository


@fixture
def trigger_repository(tenant_provider, auth_provider, parser):
    trigger_repository = MemoryTriggerRepository(
        parser, tenant_provider, auth_provider)
    trigger_repository.load({
        'default': {
            '001': Trigger(**{'id': '001', 'process_id': '001'})
        }
    })
    return trigger_repository


@fixture
def run_repository(tenant_provider, auth_provider, parser):
    run_repository = MemoryRunRepository(
        parser, tenant_provider, auth_provider)
    run_repository.load({
        'default': {
            '001': Run(**{'id': '001', 'process_id': '001',
                          'job_id': '001', 'state': 'done'}),
            '002': Run(**{'id': '002', 'process_id': '001',
                          'job_id': '002', 'state': 'pending'})
        }
    })
    return run_repository


@fixture
def procesark_informer(process_repository,
                       job_repository,
                       allocation_repository,
                       trigger_repository,
                       run_repository):
    return StandardProcesarkInformer(
        process_repository, job_repository, allocation_repository,
        trigger_repository, run_repository)


async def test_procesark_informer_search_processes_all(
        procesark_informer: ProcesarkInformer) -> None:
    domain: QueryDomain = []
    processes = await procesark_informer.search('process', domain)
    assert len(processes) == 2


async def test_procesark_informer_search_runs_done(
        procesark_informer: ProcesarkInformer) -> None:

    domain: QueryDomain = [('state', '=', 'done')]
    runs = await procesark_informer.search('run', domain)
    assert len(runs) == 1


async def test_procesark_informer_count_triggers(
        procesark_informer: ProcesarkInformer) -> None:
    triggers_count = await procesark_informer.count('trigger')
    assert triggers_count == 1
