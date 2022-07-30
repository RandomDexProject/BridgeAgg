import os
import json
from web3 import Web3
from enum import IntEnum
from Utils.Types import ChainId

global NETWORKS
with open('Utils/network_book.json') as f:
    NETWORKS = json.load(f)


class Network(IntEnum):
    BSC = 56
    FANTOM = 250
    AVALANCHE = 43114
    POLYGON = 137
    HECO = 128

    @property
    def chain_id(self) -> ChainId:
        return self.value

    @property
    def str_value(self):
        return str(self.value)

    @property
    def network_name(self):
        return NETWORKS.get(self.str_value).get("name")

    @property
    def network_value_address(self):
        return NETWORKS.get(self.str_value).get("value_address")

    @property
    def network_wrapped_address(self):
        return NETWORKS.get(self.str_value).get("wrapped_address")

    @property
    def network_value_symbol(self):
        return NETWORKS.get(self.str_value).get("value_symbol")

    @property
    def network_wrapped_symbol(self):
        return NETWORKS.get(self.str_value).get("wrapped_symbol")

    @property
    def network_value_name(self):
        return NETWORKS.get(self.str_value).get("value_name")

    @property
    def network_wrapped_name(self):
        return NETWORKS.get(self.str_value).get("wrapped_name")

    @property
    def network_token_decimal(self):
        return NETWORKS.get(self.str_value).get("value_decimal")

    @property
    def network_value_detail(self):
        return {
            "chain_id": self.value,
            "symbol": self.network_value_symbol,
            "name": self.network_value_name,
            "address": self.network_value_address,
            "decimal": self.network_token_decimal,
        }

    @property
    def network_value_wrapped_detail(self):
        return {
            "chain_id": self.value,
            "symbol": self.network_wrapped_symbol,
            "name": self.network_wrapped_name,
            "address": self.network_wrapped_address,
            "decimal": self.network_token_decimal,
        }

    @property
    def network_redis_db(self):
        return NETWORKS.get(self.str_value).get("redis_db")

    @property
    def network_rpc(self):
        return NETWORKS.get(self.str_value).get("RPC")

    @property
    def w3(self):
        return Web3(Web3.HTTPProvider(self.network_rpc))

    @property
    def router_address(self):
        return NETWORKS.get(self.str_value).get("router")
