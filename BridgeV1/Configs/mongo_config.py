import os
from odmantic import AIOEngine
from motor.motor_asyncio import AsyncIOMotorClient

from Models import Network


global _CLIENT, _ENGINES
_ENGINES = {}
_CLIENT = None



def initialize(
    network: Network
) -> AIOEngine:

    if Network:
        _database_name = network.str_value

    global _CLIENT, _ENGINES
    if not _CLIENT:
        _CLIENT = AsyncIOMotorClient(os.getenv("MONGO_URL"))
    if _database_name not in _ENGINES.keys():
        _ENGINES[_database_name] = AIOEngine(
            motor_client=_CLIENT,
            database=_database_name
        )

    return _ENGINES[_database_name]


def mongo_client(
        chain_id: int = None) -> AIOEngine:
    if chain_id is not None:
        network = Network(chain_id)
    return initialize(network)


async def isConnected():
    global _CLIENT
    return await _CLIENT.admin.command('ismaster')
