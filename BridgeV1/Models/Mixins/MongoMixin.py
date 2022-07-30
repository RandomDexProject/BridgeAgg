from Configs.mongo_config import mongo_client
from Utils.Types import ChainId
class MongoMixin:

    chain_id: ChainId

    @property
    def _redis_client(self):
        return mongo_client(self.chain_id)


