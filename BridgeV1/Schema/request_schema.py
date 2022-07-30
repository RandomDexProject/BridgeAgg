from ast import Add
from pydantic import BaseModel as BaseModel, PrivateAttr
from datetime import datetime

from Models import Network, Token
from Utils.Types import Address


class BaseRequest(BaseModel):
    token: Address
    to: Address
    chainId: int
    toChainId: int
    amountIn: float

    _timestamp: float = PrivateAttr(datetime.now().timestamp())
    _network: Network = PrivateAttr(None)
    _token: Token = PrivateAttr(None)
    _amount_in: int = PrivateAttr(0)
    _amount_out: int = PrivateAttr(0)
    _block_no: int = PrivateAttr(0)
