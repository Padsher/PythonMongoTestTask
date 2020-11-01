import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from umongo import Instance
from config.database import HOST, PORT, DATABASE

# assure that everything will be run on one loop
db = AsyncIOMotorClient(host = HOST, port = PORT, io_loop = asyncio.get_event_loop())[DATABASE]

instance = Instance(db)