"""
Procesark entrypoint
"""
import os
import sys
import logging
import asyncio
import uvloop
from .infrastructure.config import build_config
from .infrastructure.cli import Cli


async def main(args=None):  # pragma: no cover
    config_path = os.environ.get('PROCESARK_CONFIG', 'config.json')
    config = build_config('PROD', config_path)
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG,
                        format='%(message)s')

    # factory = build_factory(config)
    # strategy = build_strategy(config['strategies'], config['strategy'])
    # injector = Injectark(strategy=strategy, factory=factory)
    # injector['SetupSupplier'].setup()
    injector = None

    await Cli(config, injector).run(args or [])


if __name__ == '__main__':  # pragma: no cover
    uvloop.install()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(sys.argv[1:]))
    loop.close()
