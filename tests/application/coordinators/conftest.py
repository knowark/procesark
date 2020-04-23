from pytest import fixture
from procesark.application.models import Process, Job
from procesark.application.utilities import (
    QueryParser, StandardTenantProvider, Tenant,
    StandardAuthProvider, User)
from procesark.application.repositories import (
    MemoryAllocationRepository, MemoryTriggerRepository,
    MemoryProcessRepository, MemoryJobRepository)
from procesark.application.services import StandardScheduler, MemoryExecutor


@fixture
def auth_provider() -> StandardAuthProvider:
    auth_provider = StandardAuthProvider()
    auth_provider.setup(User(id='001', name='johndoe'))
    return auth_provider


@fixture
def tenant_provider() -> StandardTenantProvider:
    tenant_provider = StandardTenantProvider()
    tenant_provider.setup(Tenant(name="Default"))
    return tenant_provider


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
def trigger_repository(tenant_provider, auth_provider):
    trigger_repository = MemoryTriggerRepository(
        QueryParser(), tenant_provider, auth_provider)
    return trigger_repository


@fixture
def scheduler():
    class MockScheduler(StandardScheduler):
        async def start(self) -> None:
            self.active = True

    return MockScheduler()


@fixture
def executor():
    return MemoryExecutor()
