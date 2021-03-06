from injectark import Injectark
from aiohttp import web
from json import dumps
from ..schemas import ProcessSchema
from ..helpers import get_request_filter, get_request_ids


class ProcessResource:
    def __init__(self, injector: Injectark) -> None:
        self.injector = injector
        self.stage_coordinator = self.injector['StageCoordinator']
        self.procesark_informer = self.injector['ProcesarkInformer']

    async def head(self, request) -> web.Response:
        """
        ---
        summary: Return processes HEAD headers.
        tags:
          - Processes
        """
        domain, _, _ = get_request_filter(request)

        headers = {
            'Total-Count': str(await self.procesark_informer.count(
                'process', domain))
        }

        return web.Response(headers=headers)

    async def get(self, request: web.Request) -> web.Response:
        """
        ---
        summary: Return all processes.
        tags:
          - Processes
        responses:
          200:
            description: "Successful response"
            content:
              application/json:
                schema:
                  type: array
                  items:
                    $ref: '#/components/schemas/Processe'
        """
        domain, limit, offset = get_request_filter(request)

        processes = ProcessSchema().dump(
            await self.procesark_informer.search(
                'process', domain, limit=limit,
                offset=offset), many=True)

        return web.json_response(processes, dumps=dumps)

    async def put(self, request: web.Request) -> web.Response:
        """
        ---
        summary: Create or update process.
        tags:
          - Processes
        requestBody:
          required: true
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Processe'
        responses:
          201:
            description: "Processe created."
        """
        process_records = ProcessSchema(
            many=True).loads(await request.text())

        await self.stage_coordinator.set_processes(process_records)

        return web.Response(status=200)

    async def delete(self, request: web.Request) -> web.Response:
        """
        ---
        summary: Delete the specified process.
        tags:
          - Processes
        responses:
          204:
            description: "Processes deleted."
        """

        ids = await get_request_ids(request)

        await self.stage_coordinator.delete_processes(ids)

        return web.Response(status=204)
