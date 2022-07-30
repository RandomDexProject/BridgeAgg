import logging
from typing import Dict
import redis
from redis.client import Redis
from Models import Network


global _CLIENT
global _CLIENT_BYTES
_CLIENT: Dict[int, Redis] = {}
_CLIENT_BYTES: Dict[int, Redis] = {}


async def initialize(url: str) -> bool:

    global _CLIENT
    global _CLIENT_BYTES

    for network in Network:
        if _CLIENT.get(network.value) is None:
            _CLIENT[network.value] = redis.from_url(
                url, db=network.network_redis_db, decode_responses=True
            )

            _CLIENT_BYTES[network.value] = redis.from_url(
                url, db=network.network_redis_db)

        _CLIENT[network.value].set(
            f"db-{network.network_redis_db}", "connected")

    _CLIENT[0] = redis.from_url(
        url=url, db=0, decode_responses=True)
    _CLIENT_BYTES[0] = redis.from_url(url=url, db=0)


def isConnected():
    cl = redis_client(0)
    cl.set("connection", "up")
    if cl.get("connection") == "up":
        return True
    logging.critical("REDIS IS NOT CONNECTED!")
    return False


def redis_client(chainId) -> Redis:
    """Uses aioredis [Is Async]"""
    global _CLIENT
    return _CLIENT.get(chainId)


def cache_client() -> Redis:
    """Uses Normal redis client [Not Async]"""
    global _CLIENT_BYTES
    return _CLIENT_BYTES.get(0)


def redis_client_bytes(chainId) -> Redis:
    """Uses aioredis [Is Async]"""
    global _CLIENT_BYTES
    return _CLIENT_BYTES.get(chainId)


def cache_client_bytes() -> Redis:
    """Uses Normal redis client [Not Async]"""
    global _CLIENT_BYTES
    return _CLIENT_BYTES.get(0)
