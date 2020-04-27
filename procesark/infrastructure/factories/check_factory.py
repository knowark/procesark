from ..config import Config
from ...application.utilities import (
    QueryParser, StandardTenantProvider, StandardAuthProvider)
from .base_factory import BaseFactory


class CheckFactory(BaseFactory):
    def __init__(self, config: Config) -> None:
        self.config = config

    def query_parser(self) -> QueryParser:
        return QueryParser()

    def standard_tenant_provider(self) -> StandardTenantProvider:
        return StandardTenantProvider()

    def standard_auth_provider(self) -> StandardAuthProvider:
        return StandardAuthProvider()
