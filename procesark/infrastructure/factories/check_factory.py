from ..config import Config
from ...application.models import Process
from ...application.utilities import (
    QueryParser, TenantProvider, StandardTenantProvider, Tenant,
    AuthProvider, StandardAuthProvider, User)
from ...application.repositories import (
    MemoryProcessRepository)
from ...infrastructure.core import MemoryTenantSupplier
from .base_factory import BaseFactory


class CheckFactory(BaseFactory):
    def __init__(self, config: Config) -> None:
        self.config = config

    def check_tenant_provider(self) -> StandardTenantProvider:
        tenant_provider = StandardTenantProvider()
        tenant_provider.setup(Tenant(id='001', name="Default"))
        return tenant_provider

    def check_auth_provider(self) -> StandardAuthProvider:
        auth_provider = StandardAuthProvider()
        auth_provider.setup(User(id='001', name='johndoe'))
        return auth_provider

    def memory_process_repository(
            self, query_parser: QueryParser,
            tenant_provider: TenantProvider,
            auth_provider: AuthProvider
    ) -> MemoryProcessRepository:
        process_repository = super().memory_process_repository(
            query_parser, tenant_provider, auth_provider)
        process_repository.load({'default': {
            '001': Process(id='001', name='Datawarehouse Sync'),
            '002': Process(id='002', name='Logs Consolidation'),
            '003': Process(id='003', name='System Data Backup')
        }})
        return process_repository

    def check_tenant_supplier(self) -> MemoryTenantSupplier:
        tenant_supplier = MemoryTenantSupplier()
        tenant_supplier.create_tenant({
            'id': '001',
            'name': 'Default',
            'zone': 'default',
            'data': {
                'memory': {
                    'default': 'default'
                }
            }})
        return tenant_supplier
