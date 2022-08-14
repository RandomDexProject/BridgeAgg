# BridgeAgg



## Each Bridge Module have following functions

```python
from abc import ABC
from enum import Enum
from typing import Dict, Tuple, TypedDict, List


class Token(TypedDict):
    name: str
    symbol: str
    address: str
    decimals: int
    chain: int


class Chain(Enum):
    ...


class PathDetail(TypedDict):
    fromToken: Token
    toToken: Token
    toChain: Chain
    fromChain: Chain


class Bridge(ABC):
    def name(self) -> str:
        raise NotImplementedError

    def estimated_wait(self, path: PathDetail) -> float:
        raise NotImplementedError

    def chain_list(self) -> List[Chain]:
        raise NotImplementedError

    def token_list(self) -> List[Token]:
        raise NotImplementedError

    def does_support(self, path: PathDetail) -> bool:
        ...

    def connected_tokens(
        self, fromToken: Token, fromChain: Chain
    ) -> Dict[Chain, List[Token]]:
        ...
    def connected_chains(
        self, fromToken: Token, fromChain: Chain
    ) -> List[Chain]:
        ...

```