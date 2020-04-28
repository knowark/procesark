from typing import List
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


async def test_cli_run(cli):
    called = False

    class MockArgs:
        async def func(self, args):
            self.args = args

    async def mock_parse(argv: List[str]):
        nonlocal called
        called = True
        return MockArgs()

    cli.parse = mock_parse

    argv: List = []
    await cli.run(argv)

    assert called is True


async def test_cli_parse(cli):
    argv = ['version']
    result = await cli.parse(argv)

    assert result is not None


async def test_cli_parse_empty_argv(cli):
    cli.parser.print_help = lambda: None
    with raises(SystemExit) as e:
        await cli.parse([])


async def test_cli_version(cli):
    options_dict = {}
    assert await cli.version(options_dict) is None


async def test_cli_serve(cli, monkeypatch):
    called = False
    options_dict = {'port': 8080}

    async def mock_run_app(app, port):
        nonlocal called
        called = True

    monkeypatch.setattr(
        cli_module, 'run_app', mock_run_app)

    result = await cli.serve(options_dict)

    assert called
