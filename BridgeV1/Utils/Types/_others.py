from typing import NewType


Timestamp = NewType("timestamp", int)
BigInt = NewType("BigInt", str)  # mongo can't store big integers
APR = NewType("APR", float)
Transaction = NewType("BigInt", str)
BlockNumber = NewType('BlockNumber', int)
StringBlockNumber = NewType('StringBlockNumber', str)
StringTimestamp = NewType("StringTimestamp", str)
Symbol = NewType("Symbol", str)
RawPrice = NewType("RawPrice", float)
Price = NewType("Price", RawPrice)
StringFloat = NewType('StringFloat', str)
StringInt = NewType('StringInt', str)
HexStr = NewType('HexStr', str)
ChainId = NewType("ChainId", int)
NoDecimal = NewType("NoDecimal", float)
WithDecimal = NewType("WithDecimal", int)
