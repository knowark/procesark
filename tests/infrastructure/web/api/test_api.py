from pytest import raises
from json import loads, dumps
from aiohttp import web


async def test_root(app) -> None:
    response = await app.get('/')

    content = await response.text()

    assert response.status == 200
    assert 'Procesark' in content


async def test_root_api(app) -> None:
    response = await app.get('/?api')
    data = await response.text()
    api = loads(data)

    assert 'openapi' in api
    assert api['info']['title'] == 'Procesark'


async def test_processes_head(app, headers) -> None:
    response = await app.head('/processes', headers=headers)
    count = response.headers.get('Total-Count')

    assert int(count) == 3


async def test_processes_get_unauthorized(app) -> None:
    response = await app.get('/processes')
    content = await response.text()

    assert response.status == 401
    data_dict = loads(content)
    assert 'error' in data_dict


async def test_processes_get(app, headers) -> None:
    response = await app.get('/processes', headers=headers)
    content = await response.text()
    assert response.status == 200

    data_dict = loads(content)

    assert len(data_dict) == 3
    assert data_dict[1]['id'] == '002'
