from procesark.application.services.executor import MemoryExecutor
from procesark.application.services.scheduler import StandardScheduler
from ...application.services import Scheduler, Executor
from injectark import Factory
from ..config import Config
from ...application.utilities import (
    QueryParser, TenantProvider, StandardTenantProvider,
    AuthProvider, StandardAuthProvider)
from ...application.repositories import (
    ProcessRepository, MemoryProcessRepository,
    JobRepository, MemoryJobRepository,
    AllocationRepository, MemoryAllocationRepository,
    TriggerRepository, MemoryTriggerRepository,
    RunRepository, MemoryRunRepository)
from ...application.coordinators import (
    LaunchCoordinator, StageCoordinator, SessionCoordinator)
from ...application.informers import StandardProcesarkInformer
from ...infrastructure.core import MemoryTenantSupplier


class BaseFactory(Factory):
    def __init__(self, config: Config) -> None:
        self.config = config

    def query_parser(self) -> QueryParser:
        return QueryParser()

    def standard_tenant_provider(self) -> StandardTenantProvider:
        return StandardTenantProvider()

    def standard_auth_provider(self) -> StandardAuthProvider:
        return StandardAuthProvider()

    def memory_process_repository(
            self, query_parser: QueryParser,
            tenant_provider: TenantProvider,
            auth_provider: AuthProvider
    ) -> MemoryProcessRepository:
        return MemoryProcessRepository(
            query_parser, tenant_provider, auth_provider)

    def memory_job_repository(
            self, query_parser: QueryParser,
            tenant_provider: TenantProvider,
            auth_provider: AuthProvider
    ) -> MemoryJobRepository:
        return MemoryJobRepository(
            query_parser, tenant_provider, auth_provider)

    def memory_allocation_repository(
            self, query_parser: QueryParser,
            tenant_provider: TenantProvider,
            auth_provider: AuthProvider
    ) -> MemoryAllocationRepository:
        return MemoryAllocationRepository(
            query_parser, tenant_provider, auth_provider)

    def memory_trigger_repository(
            self, query_parser: QueryParser,
            tenant_provider: TenantProvider,
            auth_provider: AuthProvider
    ) -> MemoryTriggerRepository:
        return MemoryTriggerRepository(
            query_parser, tenant_provider, auth_provider)

    def memory_run_repository(
            self, query_parser: QueryParser,
            tenant_provider: TenantProvider,
            auth_provider: AuthProvider
    ) -> MemoryRunRepository:
        return MemoryRunRepository(
            query_parser, tenant_provider, auth_provider)

    def standard_scheduler(self) -> StandardScheduler:
        return StandardScheduler()

    def memory_executor(self) -> MemoryExecutor:
        return MemoryExecutor()

    def launch_coordinator(
        self, process_repository: ProcessRepository,
        job_repository: JobRepository,
        allocation_repository: AllocationRepository,
        trigger_repository: TriggerRepository,
        scheduler: Scheduler,
        executor: Executor
    ) -> LaunchCoordinator:
        return LaunchCoordinator(
            process_repository, job_repository, allocation_repository,
            trigger_repository, scheduler, executor)

    def stage_coordinator(
        self, process_repository: ProcessRepository,
        job_repository: JobRepository,
        allocation_repository: AllocationRepository,
        trigger_repository: TriggerRepository
    ) -> StageCoordinator:
        return StageCoordinator(
            process_repository, job_repository, allocation_repository,
            trigger_repository)

    def standard_procesark_informer(
        self, process_repository: ProcessRepository,
        job_repository: JobRepository,
        allocation_repository: AllocationRepository,
        trigger_repository: TriggerRepository,
        run_repository: RunRepository
    ) -> StandardProcesarkInformer:
        return StandardProcesarkInformer(
            process_repository, job_repository, allocation_repository,
            trigger_repository, run_repository)

    def session_coordinator(
            self, tenant_provider: TenantProvider,
            auth_provider: AuthProvider
    ) -> SessionCoordinator:
        return SessionCoordinator(tenant_provider, auth_provider)

    def memory_tenant_supplier(self) -> MemoryTenantSupplier:
        return MemoryTenantSupplier()
