import traceback
import json
from aiohttp import web
from config.server import PORT
from routes.all import routes
from routes.exceptions import ClientException

@web.middleware
async def globalExceptionHandler(req, handler):
    try:
        return await handler(req)
    except ClientException as e:
        return web.Response(status = 400, text = json.dumps({ 'error': e.message}))
    except Exception as e:
        print("Unknown exception") # use simple prints instead of logger for this test task
        print(e)
        traceback.print_tb(e.__traceback__)
        print()
        print(f'Req: {req.method} {req.path_qs}, body: {await req.text()}')
        return web.Response(status = 500)


app = web.Application(middlewares = [
    globalExceptionHandler
])
app.router.add_routes(routes)

async def startServer():
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', PORT)
    await site.start()
    print(f'server started on {PORT}')