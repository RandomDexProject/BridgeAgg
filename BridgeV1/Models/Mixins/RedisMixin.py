from Configs.redis_config import redis_client, redis_client_bytes
from redis.client import Redis
from Utils.Types import ChainId


class RedisMixin:
    chain_id: ChainId

    @property
    def _redis_client(self) -> Redis:
        return redis_client(self.chain_id)


    @property
    def _redis_client_bytes(self):
        return redis_client_bytes(self.chain_id)

