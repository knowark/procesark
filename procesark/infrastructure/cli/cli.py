import logging
from pathlib import Path
from argparse import ArgumentParser, Namespace
from injectark import Injectark
from typing import List, Dict
from ... import __version__
from ..config import Config
from ..web import create_app, run_app


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class Cli:
    def __init__(self, config: Config, injector: Injectark) -> None:
        self.config = config
        self.injector = injector
        self.parser = ArgumentParser('Procesark')

    async def run(self, argv: List[str]) -> None:
        namespace = await self.parse(argv)
        await namespace.func(vars(namespace))

    async def parse(self, argv: List[str]) -> Namespace:
        subparsers = self.parser.add_subparsers()

        # Serve
        serve_parser = subparsers.add_parser(
            'serve', help='Start HTTP server.')
        serve_parser.add_argument('-p', '--port')
        serve_parser.set_defaults(func=self.serve)

        # Version
        version_parser = subparsers.add_parser('version')
        version_parser.set_defaults(func=self.version)

        if len(argv) == 0:
            self.parser.print_help()
            self.parser.exit()

        return self.parser.parse_args(argv)

    async def serve(self, options_dict: Dict[str, str]) -> None:
        logger.info('SERVE')
        port = options_dict.get('port') or self.config['port']
        app = create_app(self.config, self.injector)
        await run_app(app, port)
        logger.info('END SERVE')

    async def version(self, options_dict: Dict[str, str]):
        logger.info('<< VERSION >>')
        logger.info(__version__)
