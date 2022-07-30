from typing import Optional, List

from odmantic import Field, Model

from Utils.Types import Address, ChainId


class Token(Model):
    address: str
    symbol: str
    decimal: int
    burn_rate: Optional[int]
    popularity: int = 0
