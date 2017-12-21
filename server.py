import asyncio
import json
from aiohttp import web
from log import get_log

logger = get_log('aio')

async def index(request):
    logger.info('req:{}'.format(request))
    await asyncio.sleep(0.1)
    return web.Response(body=b'<h1>Aiohttp index</h1>', content_type='text/html')


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route(method='GET', path='/api/index', handler=index)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logger.info('server start at http://127.0.0.1:9000')
    return srv


def main():
    logger.info('start web')
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(init(event_loop))
        event_loop.run_forever()
    finally:
        event_loop.close()

if __name__ == '__main__':
    main()