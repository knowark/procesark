from typing import Any
from aiohttp import web
from injectark import Injectark
from .resources import (
    RootResource, ProcessResource)
from .spec import create_spec


def create_api(app: web.Application, injector: Injectark) -> None:
    # Restful API
    spec = create_spec()

    # Root Resource
    bind_routes(app, '/', RootResource(spec))

    # Process Resource
    bind_routes(app, '/processes', ProcessResource(injector))
    spec.path(path="/processes", operations={
        'head': {}, 'get': {}, 'put': {}, 'delete': {}},
        resource=ProcessResource)


def bind_routes(app: web.Application, path: str, resource: Any):
    general_methods = ['head', 'get', 'put', 'delete', 'post', 'patch']
    identified_methods = ['get', 'delete']
    for method in general_methods + identified_methods:
        handler = getattr(resource, method, None)
        if not handler:
            continue
        if method in identified_methods:
            app.router.add_route(method, path + "/{id}", handler)
        app.router.add_route(method, path, handler)
