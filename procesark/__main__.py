"""
Procesark entrypoint
"""
import os
import sys
import asyncio
import uvloop


async def main(args=None):  # pragma: no cover
    pass


if __name__ == '__main__':  # pragma: no cover
    uvloop.install()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(sys.argv[1:]))
    loop.close()
