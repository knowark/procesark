"""
Procesark entrypoint
"""
import os
import sys
import logging
import asyncio
import uvloop
from json import loads
from pathlib import Path
from injectark import Injectark
from .infrastructure.config import Config, PRODUCTION_CONFIG
from .infrastructure.factories import strategy_builder, factory_builder
from .infrastructure.cli import Cli


async def main(args=None):  # pragma: no cover
    config_path = Path(os.environ.get('PROCESARK_CONFIG', 'config.json'))
    config = loads(config_path.read_text()) if config_path.is_file() else {}
    config: Config = {**PRODUCTION_CONFIG, **config}

    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG,
                        format='%(message)s')

    factory = factory_builder.build(config)
    strategy = strategy_builder.build(
        config['strategies'], config['strategy'])
    injector = Injectark(strategy=strategy, factory=factory)
    # injector['SetupSupplier'].setup()

    await Cli(config, injector).run(args or [])


if __name__ == '__main__':  # pragma: no cover
    uvloop.install()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(sys.argv[1:]))
    loop.close()
