from typing import Tuple, List, Dict, Any
from json import loads
from aiohttp import web
from .format import parse_domain, parse_dict


def get_request_filter(request: web.Request) -> Tuple:
    filter = request.query.get('filter')
    limit = int(request.query.get('limit') or 1000)
    offset = int(request.query.get('offset') or 0)

    domain = parse_domain(filter)

    return domain, limit, offset


# def get_request_parameters(request: web.Request) -> Dict[str, Any]:
#     return parse_dict(request.query)


async def get_request_ids(request: web.Request) -> List[str]:
    ids = []
    uri_id = request.match_info.get('id')
    if uri_id:
        ids.append(uri_id)

    body = await request.text()
    if body:
        ids.extend(loads(await request.text()))

    return ids
