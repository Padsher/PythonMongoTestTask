import asyncio
from server import startServer

async def main():
    await startServer()

    # run forever
    # maybe there is better way
    # but not web.run_app(), we must abstract entry point
    # that thing with sleep is from official aiohttp documentation
    while True:
        await asyncio.sleep(1_000_000)


asyncio.get_event_loop().run_until_complete(main())