from fastapi import APIRouter

from Schema.request_schema import BaseRequest
from Models import Network
from Utils.abi import bridge_router

routes = APIRouter()


@routes.post("/bridge")
async def bridge(request: BaseRequest):
    request._network = Network(request.chainId)
    request._amount_in = int(request.amountIn * \
        10 ** request._network.network_token_decimal)

    _c = request._network.w3.eth.contract(
        request._network.router_address, abi=bridge_router)

    p = request._network.w3.eth.gas_price
    n = request._network.w3.eth.get_transaction_count(request.to)


    if request.token == request._network.network_value_address:
        bridge = _c.functions.anySwapOutNative(
            request.token,
            request.to,
            request.toChainId
        ).buildTransaction({
            "chainId": request.chainId,
            "gasPrice": p,
            "nonce": n,
            "from": request.to,
            "value": request._amount_in
        })  
    else:
        bridge = _c.functions.anySwapOutUnderlying(
            request.token,
            request.to,
            request._amount_in,
            request.toChainId
        ).buildTransaction({
            "chainId": request.chainId,
            "gasPrice": p,
            "nonce": n,
            "from": request.to,
        })  

    print(bridge)
    return bridge
