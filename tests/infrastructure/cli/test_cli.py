import contextlib
from typing import List
import json
from asyncmock import AsyncMock
from argparse import ArgumentParser, Namespace
from pytest import fixture, raises
from injectark import Injectark
from procesark.infrastructure.factories import (
    strategy_builder, factory_builder)
from procesark.infrastructure.cli import Cli
from procesark.infrastructure.cli import cli as cli_module
from procesark.infrastructure.config import DEVELOPMENT_CONFIG


@fixture
def cli() -> Cli:
    """Create app testing client"""
    config = DEVELOPMENT_CONFIG
    strategy = strategy_builder.build(
        config['strategies'],  config['strategy'])
    factory = factory_builder.build(config)

    injector = Injectark(strategy, factory)

    return Cli(config, injector)


def test_cli_instantiation(cli):
    assert cli is not None
