import aiohttp_cors
import aiohttp_jinja2
from pathlib import Path
from jinja2 import FileSystemLoader
from aiohttp import web, ClientSession
from injectark import Injectark
from .api import create_api
from .middleware import middlewares


def create_app(config, injector: Injectark) -> web.Application:
    app = web.Application(
        middlewares=middlewares(injector)
    )
    app.cleanup_ctx.append(http_client)
    templates = str(Path(__file__).parent / 'templates')
    aiohttp_jinja2.setup(app, loader=FileSystemLoader(templates))
    create_api(app, injector)
    enable_cors(app)

    return app


async def run_app(app: web.Application, port=4321) -> None:
    await web._run_app(app, port=port)


def enable_cors(app: web.Application) -> None:
    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*"
        )
    })

    # Configure CORS on all routes.
    for route in list(app.router.routes()):
        cors.add(route)


async def http_client(app: web.Application):
    # Startup
    session = ClientSession()
    app['client'] = session
    yield
    # Cleanup
    await session.close()
