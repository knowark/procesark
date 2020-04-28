from pytest import fixture
from aiohttp import web
from injectark import Injectark
from procesark.infrastructure.config import DEVELOPMENT_CONFIG
from procesark.infrastructure.factories import (
    strategy_builder, factory_builder)
from procesark.infrastructure.web import create_app


@fixture
def app(loop, aiohttp_client):
    """Create app testing client"""
    config = DEVELOPMENT_CONFIG
    strategy = strategy_builder.build(config['strategies'])
    factory = factory_builder.build(config)

    resolver = Injectark(strategy, factory)

    app = create_app(config, resolver)

    return loop.run_until_complete(aiohttp_client(app))


@fixture
def headers() -> dict:
    return {
        "From": "john@doe.com",
        "TenantId": "001",
        "UserId": "001",
        "Roles": "user"
    }
