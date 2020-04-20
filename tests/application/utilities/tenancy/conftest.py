from pytest import fixture
from procesark.application.utilities import (
    QueryParser, TenantProvider, StandardTenantProvider)


@fixture
def tenant_provider() -> TenantProvider:
    return StandardTenantProvider()
